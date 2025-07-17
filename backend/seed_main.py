# backend/seed_data.py
"""
Seed data and seeding function for initializing the database with important data.
Includes idempotency, transactions, and error handling.
"""

print('seed_data.py run.')
from seed_data.subjects.python_programming import subject_data as python_data
from seed_data.subjects.machine_learning import subject_data as ml_data
from seed_data.subjects.javascript import subject_data as js_data
from seed_data.subjects.c_programming import subject_data as c_data
import mysql.connector

subjects = [
    python_data,
    ml_data,
    js_data,
    c_data,
]

# The seed_database function remains the same and will iterate over this expanded structure.
# For brevity, only the first level of the first subject is shown fully populated above. The rest should be filled similarly.

# The function below is a template for how to insert this new structure into the database.  
def seed_database(conn):
    """
    Insert initial data into the database. Idempotent and safe to run multiple times.
    """
    try:
        cursor = conn.cursor()
        conn.start_transaction()
        for subject in subjects:
            # Insert subject
            cursor.execute("SELECT id FROM subjects WHERE name = %s", (subject["name"],))
            result = cursor.fetchone()
            if result:
                subject_id = result[0]
            else:
                cursor.execute(
                    "INSERT INTO subjects (name, description) VALUES (%s, %s)",
                    (subject["name"], subject["description"])
                )
                subject_id = cursor.lastrowid
            for idx, level in enumerate(subject['levels'], start=1):
                # Check if the level already exists
                cursor.execute(
                    "SELECT id FROM levels WHERE subject_id = %s AND name = %s",
                    (subject_id, level['name'])
                )
                existing = cursor.fetchone()
                if not existing:
                    # Insert the new level with level_number
                    cursor.execute(
                        "INSERT INTO levels (subject_id, name, description, level_number) VALUES (%s, %s, %s, %s)",
                        (subject_id, level['name'], level['description'], idx)
                    )
                    level_id = cursor.lastrowid
                else:
                    # Optionally, update the level_number if you want to keep it in sync
                    cursor.execute(
                        "UPDATE levels SET level_number = %s WHERE id = %s",
                        (idx, existing[0])
                    )
                    level_id = existing[0]
                for quiz in level["quizzes"]:
                    cursor.execute(
                        "SELECT id FROM quizzes WHERE title = %s AND subject_id = %s AND level_id = %s",
                        (quiz["title"], subject_id, level_id)
                    )
                    result = cursor.fetchone()
                    if result:
                        quiz_id = result[0]
                    else:
                        cursor.execute(
                            "INSERT INTO quizzes (title, subject_id, level_id) VALUES (%s, %s, %s)",
                            (quiz["title"], subject_id, level_id)
                        )
                        quiz_id = cursor.lastrowid
                    for question in quiz["questions"]:
                        cursor.execute(
                            "SELECT id FROM questions WHERE quiz_id = %s AND text = %s",
                            (quiz_id, question["text"])
                        )
                        result = cursor.fetchone()
                        if result:
                            question_id = result[0]
                        else:
                            cursor.execute(
                                "INSERT INTO questions (quiz_id, text) VALUES (%s, %s)",
                                (quiz_id, question["text"])
                            )
                            question_id = cursor.lastrowid
                        for choice in question["choices"]:
                            cursor.execute(
                                "SELECT id FROM choices WHERE question_id = %s AND text = %s",
                                (question_id, choice["text"])
                            )
                            result = cursor.fetchone()
                            if not result:
                                cursor.execute(
                                    "INSERT INTO choices (question_id, text, is_correct) VALUES (%s, %s, %s)",
                                    (question_id, choice["text"], choice["is_correct"])
                                )
        conn.commit()
        print("Seed data inserted successfully.")
    except Exception as e:
        conn.rollback()
        print("Error seeding database:", e)
    finally:
        cursor.close() 

def clear_all_tables(conn):
    """
    Delete all data from all tables in the correct order, handling foreign key constraints.
    """
    print('clear_all_tables run.')
    try:
        cursor = conn.cursor()
        # Disable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        # Truncate child tables first, then parents, to reset auto-increment IDs
        cursor.execute("TRUNCATE TABLE choices;")
        cursor.execute("TRUNCATE TABLE questions;")
        cursor.execute("TRUNCATE TABLE quizzes;")
        cursor.execute("TRUNCATE TABLE levels;")
        cursor.execute("TRUNCATE TABLE subjects;")
        cursor.execute("TRUNCATE TABLE user_activity;")
        cursor.execute("TRUNCATE TABLE user_progress;")
        cursor.execute("TRUNCATE TABLE user_quiz_progress;")
        cursor.execute("TRUNCATE TABLE users;")
        # Re-enable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        conn.commit()
        print("All tables cleared successfully.")
    except Exception as e:
        conn.rollback()
        print("Error clearing tables:", e)
    finally:
        cursor.close() 

conn = mysql.connector.connect(
    host='localhost',
    user='myappuser',
    password='adeodatus',
    database='codetech_db'
)

seed_database(conn)
# clear_all_tables(conn)
conn.close()