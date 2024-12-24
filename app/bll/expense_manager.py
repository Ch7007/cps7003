from datetime import datetime
from ..dal.database import session
from ..dal.models import Expense

class ExpenseManager:
    @staticmethod
    def add_expense(date_str, amount, category, description, user_id):
        # Convert date string to date object
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        expense = Expense(date=date, amount=amount, category=category, description=description, user_id=user_id)
        session.add(expense)
        session.commit()

    @staticmethod
    def get_expenses_by_user(user_id):
        return session.query(Expense).filter_by(user_id=user_id).all()

    @staticmethod
    def get_all_expenses():
        return session.query(Expense).all()

