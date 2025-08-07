# main.py
import tkinter as tk
from login import start_login
from database import init_db
from database import init_db, add_user_column_if_missing


def main():
    init_db()  
    add_user_column_if_missing()

    root = tk.Tk()
    root.title("Expense Management System")
    root.geometry("800x600")
    root.resizable(False, False)
    start_login(root)
    root.mainloop()

if __name__ == "__main__":
    main()
