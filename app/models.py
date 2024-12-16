from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base

# Base class for SQLAlchemy ORM
Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)  # Encrypted password
    email = Column(String(100), nullable=False, unique=True)

    # Relationships
    expenses = relationship('Expense', back_populates='user', cascade="all, delete-orphan")
    sales = relationship('Sale', back_populates='user', cascade="all, delete-orphan")

# Expense Model
class Expense(Base):
    __tablename__ = 'expenses'
    expense_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)

    # Relationships
    user = relationship('User', back_populates='expenses')

# Inventory Model
class InventoryItem(Base):
    __tablename__ = 'inventory'
    item_id = Column(Integer, primary_key=True, autoincrement=True)
    item_name = Column(String(100), nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)

# Sales Model
class Sale(Base):
    __tablename__ = 'sales'
    sale_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    date = Column(Date, nullable=False)
    amount = Column(Float, nullable=False)
    items_sold = Column(String(255), nullable=False)  # List of sold items (comma-separated)

    # Relationships
    user = relationship('User', back_populates='sales')

# Function to initialize the database
def init_db(database_url='sqlite:///database/db.sqlite3'):
    """
    Initialize the database.

    :param database_url: URL of the database
    """
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
