import unittest
from src.dal.database import session
from src.dal.models import Inventory
from src.bll.inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        # Set up a database connection and create the tables
        self.session = session
        self.session.query(Inventory).delete()  # Clear the table before each test
        self.session.commit()

    def tearDown(self):
        # Tear down the database connection and drop the tables
        self.session.query(Inventory).delete()  # Clean up after each test
        self.session.commit()

    def test_add_item(self):
        InventoryManager.add_item("Coffee Beans", 100, 200.0)
        items = InventoryManager.get_all_items()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].item_name, "Coffee Beans")
        self.assertEqual(items[0].quantity, 100)
        self.assertEqual(items[0].cost, 200.0)

    def test_update_item(self):
        InventoryManager.add_item("Coffee Beans", 100, 200.0)
        item = InventoryManager.get_all_items()[0]
        InventoryManager.update_item(item.id, new_quantity=150, new_cost=250.0)
        updated_item = InventoryManager.get_all_items()[0]
        self.assertEqual(updated_item.quantity, 150)
        self.assertEqual(updated_item.cost, 250.0)

    def test_delete_item(self):
        InventoryManager.add_item("Coffee Beans", 100, 200.0)
        item = InventoryManager.get_all_items()[0]
        InventoryManager.delete_item(item.id)
        items = InventoryManager.get_all_items()
        self.assertEqual(len(items), 0)

    def test_get_all_items(self):
        InventoryManager.add_item("Coffee Beans", 100, 200.0)
        InventoryManager.add_item("Milk", 50, 100.0)
        items = InventoryManager.get_all_items()
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].item_name, "Coffee Beans")
        self.assertEqual(items[1].item_name, "Milk")

if __name__ == '__main__':
    unittest.main()