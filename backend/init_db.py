import mysql.connector

# --- CONFIGURE THESE ---
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'  # or your MySQL user
MYSQL_PASSWORD = 'adeodatus'
DB_NAME = 'codetech_db'
# -----------------------

def create_database(cursor):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print(f"Database '{DB_NAME}' ensured.")

def create_tables(cursor):
    # users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        hashed_password VARCHAR(255) NOT NULL,
        name VARCHAR(255),
        profile_picture VARCHAR(255),
        bio TEXT,
        role VARCHAR(255) DEFAULT 'user'
    )
    """)
    # subjects
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT
    )
    """)
    # levels
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS levels (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        level_number INT,
        subject_id INT,
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    )
    """)
    # quizzes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quizzes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        subject_id INT,
        level_id INT,
        title VARCHAR(255) NOT NULL,
        FOREIGN KEY (subject_id) REFERENCES subjects(id),
        FOREIGN KEY (level_id) REFERENCES levels(id)
    )
    """)
    # questions
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        quiz_id INT,
        text TEXT NOT NULL,
        FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
    )
    """)
    # choices
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS choices (
        id INT AUTO_INCREMENT PRIMARY KEY,
        question_id INT,
        text TEXT NOT NULL,
        is_correct BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (question_id) REFERENCES questions(id)
    )
    """)
    # user_progress
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_progress (
        id INT AUTO_INCREMENT PRIMARY KEY,
        progress INT DEFAULT 0,
        completed_quizzes INT DEFAULT 0,
        total_quizzes INT DEFAULT 0,
        user_id INT,
        subject_id INT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    )
    """)
    # user_quiz_progress
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_quiz_progress (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        completed INT DEFAULT 0,
        subject_id INT,
        level_id INT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id),
        FOREIGN KEY (level_id) REFERENCES levels(id)
    )
    """)
    # user_activity
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_activity (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        subject_id INT,
        action VARCHAR(255),
        timestamp DATETIME,
        score INT,
        level_id INT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id),
        FOREIGN KEY (level_id) REFERENCES levels(id)
    )
    """)
    # user_quiz_completion
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_quiz_completion (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        quiz_id INT,
        completed BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
    )
    """)
    print("All tables ensured.")

def main():
    # Debug output
    print("DEBUG: Connecting to MySQL with the following credentials:")
    print("  Host:", MYSQL_HOST)
    print("  User:", MYSQL_USER)
    print("  Password:", MYSQL_PASSWORD)

    # Connect to MySQL server (not to a specific DB yet)
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD
    )
    cursor = conn.cursor()
    create_database(cursor)
    conn.database = DB_NAME
    create_tables(cursor)
    cursor.execute("SHOW TABLES")
    print("Tables in database:", cursor.fetchall())
    cursor.close()
    conn.close()
    print("Database and schema setup complete!")

    # Now seed the database
    from seed_main import seed_database
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=DB_NAME
    )
    seed_database(conn)
    conn.close()

if __name__ == "__main__":
    main() 