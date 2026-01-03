from todo_cli.state import task_store
from todo_cli.models import Task, Priority
from datetime import datetime

# Test creating a task directly
print("Testing task creation...")
task = Task(
    id=0,  # Will be assigned by store
    title="Test task",
    priority=Priority.MEDIUM,
    description="Test description",
    status="pending",
    created_at=datetime.now(),
    updated_at=datetime.now()
)

# Add to store
added_task = task_store.add_task(task)
print(f"Task added with ID: {added_task.id}")

# Get all tasks
all_tasks = task_store.get_all_tasks()
print(f"Total tasks: {len(all_tasks)}")

# Test search functionality
search_result = task_store.search_tasks_by_title("Test")
print(f"Search results: {len(search_result)}")

print("Basic functionality test passed!")