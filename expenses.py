import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from database import insert_expense
from database import cursor, conn


# ---------- Add Expense Screen ----------
def add_expense_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Add Expense", font=("Verdana", 28, "bold"), fg="#333").pack(pady=30)
    frame = tk.Frame(root, bg="white")
    frame.pack(pady=20)

    tk.Label(frame, text="Amount:", font=("Verdana", 14), bg="white").grid(row=0, column=0, pady=10, sticky="e")
    amount_entry = tk.Entry(frame, font=("Verdana", 14), width=30)
    amount_entry.grid(row=0, column=1, pady=10, padx=10)

    tk.Label(frame, text="Category:", font=("Verdana", 14), bg="white").grid(row=1, column=0, pady=10, sticky="e")
    category_entry = tk.Entry(frame, font=("Verdana", 14), width=30)
    category_entry.grid(row=1, column=1, pady=10, padx=10)

    tk.Label(frame, text="Date:", font=("Verdana", 14), bg="white").grid(row=2, column=0, pady=10, sticky="e")
    date_entry = DateEntry(frame, font=("Verdana", 14), width=28)
    date_entry.grid(row=2, column=1, pady=10, padx=10)

    tk.Label(frame, text="Notes:", font=("Verdana", 14), bg="white").grid(row=3, column=0, pady=10, sticky="e")
    notes_entry = tk.Entry(frame, font=("Verdana", 14), width=30)
    notes_entry.grid(row=3, column=1, pady=10, padx=10)

    tk.Label(frame, text="Comment:", font=("Verdana", 14), bg="white").grid(row=4, column=0, pady=10, sticky="e")
    comment_entry = tk.Entry(frame, font=("Verdana", 14), width=30)
    comment_entry.grid(row=4, column=1, pady=10, padx=10)

    def submit_expense():
        try:
            amount = float(amount_entry.get())
            category = category_entry.get()
            date = date_entry.get()
            notes = notes_entry.get()
            comment = comment_entry.get()
            insert_expense(amount, category, date, notes, comment)
            messagebox.showinfo("Success", "Expense added successfully!")
            amount_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
            notes_entry.delete(0, tk.END)
            comment_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    tk.Button(root, text="Add Expense", command=submit_expense, font=("Verdana", 14), bg="#4CAF50", fg="white", width=20).pack(pady=10)
    tk.Button(root, text="Back to Home", command=lambda: __import__('home').home_screen(root), font=("Verdana", 14), bg="#007acc", fg="white", width=20).pack(pady=10)
