import tkinter as tk
from tkinter import messagebox
from database import cursor, conn



def open_add_expense_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Add Expense")

    tk.Label(root, text="Add New Expense", font=("Verdana", 24, "bold"), fg="#333").pack(pady=30)
    frame = tk.Frame(root)
    frame.pack(pady=20)

    tk.Label(frame, text="Amount:", font=("Verdana", 14)).grid(row=0, column=0, sticky="e", pady=10)
    amount_entry = tk.Entry(frame, font=("Verdana", 14))
    amount_entry.grid(row=0, column=1, pady=10, padx=10)

    tk.Label(frame, text="Category:", font=("Verdana", 14)).grid(row=1, column=0, sticky="e", pady=10)
    category_entry = tk.Entry(frame, font=("Verdana", 14))
    category_entry.grid(row=1, column=1, pady=10, padx=10)

    tk.Label(frame, text="Date (YYYY-MM-DD):", font=("Verdana", 14)).grid(row=2, column=0, sticky="e", pady=10)
    date_entry = tk.Entry(frame, font=("Verdana", 14))
    date_entry.grid(row=2, column=1, pady=10, padx=10)

    tk.Label(frame, text="Comment:", font=("Verdana", 14)).grid(row=3, column=0, sticky="e", pady=10)
    comment_entry = tk.Entry(frame, font=("Verdana", 14))
    comment_entry.grid(row=3, column=1, pady=10, padx=10)

    def save_expense():
        try:
            amount = float(amount_entry.get())
            category = category_entry.get()
            date = date_entry.get()
            comment = comment_entry.get()
            cursor.execute("INSERT INTO expenses (amount, category, date, comment) VALUES (?, ?, ?, ?)",
                           (amount, category, date, comment))
            conn.commit()
            messagebox.showinfo("Success", "Expense added successfully!")
            from home import home_screen
            home_screen(root)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    tk.Button(root, text="Save Expense", font=("Verdana", 14), bg="#4CAF50", fg="white",
              command=save_expense).pack(pady=20)

    tk.Button(root, text="Back to Home", font=("Verdana", 14), bg="#007acc", fg="white",
              command=lambda: __import__('home').home_screen(root)).pack(pady=10)
