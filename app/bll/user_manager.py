from sqlalchemy.exc import IntegrityError
from ..dal.database import session
from ..dal.models import User
from ..utils.security import hash_password, check_password

class UserManager:
    @staticmethod
    def add_user(username, password, email):
        hashed_password = hash_password(password)
        user = User(username=username, password=hashed_password, email=email)
        session.add(user)
        try:
            session.commit()
        except IntegrityError as e:
            session.rollback()  # Rollback the session to clean up the failed transaction
            if "UNIQUE constraint failed" in str(e.orig):
                raise ValueError("A user with this email already exists.")
            else:
                raise

    @staticmethod
    def get_user(username):
        return session.query(User).filter_by(username=username).first()

    @staticmethod
    def update_user(username, new_password=None, new_email=None):
        user = session.query(User).filter_by(username=username).first()
        if user:
            if new_password:
                user.password = hash_password(new_password)
            if new_email:
                user.email = new_email
            try:
                session.commit()
            except IntegrityError as e:
                session.rollback()
                if "UNIQUE constraint failed" in str(e.orig):
                    raise ValueError("A user with this email already exists.")
                else:
                    raise

    @staticmethod
    def delete_user(username):
        user = session.query(User).filter_by(username=username).first()
        if user:
            session.delete(user)
            session.commit()

    @staticmethod
    def check_password(stored_password, provided_password):
        return check_password(stored_password, provided_password)