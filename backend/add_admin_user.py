import sqlite3
from passlib.context import CryptContext

DB_PATH = 'users.db'
ADMIN_NAME = 'IbraGold'
ADMIN_EMAIL = 'AdminIbra@gmail.com'
ADMIN_PASSWORD = 'IbraGold@1'
ADMIN_ROLE = 'admin'

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def add_columns_if_missing(conn):
    cursor = conn.cursor()
    # Add 'name' column if missing
    cursor.execute("PRAGMA table_info(users)")
    columns = [row[1] for row in cursor.fetchall()]
    if 'name' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN name TEXT DEFAULT ''")
    if 'role' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'user'")
    conn.commit()

def insert_admin_user(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (ADMIN_EMAIL,))
    if cursor.fetchone() is None:
        hashed_password = get_password_hash(ADMIN_PASSWORD)
        cursor.execute(
            "INSERT INTO users (email, hashed_password, name, role) VALUES (?, ?, ?, ?)",
            (ADMIN_EMAIL, hashed_password, ADMIN_NAME, ADMIN_ROLE)
        )
        conn.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")

def main():
    conn = sqlite3.connect(DB_PATH)
    add_columns_if_missing(conn)
    insert_admin_user(conn)
    conn.close()

if __name__ == "__main__":
    main() 