"""
Data models for the Todo CLI application
"""
from datetime import datetime, timedelta
from typing import Optional, Union
from enum import Enum
from pydantic import BaseModel, field_validator
import re


class Priority(str, Enum):
    """
    Priority levels for tasks
    """
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Status(str, Enum):
    """
    Status of tasks
    """
    PENDING = "pending"
    COMPLETED = "completed"


class User(BaseModel):
    """
    User entity model for authentication
    """
    username: str
    password: str  # This will be hashed in the auth module

    @field_validator('username')
    @classmethod
    def validate_username(cls, v):
        if not v or not v.strip():
            raise ValueError('Username cannot be empty')
        # Username should be alphanumeric with underscores and hyphens
        if not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError('Username can only contain alphanumeric characters, underscores, and hyphens')
        return v.strip()

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if not v or len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        return v


class Task(BaseModel):
    """
    Task entity model with id, title, priority, description, due date, status, and timestamps
    """
    id: int  # Sequential numeric ID as required by spec
    title: str
    priority: Optional[Priority] = Priority.MEDIUM
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: Status = Status.PENDING
    created_at: datetime
    updated_at: datetime

    @field_validator('title')
    @classmethod
    def validate_title(cls, v):
        if not v or not v.strip():
            raise ValueError('Title cannot be empty')
        return v.strip()

    def __init__(self, **data):
        # Set timestamps if not provided
        now = datetime.now()
        if 'created_at' not in data or data['created_at'] is None:
            data['created_at'] = now
        if 'updated_at' not in data or data['updated_at'] is None:
            data['updated_at'] = now
        super().__init__(**data)

    def update(self, title: Optional[str] = None, description: Optional[str] = None):
        """
        Update task fields and update the updated_at timestamp
        Preserve unchanged fields
        """
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        self.updated_at = datetime.now()

    def mark_complete(self):
        """
        Mark task as complete
        """
        self.status = Status.COMPLETED
        self.updated_at = datetime.now()

    def mark_incomplete(self):
        """
        Mark task as incomplete
        """
        self.status = Status.PENDING
        self.updated_at = datetime.now()

    def get_remaining_time(self) -> Optional[timedelta]:
        """
        Calculate remaining time until due date
        """
        if self.due_date:
            return self.due_date - datetime.now()
        return None


class CreateTaskRequest(BaseModel):
    """
    Request model for creating a new task
    """
    title: str
    priority: Optional[Priority] = Priority.MEDIUM
    description: Optional[str] = None
    due_date: Optional[str] = None  # Will be parsed to datetime in service layer

    @field_validator('title')
    @classmethod
    def validate_title(cls, v):
        if not v or not v.strip():
            raise ValueError('Title cannot be empty')
        return v.strip()

    @field_validator('due_date')
    @classmethod
    def validate_due_date(cls, v):
        if v is not None:
            try:
                # Validate date format YYYY-MM-DD
                datetime.strptime(v, '%Y-%m-%d')
            except ValueError:
                raise ValueError('Due date must be in YYYY-MM-DD format')
        return v


class UpdateTaskRequest(BaseModel):
    """
    Request model for updating an existing task
    """
    title: Optional[str] = None
    description: Optional[str] = None

    @field_validator('title')
    @classmethod
    def validate_title(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('Title cannot be empty')
        return v


class TaskSearchRequest(BaseModel):
    """
    Request model for searching tasks
    """
    search_term: str
    search_by: str = "id_or_title"  # Options: "id", "title", "id_or_title"