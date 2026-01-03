#!/usr/bin/env python3
"""
Demo script showing how to use the CLI commands for the complete workflow
Note: This won't work as expected for persistence since each CLI command
runs in a separate process with its own in-memory store.
"""
print("=== CLI Commands for Todo Workflow ===")
print()
print("# 1. ADD a new todo")
print("todo add \"Learn FastAPI Integration\" --description \"Explore how FastAPI is used in the CLI\"")
print()
print("# 2. VIEW all todos")
print("todo list")
print()
print("# 3. UPDATE the todo (you would need the actual todo ID from the list)")
print("# todo update <todo-id> --title \"Master FastAPI Integration\" --description \"Deep dive into FastAPI usage in CLI apps\"")
print()
print("# 4. MARK as complete (you would need the actual todo ID from the list)")
print("# todo complete <todo-id>")
print()
print("# 5. DELETE the todo (you would need the actual todo ID from the list)")
print("# todo delete <todo-id>")
print()
print("=== Note ===")
print("Each CLI command runs in a separate Python process with its own in-memory store,")
print("so todos won't persist between commands. The in-memory store is only maintained")
print("within a single process execution.")