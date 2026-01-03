"""
Authentication module for the Todo CLI application
"""
import hashlib
from typing import Optional
from .models import User


class AuthManager:
    """
    Authentication manager for handling user authentication
    """
    def __init__(self):
        self.users = {}  # In-memory storage for user credentials

    def hash_password(self, password: str) -> str:
        """
        Hash a password using SHA-256
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password: str, hashed_password: str) -> bool:
        """
        Verify a password against its hash
        """
        return self.hash_password(password) == hashed_password

    def register_user(self, username: str, password: str) -> bool:
        """
        Register a new user with username and password
        """
        if username in self.users:
            return False  # User already exists

        hashed_password = self.hash_password(password)
        user = User(username=username, password=hashed_password)
        self.users[username] = user
        return True

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """
        Authenticate a user with username and password
        """
        if username not in self.users:
            return None

        user = self.users[username]
        if self.verify_password(password, user.password):
            return user

        return None

    def user_exists(self, username: str) -> bool:
        """
        Check if a user exists
        """
        return username in self.users


# Global instance of the auth manager
auth_manager = AuthManager()