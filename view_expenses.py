# view_expenses.py - View, delete, and manage expenses
import tkinter as tk
from tkinter import ttk, messagebox
from database import cursor, conn

def open_view_expenses_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("View & Manage Expenses")

    tk.Label(root, text="Your Expenses", font=("Verdana", 24, "bold"), fg="#333").pack(pady=20)

    tree = ttk.Treeview(root, columns=("ID", "Amount", "Category", "Date", "Comment"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Amount", text="Amount")
    tree.heading("Category", text="Category")
    tree.heading("Date", text="Date")
    tree.heading("Comment", text="Comment")

    tree.column("ID", width=50, anchor='center')
    tree.column("Amount", width=100, anchor='center')
    tree.column("Category", width=150, anchor='center')
    tree.column("Date", width=100, anchor='center')
    tree.column("Comment", width=250, anchor='w')

    tree.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    # Load data
    cursor.execute("SELECT ID, AMOUNT, CATEGORY, DATE, COMMENT FROM expenses")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

    def delete_expense():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an expense to delete.")
            return
        item = tree.item(selected)
        expense_id = item["values"][0]
        cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
        conn.commit()
        tree.delete(selected)
        messagebox.showinfo("Deleted", "Expense deleted successfully.")

    tk.Button(root, text="Delete Selected", font=("Verdana", 12), bg="#F44336", fg="white", command=delete_expense).pack(pady=10)
    tk.Button(root, text="Back to Home", font=("Verdana", 12), bg="#607D8B", fg="white", command=lambda: __import__('home').home_screen(root)).pack(pady=10)
