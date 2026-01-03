# Quickstart: In-Memory Todo CLI Application

## Prerequisites
- Python 3.13+
- UV package manager

## Setup
1. Clone or create the project directory
2. Install dependencies: `uv sync`
3. Activate the virtual environment: `uv venv` (if needed)

## Usage

### Adding a Todo
```bash
todo add "Buy groceries" --description "Milk, bread, eggs"
```

### Listing Todos
```bash
todo list
```

### Updating a Todo
```bash
todo update <todo-id> --title "Updated title" --description "Updated description"
```

### Deleting a Todo
```bash
todo delete <todo-id>
```

### Marking a Todo as Complete
```bash
todo complete <todo-id>
```

### Reopening a Completed Todo
```bash
todo reopen <todo-id>
```

## Development

### Running Tests
```bash
uv run pytest
```

### Running the Application
```bash
uv run python -m todo_cli
```

## Architecture

The application follows a layered architecture:
1. **CLI Layer**: Handles command-line arguments and user interaction
2. **Service Layer**: Implements business logic using FastAPI internally
3. **State Layer**: Manages in-memory storage
4. **Model Layer**: Defines data structures and validation