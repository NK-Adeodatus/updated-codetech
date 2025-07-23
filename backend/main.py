# =============================================================================
# BACKEND MAIN APPLICATION - FASTAPI SERVER
# =============================================================================
# This file contains the main FastAPI application with all endpoints, database models,
# authentication, quiz data, and business logic for the CodeTech learning platform.

# Import required libraries for FastAPI web framework
from fastapi import FastAPI, HTTPException, Depends, status, Body, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing import Optional, List, Dict
import sqlite3
import os
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

# =============================================================================
# APPLICATION CONFIGURATION
# =============================================================================
# JWT token configuration for user authentication
SECRET_KEY = "your-secret-key-change-in-production"  # Change this in production for security
ALGORITHM = "HS256"  # JWT signing algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Token expiration time

# =============================================================================
# DATABASE SETUP
# =============================================================================
# MySQL database configuration and connection setup
DATABASE_URL = "mysql+mysqlconnector://root:adeodatus@localhost/codetech_db"  # MySQL database
Base = declarative_base()  # SQLAlchemy base class for models
engine = create_engine(DATABASE_URL)  # Database engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # Database session factory

# =============================================================================
# DATABASE MODELS (SQLAlchemy ORM)
# =============================================================================
# These models define the database structure and relationships

class User(Base):
    """User model - stores user account information"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)  # Unique user ID
    email = Column(String, unique=True, index=True)  # User's email (unique)
    hashed_password = Column(String)  # Encrypted password
    name = Column(String, default="")  # User's display name
    role = Column(String, default="user")  # User role: "user" or "admin"
    profile_picture = Column(String, nullable=True)  # Optional profile picture
    bio = Column(String, nullable=True)  # Optional bio

class UserProgress(Base):
    """User progress model - tracks overall progress per subject"""
    __tablename__ = "user_progress"
    id = Column(Integer, primary_key=True, index=True)  # Unique progress record ID
    user_id = Column(Integer, ForeignKey("users.id"))  # Links to User table
    subject_id = Column(Integer)  # Subject ID (1=Python, 2=ML, 3=JS, 4=C)
    progress = Column(Integer, default=0)  # Progress percentage (0-100)
    completed_quizzes = Column(Integer, default=0)  # Number of completed quizzes
    total_quizzes = Column(Integer, default=0)  # Total quizzes in subject

    user = relationship("User")  # SQLAlchemy relationship to User

class UserQuizProgress(Base):
    """Quiz progress model - tracks completion status of individual quiz levels"""
    __tablename__ = "user_quiz_progress"
    id = Column(Integer, primary_key=True, index=True)  # Unique quiz progress ID
    user_id = Column(Integer, ForeignKey("users.id"))  # Links to User table
    subject_id = Column(Integer)  # Subject ID
    level_id = Column(Integer)  # Level ID within subject
    completed = Column(Integer, default=0)  # 0 = not started, 1 = completed
    user = relationship("User")  # SQLAlchemy relationship to User

class UserActivity(Base):
    """User activity model - logs user actions and quiz scores"""
    __tablename__ = "user_activity"
    id = Column(Integer, primary_key=True, index=True)  # Unique activity ID
    user_id = Column(Integer, ForeignKey("users.id"))  # Links to User table
    subject_id = Column(Integer)  # Subject ID
    level_id = Column(Integer)  # Level ID
    action = Column(String)  # Description of the action (e.g., "Completed Quiz")
    timestamp = Column(String)  # When the action occurred
    score = Column(Integer, default=None)  # Quiz score (if applicable)
    user = relationship("User")  # SQLAlchemy relationship to User

# --- User Goal Model ---
class UserGoal(Base):
    __tablename__ = "user_goals"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String)
    target = Column(String)
    deadline = Column(String)
    description = Column(String)
    created_at = Column(String, default=datetime.utcnow().isoformat)
    user = relationship("User")

# --- User Challenge Model ---
class UserChallenge(Base):
    __tablename__ = "user_challenges"
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    recipient_email = Column(String)
    message = Column(String)
    quiz_type = Column(String)
    created_at = Column(String, default=datetime.utcnow().isoformat)
    user = relationship("User", foreign_keys=[sender_id])

# --- Add SQLAlchemy models for Subject, Level, Quiz, Question, Choice ---
class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    levels = relationship("Level", back_populates="subject")

class Level(Base):
    __tablename__ = "levels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)  # <-- Add this line
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    subject = relationship("Subject", back_populates="levels")
    quizzes = relationship("Quiz", back_populates="level")

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    level_id = Column(Integer, ForeignKey("levels.id"))
    title = Column(String(255), nullable=False)
    level = relationship("Level", back_populates="quizzes")
    questions = relationship("Question", back_populates="quiz")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    text = Column(Text, nullable=False)
    quiz = relationship("Quiz", back_populates="questions")
    choices = relationship("Choice", back_populates="question")

class Choice(Base):
    __tablename__ = "choices"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    text = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False)
    question = relationship("Question", back_populates="choices")

class UserQuizCompletion(Base):
    __tablename__ = "user_quiz_completion"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    completed = Column(Boolean, default=False)

# Create all database tables based on the models defined above
# Base.metadata.create_all(bind=engine)

# =============================================================================
# AUTHENTICATION UTILITIES
# =============================================================================
# Password hashing and JWT token management functions

# Password hashing context using bcrypt algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    """Hash a plain text password using bcrypt"""
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """Verify a plain text password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    """Create a JWT access token for user authentication"""
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_user(db: Session, email: str):
    """Get a user from database by email address"""
    return db.query(User).filter(User.email == email).first()



