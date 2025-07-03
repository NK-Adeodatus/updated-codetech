from fastapi import FastAPI, HTTPException, Depends, status, Body, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing import Optional, List, Dict
import sqlite3
import os
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta

# --- Config ---
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# --- DB Setup ---
DATABASE_URL = "sqlite:///./users.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class UserProgress(Base):
    __tablename__ = "user_progress"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    subject_id = Column(Integer)
    progress = Column(Integer, default=0)  # percent
    completed_quizzes = Column(Integer, default=0)
    total_quizzes = Column(Integer, default=0)

    user = relationship("User")

class UserQuizProgress(Base):
    __tablename__ = "user_quiz_progress"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    subject_id = Column(Integer)
    level_id = Column(Integer)
    completed = Column(Integer, default=0)  # 0 = not started, 1 = completed
    user = relationship("User")

class UserActivity(Base):
    __tablename__ = "user_activity"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    subject_id = Column(Integer)
    level_id = Column(Integer)
    action = Column(String)
    timestamp = Column(String)
    score = Column(Integer, default=None)
    user = relationship("User")

Base.metadata.create_all(bind=engine)

# --- Auth ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# --- Schemas ---
class UserCreate(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserOut(BaseModel):
    id: int
    email: str
    class Config:
        orm_mode = True

# --- Sample Quiz Data (move to DB in production) ---
QUIZ_DATA = {
    1: {  # Python Programming
        1: {
            "title": "Python Variables & Data Types",
            "description": "Test your understanding of Python variables and basic data types",
            "questions": [
                {
                    "id": 1,
                    "question": "Which of the following is NOT a valid Python variable name?",
                    "options": ["my_var", "2variable", "_private", "Variable"],
                    "correct": "2variable",
                    "explanation": "Variable names in Python cannot start with a number. They must start with a letter or underscore.",
                    "resources": [
                        {"title": "Python Variable Naming Rules", "url": "https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator"},
                        {"title": "PEP 8 Style Guide", "url": "https://pep8.org/"},
                    ],
                },
                {
                    "id": 2,
                    "question": "What is the data type of the value 3.14 in Python?",
                    "options": ["int", "float", "double", "decimal"],
                    "correct": "float",
                    "explanation": "In Python, decimal numbers are represented as float data type.",
                    "resources": [
                        {"title": "Python Numeric Types", "url": "https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex"},
                    ],
                },
            ],
        },
    },
    2: {  # Machine Learning
        1: {
            "title": "ML Fundamentals",
            "description": "Test your understanding of basic ML concepts",
            "questions": [
                {
                    "id": 1,
                    "question": "What is the main goal of supervised learning?",
                    "options": [
                        "Find hidden patterns",
                        "Learn from labeled data",
                        "Reduce dimensionality",
                        "Cluster similar data",
                    ],
                    "correct": "Learn from labeled data",
                    "explanation": "Supervised learning uses labeled training data to learn a mapping from inputs to outputs.",
                    "resources": [
                        {"title": "Supervised Learning Overview", "url": "https://scikit-learn.org/stable/supervised_learning.html"},
                    ],
                },
                {
                    "id": 2,
                    "question": "What is overfitting in machine learning?",
                    "options": [
                        "Model is too simple",
                        "Model performs well on training but poorly on test data",
                        "Model has too few parameters",
                        "Model trains too slowly",
                    ],
                    "correct": "Model performs well on training but poorly on test data",
                    "explanation": "Overfitting occurs when a model learns the training data too well, including noise, leading to poor generalization.",
                    "resources": [
                        {"title": "Overfitting and Underfitting", "url": "https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html"},
                    ],
                },
            ],
        },
    },
    3: {  # JavaScript
        1: {
            "title": "JavaScript Basics",
            "description": "Test your understanding of JavaScript fundamentals",
            "questions": [
                {
                    "id": 1,
                    "question": "Which of the following is NOT a valid way to declare a variable in JavaScript?",
                    "options": ["var", "let", "const", "int"],
                    "correct": "int",
                    "explanation": "'int' is not a keyword in JavaScript for variable declaration.",
                    "resources": [
                        {"title": "MDN var", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var"},
                    ],
                },
                {
                    "id": 2,
                    "question": "What is the output of: console.log(typeof null);",
                    "options": ["'object'", "'null'", "'undefined'", "'number'"],
                    "correct": "'object'",
                    "explanation": "In JavaScript, typeof null returns 'object' due to legacy reasons.",
                    "resources": [
                        {"title": "MDN typeof", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof"},
                    ],
                },
            ],
        },
    },
    4: {  # C Programming
        1: {
            "title": "C Basics",
            "description": "Test your understanding of C programming fundamentals",
            "questions": [
                {
                    "id": 1,
                    "question": "Which of the following is the correct syntax to declare an integer variable in C?",
                    "options": ["int x;", "integer x;", "x int;", "var x;"],
                    "correct": "int x;",
                    "explanation": "'int x;' is the correct way to declare an integer variable in C.",
                    "resources": [
                        {"title": "C Variables", "url": "https://www.tutorialspoint.com/cprogramming/c_variables.htm"},
                    ],
                },
                {
                    "id": 2,
                    "question": "What is the output of: printf(\"%d\", 5 + 2 * 3);",
                    "options": ["21", "11", "17", "15"],
                    "correct": "11",
                    "explanation": "Multiplication has higher precedence, so 2*3=6, then 5+6=11.",
                    "resources": [
                        {"title": "C Operator Precedence", "url": "https://www.tutorialspoint.com/cprogramming/c_operators.htm"},
                    ],
                },
            ],
        },
    },
}

LEADERBOARD_DATA = {
    "all-time": [
        {
            "rank": 1,
            "name": "Sarah Johnson",
            "email": "sarah.j@alu.edu",
            "score": 2847,
            "quizzes": 156,
            "avgScore": 94,
            "streak": 23,
            "subjects": ["Python", "ML", "JavaScript"],
        },
        {
            "rank": 2,
            "name": "Michael Chen",
            "email": "michael.c@alu.edu",
            "score": 2756,
            "quizzes": 142,
            "avgScore": 92,
            "streak": 18,
            "subjects": ["Python", "C", "JavaScript"],
        },
        {
            "rank": 3,
            "name": "Amara Okafor",
            "email": "amara.o@alu.edu",
            "score": 2698,
            "quizzes": 138,
            "avgScore": 91,
            "streak": 15,
            "subjects": ["ML", "Python", "JavaScript"],
        },
        {
            "rank": 4,
            "name": "David Kim",
            "email": "david.k@alu.edu",
            "score": 2634,
            "quizzes": 134,
            "avgScore": 89,
            "streak": 12,
            "subjects": ["JavaScript", "Python", "C"],
        },
        {
            "rank": 5,
            "name": "Fatima Al-Rashid",
            "email": "fatima.a@alu.edu",
            "score": 2587,
            "quizzes": 129,
            "avgScore": 88,
            "streak": 20,
            "subjects": ["Python", "ML"],
        },
    ],
    "monthly": [
        {
            "rank": 1,
            "name": "Sarah Johnson",
            "email": "sarah.j@alu.edu",
            "score": 487,
            "quizzes": 26,
            "avgScore": 95,
            "streak": 23,
            "subjects": ["Python", "ML"],
        },
        {
            "rank": 2,
            "name": "Amara Okafor",
            "email": "amara.o@alu.edu",
            "score": 456,
            "quizzes": 24,
            "avgScore": 93,
            "streak": 15,
            "subjects": ["ML", "JavaScript"],
        },
        {
            "rank": 3,
            "name": "Michael Chen",
            "email": "michael.c@alu.edu",
            "score": 434,
            "quizzes": 22,
            "avgScore": 91,
            "streak": 18,
            "subjects": ["Python", "C"],
        },
    ],
    "weekly": [
        {
            "rank": 1,
            "name": "Fatima Al-Rashid",
            "email": "fatima.a@alu.edu",
            "score": 156,
            "quizzes": 8,
            "avgScore": 97,
            "streak": 20,
            "subjects": ["Python"],
        },
        {
            "rank": 2,
            "name": "Sarah Johnson",
            "email": "sarah.j@alu.edu",
            "score": 142,
            "quizzes": 7,
            "avgScore": 96,
            "streak": 23,
            "subjects": ["ML"],
        },
        {
            "rank": 3,
            "name": "David Kim",
            "email": "david.k@alu.edu",
            "score": 128,
            "quizzes": 6,
            "avgScore": 89,
            "streak": 12,
            "subjects": ["JavaScript"],
        },
    ],
}

# --- Sample Subjects Data ---
SUBJECTS = [
    {
        "id": 1,
        "name": "Python Programming",
        "description": "Master Python fundamentals and advanced concepts step by step",
        "icon": "🐍",
        "color": "bg-blue-500",
        "totalLevels": 5,
        "totalQuizzes": 50,
        "levels": [
            {"id": 1, "name": "Variables & Data Types", "description": "Learn about Python variables, strings, numbers, and basic data types", "quizzes": 10, "estimatedTime": "2 hours", "topics": ["Variables", "Strings", "Numbers", "Booleans", "Type Conversion"]},
            {"id": 2, "name": "Control Structures", "description": "Master if statements, loops, and conditional logic", "quizzes": 12, "estimatedTime": "3 hours", "topics": ["If Statements", "For Loops", "While Loops", "Break & Continue", "Nested Loops"]},
            {"id": 3, "name": "Functions & Modules", "description": "Create reusable code with functions and organize with modules", "quizzes": 10, "estimatedTime": "4 hours", "topics": ["Function Definition", "Parameters", "Return Values", "Scope", "Modules", "Packages"]},
            {"id": 4, "name": "Object-Oriented Programming", "description": "Understand classes, objects, inheritance, and OOP principles", "quizzes": 8, "estimatedTime": "5 hours", "topics": ["Classes", "Objects", "Inheritance", "Polymorphism", "Encapsulation"]},
            {"id": 5, "name": "Advanced Topics", "description": "Explore decorators, generators, context managers, and more", "quizzes": 10, "estimatedTime": "6 hours", "topics": ["Decorators", "Generators", "Context Managers", "Exception Handling", "File I/O"]},
        ],
    },
    {
        "id": 2,
        "name": "Machine Learning",
        "description": "Understand ML algorithms and theoretical foundations",
        "icon": "🤖",
        "color": "bg-purple-500",
        "totalLevels": 4,
        "totalQuizzes": 40,
        "levels": [
            {"id": 1, "name": "ML Fundamentals", "description": "Introduction to machine learning concepts and terminology", "quizzes": 10, "estimatedTime": "3 hours", "topics": ["What is ML", "Types of Learning", "Training vs Testing", "Overfitting", "Cross-validation"]},
            {"id": 2, "name": "Supervised Learning", "description": "Learn about classification and regression algorithms", "quizzes": 10, "estimatedTime": "4 hours", "topics": ["Linear Regression", "Logistic Regression", "Decision Trees", "SVM", "Evaluation Metrics"]},
            {"id": 3, "name": "Unsupervised Learning", "description": "Explore clustering and dimensionality reduction", "quizzes": 10, "estimatedTime": "4 hours", "topics": ["K-Means", "Hierarchical Clustering", "PCA", "t-SNE", "Association Rules"]},
            {"id": 4, "name": "Deep Learning Basics", "description": "Introduction to neural networks and deep learning", "quizzes": 10, "estimatedTime": "5 hours", "topics": ["Neural Networks", "Backpropagation", "CNN", "RNN", "Transfer Learning"]},
        ],
    },
]

# --- Dashboard Data ---
DASHBOARD_DATA = {
    "stats": [
        {"label": "Total Quizzes Completed", "value": 87, "icon": "BookOpen", "color": "text-blue-600"},
        {"label": "Average Score", "value": "82%", "icon": "Target", "color": "text-green-600"},
        {"label": "Current Streak", "value": "5 days", "icon": "TrendingUp", "color": "text-purple-600"},
        {"label": "Rank Position", "value": "#23", "icon": "Trophy", "color": "text-yellow-600"},
    ],
    "recentActivity": [
        {"subject": "Python Programming", "action": "Completed Quiz: Functions Basics", "time": "2 hours ago", "score": 85},
        {"subject": "JavaScript", "action": "Started Level: Modern ES6+", "time": "1 day ago", "score": None},
        {"subject": "Machine Learning", "action": "Completed Quiz: Linear Regression", "time": "2 days ago", "score": 92},
        {"subject": "Python Programming", "action": "Completed Quiz: Loops & Iterations", "time": "3 days ago", "score": 78},
    ],
}

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

# --- Endpoints ---
@app.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)
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
def get_quiz(subject_id: int, level_id: int):
    subject = QUIZ_DATA.get(subject_id, {})
    quiz = subject.get(level_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    # Don't send correct answers to frontend
    questions = [
        {k: v for k, v in q.items() if k != "correct"} for q in quiz["questions"]
    ]
    return {"title": quiz["title"], "description": quiz["description"], "questions": questions}

@app.post("/quiz/{subject_id}/{level_id}/submit")
def submit_quiz(subject_id: int, level_id: int, answers: Dict[int, str] = Body(...), db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    subject = QUIZ_DATA.get(subject_id, {})
    quiz = subject.get(level_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    correct = 0
    total = len(quiz["questions"])
    for q in quiz["questions"]:
        if answers.get(q["id"]) == q["correct"]:
            correct += 1
    score = int((correct / total) * 100) if total else 0
    # Mark quiz as completed for user
    user_id = None
    if token:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            user = get_user(db, email)
            if user:
                user_id = user.id
                quiz_progress = db.query(UserQuizProgress).filter_by(user_id=user.id, subject_id=subject_id, level_id=level_id).first()
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
                db.commit()
                update_user_progress(db, user.id, subject_id)
        except Exception:
            pass
    # Log activity
    if user_id:
        log_user_activity(db, user_id, subject_id, level_id, f"Completed Quiz: {quiz['title']}", score)
    return {"score": score, "correct": correct, "total": total}

# --- Leaderboard Endpoint ---
@app.get("/leaderboard")
def get_leaderboard(period: str = "all-time", db: Session = Depends(get_db)):
    # For demo, rank by total completed quizzes
    leaderboard = (
        db.query(User, UserProgress)
        .join(UserProgress, User.id == UserProgress.user_id)
        .all()
    )
    user_scores = {}
    for user, progress in leaderboard:
        if user.email not in user_scores:
            user_scores[user.email] = {
                "name": user.email.split("@")[0].replace(".", " ").title(),
                "email": user.email,
                "score": 0,
                "quizzes": 0,
                "avgScore": 0,
                "streak": 0,
                "subjects": [],
            }
        user_scores[user.email]["score"] += progress.completed_quizzes
        user_scores[user.email]["quizzes"] += progress.completed_quizzes
        user_scores[user.email]["subjects"].append(next((s["name"] for s in SUBJECTS if s["id"] == progress.subject_id), ""))
    # Convert to list and sort
    leaderboard_list = list(user_scores.values())
    leaderboard_list.sort(key=lambda x: x["score"], reverse=True)
    for i, entry in enumerate(leaderboard_list):
        entry["rank"] = i + 1
    return {"period": period, "data": leaderboard_list}

# --- API Endpoints ---
@app.get("/subjects")
def get_subjects():
    return SUBJECTS

@app.get("/subjects/{subject_id}")
def get_subject(subject_id: int):
    for subject in SUBJECTS:
        if subject["id"] == subject_id:
            return subject
    raise HTTPException(status_code=404, detail="Subject not found")

@app.get("/dashboard-data")
def get_dashboard_data():
    return DASHBOARD_DATA

@app.get("/user/subjects")
def get_user_subjects(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    user = get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    quiz_progress_list = db.query(UserQuizProgress).filter(UserQuizProgress.user_id == user.id).all()
    result = []
    for subject in SUBJECTS:
        subj = subject.copy()
        completed_quizzes = sum(
            1 for qp in quiz_progress_list if qp.subject_id == subject["id"] and qp.completed == 1
        )
        subj["completedQuizzes"] = completed_quizzes
        subj["progress"] = int((completed_quizzes / subject["totalQuizzes"]) * 100) if subject["totalQuizzes"] else 0
        # Level progress and unlocks
        levels = []
        prev_completed = True
        found_current = False
        for i, level in enumerate(subject["levels"]):
            qp = next(
                (qp for qp in quiz_progress_list if qp.subject_id == subject["id"] and qp.level_id == level["id"]),
                None,
            )
            completed = qp.completed == 1 if qp else False
            unlocked = prev_completed if i > 0 else True
            current = False
            if unlocked and not completed and not found_current:
                current = True
                found_current = True
            # Debug logging
            print(f"Subject {subject['id']} Level {level['id']} - completed: {completed}, unlocked: {unlocked}, current: {current}")
            levels.append({
                **level,
                "completed": completed,
                "unlocked": unlocked,
                "current": current,
            })
            prev_completed = completed
        subj["levels"] = levels
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
    for subject in SUBJECTS:
        progress = UserProgress(
            user_id=user_id,
            subject_id=subject["id"],
            progress=0,
            completed_quizzes=0,
            total_quizzes=subject["totalQuizzes"],
        )
        db.add(progress)
    db.commit()

# --- Helper: Initialize Quiz Progress for New User ---
def initialize_user_quiz_progress(db, user_id):
    for subject in SUBJECTS:
        for level in subject["levels"]:
            quiz_progress = db.query(UserQuizProgress).filter_by(user_id=user_id, subject_id=subject["id"], level_id=level["id"]).first()
            if not quiz_progress:
                quiz_progress = UserQuizProgress(
                    user_id=user_id,
                    subject_id=subject["id"],
                    level_id=level["id"],
                    completed=0,
                )
                db.add(quiz_progress)
    db.commit()

# --- Log Activity Helper ---
def log_user_activity(db, user_id, subject_id, level_id, action, score=None):
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
        subject = next((s for s in SUBJECTS if s["id"] == act.subject_id), None)
        level = next((l for l in subject["levels"] if l["id"] == act.level_id), None) if subject else None
        result.append({
            "subject": subject["name"] if subject else "",
            "action": act.action,
            "level": level["name"] if level else "",
            "time": act.timestamp,
            "score": act.score,
        })
    return result

# --- Admin: Add Subject ---
@app.post("/admin/add-subject")
def add_subject(subject: dict, request: Request):
    # In production, validate and save to DB
    subject["id"] = max(s["id"] for s in SUBJECTS) + 1 if SUBJECTS else 1
    SUBJECTS.append(subject)
    return {"success": True, "subject": subject}

# --- Admin: Add Level/Question to Subject ---
@app.post("/admin/add-level")
def add_level(data: dict, request: Request):
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
    # Total quizzes completed
    quiz_progress_list = db.query(UserQuizProgress).filter(UserQuizProgress.user_id == user.id).all()
    total_completed = sum(1 for qp in quiz_progress_list if qp.completed == 1)
    # Average score from activity
    activities = db.query(UserActivity).filter_by(user_id=user.id).all()
    scores = [a.score for a in activities if a.score is not None]
    avg_score = int(sum(scores) / len(scores)) if scores else 0
    # Streak: count consecutive days with activity
    days = set(a.timestamp[:10] for a in activities)
    today = datetime.utcnow().date()
    streak = 0
    for i in range(0, 100):
        day = (today - timedelta(days=i)).isoformat()
        if day in days:
            streak += 1
        else:
            break
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
    }

def update_user_progress(db, user_id, subject_id):
    # Count completed quizzes for this subject
    completed_quizzes = db.query(UserQuizProgress).filter_by(user_id=user_id, subject_id=subject_id, completed=1).count()
    # Get total quizzes for this subject
    subject = next((s for s in SUBJECTS if s["id"] == subject_id), None)
    total_quizzes = subject["totalQuizzes"] if subject else 1
    progress = int((completed_quizzes / total_quizzes) * 100) if total_quizzes else 0
    # Update UserProgress
    user_progress = db.query(UserProgress).filter_by(user_id=user_id, subject_id=subject_id).first()
    if user_progress:
        user_progress.completed_quizzes = completed_quizzes
        user_progress.progress = progress
        db.commit()

@app.post("/admin/initialize-quiz-progress")
def admin_initialize_quiz_progress(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    user = get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    initialize_user_quiz_progress(db, user.id)
    return {"status": "initialized"} 