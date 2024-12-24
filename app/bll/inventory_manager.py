from ..dal.database import session
from ..dal.models import Inventory

class InventoryManager:
    @staticmethod
    def add_item(item_name, quantity, cost):
        item = Inventory(item_name=item_name, quantity=quantity, cost=cost)
        session.add(item)
        try:
            session.commit()
            print(f"Item added: {item_name}, Quantity: {quantity}, Cost: {cost}")
        except Exception as e:
            session.rollback()
            print(f"Error adding item: {e}")

    @staticmethod
    def update_item(item_id, new_quantity=None, new_cost=None):
        item = session.query(Inventory).filter_by(id=item_id).first()
        if item:
            if new_quantity is not None:
                item.quantity = new_quantity
            if new_cost is not None:
                item.cost = new_cost
            try:
                session.commit()
                print(f"Item updated: ID: {item_id}, New Quantity: {new_quantity}, New Cost: {new_cost}")
            except Exception as e:
                session.rollback()
                print(f"Error updating item: {e}")
        else:
            print(f"Item not found: ID: {item_id}")

    @staticmethod
    def delete_item(item_id):
        item = session.query(Inventory).filter_by(id=item_id).first()
        if item:
            try:
                session.delete(item)
                session.commit()
                print(f"Item deleted: ID: {item_id}")
            except Exception as e:
                session.rollback()
                print(f"Error deleting item: {e}")
        else:
            print(f"Item not found: ID: {item_id}")

    @staticmethod
    def get_all_items():
        try:
            items = session.query(Inventory).all()
            print(f"Retrieved {len(items)} items from inventory.")
            return items
        except Exception as e:
            print(f"Error retrieving items: {e}")
            return []