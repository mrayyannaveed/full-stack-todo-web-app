# Feature Specification: In-Memory Python CLI Todo Application

**Feature Branch**: `001-in-memory-todo-cli`
**Created**: 2025-12-29
**Status**: Draft
**Input**: User description: "Phase I: In-Memory Python CLI Todo Application"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Application Start and Authentication (Priority: P1)

A user wants to run the CLI todo application. When they execute the program, they are prompted for a username, and if it's a new user, they create a password. Returning users authenticate with their existing credentials.

**Why this priority**: This is the foundational user experience that allows users to access the application. Without this initial authentication flow, users cannot use any of the other features.

**Independent Test**: Can be fully tested by running the application, entering a new username to create an account, and then logging in with the same credentials. Delivers the basic application access functionality.

**Acceptance Scenarios**:

1. **Given** a new username is provided, **When** user runs the application, **Then** they are prompted to create and confirm a password, and a welcome message is displayed
2. **Given** an existing username is provided, **When** user runs the application, **Then** they are authenticated and a welcome message is displayed

---

### User Story 2 - Main Menu Navigation (Priority: P1)

A user wants to navigate the main menu to access different todo management functions like adding, viewing, updating, deleting, and marking tasks.

**Why this priority**: This provides the core navigation experience that connects all other functionality together. Users need to be able to access all features through a consistent menu system.

**Independent Test**: Can be fully tested by running the application, viewing the main menu options, and selecting different options to verify they are properly presented to the user.

**Acceptance Scenarios**:

1. **Given** user is authenticated, **When** main menu is displayed, **Then** all 7 menu options (Add, View, Update, Delete, Mark Complete/Incomplete, Search/Filter, Exit) are presented clearly
2. **Given** main menu is displayed, **When** user selects an option, **Then** the appropriate submenu or functionality is accessed

---

### User Story 3 - Add Tasks (Priority: P1)

A user wants to create new tasks with title, priority, description, and due date. The system assigns a unique ID and displays accurate remaining time.

**Why this priority**: This is one of the core functions of a todo application - users must be able to add tasks to manage them.

**Independent Test**: Can be fully tested by adding a new task with all required and optional fields, and verifying the task is created with correct details and assigned ID.

**Acceptance Scenarios**:

1. **Given** user is in add task mode, **When** they provide a title and other optional fields, **Then** a new task is created with sequential ID and displayed with remaining time
2. **Given** user adds a task, **When** task details are confirmed, **Then** the task details are displayed showing ID, due date, status, title, and description

---

### User Story 4 - View Tasks (Priority: P1)

A user wants to see all their tasks displayed with relevant information including ID, due date, status, title, and description.

**Why this priority**: This is fundamental functionality that allows users to see their tasks at a glance, which is essential for task management.

**Independent Test**: Can be fully tested by creating several tasks and then viewing the task list to verify all tasks are displayed with correct information.

**Acceptance Scenarios**:

1. **Given** multiple tasks exist, **When** user selects view tasks option, **Then** all tasks are displayed with ID, due date, status, title, and description
2. **Given** no tasks exist, **When** user selects view tasks option, **Then** appropriate message is displayed indicating no tasks exist

---

### User Story 5 - Update and Delete Tasks (Priority: P2)

A user wants to modify existing tasks (title and description) or remove tasks they no longer need.

**Why this priority**: These are essential management functions that allow users to maintain their task lists over time as requirements change.

**Independent Test**: Can be fully tested by creating a task, updating its details, and then deleting it to verify both operations work correctly.

**Acceptance Scenarios**:

1. **Given** a task exists, **When** user updates the title or description, **Then** the task details are updated while preserving unchanged fields
2. **Given** a task exists, **When** user deletes the task by ID, **Then** the task is removed and confirmation is provided

---

### User Story 6 - Mark Complete/Incomplete (Priority: P2)

A user wants to toggle the completion status of tasks to track which ones are done and which are pending.

**Why this priority**: This is a core functionality for task management, allowing users to track progress and completion status.

**Independent Test**: Can be fully tested by creating a task, marking it complete, then marking it incomplete again to verify the status can be toggled.

**Acceptance Scenarios**:

