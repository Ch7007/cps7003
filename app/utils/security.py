import hashlib
import os

def hash_password(password: str) -> str:
    """Hash a password for storing."""
    salt = os.urandom(32)  # A new salt for this user
    key = hashlib.pbkdf2_hmac(
        'sha256',  # The hash digest algorithm for HMAC
        password.encode('utf-8'),  # Convert the password to bytes
        salt,  # Provide the salt
        100000  # It is recommended to use at least 100,000 iterations of SHA-256
    )
    return salt.hex() + key.hex()

def check_password(stored_password: str, provided_password: str) -> bool:
    """Verify a stored password against one provided by user."""
    salt = bytes.fromhex(stored_password[:64])
    key = bytes.fromhex(stored_password[64:])
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode('utf-8'),
        salt,
        100000
    )
    return new_key == key