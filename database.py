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