# =============================================================================
# PYDANTIC SCHEMAS (API REQUEST/RESPONSE MODELS)
# =============================================================================
# These schemas define the structure of API requests and responses
# They provide automatic validation and serialization

class UserCreate(BaseModel):
    """Schema for user registration requests"""
    email: str  # User's email address
    password: str  # Plain text password (will be hashed)
    name: str = ""  # User's display name (optional)
    role: str = "user"  # User role (defaults to "user")

class Token(BaseModel):
    """Schema for authentication token responses"""
    access_token: str  # JWT token for authentication
    token_type: str  # Token type (usually "bearer")

class UserOut(BaseModel):
    """Schema for user data responses (without sensitive info)"""
    id: int  # User ID
    email: str  # User's email
    name: str = ""  # User's display name
    role: str = "user"  # User role
    class Config:
        from_attributes = True  # Allow creation from SQLAlchemy model

class UserWithProgress(BaseModel):
    """Schema for user data with progress statistics"""
    id: int  # User ID
    email: str  # User's email
    name: str = ""  # User's display name
    role: str = "user"  # User role
    total_completed: int = 0  # Total quizzes completed
    avg_score: float = 0.0  # Average quiz score
    last_activity: str = ""  # Last activity timestamp
    class Config:
        from_attributes = True  # Allow creation from SQLAlchemy model


# --- FastAPI App ---
app = FastAPI()

