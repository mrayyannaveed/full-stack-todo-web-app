# Todo CLI Application

A command-line interface application for managing todos with in-memory storage.

## Features

- Add new todos with titles and optional descriptions
- List all todos with their completion status
- Update existing todos
- Delete todos
- Mark todos as complete/incomplete

## Installation

1. Clone the repository
2. Install dependencies: `uv sync`
3. Activate the virtual environment: `uv venv`

## Usage

```bash
# Add a new todo
todo add "Buy groceries" --description "Milk, bread, eggs"

# List all todos
todo list

# Update a todo
todo update <todo-id> --title "Updated title" --description "Updated description"

# Delete a todo
todo delete <todo-id>

# Mark a todo as complete
todo complete <todo-id>

# Reopen a completed todo
todo reopen <todo-id>
```

### Example Usage

```bash
# Add a few todos
todo add "Learn Python"
todo add "Build CLI app" --description "Create a todo CLI application"
todo add "Deploy application"

# List all todos
todo list

# Update a todo
todo update 123e4567-e89b-12d3-a456-426614174000 --title "Master Python"

# Mark a todo as complete
todo complete 123e4567-e89b-12d3-a456-426614174000

# Reopen a completed todo
todo reopen 123e4567-e89b-12d3-a456-426614174000

# Delete a todo
todo delete 123e4567-e89b-12d3-a456-426614174000
```

## Architecture

The application follows a layered architecture:
1. **CLI Layer**: Handles command-line arguments and user interaction
2. **Service Layer**: Implements business logic using FastAPI internally
3. **State Layer**: Manages in-memory storage
4. **Model Layer**: Defines data structures and validation