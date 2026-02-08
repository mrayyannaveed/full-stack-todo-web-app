"""
Service layer for the Todo CLI application using FastAPI as internal service
"""
from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from .models import Task, CreateTaskRequest, UpdateTaskRequest, TaskSearchRequest, User, Status
from .state import task_store


class TaskService:
    """
    Service layer for task operations
    """
    def __init__(self):
        self.app = FastAPI(title="Task CLI Internal API", description="Internal API for the Task CLI application")

        # Define API routes
        @self.app.post("/tasks", response_model=Task, status_code=201)
        def create_task(request: CreateTaskRequest, username: str):
            return self.create_task(request, username)

        @self.app.get("/tasks", response_model=List[Task])
        def get_all_tasks(username: str):
            return self.get_all_tasks(username)

        @self.app.get("/tasks/{task_id}", response_model=Task)
        def get_task(task_id: int, username: str):
            task = self.get_task(task_id, username)
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
            return task

        @self.app.put("/tasks/{task_id}", response_model=Task)
        def update_task(task_id: int, username: str, request: UpdateTaskRequest):
            # Validate the request before attempting to update
            if request.title is not None and len(request.title.strip()) == 0:
                raise HTTPException(status_code=400, detail="Title cannot be empty")

            updated_task = self.update_task(task_id, username, request.title, request.description)
            if not updated_task:
                raise HTTPException(status_code=404, detail="Task not found")
            return updated_task

        @self.app.delete("/tasks/{task_id}", status_code=204)
        def delete_task(task_id: int, username: str):
            success = self.delete_task(task_id, username)
            if not success:
                raise HTTPException(status_code=404, detail="Task not found")
            return {"detail": "Task deleted successfully"}

        @self.app.post("/tasks/{task_id}/complete", response_model=Task)
        def mark_complete(task_id: int, username: str):
            task = self.mark_complete(task_id, username)
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
            return task

        @self.app.post("/tasks/{task_id}/incomplete", response_model=Task)
        def mark_incomplete(task_id: int, username: str):
            task = self.mark_incomplete(task_id, username)
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
            return task

        @self.app.get("/tasks/search", response_model=List[Task])
        def search_tasks(search_term: str, username: str, search_by: str = "id_or_title"):
            return self.search_tasks(search_term, username, search_by)

    def create_task(self, request: CreateTaskRequest, username: str) -> Task:
        """
        Create a new task with sequential ID assignment and due date handling for a specific user
        """
        # Parse due date if provided
        due_date = None
        if request.due_date:
            try:
                due_date = datetime.strptime(request.due_date, '%Y-%m-%d')
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid due date format. Use YYYY-MM-DD.")

        # Create a new Task instance with the provided data
        new_task = Task(
            id=0,  # Will be assigned by the store
            title=request.title,
            priority=request.priority,
            description=request.description,
            due_date=due_date,
            status=Status.PENDING,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        return task_store.add_task(new_task, username)

    def get_all_tasks(self, username: str) -> List[Task]:
        """
        Get all tasks for a specific user
        """
        return task_store.get_all_tasks(username)

    def get_task(self, task_id: int, username: str) -> Optional[Task]:
        """
        Get a specific task by ID for a specific user
        """
        return task_store.get_task(task_id, username)

    def update_task(self, task_id: int, username: str, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task for a specific user, preserving unchanged fields
        """
        return task_store.update_task(task_id, username, title, description)

    def delete_task(self, task_id: int, username: str) -> bool:
        """
        Delete a task by ID for a specific user
        """
        return task_store.delete_task(task_id, username)

    def mark_complete(self, task_id: int, username: str) -> Optional[Task]:
        """
        Mark a task as complete for a specific user
        """
        return task_store.mark_complete(task_id, username)

    def mark_incomplete(self, task_id: int, username: str) -> Optional[Task]:
        """
        Mark a completed task as incomplete for a specific user
        """
        return task_store.mark_incomplete(task_id, username)

    def search_tasks(self, search_term: str, username: str, search_by: str = "id_or_title") -> List[Task]:
        """
        Search for tasks by ID or title based on search_by parameter for a specific user
        """
        if search_by == "id":
            try:
                task_id = int(search_term)
                task = task_store.search_tasks_by_id(task_id, username)
                if task:
                    return [task]
                else:
                    return []
            except ValueError:
                # If search_term is not a valid integer for ID search, return empty list
                return []
        elif search_by == "title":
            return task_store.search_tasks_by_title(search_term, username)
        elif search_by == "id_or_title":
            # Try both ID and title search
            try:
                task_id = int(search_term)
                task = task_store.search_tasks_by_id(task_id, username)
                if task:
                    return [task]
            except ValueError:
                # If not a valid ID, continue with title search
                pass
            # Combine results from both searches
            title_results = task_store.search_tasks_by_title(search_term, username)
            return title_results
        else:
            # Default to searching both ID and title
            try:
                task_id = int(search_term)
                task = task_store.search_tasks_by_id(task_id, username)
                if task:
                    return [task]
            except ValueError:
                pass
            title_results = task_store.search_tasks_by_title(search_term, username)
            return title_results

    def get_total_task_count(self, username: str) -> int:
        """
        Get the total count of tasks for a specific user
        """
        return task_store.get_total_task_count(username)

    def add_user(self, user: User) -> User:
        """
        Add a new user
        """
        return task_store.add_user(user)

    def get_user(self, username: str) -> Optional[User]:
        """
        Get a user by username
        """
        return task_store.get_user(username)


# Create a global instance of the service
task_service = TaskService()