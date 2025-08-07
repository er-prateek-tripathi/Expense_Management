# auth.py - Handles Login and Registration
import tkinter as tk
from tkinter import messagebox
from database import cursor, conn
from home import home_screen

def login_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

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
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        if cursor.fetchone():
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
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Account created successfully!")
            login_screen(root)
        except:
            messagebox.showerror("Error", "Username already exists.")

    tk.Button(root, text="Register", command=register, font=("Verdana", 14), bg="#4CAF50", fg="white", width=20).pack(pady=10)
    tk.Button(root, text="Back to Login", command=lambda: login_screen(root), font=("Verdana", 14), bg="#007acc", fg="white", width=20).pack(pady=10)
