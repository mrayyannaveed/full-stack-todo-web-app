"""
State management for the Todo CLI application - file-based storage with in-memory caching
"""
import json
import os
from typing import Dict, List, Optional
from datetime import datetime
from .models import Task, User


class FileTaskStore:
    """
    File-based storage for tasks with in-memory caching using JSON files
    """
    def __init__(self, tasks_file="tasks.json", users_file="users.json"):
        self.tasks_file = tasks_file
        self.users_file = users_file
        self._tasks: Dict[int, Task] = {}
        self._users: Dict[str, User] = {}
        self._next_id = 1
        self.load_from_file()

    def _serialize_task(self, task: Task) -> dict:
        """Convert Task object to serializable dict"""
        return {
            "id": task.id,
            "title": task.title,
            "priority": task.priority.value if hasattr(task.priority, 'value') else task.priority,
            "description": task.description,
            "due_date": task.due_date.isoformat() if task.due_date else None,
            "status": task.status.value if hasattr(task.status, 'value') else task.status,
            "created_at": task.created_at.isoformat(),
            "updated_at": task.updated_at.isoformat()
        }

    def _deserialize_task(self, data: dict) -> Task:
        """Convert dict back to Task object"""
        # Convert string dates back to datetime objects
        created_at = datetime.fromisoformat(data["created_at"])
        updated_at = datetime.fromisoformat(data["updated_at"])
        due_date = datetime.fromisoformat(data["due_date"]) if data["due_date"] else None

        return Task(
            id=data["id"],
            title=data["title"],
            priority=data["priority"],
            description=data["description"],
            due_date=due_date,
            status=data["status"],
            created_at=created_at,
            updated_at=updated_at
        )

    def _serialize_user(self, user: User) -> dict:
        """Convert User object to serializable dict"""
        return {
            "username": user.username,
            "password": user.password
        }

    def _deserialize_user(self, data: dict) -> User:
        """Convert dict back to User object"""
        return User(
            username=data["username"],
            password=data["password"]
        )

    def save_to_file(self):
        """Save tasks and users to JSON files"""
        # Save tasks
        tasks_data = {str(task_id): self._serialize_task(task) for task_id, task in self._tasks.items()}
        with open(self.tasks_file, 'w', encoding='utf-8') as f:
            json.dump(tasks_data, f, indent=2)

        # Save users
        users_data = {username: self._serialize_user(user) for username, user in self._users.items()}
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(users_data, f, indent=2)

    def load_from_file(self):
        """Load tasks and users from JSON files"""
        # Load tasks
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, 'r', encoding='utf-8') as f:
                    tasks_data = json.load(f)

                for task_id_str, task_data in tasks_data.items():
                    task = self._deserialize_task(task_data)
                    self._tasks[int(task_id_str)] = task
                    # Update next_id to ensure sequential IDs continue properly
                    if task.id >= self._next_id:
                        self._next_id = task.id + 1
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"Warning: Could not load tasks from {self.tasks_file}: {e}")
                self._tasks = {}

        # Load users
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    users_data = json.load(f)

                for username, user_data in users_data.items():
                    user = self._deserialize_user(user_data)
                    self._users[username] = user
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"Warning: Could not load users from {self.users_file}: {e}")
                self._users = {}

    def add_task(self, task: Task) -> Task:
        """
        Add a new task to the store with sequential ID assignment
        """
        # Assign the next available ID
        task.id = self._next_id
        self._tasks[task.id] = task
        self._next_id += 1
        self.save_to_file()  # Save to file after modification
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by ID
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks
        """
        return list(self._tasks.values())

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task, preserving unchanged fields
        """
        task = self.get_task(task_id)
        if task is None:
            return None

        task.update(title=title, description=description)
        self._tasks[task_id] = task
        self.save_to_file()  # Save to file after modification
        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            self.save_to_file()  # Save to file after modification
            return True
        return False

    def mark_complete(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as complete
        """
        task = self.get_task(task_id)
        if task is None:
            return None

        task.mark_complete()
        self._tasks[task_id] = task
        self.save_to_file()  # Save to file after modification
        return task

    def mark_incomplete(self, task_id: int) -> Optional[Task]:
        """
        Mark a completed task as incomplete
        """
        task = self.get_task(task_id)
        if task is None:
            return None

        task.mark_incomplete()
        self._tasks[task_id] = task
        self.save_to_file()  # Save to file after modification
        return task

    def search_tasks_by_id(self, task_id: int) -> Optional[Task]:
        """
        Search for a task by ID
        """
        return self.get_task(task_id)

    def search_tasks_by_title(self, title: str) -> List[Task]:
        """
        Search for tasks by title (case-insensitive partial match)
        """
        matching_tasks = []
        for task in self._tasks.values():
            if title.lower() in task.title.lower():
                matching_tasks.append(task)
        return matching_tasks

    def add_user(self, user: User) -> User:
        """
        Add a new user to the store
        """
        self._users[user.username] = user
        self.save_to_file()  # Save to file after modification
        return user

    def get_user(self, username: str) -> Optional[User]:
        """
        Get a user by username
        """
        return self._users.get(username)

    def get_total_task_count(self) -> int:
        """
        Get the total count of tasks
        """
        return len(self._tasks)


# Global instance of the file-based store
task_store = FileTaskStore()