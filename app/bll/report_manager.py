from ..dal.database import session
from ..dal.models import Expense, Inventory, Sale
from sqlalchemy.sql import func

class ReportManager:
    @staticmethod
    def generate_expense_report():
        return session.query(Expense).all()

    @staticmethod
    def generate_inventory_report():
        return session.query(Inventory).all()

    @staticmethod
    def generate_sales_report():
        return session.query(Sale).all()

    @staticmethod
    def generate_summary_report():
        total_expense = session.query(func.sum(Expense.amount)).scalar()
        total_sales = session.query(func.sum(Sale.amount)).scalar()
        total_inventory_value = session.query(func.sum(Inventory.quantity * Inventory.cost)).scalar()

        return {
            'total_expense': total_expense,
            'total_sales': total_sales,
            'total_inventory_value': total_inventory_value
        }