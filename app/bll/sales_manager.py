from ..dal.database import session
from datetime import datetime
from ..dal.models import Sale

class SalesManager:
    @staticmethod
    def add_sale(date, amount, items_sold, user_id):
        sale = Sale(date=datetime.strptime(date, '%Y-%m-%d').date(), amount=amount, items_sold=items_sold, user_id=user_id)
        session.add(sale)
        session.commit()

    @staticmethod
    def get_all_sales():
        return session.query(Sale).all()

    @staticmethod
    def get_sales_by_user(user_id):
        return session.query(Sale).filter_by(user_id=user_id).all()