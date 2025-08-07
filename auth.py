# auth.py - Handles Login and Registration
import tkinter as tk
from tkinter import messagebox

from database import connect_db  # use fresh connections inside functions
from home import home_screen
import session  # <-- import the module, not the value


def login_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Login - Expense Management")

    tk.Label(root, text="Login", font=("Verdana", 28, "bold"), fg="#333").pack(pady=30)
    frame = tk.Frame(root, bg="white")
    frame.pack(pady=20)

    tk.Label(frame, text="Username:", font=("Verdana", 14), bg="white").grid(row=0, column=0, pady=10, sticky="e")
    username_entry = tk.Entry(frame, font=("Verdana", 14), width=30)
    username_entry.grid(row=0, column=1, pady=10, padx=10)

    tk.Label(frame, text="Password:", font=("Verdana", 14), bg="white").grid(row=1, column=0, pady=10, sticky="e")
    password_entry = tk.Entry(frame, show='*', font=("Verdana", 14), width=30)
    password_entry.grid(row=1, column=1, pady=10, padx=10)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT id, username FROM users WHERE username=? AND password=?", (username, password))
        row = cur.fetchone()
        conn.close()

        if row:
            user_id, uname = row[0], row[1]
            # optional debug:
            # print("before set_user, session.session.current_user_id =", session.session.current_user_id)
            session.set_user(user_id, uname)  # <-- CRITICAL: store the logged-in user in the session module
            # print("after  set_user, session.session.current_user_id =", session.session.current_user_id)
            home_screen(root)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def go_to_register():
        register_screen(root)

    tk.Button(root, text="Login", command=login, font=("Verdana", 14), bg="#4CAF50", fg="white", width=20).pack(pady=10)
    tk.Button(root, text="Register", command=go_to_register, font=("Verdana", 14), bg="#2196F3", fg="white", width=20).pack(pady=10)


def register_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Register - Expense Management")

    tk.Label(root, text="Register", font=("Verdana", 28, "bold"), fg="#333").pack(pady=30)
    frame = tk.Frame(root, bg="white")
    frame.pack(pady=20)

    tk.Label(frame, text="Username:", font=("Verdana", 14), bg="white").grid(row=0, column=0, pady=10, sticky="e")
    username_entry = tk.Entry(frame, font=("Verdana", 14), width=30)
    username_entry.grid(row=0, column=1, pady=10, padx=10)

    tk.Label(frame, text="Password:", font=("Verdana", 14), bg="white").grid(row=1, column=0, pady=10, sticky="e")
    password_entry = tk.Entry(frame, show='*', font=("Verdana", 14), width=30)
    password_entry.grid(row=1, column=1, pady=10, padx=10)

    def register():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password are required.")
            return

        conn = connect_db()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Account created successfully!")
            login_screen(root)
        except Exception:
            messagebox.showerror("Error", "Username already exists.")
        finally:
            conn.close()

    tk.Button(root, text="Register", command=register, font=("Verdana", 14), bg="#4CAF50", fg="white", width=20).pack(pady=10)
    tk.Button(root, text="Back to Login", command=lambda: login_screen(root), font=("Verdana", 14), bg="#007acc", fg="white", width=20).pack(pady=10)
