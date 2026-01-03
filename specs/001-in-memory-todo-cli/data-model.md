# Data Model: In-Memory Python CLI Todo Application

## Task Entity

### Fields
- **id**: int (required) - Sequential numeric ID assigned when task is created (FR-009, FR-022)
- **title**: string (required) - Title of the task (FR-008)
- **description**: string (optional) - Optional description of the task (FR-008)
- **status**: string (required) - Task completion status - "pending" or "completed" (FR-012, FR-016)
- **priority**: string (optional) - Priority level - "High", "Medium", or "Low" (FR-008)
- **due_date**: datetime (optional) - Optional due date in YYYY-MM-DD format (FR-008)
- **created_at**: datetime (required) - Timestamp when the task was created
- **updated_at**: datetime (required) - Timestamp when the task was last updated

### Validation Rules
- title must be a non-empty string (FR-008)
- id must be a sequential integer unique per session (FR-022)
- status must be either "pending" or "completed" (FR-012)
- priority must be one of "High", "Medium", or "Low" if provided (FR-008)
- due_date must be in valid YYYY-MM-DD format if provided (FR-008)
- created_at and updated_at must be valid datetime objects
- updated_at must be updated when any field changes

### State Transitions
- **Creation**: New task is created with status="pending", sequential id assigned, created_at and updated_at set to current time
- **Update**: When any field changes, updated_at is set to current time
- **Complete**: status changes from "pending" to "completed" (FR-016)
- **Incomplete**: status changes from "completed" to "pending" (FR-023)

### Relationships
- No relationships with other entities (standalone entity)

### Constraints
- Title cannot be empty (FR-008)
- ID must be unique and sequential across all tasks in session (FR-022)
- created_at is immutable after creation
- updated_at is automatically updated on any modification

## User Entity

### Fields
- **username**: string (required) - Unique identifier for user authentication
- **password**: string (required) - Hashed password for authentication

### Validation Rules
- username must be unique across all users
- username cannot be empty
- password must be at least 6 characters (implementation detail)