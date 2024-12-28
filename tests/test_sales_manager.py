import unittest
from datetime import datetime
from src.dal.database import session
from src.dal.models import Sale
from src.bll.sales_manager import SalesManager

class TestSalesManager(unittest.TestCase):
    def setUp(self):
        # Set up a database connection and create the tables
        self.session = session
        self.session.query(Sale).delete()  # Clear the table before each test
        self.session.commit()

    def tearDown(self):
        # Tear down the database connection and drop the tables
        self.session.query(Sale).delete()  # Clean up after each test
        self.session.commit()

    def test_add_sale(self):
        SalesManager.add_sale('2024-12-22', 1000.0, 'Coffee, Cake', 1)
        sales = SalesManager.get_sales_by_user(1)
        self.assertEqual(len(sales), 1)
        self.assertEqual(sales[0].date, datetime.strptime('2024-12-22', '%Y-%m-%d').date())
        self.assertEqual(sales[0].amount, 1000.0)
        self.assertEqual(sales[0].items_sold, 'Coffee, Cake')

    def test_update_sale(self):
        SalesManager.add_sale('2024-12-22', 1000.0, 'Coffee, Cake', 1)
        sale = SalesManager.get_sales_by_user(1)[0]
        # Assuming there's an update_sale method
        SalesManager.update_sale(sale.id, new_amount=1500.0, new_items_sold='Coffee, Cake, Sandwich')
        updated_sale = SalesManager.get_sales_by_user(1)[0]
        self.assertEqual(updated_sale.amount, 1500.0)
        self.assertEqual(updated_sale.items_sold, 'Coffee, Cake, Sandwich')

    def test_delete_sale(self):
        SalesManager.add_sale('2024-12-22', 1000.0, 'Coffee, Cake', 1)
        sale = SalesManager.get_sales_by_user(1)[0]
        SalesManager.delete_sale(sale.id)
        sales = SalesManager.get_sales_by_user(1)
        self.assertEqual(len(sales), 0)

    def test_get_sales_by_user(self):
        SalesManager.add_sale('2024-12-22', 1000.0, 'Coffee, Cake', 1)
        SalesManager.add_sale('2024-12-23', 500.0, 'Tea, Pastry', 1)
        sales = SalesManager.get_sales_by_user(1)
        self.assertEqual(len(sales), 2)
        self.assertEqual(sales[0].date, datetime.strptime('2024-12-22', '%Y-%m-%d').date())
        self.assertEqual(sales[1].date, datetime.strptime('2024-12-23', '%Y-%m-%d').date())

if __name__ == '__main__':
    unittest.main()