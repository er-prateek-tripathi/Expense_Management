# analytics.py - Visual insights for expense analysis
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database import fetch_expenses
from collections import defaultdict
from database import cursor, conn

from database import connect_db
from tkinter import *
from tkinter import ttk
from collections import defaultdict

def open_analytics_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Expense Analytics")

    Label(root, text="Expense Analytics", font=("Verdana", 24, "bold"), fg="#333").pack(pady=20)

    conn = connect_db()
    cursor = conn.cursor()

    # ✅ Ensure correct order
    cursor.execute("SELECT category, amount FROM expenses")
    data = cursor.fetchall()

    category_totals = defaultdict(float)

    for category, amount in data:
        try:
            category_totals[category] += float(amount)
        except ValueError:
            pass  # If somehow 'amount' is invalid

    # Display totals in table
    table_frame = Frame(root)
    table_frame.pack(pady=20)

    tree = ttk.Treeview(table_frame, columns=("Category", "Total"), show="headings", height=10)
    tree.heading("Category", text="Category")
    tree.heading("Total", text="Total Spent")

    for cat, total in category_totals.items():
        tree.insert("", "end", values=(cat, f"{total:.2f}"))

    tree.pack()

    Button(root, text="Back to Home", command=lambda: __import__('home').home_screen(root),
           font=("Verdana", 12), bg="#007acc", fg="white").pack(pady=20)

    conn.close()
