# main.py
import tkinter as tk
from login import start_login
from database import init_db

def main():
    init_db()  # 🛠️ Call this before launching the app

    root = tk.Tk()
    root.title("Expense Management System")
    root.geometry("800x600")
    root.resizable(False, False)
    start_login(root)
    root.mainloop()

if __name__ == "__main__":
    main()
