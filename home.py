import tkinter as tk
from tkinter import messagebox
from add_expense import open_add_expense_screen
from view_expenses import open_view_expenses_screen
from analytics import open_analytics_screen
from export import export_expenses_to_csv
# from login import login_screen  
from database import cursor, conn


def home_screen(root):
    from auth import login_screen
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Expense Management System - Home")

    tk.Label(root, text="Expense Management Home", font=("Verdana", 24, "bold"), fg="#333").pack(pady=40)

    tk.Button(root, text="Add Expense", font=("Verdana", 14), width=25, bg="#4CAF50", fg="white",
              command=lambda: open_add_expense_screen(root)).pack(pady=10)

    tk.Button(root, text="View & Manage Expenses", font=("Verdana", 14), width=25, bg="#2196F3", fg="white",
              command=lambda: open_view_expenses_screen(root)).pack(pady=10)

    tk.Button(root, text="Analytics", font=("Verdana", 14), width=25, bg="#FF9800", fg="white",
              command=lambda: open_analytics_screen(root)).pack(pady=10)

    tk.Button(root, text="Export Expenses to CSV", font=("Verdana", 14), width=25, bg="#9C27B0", fg="white",
              command=export_expenses_to_csv).pack(pady=10)

    from session import clear_user

    tk.Button(
        root,
        text="Logout",
        font=("Verdana", 14),
        width=25,
        bg="#F44336",
        fg="white",
        command=lambda: (clear_user(), __import__('login').start_login(root))
    ).pack(pady=20)
