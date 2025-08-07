# database.py
import sqlite3

DB_NAME = "expense_mgmt.db"

# Create and expose the connection and cursor for global use
conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = conn.cursor()

# database.py
import sqlite3

DB_NAME = "expense_mgmt.db"

def connect_db():
    import sqlite3
    return sqlite3.connect(DB_NAME)


# Create tables
def init_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            notes TEXT,
            comment TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    
# Add this to database.py
def fetch_expenses():
    cursor.execute("SELECT amount, category, date FROM expenses")
    return cursor.fetchall()

def add_user_column_if_missing():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(expenses)")
    cols = [r[1] for r in cur.fetchall()]
    if "user_id" not in cols:
        cur.execute("ALTER TABLE expenses ADD COLUMN user_id INTEGER")
        conn.commit()
    conn.close()

def get_user_id(username):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username=?", (username,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None

