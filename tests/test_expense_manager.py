import unittest
from datetime import datetime
from src.dal.database import session
from src.dal.models import Expense
from src.bll.expense_manager import ExpenseManager

class TestExpenseManager(unittest.TestCase):
    def setUp(self):
        # Set up a database connection and create the tables
        self.session = session
        self.session.query(Expense).delete()  # Clear the table before each test
        self.session.commit()

    def tearDown(self):
        # Tear down the database connection and drop the tables
        self.session.query(Expense).delete()  # Clean up after each test
        self.session.commit()

    def test_add_expense(self):
        ExpenseManager.add_expense('2024-12-22', 200.0, 'Supplies', 'Coffee beans', 1)
        expenses = ExpenseManager.get_expenses_by_user(1)
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0].date, datetime.strptime('2024-12-22', '%Y-%m-%d').date())
        self.assertEqual(expenses[0].amount, 200.0)
        self.assertEqual(expenses[0].category, 'Supplies')
        self.assertEqual(expenses[0].description, 'Coffee beans')

    def test_update_expense(self):
        ExpenseManager.add_expense('2024-12-22', 200.0, 'Supplies', 'Coffee beans', 1)
        expense = ExpenseManager.get_expenses_by_user(1)[0]
        # Assuming there's an update_expense method
        ExpenseManager.update_expense(expense.id, new_amount=250.0, new_category='Food', new_description='Pastries')
        updated_expense = ExpenseManager.get_expenses_by_user(1)[0]
        self.assertEqual(updated_expense.amount, 250.0)
        self.assertEqual(updated_expense.category, 'Food')
        self.assertEqual(updated_expense.description, 'Pastries')

    def test_delete_expense(self):
        ExpenseManager.add_expense('2024-12-22', 200.0, 'Supplies', 'Coffee beans', 1)
        expense = ExpenseManager.get_expenses_by_user(1)[0]
        ExpenseManager.delete_expense(expense.id)
        expenses = ExpenseManager.get_expenses_by_user(1)
        self.assertEqual(len(expenses), 0)

    def test_get_expenses_by_user(self):
        ExpenseManager.add_expense('2024-12-22', 200.0, 'Supplies', 'Coffee beans', 1)
        ExpenseManager.add_expense('2024-12-23', 100.0, 'Utilities', 'Electricity bill', 1)
        expenses = ExpenseManager.get_expenses_by_user(1)
        self.assertEqual(len(expenses), 2)
        self.assertEqual(expenses[0].date, datetime.strptime('2024-12-22', '%Y-%m-%d').date())
        self.assertEqual(expenses[1].date, datetime.strptime('2024-12-23', '%Y-%m-%d').date())

if __name__ == '__main__':
    unittest.main()