1. **Given** a pending task exists, **When** user marks it complete, **Then** the task status changes to completed and reflects in the task list
2. **Given** a completed task exists, **When** user marks it incomplete, **Then** the task status changes to pending and reflects in the task list

---

### User Story 7 - Search/Filter Tasks (Priority: P3)

A user wants to find specific tasks by searching for them by ID or title.

**Why this priority**: This is a convenience feature that helps users quickly find specific tasks when they have many tasks in their list.

**Independent Test**: Can be fully tested by creating multiple tasks and then searching for them by ID or title to verify only matching tasks are displayed.

**Acceptance Scenarios**:

1. **Given** multiple tasks exist, **When** user searches by ID, **Then** only the matching task is displayed
2. **Given** multiple tasks exist, **When** user searches by title, **Then** all matching tasks are displayed

---

### Edge Cases

- What happens when a user enters invalid credentials multiple times?
- How does the system handle invalid menu selections or non-existent task IDs?
- What occurs when due dates are in the past or invalid date formats are entered?
- How does the system handle empty titles when adding tasks?
- What happens when trying to update/delete/complete a task that doesn't exist?
- How does the system handle very long text inputs for titles or descriptions?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST run via `python todo_cli/main.py` command
- **FR-002**: System MUST prompt for username on application start
- **FR-003**: System MUST create a new account if username is new, prompting for password creation and confirmation
- **FR-004**: System MUST authenticate returning users with their existing credentials
- **FR-005**: System MUST display a welcome message showing "Welcome to CLI Todo App" and "Hi, <username>" after successful authentication
- **FR-006**: System MUST show the total task count after the welcome message
- **FR-007**: System MUST display a main menu with 7 options: Add Tasks, View Tasks, Update Tasks, Delete Tasks, Mark Complete/Incomplete, Search/Filter Tasks, and Exit
- **FR-008**: System MUST allow users to add tasks with required title and optional priority (High/Medium/Low), description, and due date (YYYY-MM-DD)
- **FR-009**: System MUST assign sequential numeric IDs to tasks when they are created
- **FR-010**: System MUST calculate and display accurate remaining time for due dates
- **FR-011**: System MUST confirm successful task creation and display created task details
- **FR-012**: System MUST display task list with ID, Due Date, Status ([pending] or [completed]), Title, and Description
- **FR-013**: System MUST allow updating of task Title and Description while preserving unchanged fields
- **FR-014**: System MUST delete tasks by ID and confirm deletion
- **FR-015**: System MUST handle invalid IDs gracefully when deleting tasks
- **FR-016**: System MUST toggle task status by ID with Mark Complete/Incomplete functionality
- **FR-017**: System MUST reflect status changes in the task list after toggling completion
- **FR-018**: System MUST support searching/filtering tasks by ID or title
- **FR-019**: System MUST display only matching tasks when searching/filtering
- **FR-020**: System MUST provide graceful termination when Exit option is selected
- **FR-021**: System MUST store all data in memory only (no persistent storage)
- **FR-022**: System MUST ensure task IDs are unique and sequential
- **FR-023**: System MUST ensure task completion is reversible
- **FR-024**: System MUST ensure due date calculations are accurate at all times

### Key Entities

- **User**: An authenticated user with a username and password for accessing the todo application
- **Task**: A todo item with ID (sequential numeric), Title (required string), Priority (optional: High/Medium/Low), Description (optional string), Due Date (optional date in YYYY-MM-DD format), Status (pending/completed), and Remaining Time (calculated from due date)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully run the application, authenticate, and access the main menu within 10 seconds of starting
- **SC-002**: All 5 basic todo functions (Add, View, Update, Delete, Mark Complete/Incomplete) work reliably without crashes
- **SC-003**: Task data persists correctly in memory during a single application session
- **SC-004**: All menu navigation options work as expected and return users to appropriate menus
- **SC-005**: Due date calculations are accurate and updated in real-time
- **SC-006**: Search/Filter functionality correctly returns matching tasks by ID or title
- **SC-007**: The application gracefully handles all edge cases and invalid inputs with appropriate error messages
- **SC-008**: The application exits cleanly when the Exit option is selected
