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
SECRET_KEY = "your-secret-key-change-in-production"
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
    name = Column(String, default="")
    role = Column(String, default="user")

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
    name: str = ""
    role: str = "user"

class Token(BaseModel):
    access_token: str
    token_type: str

class UserOut(BaseModel):
    id: int
    email: str
    name: str = ""
    role: str = "user"
    class Config:
        from_attributes = True

class UserWithProgress(BaseModel):
    id: int
    email: str
    name: str = ""
    role: str = "user"
    total_completed: int = 0
    avg_score: float = 0.0
    last_activity: str = ""
    class Config:
        from_attributes = True

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
            "description": "Variables, types, and operators",
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
                {
                    "id": 3,
                    "question": "Which operator is used for strict equality comparison in JavaScript?",
                    "options": ["==", "===", "=", "!="],
                    "correct": "===",
                    "explanation": "The === operator checks both value and type equality.",
                    "resources": [
                        {"title": "MDN Equality", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness"},
                    ],
                },
                {
                    "id": 4,
                    "question": "What is the result of: 5 + '5' in JavaScript?",
                    "options": ["10", "55", "Error", "undefined"],
                    "correct": "55",
                    "explanation": "JavaScript converts the number to string and concatenates them.",
                    "resources": [
                        {"title": "MDN Type Coercion", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition"},
                    ],
                },
                {
                    "id": 5,
                    "question": "Which of these is a falsy value in JavaScript?",
                    "options": ["'hello'", "1", "0", "true"],
                    "correct": "0",
                    "explanation": "0 is one of the falsy values in JavaScript.",
                    "resources": [
                        {"title": "MDN Falsy", "url": "https://developer.mozilla.org/en-US/docs/Glossary/Falsy"},
                    ],
                },
            ],
        },
        2: {
            "title": "Control Flow",
            "description": "If, else, switch, and loops",
            "questions": [
                {
                    "id": 1,
                    "question": "Which statement is used to skip the current iteration of a loop in JavaScript?",
                    "options": ["break", "continue", "skip", "exit"],
                    "correct": "continue",
                    "explanation": "'continue' skips the current iteration of a loop.",
                    "resources": [
                        {"title": "MDN continue", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue"},
                    ],
                },
                {
                    "id": 2,
                    "question": "Which loop will always execute at least once?",
                    "options": ["for", "while", "do...while", "foreach"],
                    "correct": "do...while",
                    "explanation": "'do...while' executes the block at least once before checking the condition.",
                    "resources": [
                        {"title": "MDN do...while", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while"},
                    ],
                },
                {
                    "id": 3,
                    "question": "What is the output of: for(let i = 0; i < 3; i++) { console.log(i); }",
                    "options": ["0,1,2", "1,2,3", "0,1,2,3", "1,2"],
                    "correct": "0,1,2",
                    "explanation": "The loop runs from 0 to 2 (less than 3).",
                    "resources": [
                        {"title": "MDN for", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for"},
                    ],
                },
                {
                    "id": 4,
                    "question": "Which statement is used to exit a switch case in JavaScript?",
                    "options": ["break", "continue", "return", "exit"],
                    "correct": "break",
                    "explanation": "break is used to exit a switch case.",
                    "resources": [
                        {"title": "MDN switch", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch"},
                    ],
                },
                {
                    "id": 5,
                    "question": "What is the result of: if (0) { console.log('true'); } else { console.log('false'); }",
                    "options": ["true", "false", "Error", "undefined"],
                    "correct": "false",
                    "explanation": "0 is falsy, so the else block executes.",
                    "resources": [
                        {"title": "MDN if...else", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else"},
                    ],
                },
            ],
        },
        3: {
            "title": "Functions & ES6",
            "description": "Functions, arrow functions, and ES6 features",
            "questions": [
                {
                    "id": 1,
                    "question": "How do you define an arrow function in JavaScript?",
                    "options": [
                        "function() => {}",
                        "() => {}",
                        "=> function() {}",
                        "function => {}"
                    ],
                    "correct": "() => {}",
                    "explanation": "Arrow functions use the syntax: () => {}",
                    "resources": [
                        {"title": "MDN Arrow Functions", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions"},
                    ],
                },
                {
                    "id": 2,
                    "question": "Which ES6 feature allows you to declare a block-scoped variable?",
                    "options": ["var", "let", "const", "both let and const"],
                    "correct": "both let and const",
                    "explanation": "'let' and 'const' are block-scoped in ES6.",
                    "resources": [
                        {"title": "MDN let", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let"},
                    ],
                },
                {
                    "id": 3,
                    "question": "What is the output of: const add = (a, b) => a + b; console.log(add(2, 3));",
                    "options": ["5", "23", "Error", "undefined"],
                    "correct": "5",
                    "explanation": "Arrow functions can have implicit return for single expressions.",
                    "resources": [
                        {"title": "MDN Arrow Functions", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions"},
                    ],
                },
                {
                    "id": 4,
                    "question": "Which ES6 feature allows you to extract values from objects?",
                    "options": ["Destructuring", "Spread", "Rest", "Template literals"],
                    "correct": "Destructuring",
                    "explanation": "Destructuring allows you to extract values from objects and arrays.",
                    "resources": [
                        {"title": "MDN Destructuring", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment"},
                    ],
                },
                {
                    "id": 5,
                    "question": "What is the result of: const name = 'John'; console.log(`Hello ${name}!`);",
                    "options": ["Hello John!", "Hello ${name}!", "Error", "undefined"],
                    "correct": "Hello John!",
                    "explanation": "Template literals use backticks and ${} for variable interpolation.",
                    "resources": [
                        {"title": "MDN Template Literals", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals"},
                    ],
                },
            ],
        },
        4: {
            "title": "DOM & Events",
            "description": "Document Object Model and event handling",
            "questions": [
                {
                    "id": 1,
                    "question": "Which method is used to select an element by its ID in JavaScript?",
                    "options": ["getElementById", "querySelector", "getElementsByClassName", "getElementByTag"],
                    "correct": "getElementById",
                    "explanation": "getElementById is used to select an element by its ID.",
                    "resources": [
                        {"title": "MDN getElementById", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById"},
                    ],
                },
                {
                    "id": 2,
                    "question": "Which event is triggered when a user clicks on an HTML element?",
                    "options": ["onchange", "onmouseover", "onclick", "onload"],
                    "correct": "onclick",
                    "explanation": "The 'onclick' event is triggered when an element is clicked.",
                    "resources": [
                        {"title": "MDN onclick", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event"},
                    ],
                },
                {
                    "id": 3,
                    "question": "How do you add an event listener in JavaScript?",
                    "options": ["addEventListener", "onEvent", "attachEvent", "bindEvent"],
                    "correct": "addEventListener",
                    "explanation": "addEventListener is the modern way to add event handlers.",
                    "resources": [
                        {"title": "MDN addEventListener", "url": "https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener"},
                    ],
                },
                {
                    "id": 4,
                    "question": "Which method is used to create a new HTML element?",
                    "options": ["createElement", "newElement", "makeElement", "buildElement"],
                    "correct": "createElement",
                    "explanation": "createElement creates a new HTML element.",
                    "resources": [
                        {"title": "MDN createElement", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement"},
                    ],
                },
                {
                    "id": 5,
                    "question": "How do you change the text content of an element?",
                    "options": ["textContent", "innerHTML", "value", "content"],
                    "correct": "textContent",
                    "explanation": "textContent sets or returns the text content of an element.",
                    "resources": [
                        {"title": "MDN textContent", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent"},
                    ],
                },
            ],
        },
        5: {
            "title": "Arrays & Objects",
            "description": "Working with arrays, objects, and methods",
            "questions": [
                {
                    "id": 1,
                    "question": "Which method adds an element to the end of an array?",
                    "options": ["push", "pop", "shift", "unshift"],
                    "correct": "push",
                    "explanation": "push adds one or more elements to the end of an array.",
                    "resources": [
                        {"title": "MDN push", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push"},
                    ],
                },
                {
                    "id": 2,
                    "question": "How do you access an object property in JavaScript?",
                    "options": ["object.property", "object['property']", "Both A and B", "object->property"],
                    "correct": "Both A and B",
                    "explanation": "You can use dot notation or bracket notation to access object properties.",
                    "resources": [
                        {"title": "MDN Objects", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object"},
                    ],
                },
                {
                    "id": 3,
                    "question": "Which method creates a new array with the results of calling a function for every array element?",
                    "options": ["map", "filter", "reduce", "forEach"],
                    "correct": "map",
                    "explanation": "map creates a new array with the results of calling a function for every array element.",
                    "resources": [
                        {"title": "MDN map", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map"},
                    ],
                },
                {
                    "id": 4,
                    "question": "What is the output of: const arr = [1, 2, 3]; console.log(arr.length);",
                    "options": ["3", "2", "4", "undefined"],
                    "correct": "3",
                    "explanation": "The length property returns the number of elements in an array.",
                    "resources": [
                        {"title": "MDN Array length", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length"},
                    ],
                },
                {
                    "id": 5,
                    "question": "Which method removes the last element from an array?",
                    "options": ["pop", "push", "shift", "unshift"],
                    "correct": "pop",
                    "explanation": "pop removes the last element from an array and returns it.",
                    "resources": [
                        {"title": "MDN pop", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop"},
                    ],
                },
            ],
        },
        6: {
            "title": "Advanced JavaScript",
            "description": "Closures, promises, and modern patterns",
            "questions": [
                {
                    "id": 1,
                    "question": "What is a closure in JavaScript?",
                    "options": ["A function that has access to variables in its outer scope", "A way to close a function", "A type of loop", "A method to end execution"],
                    "correct": "A function that has access to variables in its outer scope",
                    "explanation": "A closure is a function that has access to variables in its outer scope.",
                    "resources": [
                        {"title": "MDN Closures", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures"},
                    ],
                },
                {
                    "id": 2,
                    "question": "Which method is used to handle asynchronous operations in modern JavaScript?",
                    "options": ["async/await", "callbacks", "promises", "All of the above"],
                    "correct": "All of the above",
                    "explanation": "JavaScript supports callbacks, promises, and async/await for asynchronous operations.",
                    "resources": [
                        {"title": "MDN async/await", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function"},
                    ],
                },
                {
                    "id": 3,
                    "question": "What is the output of: Promise.resolve(5).then(x => x * 2).then(console.log);",
                    "options": ["5", "10", "Error", "undefined"],
                    "correct": "10",
                    "explanation": "The promise resolves to 5, then multiplies by 2, resulting in 10.",
                    "resources": [
                        {"title": "MDN Promise", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise"},
                    ],
                },
                {
                    "id": 4,
                    "question": "Which keyword is used to declare an async function?",
                    "options": ["async", "await", "function", "async function"],
                    "correct": "async",
                    "explanation": "The async keyword is used to declare an async function.",
                    "resources": [
                        {"title": "MDN async function", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function"},
                    ],
                },
                {
                    "id": 5,
                    "question": "What is the purpose of the 'this' keyword in JavaScript?",
                    "options": ["Refers to the current object", "Creates a new object", "Ends a function", "Starts a loop"],
                    "correct": "Refers to the current object",
                    "explanation": "The 'this' keyword refers to the current object context.",
                    "resources": [
                        {"title": "MDN this", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this"},
                    ],
                },
            ],
        },
    },
    4: {  # C Programming
        1: {
            "title": "C Basics",
            "description": "Variables, data types, and operators",
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
                {
                    "id": 3,
                    "question": "Which data type is used to store a single character in C?",
                    "options": ["char", "string", "character", "text"],
                    "correct": "char",
                    "explanation": "char is used to store a single character in C.",
                    "resources": [
                        {"title": "C Data Types", "url": "https://www.tutorialspoint.com/cprogramming/c_data_types.htm"},
                    ],
                },
                {
                    "id": 4,
                    "question": "What is the size of an int data type in C (typically)?",
                    "options": ["2 bytes", "4 bytes", "8 bytes", "1 byte"],
                    "correct": "4 bytes",
                    "explanation": "An int is typically 4 bytes on most modern systems.",
                    "resources": [
                        {"title": "C Data Types", "url": "https://www.tutorialspoint.com/cprogramming/c_data_types.htm"},
                    ],
                },
                {
                    "id": 5,
                    "question": "Which operator is used to get the address of a variable?",
                    "options": ["&", "*", "#", "%"],
                    "correct": "&",
                    "explanation": "The & operator is used to get the address of a variable.",
                    "resources": [
                        {"title": "C Pointers", "url": "https://www.tutorialspoint.com/cprogramming/c_pointers.htm"},
                    ],
                },
            ],
        },
        2: {
            "title": "Control Flow",
            "description": "If, else, switch, and loops in C",
            "questions": [
                {
                    "id": 1,
                    "question": "Which statement is used to exit a loop in C?",
                    "options": ["break", "continue", "exit", "stop"],
                    "correct": "break",
                    "explanation": "'break' is used to exit a loop in C.",
                    "resources": [
                        {"title": "C break", "url": "https://www.tutorialspoint.com/cprogramming/c_break_statement.htm"},
                    ],
                },
                {
                    "id": 2,
                    "question": "Which loop will always execute at least once in C?",
                    "options": ["for", "while", "do...while", "foreach"],
                    "correct": "do...while",
                    "explanation": "'do...while' executes the block at least once before checking the condition.",
                    "resources": [
                        {"title": "C do...while", "url": "https://www.tutorialspoint.com/cprogramming/c_do_while_loop.htm"},
                    ],
                },
                {
                    "id": 3,
                    "question": "What is the output of: int i = 0; while(i < 3) { printf(\"%d \", i); i++; }",
                    "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
                    "correct": "0 1 2",
                    "explanation": "The while loop prints 0, 1, 2 and stops when i becomes 3.",
                    "resources": [
                        {"title": "C while loop", "url": "https://www.tutorialspoint.com/cprogramming/c_while_loop.htm"},
                    ],
                },
                {
                    "id": 4,
                    "question": "Which statement is used to skip the current iteration in a loop?",
                    "options": ["continue", "break", "skip", "next"],
                    "correct": "continue",
                    "explanation": "continue skips the current iteration and continues with the next one.",
                    "resources": [
                        {"title": "C continue", "url": "https://www.tutorialspoint.com/cprogramming/c_continue_statement.htm"},
                    ],
                },
                {
                    "id": 5,
                    "question": "What is the result of: if (5 > 3) printf(\"true\"); else printf(\"false\");",
                    "options": ["true", "false", "Error", "Nothing"],
                    "correct": "true",
                    "explanation": "5 is greater than 3, so the if condition is true.",
                    "resources": [
                        {"title": "C if...else", "url": "https://www.tutorialspoint.com/cprogramming/c_if_else_statement.htm"},
                    ],
                },
            ],
        },
        3: {
            "title": "Functions",
            "description": "Functions, parameters, and return values",
            "questions": [
                {
                    "id": 1,
                    "question": "Which keyword is used to define a function in C?",
                    "options": ["function", "def", "void", "int"],
                    "correct": "void",
                    "explanation": "Functions in C are defined with a return type, such as 'void' or 'int'.",
                    "resources": [
                        {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"},
                    ],
                },
                {
                    "id": 2,
                    "question": "How do you return a value from a function in C?",
                    "options": ["return value;", "output value;", "send value;", "give value;"],
                    "correct": "return value;",
                    "explanation": "The 'return' statement is used to return a value from a function.",
                    "resources": [
                        {"title": "C return", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"},
                    ],
                },
                {
                    "id": 3,
                    "question": "What is the output of: int add(int a, int b) { return a + b; } printf(\"%d\", add(3, 4));",
                    "options": ["7", "34", "Error", "Nothing"],
                    "correct": "7",
                    "explanation": "The function adds 3 and 4, returning 7.",
                    "resources": [
                        {"title": "C Functions", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"},
                    ],
                },
                {
                    "id": 4,
                    "question": "Which type of parameter passing copies the value in C?",
                    "options": ["Pass by value", "Pass by reference", "Pass by pointer", "Pass by address"],
                    "correct": "Pass by value",
                    "explanation": "By default, C uses pass by value, which copies the parameter value.",
                    "resources": [
                        {"title": "C Function Parameters", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"},
                    ],
                },
                {
                    "id": 5,
                    "question": "What is a function prototype in C?",
                    "options": ["A function declaration without body", "A function definition", "A function call", "A function pointer"],
                    "correct": "A function declaration without body",
                    "explanation": "A function prototype declares the function signature without the body.",
                    "resources": [
                        {"title": "C Function Prototypes", "url": "https://www.tutorialspoint.com/cprogramming/c_functions.htm"},
                    ],
                },
            ],
        },
        4: {
            "title": "Pointers & Arrays",
            "description": "Pointers, arrays, and memory management",
            "questions": [
                {
                    "id": 1,
                    "question": "Which symbol is used to declare a pointer in C?",
                    "options": ["&", "*", "#", "%"],
                    "correct": "*",
                    "explanation": "The asterisk (*) is used to declare a pointer.",
                    "resources": [
                        {"title": "C Pointers", "url": "https://www.tutorialspoint.com/cprogramming/c_pointers.htm"},
                    ],
                },
                {
                    "id": 2,
                    "question": "How do you access the third element of an array 'arr' in C?",
                    "options": ["arr[2]", "arr(3)", "arr[3]", "arr{2}"],
                    "correct": "arr[2]",
                    "explanation": "Arrays in C are zero-indexed, so arr[2] is the third element.",
                    "resources": [
                        {"title": "C Arrays", "url": "https://www.tutorialspoint.com/cprogramming/c_arrays.htm"},
                    ],
                },
                {
                    "id": 3,
                    "question": "What is the output of: int arr[] = {1, 2, 3}; printf(\"%d\", arr[1]);",
                    "options": ["1", "2", "3", "Error"],
                    "correct": "2",
                    "explanation": "arr[1] accesses the second element (index 1) which is 2.",
                    "resources": [
                        {"title": "C Arrays", "url": "https://www.tutorialspoint.com/cprogramming/c_arrays.htm"},
                    ],
                },
                {
                    "id": 4,
                    "question": "Which function is used to allocate memory dynamically in C?",
                    "options": ["malloc", "alloc", "new", "create"],
                    "correct": "malloc",
                    "explanation": "malloc is used to allocate memory dynamically in C.",
                    "resources": [
                        {"title": "C malloc", "url": "https://www.tutorialspoint.com/cprogramming/c_memory_management.htm"},
                    ],
                },
                {
                    "id": 5,
                    "question": "What is the output of: int *ptr = NULL; printf(\"%p\", ptr);",
                    "options": ["0x0", "NULL", "0", "Error"],
                    "correct": "0x0",
                    "explanation": "NULL pointer typically prints as 0x0 or (nil).",
                    "resources": [
                        {"title": "C NULL Pointer", "url": "https://www.tutorialspoint.com/cprogramming/c_null_pointers.htm"},
                    ],
                },
            ],
        },
        5: {
            "title": "Strings & Structures",
            "description": "String manipulation and structs",
            "questions": [
                {
                    "id": 1,
                    "question": "Which function is used to find the length of a string in C?",
                    "options": ["strlen", "length", "size", "count"],
                    "correct": "strlen",
                    "explanation": "strlen is used to find the length of a string.",
                    "resources": [
                        {"title": "C strlen", "url": "https://www.tutorialspoint.com/cprogramming/c_strings.htm"},
                    ],
                },
                {
                    "id": 2,
                    "question": "How do you declare a structure in C?",
                    "options": ["struct", "structure", "class", "object"],
                    "correct": "struct",
                    "explanation": "The 'struct' keyword is used to declare a structure in C.",
                    "resources": [
                        {"title": "C Structures", "url": "https://www.tutorialspoint.com/cprogramming/c_structures.htm"},
                    ],
                },
                {
                    "id": 3,
                    "question": "Which function is used to copy one string to another?",
                    "options": ["strcpy", "copy", "assign", "move"],
                    "correct": "strcpy",
                    "explanation": "strcpy is used to copy one string to another.",
                    "resources": [
                        {"title": "C strcpy", "url": "https://www.tutorialspoint.com/cprogramming/c_strings.htm"},
                    ],
                },
                {
                    "id": 4,
                    "question": "What is the output of: char str[] = \"Hello\"; printf(\"%d\", strlen(str));",
                    "options": ["5", "6", "4", "Error"],
                    "correct": "5",
                    "explanation": "strlen returns the length of the string excluding the null terminator.",
                    "resources": [
                        {"title": "C strlen", "url": "https://www.tutorialspoint.com/cprogramming/c_strings.htm"},
                    ],
                },
                {
                    "id": 5,
                    "question": "How do you access a member of a structure?",
                    "options": ["structure.member", "structure->member", "Both A and B", "structure[member]"],
                    "correct": "Both A and B",
                    "explanation": "You can use dot (.) for structure variables and arrow (->) for structure pointers.",
                    "resources": [
                        {"title": "C Structures", "url": "https://www.tutorialspoint.com/cprogramming/c_structures.htm"},
                    ],
                },
            ],
        },
        6: {
            "title": "File I/O & Advanced",
            "description": "File operations and advanced concepts",
            "questions": [
                {
                    "id": 1,
                    "question": "Which function is used to open a file in C?",
                    "options": ["fopen", "open", "file", "create"],
                    "correct": "fopen",
                    "explanation": "fopen is used to open a file in C.",
                    "resources": [
                        {"title": "C File I/O", "url": "https://www.tutorialspoint.com/cprogramming/c_file_io.htm"},
                    ],
                },
                {
                    "id": 2,
                    "question": "Which mode opens a file for reading in C?",
                    "options": ["r", "w", "a", "x"],
                    "correct": "r",
                    "explanation": "'r' mode opens a file for reading.",
                    "resources": [
                        {"title": "C File Modes", "url": "https://www.tutorialspoint.com/cprogramming/c_file_io.htm"},
                    ],
                },
                {
                    "id": 3,
                    "question": "Which function is used to read a character from a file?",
                    "options": ["fgetc", "getc", "read", "scanf"],
                    "correct": "fgetc",
                    "explanation": "fgetc is used to read a character from a file.",
                    "resources": [
                        {"title": "C fgetc", "url": "https://www.tutorialspoint.com/cprogramming/c_file_io.htm"},
                    ],
                },
                {
                    "id": 4,
                    "question": "What does #include do in C?",
                    "options": ["Includes a header file", "Defines a macro", "Creates a function", "Declares a variable"],
                    "correct": "Includes a header file",
                    "explanation": "#include is a preprocessor directive that includes header files.",
                    "resources": [
                        {"title": "C Preprocessor", "url": "https://www.tutorialspoint.com/cprogramming/c_preprocessors.htm"},
                    ],
                },
                {
                    "id": 5,
                    "question": "Which function is used to close a file in C?",
                    "options": ["fclose", "close", "end", "finish"],
                    "correct": "fclose",
                    "explanation": "fclose is used to close a file in C.",
                    "resources": [
                        {"title": "C fclose", "url": "https://www.tutorialspoint.com/cprogramming/c_file_io.htm"},
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
    {
        "id": 3,
        "name": "JavaScript",
        "description": "Learn JavaScript concepts and modern ES6+ features",
        "icon": "⚡",
        "color": "bg-yellow-500",
        "totalLevels": 6,
        "totalQuizzes": 30,
        "levels": [
            {"id": 1, "name": "JavaScript Basics", "description": "Variables, types, and operators", "quizzes": 5, "estimatedTime": "1 hour", "topics": ["Variables", "Types", "Operators"]},
            {"id": 2, "name": "Control Flow", "description": "If, else, switch, and loops", "quizzes": 5, "estimatedTime": "1 hour", "topics": ["If", "Else", "Switch", "Loops"]},
            {"id": 3, "name": "Functions & ES6", "description": "Functions, arrow functions, and ES6 features", "quizzes": 5, "estimatedTime": "1 hour", "topics": ["Functions", "Arrow Functions", "ES6"]},
            {"id": 4, "name": "DOM & Events", "description": "Document Object Model and event handling", "quizzes": 5, "estimatedTime": "1 hour", "topics": ["DOM", "Events", "Selectors"]},
            {"id": 5, "name": "Arrays & Objects", "description": "Working with arrays, objects, and methods", "quizzes": 5, "estimatedTime": "1 hour", "topics": ["Arrays", "Objects", "Methods"]},
            {"id": 6, "name": "Advanced JavaScript", "description": "Closures, promises, and modern patterns", "quizzes": 5, "estimatedTime": "1 hour", "topics": ["Closures", "Promises", "Async/Await"]},
        ],
    },
    {
        "id": 4,
        "name": "C Programming",
        "description": "Build strong foundations in C programming language",
        "icon": "⚙️",
        "color": "bg-green-500",
        "totalLevels": 6,
        "totalQuizzes": 30,
        "levels": [
            {"id": 1, "name": "C Basics", "description": "Variables, data types, and operators", "quizzes": 5, "estimatedTime": "1 hour", "topics": ["Variables", "Data Types", "Operators"]},
            {"id": 2, "name": "Control Flow", "description": "If, else, switch, and loops in C", "quizzes": 5, "estimatedTime": "1 hour", "topics": ["If", "Else", "Switch", "Loops"]},
            {"id": 3, "name": "Functions", "description": "Functions, parameters, and return values", "quizzes": 5, "estimatedTime": "1 hour", "topics": ["Functions", "Parameters", "Return Values"]},
            {"id": 4, "name": "Pointers & Arrays", "description": "Pointers, arrays, and memory management", "quizzes": 5, "estimatedTime": "1 hour", "topics": ["Pointers", "Arrays", "Memory"]},
            {"id": 5, "name": "Strings & Structures", "description": "String manipulation and structs", "quizzes": 5, "estimatedTime": "1 hour", "topics": ["Strings", "Structs", "Unions"]},
            {"id": 6, "name": "File I/O & Advanced", "description": "File operations and advanced concepts", "quizzes": 5, "estimatedTime": "1 hour", "topics": ["File I/O", "Preprocessor", "Headers"]},
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

# --- Create Demo Users for Testing ---
def create_demo_users():
    db = SessionLocal()
    try:
        # Create demo student user
        demo_user = db.query(User).filter(User.email == "student@alu.edu").first()
        if not demo_user:
            hashed_password = get_password_hash("password123")
            demo_user = User(
                email="student@alu.edu",
                hashed_password=hashed_password,
                name="Demo Student",
                role="user"
            )
            db.add(demo_user)
            db.commit()
            db.refresh(demo_user)
            print("Demo student user created successfully!")
            # Initialize demo user progress
            initialize_user_progress(db, demo_user.id)
            initialize_user_quiz_progress(db, demo_user.id)
        else:
            print("Demo student user already exists!")
    except Exception as e:
        print(f"Error creating demo user: {e}")
    finally:
        db.close()

# Create demo users on startup
create_demo_users()

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