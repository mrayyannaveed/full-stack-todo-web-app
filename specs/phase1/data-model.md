# Data Model: In-Memory Todo CLI Application

## Entity: Todo

### Fields
- **id**: UUID (required) - Unique identifier for the todo
- **title**: string (required) - Title of the todo task
- **description**: string (optional) - Optional description of the todo task
- **completed**: boolean (required) - Completion status of the todo
- **created_at**: datetime (required) - Timestamp when the todo was created
- **updated_at**: datetime (required) - Timestamp when the todo was last updated

### Validation Rules
- title must be a non-empty string
- id must be a valid UUID
- completed must be a boolean value
- created_at and updated_at must be valid datetime objects
- updated_at must be updated when any field changes

### State Transitions
- **Creation**: New todo is created with completed=False, id generated automatically, created_at and updated_at set to current time
- **Update**: When any field changes, updated_at is set to current time
- **Complete**: completed field changes from False to True
- **Reopen**: completed field changes from True to False

### Relationships
- No relationships with other entities (standalone entity)

### Constraints
- Title cannot be empty
- ID must be unique across all todos
- created_at is immutable after creation
- updated_at is automatically updated on any modification