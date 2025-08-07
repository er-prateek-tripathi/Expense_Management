# export.py - Exports expenses to CSV
import csv
from tkinter import messagebox
from database import cursor
from tkinter import filedialog
from database import cursor, conn


def export_expenses_to_csv():
    try:
        # Fetch all expenses
        cursor.execute("SELECT date, category, amount, comment FROM expenses")
        data = cursor.fetchall()

        if not data:
            messagebox.showinfo("No Data", "No expenses to export.")
            return

        # Ask user where to save the CSV
        filepath = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv")])
        if not filepath:
            return

        # Write to CSV
        with open(filepath, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Comment"])
            writer.writerows(data)

        messagebox.showinfo("Export Successful", f"Expenses exported successfully to:\n{filepath}")
    except Exception as e:
        messagebox.showerror("Export Failed", str(e))