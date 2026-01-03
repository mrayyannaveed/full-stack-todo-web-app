#!/usr/bin/env python3
"""
Demo script to show the complete todo workflow: add, update, view, mark complete, delete
"""
from todo_cli.state import todo_store
from todo_cli.service import todo_service
from todo_cli.models import CreateTodoRequest, UpdateTodoRequest
import uuid

def main():
    print("=== Todo CLI Workflow Demo ===\n")

    # 1. ADD a new todo
    print("1. ADDING a new todo:")
    create_request = CreateTodoRequest(title="Learn FastAPI Integration", description="Explore how FastAPI is used in the CLI")
    new_todo = todo_service.create_todo(create_request)
    print(f"   Added todo: {new_todo.id} - {new_todo.title}")
    print(f"   Description: {new_todo.description}")
    print(f"   Completed: {new_todo.completed}\n")

    # 2. VIEW all todos
    print("2. VIEWING all todos:")
    all_todos = todo_service.get_all_todos()
    for todo in all_todos:
        status = 'x' if todo.completed else ' '
        description = f" - {todo.description}" if todo.description else ""
        print(f"   [{status}] {todo.id} - {todo.title}{description}")
    print()

    # 3. UPDATE the todo
    print("3. UPDATING the todo:")
    update_request = UpdateTodoRequest(title="Master FastAPI Integration", description="Deep dive into FastAPI usage in CLI apps")
    updated_todo = todo_service.update_todo(new_todo.id, update_request.title, update_request.description)
    if updated_todo:
        print(f"   Updated todo: {updated_todo.id}")
        print(f"   New title: {updated_todo.title}")
        print(f"   New description: {updated_todo.description}")
    print()

    # 4. VIEW the updated todo
    print("4. VIEWING the updated todo:")
    updated_from_store = todo_service.get_todo(new_todo.id)
    if updated_from_store:
        status = 'x' if updated_from_store.completed else ' '
        description = f" - {updated_from_store.description}" if updated_from_store.description else ""
        print(f"   [{status}] {updated_from_store.id} - {updated_from_store.title}{description}")
    print()

    # 5. MARK as complete
    print("5. MARKING todo as complete:")
    completed_todo = todo_service.mark_complete(new_todo.id)
    if completed_todo:
        print(f"   Marked as complete: {completed_todo.id} - {completed_todo.title}")
        print(f"   Completed status: {completed_todo.completed}")
    print()

    # 6. VIEW after marking complete
    print("6. VIEWING todo after marking complete:")
    completed_from_store = todo_service.get_todo(new_todo.id)
    if completed_from_store:
        status = 'x' if completed_from_store.completed else ' '
        description = f" - {completed_from_store.description}" if completed_from_store.description else ""
        print(f"   [{status}] {completed_from_store.id} - {completed_from_store.title}{description}")
    print()

    # 7. DELETE the todo
    print("7. DELETING the todo:")
    delete_success = todo_service.delete_todo(new_todo.id)
    if delete_success:
        print(f"   Deleted todo with ID: {new_todo.id}")
    else:
        print(f"   Failed to delete todo with ID: {new_todo.id}")
    print()

    # 8. VIEW all todos after deletion
    print("8. VIEWING all todos after deletion:")
    remaining_todos = todo_service.get_all_todos()
    if remaining_todos:
        for todo in remaining_todos:
            status = 'x' if todo.completed else ' '
            description = f" - {todo.description}" if todo.description else ""
            print(f"   [{status}] {todo.id} - {todo.title}{description}")
    else:
        print("   No todos found.")

    print("\n=== Workflow completed successfully! ===")

if __name__ == "__main__":
    main()