# Enable CORS for all origins (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Admin Authentication Helper ---
def get_current_admin_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = get_user(db, email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user

# --- Create Admin User on Startup ---
def create_admin_user():
    db = SessionLocal()
    try:
        # Check if admin user exists
        admin_user = db.query(User).filter(User.email == "AdminIbra@gmail.com").first()
        if not admin_user:
            # Create admin user
            hashed_password = get_password_hash("IbraGold@1")
            admin_user = User(
                email="AdminIbra@gmail.com",
                hashed_password=hashed_password,
                name="IbraGold",
                role="admin"
            )
            db.add(admin_user)
            db.commit()
            db.refresh(admin_user)
            print("Admin user created successfully!")
            # Initialize admin progress
            initialize_user_progress(db, admin_user.id)
            initialize_user_quiz_progress(db, admin_user.id)
        else:
            print("Admin user already exists!")
    except Exception as e:
        print(f"Error creating admin user: {e}")
    finally:
        db.close()

# Create admin user on startup
create_admin_user()

# Remove demo student user if it exists
def remove_demo_student():
    db = SessionLocal()
    try:
        demo_user = db.query(User).filter(User.email == "student@alu.edu").first()
        if demo_user:
            # Delete user's progress and activities
            db.query(UserProgress).filter(UserProgress.user_id == demo_user.id).delete()
            db.query(UserQuizProgress).filter(UserQuizProgress.user_id == demo_user.id).delete()
            db.query(UserActivity).filter(UserActivity.user_id == demo_user.id).delete()
            # Delete the user
            db.delete(demo_user)
            db.commit()
            print("Demo student user removed successfully!")
        else:
            print("Demo student user not found!")
    except Exception as e:
        print(f"Error removing demo student: {e}")
    finally:
        db.close()

# Remove demo student on startup
remove_demo_student()



# --- Endpoints ---
@app.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password, name=user.name, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    initialize_user_progress(db, new_user.id)
    initialize_user_quiz_progress(db, new_user.id)
    return new_user

@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/me", response_model=UserOut)
def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = get_user(db, email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# --- Quiz Endpoints ---
@app.get("/quiz/{subject_id}/{level_id}")
def get_quiz(subject_id: int, level_id: int, db: Session = Depends(get_db)):
    quiz = db.query(Quiz).filter_by(subject_id=subject_id, level_id=level_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    questions = db.query(Question).filter_by(quiz_id=quiz.id).all()
    question_list = []
    for question in questions:
        choices = db.query(Choice).filter_by(question_id=question.id).all()
        question_list.append({
            "id": question.id,
            "question": question.text,
            "options": [choice.text for choice in choices],
            "correct": next((choice.text for choice in choices if choice.is_correct), None),
            "explanation": None,  # Add if you have an explanation field
            "resources": [],      # Add if you have resources
        })
    return {"title": quiz.title, "questions": question_list}

@app.post("/quiz/{subject_id}/{level_id}/submit")
def submit_quiz(subject_id: int, level_id: int, answers: Dict[int, str] = Body(...), db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    quiz = db.query(Quiz).filter_by(subject_id=subject_id, level_id=level_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    questions = db.query(Question).filter_by(quiz_id=quiz.id).all()
    correct = 0
    total = len(questions)
    for question in questions:
        choices = db.query(Choice).filter_by(question_id=question.id).all()
        correct_choice = next((choice.text for choice in choices if choice.is_correct), None)
        if answers.get(question.id) == correct_choice:
            correct += 1
        print(f"QID: {question.id}, correct_choice: {correct_choice}, user_answer: {answers.get(question.id)}")
    score = int((correct / total) * 100) if total else 0
    user_id = None
    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            user = get_user(db, email)
            if user:
                user_id = user.id
                # Mark this quiz as completed for the user
                quiz_completion = db.query(UserQuizCompletion).filter_by(user_id=user.id, quiz_id=quiz.id).first()
                if not quiz_completion:
                    quiz_completion = UserQuizCompletion(user_id=user.id, quiz_id=quiz.id, completed=True)
                    db.add(quiz_completion)
                else:
                    quiz_completion.completed = True
                db.commit()
                # Check if all quizzes in this level are completed
                quizzes_in_level = db.query(Quiz).filter_by(subject_id=subject_id, level_id=level_id).all()
                all_completed = all(
                    db.query(UserQuizCompletion).filter_by(user_id=user.id, quiz_id=q.id, completed=True).first()
                    for q in quizzes_in_level
                )
                quiz_progress = db.query(UserQuizProgress).filter_by(user_id=user.id, subject_id=subject_id, level_id=level_id).first()
                if all_completed:
                    if quiz_progress:
                        quiz_progress.completed = 1
                    else:
                        quiz_progress = UserQuizProgress(
                            user_id=user.id,
                            subject_id=subject_id,
                            level_id=level_id,
                            completed=1,
                        )
                        db.add(quiz_progress)
                else:
                    if quiz_progress:
                        quiz_progress.completed = 0
                db.commit()
                # --- CHANGED: Always update user progress after any quiz completion ---
                update_user_progress(db, user.id, subject_id)
        except Exception:
            pass
    if user_id:
        log_user_activity(db, user_id, subject_id, level_id, f"Completed Quiz: {quiz.title}", score)
    print("Submitting quiz: correct =", correct, "total =", total, "score =", score)
    print("Received answers:", answers)
    return {"score": score, "correct": correct, "total": total}

# --- Leaderboard Endpoint ---
@app.get("/leaderboard")
def get_leaderboard(period: str = "all-time", db: Session = Depends(get_db)):
    leaderboard = (
        db.query(User, UserProgress)
        .join(UserProgress, User.id == UserProgress.user_id)
        .filter(User.role != "admin")
        .all()
    )
    user_scores = {}
    for user, progress in leaderboard:
        if user.email not in user_scores:
            # NEW: Only count real quiz completions for avgScore
            activities = db.query(UserActivity).filter_by(user_id=user.id).all()
            scores = [a.score for a in activities if a.score is not None and a.action.startswith("Completed Quiz")]
            avg_score = int(sum(scores) / len(scores)) if scores else 0
            user_scores[user.email] = {
                "name": user.email.split("@")[0].replace(".", " ").title(),
                "email": user.email,
                "score": 0,
                "quizzes": 0,
                "avgScore": avg_score,
                "streak": 0,
                "subjects": [],
            }
        user_scores[user.email]["score"] += progress.completed_quizzes
        user_scores[user.email]["quizzes"] += progress.completed_quizzes
        # Use the database for subject name lookup
        subject = db.query(Subject).filter_by(id=progress.subject_id).first()
        subject_name = subject.name if subject else ""
        user_scores[user.email]["subjects"].append(subject_name)
    leaderboard_list = list(user_scores.values())
    leaderboard_list.sort(key=lambda x: x["score"], reverse=True)
    for i, entry in enumerate(leaderboard_list):
        entry["rank"] = i + 1
    return {"period": period, "data": leaderboard_list}

# --- API Endpoints ---
@app.get("/subjects")
def get_subjects(db: Session = Depends(get_db)):
    subjects = db.query(Subject).all()
    result = []
    for subject in subjects:
        result.append({
            "id": subject.id,
            "name": subject.name,
            "description": subject.description,
        })
    return result

@app.get("/subjects/{subject_id}")
def get_subject(subject_id: int, db: Session = Depends(get_db)):
    subject = db.query(Subject).filter_by(id=subject_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    # Optionally include levels and quizzes if needed
    levels = db.query(Level).filter_by(subject_id=subject.id).order_by(Level.level_number).all()
    level_list = []
    for level in levels:
        quizzes = db.query(Quiz).filter_by(subject_id=subject.id, level_id=level.id).all()
        quiz_list = []
        for quiz in quizzes:
            quiz_list.append({
                "id": quiz.id,
                "title": quiz.title,
            })
        level_list.append({
            "id": level.id,
            "name": level.name,
            "description": level.description,
            "level_number": level.level_number,
            "quizzes": quiz_list,
        })
    return {
        "id": subject.id,
        "name": subject.name,
        "description": subject.description,
        "levels": level_list,
    }

@app.get("/dashboard-data")
def get_dashboard_data(db: Session = Depends(get_db)):
    # Total quizzes completed (all users)
    total_completed = db.query(UserQuizCompletion).filter_by(completed=True).count()
    # Average score (all users, all activities with a score)
    activities_with_score = db.query(UserActivity).filter(UserActivity.score != None).all()
    scores = [a.score for a in activities_with_score if a.score is not None]
    avg_score = int(sum(scores) / len(scores)) if scores else 0
    # Recent activity (last 10)
    recent_activities = db.query(UserActivity).order_by(UserActivity.timestamp.desc()).limit(10).all()
    recent = []
    for act in recent_activities:
        # Get subject name
        subject = db.query(Subject).filter_by(id=act.subject_id).first()
        subject_name = subject.name if subject else ""
        recent.append({
            "subject": subject_name,
            "action": act.action,
            "time": act.timestamp,
            "score": act.score,
        })
    # Compose stats
    stats = [
        {"label": "Total Quizzes Completed", "value": total_completed, "icon": "BookOpen", "color": "text-blue-600"},
        {"label": "Average Score", "value": f"{avg_score}%", "icon": "Target", "color": "text-green-600"},
        {"label": "Current Streak", "value": "-", "icon": "TrendingUp", "color": "text-purple-600"},
        {"label": "Rank Position", "value": "-", "icon": "Trophy", "color": "text-yellow-600"},
    ]
    return {"stats": stats, "recentActivity": recent}

@app.get("/user/subjects")
def get_user_subjects(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    user = get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    subjects = db.query(Subject).all()
    result = []
    for subject in subjects:
        subj = {
            "id": subject.id,
            "name": subject.name,
            "description": subject.description,
            "icon": getattr(subject, "icon", ""),
            "color": getattr(subject, "color", ""),
        }
        # Sort levels by level_number (default to id if missing)
        levels = db.query(Level).filter(Level.subject_id == subject.id).order_by(getattr(Level, 'level_number', Level.id)).all()
        # --- CHANGED: Count quizzes and completed quizzes per quiz, not per level ---
        all_quizzes = db.query(Quiz).filter_by(subject_id=subject.id).all()
        total_quizzes = len(all_quizzes)
        completed_quizzes = 0
        for quiz in all_quizzes:
            quiz_completion = db.query(UserQuizCompletion).filter_by(user_id=user.id, quiz_id=quiz.id, completed=True).first()
            if quiz_completion:
                completed_quizzes += 1
        subj["completedQuizzes"] = completed_quizzes
        subj["totalQuizzes"] = total_quizzes
        subj["progress"] = int((completed_quizzes / total_quizzes) * 100) if total_quizzes else 0
        # --- NEW: Add estimatedTime for the subject (sum of all quizzes * 5 min) ---
        subj["estimatedTime"] = f"{total_quizzes * 5} min"
        level_list = []
        prev_completed = True
        found_current = False
        for level in levels:
            quizzes = db.query(Quiz).filter(Quiz.subject_id == subject.id, Quiz.level_id == level.id).all()
            num_quizzes = len(quizzes)
            qp = next((qp for qp in db.query(UserQuizProgress).filter_by(user_id=user.id, subject_id=subject.id, level_id=level.id)), None)
            completed = qp.completed == 1 if qp else False
            unlocked = prev_completed if level_list else True
            current = False
            if unlocked and not completed and not found_current:
                current = True
                found_current = True
            quiz_list = []
            for quiz in quizzes:
                quiz_completed = db.query(UserQuizCompletion).filter_by(user_id=user.id, quiz_id=quiz.id, completed=True).first() is not None
                quiz_list.append({
                    "id": quiz.id,
                    "title": quiz.title,
                    "completed": quiz_completed,
                })
            level_number = getattr(level, 'level_number', None)
            # --- NEW: Add estimatedTime for the level (num_quizzes * 5 min) ---
            estimated_time = f"{num_quizzes * 5} min"
            level_list.append({
                "id": level.id,
                "name": level.name,
                "description": level.description,
                "quizzes": quiz_list,
                "completed": completed,
                "unlocked": unlocked,
                "current": current,
                "level_number": level_number,
                "estimatedTime": estimated_time,
                "topics": getattr(level, 'topics', []),
            })
            prev_completed = completed
        subj["levels"] = level_list
        subj["totalLevels"] = len(level_list)
        subj["currentLevel"] = (
            next(
                (lvl["level_number"] for lvl in level_list if lvl["current"] and lvl["level_number"] is not None),
                None
            )
            or next((i + 1 for i, lvl in enumerate(level_list) if lvl["current"]), len(level_list))
        )
        result.append(subj)
    return result

@app.post("/user/subjects/{subject_id}/levels/{level_id}/complete")
def complete_quiz_level(subject_id: int, level_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    user = get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    quiz_progress = db.query(UserQuizProgress).filter_by(user_id=user.id, subject_id=subject_id, level_id=level_id).first()
    if not quiz_progress:
        raise HTTPException(status_code=404, detail="Quiz progress not found")
    quiz_progress.completed = 1
    db.commit()
    update_user_progress(db, user.id, subject_id)
    return {"completed": True}

# --- Helper: Initialize Progress for New User ---
def initialize_user_progress(db, user_id):
    subjects = db.query(Subject).all()
    for subject in subjects:
        quiz_count = db.query(Quiz).filter(Quiz.subject_id == subject.id).count()
        progress = UserProgress(
            user_id=user_id,
            subject_id=subject.id,
            progress=0,
            completed_quizzes=0,
            total_quizzes=quiz_count,
        )
        db.add(progress)
    db.commit()

# --- Helper: Initialize Quiz Progress for New User ---
def initialize_user_quiz_progress(db, user_id):
    subjects = db.query(Subject).all()
    for subject in subjects:
        levels = db.query(Level).filter(Level.subject_id == subject.id).all()
        for level in levels:
            quiz_progress = db.query(UserQuizProgress).filter_by(
                user_id=user_id, subject_id=subject.id, level_id=level.id
            ).first()
            if not quiz_progress:
                quiz_progress = UserQuizProgress(
                    user_id=user_id,
                    subject_id=subject.id,
                    level_id=level.id,
                    completed=0,
                )
                db.add(quiz_progress)
    db.commit()

# --- Log Activity Helper ---
def log_user_activity(db, user_id, subject_id, level_id, action, score=None):
    # Update if exists, else create new
    activity = db.query(UserActivity).filter_by(user_id=user_id, subject_id=subject_id, level_id=level_id).first()
    if activity:
        activity.action = action
        activity.timestamp = datetime.utcnow().isoformat()
        activity.score = score
    else:
        activity = UserActivity(
            user_id=user_id,
            subject_id=subject_id,
            level_id=level_id,
            action=action,
            timestamp=datetime.utcnow().isoformat(),
            score=score,
        )
        db.add(activity)
    db.commit()

# --- Endpoint: Get User Activity ---
@app.get("/user/activity")
def get_user_activity(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    user = get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    activities = db.query(UserActivity).filter_by(user_id=user.id).order_by(UserActivity.timestamp.desc()).limit(10).all()
    result = []
    for act in activities:
        # Use the database for subject lookup
        subject = db.query(Subject).filter_by(id=act.subject_id).first()
        subject_name = subject.name if subject else ""
        # Optionally, you can also look up the level name if needed
        result.append({
            "subject": subject_name,
            "action": act.action,
            "level_id": act.level_id,
            "time": act.timestamp,
            "score": act.score,
        })
    return result

# --- Admin: Add Subject ---
@app.post("/admin/add-subject")
def add_subject(subject: dict, admin_user: User = Depends(get_current_admin_user)):
    # In production, validate and save to DB
    subject["id"] = max(s["id"] for s in SUBJECTS) + 1 if SUBJECTS else 1
    SUBJECTS.append(subject)
    return {"success": True, "subject": subject}

# --- Admin: Add Level/Question to Subject ---
@app.post("/admin/add-level")
def add_level(data: dict, admin_user: User = Depends(get_current_admin_user)):
    subject_id = data.get("subject_id")
    level = data.get("level")
    subject = next((s for s in SUBJECTS if s["id"] == subject_id), None)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    level["id"] = max((l["id"] for l in subject["levels"]), default=0) + 1
    subject["levels"].append(level)
    return {"success": True, "level": level}

# --- Endpoint: Get User Stats for Dashboard ---
@app.get("/user/stats")
def get_user_stats(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    user = get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Count completed quizzes (not levels)
    total_completed = db.query(UserQuizCompletion).filter_by(user_id=user.id, completed=True).count()
    # NEW: Only count real quiz completions for avgScore
    activities = db.query(UserActivity).filter_by(user_id=user.id).all()
    scores = [a.score for a in activities if a.score is not None and a.action.startswith("Completed Quiz")]
    avg_score = int(sum(scores) / len(scores)) if scores else 0
    # Streak: count consecutive days with activity
    days = set(a.timestamp.strftime("%Y-%m-%d") for a in activities)
    today = datetime.utcnow().date()
    streak = 0
    for i in range(0, 100):
        day = (today - timedelta(days=i)).isoformat()
        if day in days:
            streak += 1
        else:
            break
    # Calculate total points (each quiz completed = 10 points + score points)
    total_points = 0
    quiz_progress_list = db.query(UserQuizProgress).filter(UserQuizProgress.user_id == user.id).all()
    for qp in quiz_progress_list:
        if qp.completed == 1:
            # Base points for completing quiz
            total_points += 10
            # Add score points from activity
            activity = db.query(UserActivity).filter_by(
                user_id=user.id, 
                subject_id=qp.subject_id, 
                level_id=qp.level_id
            ).first()
            if activity and activity.score is not None:
                total_points += activity.score
    # Rank: get from leaderboard
    leaderboard = (
        db.query(User, UserProgress)
        .join(UserProgress, User.id == UserProgress.user_id)
        .all()
    )
    user_scores = {}
    for u, progress in leaderboard:
        if u.email not in user_scores:
            user_scores[u.email] = 0
        user_scores[u.email] += progress.completed_quizzes
    sorted_users = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
    rank = next((i + 1 for i, (email, _) in enumerate(sorted_users) if email == user.email), None)
    return {
        "totalCompleted": total_completed,
        "avgScore": avg_score,
        "streak": streak,
        "rank": rank or "-",
        "totalPoints": total_points,
    }

# --- Endpoint: Get Total Students Count ---
@app.get("/total-students")
def get_total_students(db: Session = Depends(get_db)):
    # Only count users who have at least one activity (i.e., have signed in and done something)
    active_user_ids = db.query(UserActivity.user_id).distinct()
    total_users = db.query(User).filter(User.id.in_(active_user_ids)).count()
    return {"totalStudents": total_users}

def update_user_progress(db, user_id, subject_id):
    # Count completed quizzes for this subject (per-quiz, not per-level)
    subject = next((s for s in SUBJECTS if s["id"] == subject_id), None)
    if not subject:
        return
    # Get all quizzes for this subject
    all_quizzes = db.query(Quiz).filter_by(subject_id=subject_id).all()
    total_quizzes = len(all_quizzes)
    # Count how many quizzes are completed by the user
    completed_quizzes = 0
    for quiz in all_quizzes:
        quiz_completion = db.query(UserQuizCompletion).filter_by(user_id=user_id, quiz_id=quiz.id, completed=True).first()
        if quiz_completion:
            completed_quizzes += 1
    progress = int((completed_quizzes / total_quizzes) * 100) if total_quizzes else 0
    # Update UserProgress
    user_progress = db.query(UserProgress).filter_by(user_id=user_id, subject_id=subject_id).first()
    if user_progress:
        user_progress.completed_quizzes = completed_quizzes
        user_progress.progress = progress
        user_progress.total_quizzes = total_quizzes
        db.commit()

@app.post("/admin/initialize-quiz-progress")
def admin_initialize_quiz_progress(admin_user: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    initialize_user_quiz_progress(db, admin_user.id)
    return {"status": "initialized"}

@app.get("/admin/users", response_model=List[UserWithProgress])
def get_all_users(admin_user: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    users = db.query(User).all()
    result = []
    for user in users:
        # Get user progress
        quiz_progress_list = db.query(UserQuizProgress).filter(UserQuizProgress.user_id == user.id).all()
        total_completed = sum(1 for qp in quiz_progress_list if qp.completed == 1)
        
        # Get average score
        activities = db.query(UserActivity).filter_by(user_id=user.id).all()
        scores = [a.score for a in activities if a.score is not None]
        avg_score = float(sum(scores) / len(scores)) if scores else 0.0
        
        # Get last activity
        last_activity = db.query(UserActivity).filter_by(user_id=user.id).order_by(UserActivity.timestamp.desc()).first()
        last_activity_time = last_activity.timestamp if last_activity else ""
        # Ensure last_activity_time is a string
        if last_activity_time and not isinstance(last_activity_time, str):
            last_activity_time = last_activity_time.isoformat()
        result.append(UserWithProgress(
            id=user.id,
            email=user.email,
            name=user.name,
            role=user.role,
            total_completed=total_completed,
            avg_score=avg_score,
            last_activity=last_activity_time
        ))
    return result

@app.get("/admin/user/{user_id}/progress")
def get_user_progress(user_id: int, admin_user: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get all progress for this user
    quiz_progress_list = db.query(UserQuizProgress).filter(UserQuizProgress.user_id == user.id).all()
    activities = db.query(UserActivity).filter_by(user_id=user.id).order_by(UserActivity.timestamp.desc()).all()
    
    # Group by subject
    subject_progress = {}
    for qp in quiz_progress_list:
        if qp.subject_id not in subject_progress:
            subject_progress[qp.subject_id] = {"completed": 0, "total": 0}
        if qp.completed == 1:
            subject_progress[qp.subject_id]["completed"] += 1
        subject_progress[qp.subject_id]["total"] += 1
    
    # Get subject names
    subject_names = {s["id"]: s["name"] for s in SUBJECTS}
    
    result = {
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "role": user.role
        },
        "subjects": [
            {
                "id": subject_id,
                "name": subject_names.get(subject_id, f"Subject {subject_id}"),
                "completed": progress["completed"],
                "total": progress["total"],
                "percentage": int((progress["completed"] / progress["total"]) * 100) if progress["total"] > 0 else 0
            }
            for subject_id, progress in subject_progress.items()
        ],
        "recent_activities": [
            {
                "action": act.action,
                "timestamp": act.timestamp,
                "score": act.score,
                "subject_id": act.subject_id,
                "level_id": act.level_id
            }
            for act in activities[:10]  # Last 10 activities
        ]
    }
    return result

@app.delete("/admin/user/{user_id}")
def delete_user(user_id: int, admin_user: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Don't allow admin to delete themselves
    if user.id == admin_user.id:
        raise HTTPException(status_code=400, detail="Cannot delete your own account")
    
    # Protect the original creator admin (AdminIbra@gmail.com)
    if user.email == "AdminIbra@gmail.com":
        raise HTTPException(status_code=400, detail="Cannot delete the original creator admin account")
    
    # Check if this is the last admin user
    if user.role == "admin":
        admin_count = db.query(User).filter(User.role == "admin").count()
        if admin_count <= 1:
            raise HTTPException(status_code=400, detail="Cannot delete the last admin user")
    
    # Delete user's progress and activities
    db.query(UserProgress).filter(UserProgress.user_id == user_id).delete()
    db.query(UserQuizProgress).filter(UserQuizProgress.user_id == user_id).delete()
    db.query(UserActivity).filter(UserActivity.user_id == user_id).delete()
    
    # Delete the user
    db.delete(user)
    db.commit()
    
    return {"message": "User deleted successfully"}

@app.post("/admin/create-admin")
def create_admin_user(user_data: dict, admin_user: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    email = user_data.get("email")
    password = user_data.get("password")
    name = user_data.get("name", "")
    
    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password are required")
    
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    
    # Create new admin user
    hashed_password = get_password_hash(password)
    new_admin = User(
        email=email,
        hashed_password=hashed_password,
        name=name,
        role="admin"
    )
    
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    
    # Initialize progress for the new admin
    initialize_user_progress(db, new_admin.id)
    initialize_user_quiz_progress(db, new_admin.id)
    
    return {"message": "Admin user created successfully", "user": {"id": new_admin.id, "email": new_admin.email, "name": new_admin.name}}

@app.post("/admin/repair-user-stats")
def admin_repair_user_stats(admin_user: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    users = db.query(User).all()
    repaired = 0
    for user in users:
        quiz_progress_list = db.query(UserQuizProgress).filter(UserQuizProgress.user_id == user.id).all()
        # Build a lookup for quick access
        qp_lookup = {(qp.subject_id, qp.level_id): qp for qp in quiz_progress_list}
        for subject in SUBJECTS:
            for level in subject["levels"]:
                key = (subject["id"], level["id"])
                qp = qp_lookup.get(key)
                # If quiz progress exists and is completed, ensure activity exists
                if qp and qp.completed == 1:
                    # Check for activity
                    activity = db.query(UserActivity).filter_by(
                        user_id=user.id,
                        subject_id=subject["id"],
                        level_id=level["id"]
                    ).first()
                    if not activity:
                        # Only create activity if a score is available (from another activity)
                        score_activity = db.query(UserActivity).filter_by(
                            user_id=user.id,
                            subject_id=subject["id"],
                            level_id=level["id"]
                        ).filter(UserActivity.score != None).first()
                        if score_activity:
                            log_user_activity(db, user.id, subject["id"], level["id"], f"Completed Quiz: {level['name']}", score_activity.score)
                # If quiz progress does not exist but should (e.g., user has activity), create it
                elif not qp:
                    # Check for activity
                    activity = db.query(UserActivity).filter_by(
                        user_id=user.id,
                        subject_id=subject["id"],
                        level_id=level["id"]
                    ).first()
                    if activity:
                        quiz_progress = UserQuizProgress(
                            user_id=user.id,
                            subject_id=subject["id"],
                            level_id=level["id"],
                            completed=1,
                        )
                        db.add(quiz_progress)
                        db.commit()
                # Optionally, you could also check for missing UserProgress and update
            # Update UserProgress for this subject
            update_user_progress(db, user.id, subject["id"])
        repaired += 1
    return {"status": "repaired", "users": repaired}

@app.post("/admin/reset-user-progress/{user_id}")
def admin_reset_user_progress(user_id: int, admin_user: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Delete user's progress, activities, and goals
    db.query(UserProgress).filter(UserProgress.user_id == user_id).delete()
    db.query(UserQuizProgress).filter(UserQuizProgress.user_id == user_id).delete()
    db.query(UserActivity).filter(UserActivity.user_id == user_id).delete()
    db.query(UserGoal).filter(UserGoal.user_id == user_id).delete()
    db.commit()
    # Re-initialize progress for the user
    initialize_user_progress(db, user_id)
    initialize_user_quiz_progress(db, user_id)
    return {"message": "User progress and goals reset successfully"}

# --- API: Add User Goal ---
@app.post("/user/goals")
def add_user_goal(goal: dict = Body(...), token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    user = get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_goal = UserGoal(
        user_id=user.id,
        type=goal.get("type"),
        target=goal.get("target"),
        deadline=goal.get("deadline"),
        description=goal.get("description"),
        created_at=datetime.utcnow().isoformat(),
    )
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return {"message": "Goal saved", "goal": {
        "id": new_goal.id,
        "type": new_goal.type,
        "target": new_goal.target,
        "deadline": new_goal.deadline,
        "description": new_goal.description,
        "created_at": new_goal.created_at,
    }}

# --- API: Get User Goals ---
@app.get("/user/goals")
def get_user_goals(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    user = get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    goals = db.query(UserGoal).filter_by(user_id=user.id).order_by(UserGoal.created_at.desc()).all()
    return [{
        "id": g.id,
        "type": g.type,
        "target": g.target,
        "deadline": g.deadline,
        "description": g.description,
        "created_at": g.created_at,
    } for g in goals]

# --- API: Send Challenge to Friend ---
@app.post("/user/challenge")
def send_challenge(data: dict = Body(...), token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    user = get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    challenge = UserChallenge(
        sender_id=user.id,
        recipient_email=data.get("friendEmail"),
        message=data.get("message"),
        quiz_type=data.get("quizType"),
        created_at=datetime.utcnow().isoformat(),
    )
    db.add(challenge)
    db.commit()
    # --- Email sending placeholder ---
    # You can configure SMTP here. For now, just a placeholder.
    # try:
    #     msg = MIMEText(f"You've been challenged by {user.email}! Message: {data.get('message')}")
    #     msg['Subject'] = 'You have a new quiz challenge!'
    #     msg['From'] = 'noreply@yourapp.com'
    #     msg['To'] = data.get('friendEmail')
    #     s = smtplib.SMTP('localhost')
    #     s.send_message(msg)
    #     s.quit()
    # except Exception as e:
    #     print('Email send failed:', e)
    return {"message": "Challenge sent! (Email sending placeholder)", "challenge": {
        "id": challenge.id,
        "recipient_email": challenge.recipient_email,
        "message": challenge.message,
        "quiz_type": challenge.quiz_type,
        "created_at": challenge.created_at,
    }}

# --- API: Get Challenges for User (by email) ---
@app.get("/user/challenges")
def get_user_challenges(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    user = get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    challenges = db.query(UserChallenge).filter_by(recipient_email=user.email).order_by(UserChallenge.created_at.desc()).all()
    return [{
        "id": c.id,
        "sender_id": c.sender_id,
        "recipient_email": c.recipient_email,
        "message": c.message,
        "quiz_type": c.quiz_type,
        "created_at": c.created_at,
    } for c in challenges]

@app.post("/admin/cleanup-null-activity")
def admin_cleanup_null_activity(admin_user: User = Depends(get_current_admin_user), db: Session = Depends(get_db)):
    deleted = db.query(UserActivity).filter(UserActivity.score == None).delete()
    db.commit()
    return {"deleted": deleted, "message": "Removed UserActivity records with null score."}

# --- New Endpoint: Get Quiz by Quiz ID ---
@app.get("/quiz/{quiz_id}")
def get_quiz_by_id(quiz_id: int, db: Session = Depends(get_db)):
    quiz = db.query(Quiz).filter_by(id=quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    questions = db.query(Question).filter_by(quiz_id=quiz.id).all()
    question_list = []
    for question in questions:
        choices = db.query(Choice).filter_by(question_id=question.id).all()
        question_list.append({
            "id": question.id,
            "question": question.text,
            "options": [choice.text for choice in choices],
            "correct": next((choice.text for choice in choices if choice.is_correct), None),
            "explanation": None,
            "resources": [],
        })
    return {"title": quiz.title, "questions": question_list}

# --- New Endpoint: Submit Quiz by Quiz ID ---
@app.post("/quiz/{quiz_id}/submit")
def submit_quiz_by_id(quiz_id: int, answers: Dict[int, str] = Body(...), db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    quiz = db.query(Quiz).filter_by(id=quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    questions = db.query(Question).filter_by(quiz_id=quiz.id).all()
    correct = 0
    total = len(questions)
    for question in questions:
        choices = db.query(Choice).filter_by(question_id=question.id).all()
        correct_choice = next((choice.text for choice in choices if choice.is_correct), None)
        if answers.get(question.id) == correct_choice:
            correct += 1
    score = int((correct / total) * 100) if total else 0
    user_id = None
    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            user = get_user(db, email)
            if user:
                user_id = user.id
                # Mark this quiz as completed for the user
                quiz_completion = db.query(UserQuizCompletion).filter_by(user_id=user.id, quiz_id=quiz.id).first()
                if not quiz_completion:
                    quiz_completion = UserQuizCompletion(user_id=user.id, quiz_id=quiz.id, completed=True)
                    db.add(quiz_completion)
                else:
                    quiz_completion.completed = True
                db.commit()
                # Check if all quizzes in this level are completed
                quizzes_in_level = db.query(Quiz).filter_by(subject_id=quiz.subject_id, level_id=quiz.level_id).all()
                all_completed = all(
                    db.query(UserQuizCompletion).filter_by(user_id=user.id, quiz_id=q.id, completed=True).first()
                    for q in quizzes_in_level
                )
                quiz_progress = db.query(UserQuizProgress).filter_by(user_id=user.id, subject_id=quiz.subject_id, level_id=quiz.level_id).first()
                if all_completed:
                    if quiz_progress:
                        quiz_progress.completed = 1
                    else:
                        quiz_progress = UserQuizProgress(
                            user_id=user.id,
                            subject_id=quiz.subject_id,
                            level_id=quiz.level_id,
                            completed=1,
                        )
                        db.add(quiz_progress)
                else:
                    if quiz_progress:
                        quiz_progress.completed = 0
                db.commit()
                update_user_progress(db, user.id, quiz.subject_id)
        except Exception:
            pass
    if user_id:
        log_user_activity(db, user_id, quiz.subject_id, quiz.level_id, f"Completed Quiz: {quiz.title}", score)
    return {"score": score, "correct": correct, "total": total}