import tkinter as tk
from tkinter import messagebox, ttk
from src.bll.user_manager import UserManager
from src.bll.expense_manager import ExpenseManager
from src.bll.inventory_manager import InventoryManager
from src.bll.sales_manager import SalesManager
from src.bll.report_manager import ReportManager

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Brew and Bite Café Management System")
        self.geometry("800x600")
        self.current_user = None
        self.create_login_widgets()

    def create_login_widgets(self):
        self.clear_widgets()

        login_frame = tk.Frame(self)
        login_frame.pack(pady=20)

        tk.Label(login_frame, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(login_frame, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(login_frame, text="Login", command=self.login).grid(row=2, columnspan=2, pady=10)
        tk.Button(login_frame, text="Register", command=self.create_register_widgets).grid(row=3, columnspan=2, pady=10)

    def create_register_widgets(self):
        self.clear_widgets()

        register_frame = tk.Frame(self)
        register_frame.pack(pady=20)

        tk.Label(register_frame, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        self.reg_username_entry = tk.Entry(register_frame)
        self.reg_username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(register_frame, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        self.reg_password_entry = tk.Entry(register_frame, show="*")
        self.reg_password_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(register_frame, text="Email:").grid(row=2, column=0, padx=10, pady=10)
        self.reg_email_entry = tk.Entry(register_frame)
        self.reg_email_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(register_frame, text="Register", command=self.register).grid(row=3, columnspan=2, pady=10)
        tk.Button(register_frame, text="Back to Login", command=self.create_login_widgets).grid(row=4, columnspan=2, pady=10)

    def create_main_widgets(self):
        self.clear_widgets()

        main_frame = tk.Frame(self)
        main_frame.pack(pady=20)

        tk.Button(main_frame, text="User Management", command=self.create_user_management_widgets).grid(row=0, column=0, padx=20, pady=10)
        tk.Button(main_frame, text="Expense Management", command=self.create_expense_management_widgets).grid(row=0, column=1, padx=20, pady=10)
        tk.Button(main_frame, text="Inventory Management", command=self.create_inventory_management_widgets).grid(row=1, column=0, padx=20, pady=10)
        tk.Button(main_frame, text="Sales Tracking", command=self.create_sales_tracking_widgets).grid(row=1, column=1, padx=20, pady=10)
        tk.Button(main_frame, text="Reporting", command=self.create_reporting_widgets).grid(row=2, columnspan=2, pady=10)

        tk.Button(main_frame, text="Logout", command=self.logout).grid(row=3, columnspan=2, pady=10)

    def create_user_management_widgets(self):
        self.clear_widgets()

        user_frame = tk.Frame(self)
        user_frame.pack(pady=20)

        tk.Label(user_frame, text="Update User Information").grid(row=0, columnspan=2, pady=10)

        tk.Label(user_frame, text="New Password:").grid(row=1, column=0, padx=10, pady=10)
        self.new_password_entry = tk.Entry(user_frame, show="*")
        self.new_password_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(user_frame, text="New Email:").grid(row=2, column=0, padx=10, pady=10)
        self.new_email_entry = tk.Entry(user_frame)
        self.new_email_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Button(user_frame, text="Update", command=self.update_user).grid(row=3, columnspan=2, pady=10)
        tk.Button(user_frame, text="Delete Account", command=self.delete_user).grid(row=4, columnspan=2, pady=10)
        tk.Button(user_frame, text="Back", command=self.create_main_widgets).grid(row=5, columnspan=2, pady=10)

    def create_expense_management_widgets(self):
        self.clear_widgets()

        expense_frame = tk.Frame(self)
        expense_frame.pack(pady=20)

        tk.Label(expense_frame, text="Record Daily Expense").grid(row=0, columnspan=2, pady=10)

        tk.Label(expense_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10)
        self.expense_date_entry = tk.Entry(expense_frame)
        self.expense_date_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(expense_frame, text="Amount:").grid(row=2, column=0, padx=10, pady=10)
        self.expense_amount_entry = tk.Entry(expense_frame)
        self.expense_amount_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(expense_frame, text="Category:").grid(row=3, column=0, padx=10, pady=10)
        self.expense_category_entry = tk.Entry(expense_frame)
        self.expense_category_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(expense_frame, text="Description:").grid(row=4, column=0, padx=10, pady=10)
        self.expense_description_entry = tk.Entry(expense_frame)
        self.expense_description_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(expense_frame, text="Add Expense", command=self.add_expense).grid(row=5, columnspan=2, pady=10)
        tk.Button(expense_frame, text="View Expense History", command=self.view_expense_history).grid(row=6, columnspan=2, pady=10)
        tk.Button(expense_frame, text="Back", command=self.create_main_widgets).grid(row=7, columnspan=2, pady=10)

    def create_inventory_management_widgets(self):
        self.clear_widgets()

        inventory_frame = tk.Frame(self)
        inventory_frame.pack(pady=20)

        tk.Label(inventory_frame, text="Manage Inventory").grid(row=0, columnspan=2, pady=10)

        tk.Label(inventory_frame, text="Item ID:").grid(row=1, column=0, padx=10, pady=10)
        self.item_id_entry = tk.Entry(inventory_frame)
        self.item_id_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(inventory_frame, text="Item Name:").grid(row=2, column=0, padx=10, pady=10)
        self.item_name_entry = tk.Entry(inventory_frame)
        self.item_name_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(inventory_frame, text="Quantity:").grid(row=3, column=0, padx=10, pady=10)
        self.quantity_entry = tk.Entry(inventory_frame)
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(inventory_frame, text="Cost:").grid(row=4, column=0, padx=10, pady=10)
        self.cost_entry = tk.Entry(inventory_frame)
        self.cost_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(inventory_frame, text="Add Item", command=self.add_item).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(inventory_frame, text="Update Item", command=self.update_item).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(inventory_frame, text="Delete Item", command=self.delete_item).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(inventory_frame, text="View Inventory", command=self.view_inventory).grid(row=8, column=0, columnspan=2, pady=10)
        tk.Button(inventory_frame, text="Back", command=self.create_main_widgets).grid(row=9, column=0, columnspan=2, pady=10)

        self.inventory_list = ttk.Treeview(inventory_frame, columns=("ID", "Name", "Quantity", "Cost"), show='headings')
        self.inventory_list.heading("ID", text="ID")
        self.inventory_list.heading("Name", text="Name")
        self.inventory_list.heading("Quantity", text="Quantity")
        self.inventory_list.heading("Cost", text="Cost")
        self.inventory_list.grid(row=10, column=0, columnspan=2, pady=20)

    def create_sales_tracking_widgets(self):
        self.clear_widgets()

        sales_frame = tk.Frame(self)
        sales_frame.pack(pady=20)

        tk.Label(sales_frame, text="Record Sales").grid(row=0, columnspan=2, pady=10)

        tk.Label(sales_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10)
        self.sales_date_entry = tk.Entry(sales_frame)
        self.sales_date_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(sales_frame, text="Amount:").grid(row=2, column=0, padx=10, pady=10)
        self.sales_amount_entry = tk.Entry(sales_frame)
        self.sales_amount_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(sales_frame, text="Items Sold:").grid(row=3, column=0, padx=10, pady=10)
        self.items_sold_entry = tk.Entry(sales_frame)
        self.items_sold_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Button(sales_frame, text="Add Sale", command=self.add_sale).grid(row=4, columnspan=2, pady=10)
        tk.Button(sales_frame, text="View Sales History", command=self.view_sales_history).grid(row=5, columnspan=2, pady=10)
        tk.Button(sales_frame, text="Back", command=self.create_main_widgets).grid(row=6, columnspan=2, pady=10)

        self.sales_list = ttk.Treeview(sales_frame, columns=("ID", "Date", "Amount", "Items Sold"), show='headings')
        self.sales_list.heading("ID", text="ID")
        self.sales_list.heading("Date", text="Date")
        self.sales_list.heading("Amount", text="Amount")
        self.sales_list.heading("Items Sold", text="Items Sold")
        self.sales_list.grid(row=7, column=0, columnspan=2, pady=20)
        self.refresh_sales_view()


    def create_reporting_widgets(self):
        self.clear_widgets()

        report_frame = tk.Frame(self)
        report_frame.pack(pady=20)

        tk.Label(report_frame, text="Generate Reports").grid(row=0, columnspan=2, pady=10)

        tk.Button(report_frame, text="Expense Report", command=self.generate_expense_report).grid(row=1, columnspan=2, pady=10)
        tk.Button(report_frame, text="Inventory Report", command=self.generate_inventory_report).grid(row=2, columnspan=2, pady=10)
        tk.Button(report_frame, text="Sales Report", command=self.generate_sales_report).grid(row=3, columnspan=2, pady=10)
        tk.Button(report_frame, text="Summary Report", command=self.generate_summary_report).grid(row=4, columnspan=2, pady=10)
        tk.Button(report_frame, text="Back", command=self.create_main_widgets).grid(row=5, columnspan=2, pady=10)

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = UserManager.get_user(username)
        if user and UserManager.check_password(user.password, password):
            self.current_user = user
            self.create_main_widgets()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        email = self.reg_email_entry.get()
        try:
            UserManager.add_user(username, password, email)
            messagebox.showinfo("Success", "User registered successfully!")
            self.create_login_widgets()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_user(self):
        new_password = self.new_password_entry.get()
        new_email = self.new_email_entry.get()
        try:
            UserManager.update_user(self.current_user.username, new_password, new_email)
            messagebox.showinfo("Success", "User information updated successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_user(self):
        UserManager.delete_user(self.current_user.username)
        self.current_user = None
        self.create_login_widgets()
        messagebox.showinfo("Success", "User account deleted successfully!")

    def add_expense(self):
        date = self.expense_date_entry.get()
        amount = self.expense_amount_entry.get()
        category = self.expense_category_entry.get()
        description = self.expense_description_entry.get()

        try:
            ExpenseManager.add_expense(date, amount, category, description, self.current_user.id)
            messagebox.showinfo("Success", "Expense added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_expense_history(self):
        expenses = ExpenseManager.get_expenses_by_user(self.current_user.id)
        expense_history = "\n".join([f"{exp.date} - {exp.category}: {exp.amount}" for exp in expenses])
        messagebox.showinfo("Expense History", expense_history)

    def add_item(self):
        item_name = self.item_name_entry.get()
        quantity = self.quantity_entry.get()
        cost = self.cost_entry.get()
        try:
            InventoryManager.add_item(item_name, quantity, cost)
            self.refresh_inventory_view()
            messagebox.showinfo("Success", "Item added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_item(self):
        item_id = self.get_selected_item_id()
        new_quantity = self.quantity_entry.get()
        new_cost = self.cost_entry.get()
        try:
            InventoryManager.update_item(item_id, new_quantity, new_cost)
            self.refresh_inventory_view()
            messagebox.showinfo("Success", "Item updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_item(self):
        item_id = self.get_selected_item_id()
        try:
            InventoryManager.delete_item(item_id)
            self.refresh_inventory_view()
            messagebox.showinfo("Success", "Item deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_inventory(self):
        self.refresh_inventory_view()

    def refresh_inventory_view(self):
        items = InventoryManager.get_all_items()
        self.inventory_list.delete(*self.inventory_list.get_children())
        for item in items:
            self.inventory_list.insert('', 'end', values=(item.id, item.item_name, item.quantity, item.cost))

    def get_selected_item_id(self):
        selected_item = self.inventory_list.selection()
        if selected_item:
            item_id = self.inventory_list.item(selected_item)['values'][0]
            return item_id
        else:
            messagebox.showerror("Error", "No item selected")
            return None

    def add_sale(self):
        date = self.sales_date_entry.get()
        amount = self.sales_amount_entry.get()
        items_sold = self.items_sold_entry.get()
        try:
            SalesManager.add_sale(date, amount, items_sold, self.current_user.id)
            self.refresh_sales_view()
            messagebox.showinfo("Success", "Sale recorded successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_sales_history(self):
        self.refresh_sales_view()

    def refresh_sales_view(self):
        sales = SalesManager.get_sales_by_user(self.current_user.id)
        self.sales_list.delete(*self.sales_list.get_children())
        for sale in sales:
            self.sales_list.insert('', 'end', values=(sale.id, sale.date, sale.amount, sale.items_sold))

    def generate_expense_report(self):
        expenses = ReportManager.generate_expense_report()
        report = "\n".join([f"{exp.date} - {exp.category}: {exp.amount}" for exp in expenses])
        messagebox.showinfo("Expense Report", report)

    def generate_inventory_report(self):
        items = ReportManager.generate_inventory_report()
        report = "\n".join([f"{item.item_name} - Quantity: {item.quantity}, Cost: {item.cost}" for item in items])
        messagebox.showinfo("Inventory Report", report)

    def generate_sales_report(self):
        sales = ReportManager.generate_sales_report()
        report = "\n".join([f"{sale.date} - {sale.items_sold}: {sale.amount}" for sale in sales])
        messagebox.showinfo("Sales Report", report)

    def generate_summary_report(self):
        summary = ReportManager.generate_summary_report()
        report = (
            f"Total Expense: {summary['total_expense']}\n"
            f"Total Sales: {summary['total_sales']}\n"
            f"Total Inventory Value: {summary['total_inventory_value']}"
        )
        messagebox.showinfo("Summary Report", report)

    def logout(self):
        self.current_user = None
        self.create_login_widgets()

if __name__ == "__main__":
    app = Application()
    app.mainloop()