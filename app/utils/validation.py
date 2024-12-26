import re

def validate_username(username: str) -> bool:
    """Validate the username to contain only alphanumeric characters and underscores."""
    return re.match(r"^\w+$", username) is not None

def validate_password(password: str) -> bool:
    """Validate the password to be at least 8 characters long."""
    return len(password) >= 8

def validate_email(email: str) -> bool:
    """Validate the email address."""
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None
