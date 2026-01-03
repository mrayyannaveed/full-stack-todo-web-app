# Quickstart Guide: In-Memory Python CLI Todo Application

## Prerequisites
- Python 3.13+
- UV package manager (for fast dependency resolution)

## Setup
1. Clone the repository
2. Navigate to the `todo-cli` directory
3. Install dependencies:
   ```bash
   uv sync
   ```
   Or alternatively:
   ```bash
   pip install -e .
   ```

## Running the Application
Run the CLI application:
```bash
python -m src.todo_cli.main
```

Or if installed as a package:
```bash
todo
```

## Usage Guide

### Authentication
- On first run, enter a new username when prompted
- Create and confirm your password
- On subsequent runs, enter your existing username and password

### Main Menu Options
1. **Add Tasks**: Create new tasks with title, priority, description, and due date
2. **View Tasks**: See all your tasks with ID, status, priority, and due date
3. **Update Tasks**: Modify existing task title or description
4. **Delete Tasks**: Remove tasks by ID
5. **Mark Complete/Incomplete**: Toggle task completion status
6. **Search/Filter Tasks**: Find tasks by ID or title
7. **Exit**: Close the application

### Task Fields
- **Title**: Required text for the task
- **Priority**: High, Medium, or Low (default: Medium)
- **Description**: Optional additional details
- **Due Date**: Optional date in YYYY-MM-DD format

## Development
- All data is stored in-memory only (no persistence between sessions)
- The application uses Click for the CLI interface
- Pydantic for data validation
- FastAPI for internal API structure