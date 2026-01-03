#!/usr/bin/env python3
"""
Test script to verify file persistence functionality
"""
from todo_cli.state import task_store
from todo_cli.models import Task, Priority
from datetime import datetime

def test_persistence():
    print("Testing file persistence...")

    # Get initial task count
    initial_tasks = task_store.get_all_tasks()
    print(f"Initial tasks count: {len(initial_tasks)}")

    # Add a new task
    test_task = Task(
        id=0,  # Will be assigned by store
        title="Persistence Test Task",
        priority=Priority.HIGH,
        description="Test task to verify file persistence",
        status="pending",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    added_task = task_store.add_task(test_task)
    print(f"Added task with ID: {added_task.id}")

    # Verify task exists
    all_tasks = task_store.get_all_tasks()
    print(f"Total tasks after adding: {len(all_tasks)}")

    # Check if our task is there
    found_task = task_store.get_task(added_task.id)
    if found_task:
        print(f"Found task: {found_task.title}")
        print(f"Task priority: {found_task.priority}")
        print(f"Task status: {found_task.status}")
    else:
        print("ERROR: Task not found!")
        return False

    # Update the task
    updated_task = task_store.update_task(added_task.id, title="Updated Persistence Test Task")
    if updated_task:
        print(f"Updated task: {updated_task.title}")
    else:
        print("ERROR: Task update failed!")
        return False

    # Mark as complete
    completed_task = task_store.mark_complete(added_task.id)
    if completed_task:
        print(f"Marked task as complete: {completed_task.status}")
    else:
        print("ERROR: Mark complete failed!")
        return False

    # Delete the task
    delete_result = task_store.delete_task(added_task.id)
    if delete_result:
        print("Task deleted successfully")
    else:
        print("ERROR: Task deletion failed!")
        return False

    # Verify deletion
    final_tasks = task_store.get_all_tasks()
    print(f"Total tasks after deletion: {len(final_tasks)}")

    print("File persistence test completed successfully!")
    return True

if __name__ == "__main__":
    test_persistence()