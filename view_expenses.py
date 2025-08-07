import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db
import session

def open_view_expenses_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("View & Manage Expenses")

    tk.Label(root, text="Your Expenses", font=("Verdana", 24, "bold"), fg="#333").pack(pady=20)

    columns = ("ID", "Amount", "Category", "Date", "Comment")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=15)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(pady=20)

    def refresh_tree():
        for iid in tree.get_children():
            tree.delete(iid)

        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, amount, category, date, comment FROM expenses WHERE user_id=? ORDER BY date DESC",
            (session.current_user_id,)
        )
        rows = cur.fetchall()
        conn.close()

        for row in rows:
            tree.insert("", tk.END, values=row)

    def delete_expense():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an expense to delete.")
            return

        iid = selected[0]
        values = tree.item(iid, "values")
        expense_id = values[0]

        conn = connect_db()
        cur = conn.cursor()
        try:
            cur.execute(
                "DELETE FROM expenses WHERE id=? AND user_id=?",
                (expense_id, session.current_user_id)
            )
            conn.commit()
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

        refresh_tree()
        messagebox.showinfo("Deleted", "Expense deleted successfully.")

    tk.Button(
        root, text="Delete Selected",
        font=("Verdana", 14), bg="#F44336", fg="white",
        command=delete_expense
    ).pack(pady=10)

    tk.Button(
        root, text="Back to Home",
        font=("Verdana", 14), bg="#2196F3", fg="white",
        command=lambda: __import__("home").home_screen(root)
    ).pack(pady=10)

    refresh_tree()
