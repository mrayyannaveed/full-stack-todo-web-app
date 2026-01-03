---
description: "Task list for In-Memory Python CLI Todo Application implementation"
---

# Tasks: In-Memory Python CLI Todo Application

**Input**: Design documents from `/specs/001-in-memory-todo-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in todo-cli/
- [X] T002 Initialize Python project with uv dependencies in pyproject.toml
- [X] T003 [P] Configure linting and formatting tools (black, flake8, mypy)
- [X] T004 [P] Set up Click CLI framework dependencies in pyproject.toml
- [X] T005 [P] Set up FastAPI internal service layer dependencies in pyproject.toml

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Setup basic project structure with src/todo_cli/ directory
- [X] T007 [P] Create models module with User and Task Pydantic models in src/todo_cli/models.py
- [X] T008 Create state management module for in-memory storage in src/todo_cli/state.py
- [X] T009 Create service layer with FastAPI app in src/todo_cli/service.py
- [X] T010 Create CLI module structure in src/todo_cli/cli.py
- [X] T011 Configure error handling and logging infrastructure in src/todo_cli/
- [X] T012 Setup authentication and user management infrastructure in src/todo_cli/auth.py
- [X] T013 Create main application entry point in src/todo_cli/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Application Start and Authentication (Priority: P1) 🎯 MVP

**Goal**: Enable users to run the CLI todo application, authenticate with username/password, and receive a welcome message with total task count

**Independent Test**: Can be fully tested by running the application, entering a new username to create an account, and then logging in with the same credentials. Delivers the basic application access functionality.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T014 [P] [US1] Unit test for user authentication in tests/unit/test_auth.py
- [X] T015 [P] [US1] Integration test for application startup flow in tests/integration/test_startup.py

### Implementation for User Story 1

- [X] T016 [P] [US1] Create User model with username and password in src/todo_cli/models.py
- [X] T017 [US1] Implement user authentication and management in src/todo_cli/auth.py
- [X] T018 [US1] Implement user creation with password confirmation in src/todo_cli/auth.py
- [X] T019 [US1] Implement application startup flow in src/todo_cli/main.py
- [X] T020 [US1] Implement welcome message display with username in src/todo_cli/main.py
- [X] T021 [US1] Implement total task count display in src/todo_cli/main.py
- [X] T022 [US1] Add validation for username and password requirements in src/todo_cli/models.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Main Menu Navigation (Priority: P1)

**Goal**: Provide main menu navigation to access different todo management functions like adding, viewing, updating, deleting, and marking tasks

**Independent Test**: Can be fully tested by running the application, viewing the main menu options, and selecting different options to verify they are properly presented to the user.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T023 [P] [US2] Unit test for menu navigation in tests/unit/test_menu.py
- [X] T024 [P] [US2] Integration test for main menu functionality in tests/integration/test_menu.py

### Implementation for User Story 2

- [X] T025 [P] [US2] Implement main menu display with 7 options in src/todo_cli/cli.py
- [X] T026 [US2] Implement menu option selection and routing in src/todo_cli/cli.py
- [X] T027 [US2] Create navigation handlers for each menu option in src/todo_cli/cli.py
- [X] T028 [US2] Implement graceful exit functionality in src/todo_cli/cli.py
- [X] T029 [US2] Add menu validation and error handling in src/todo_cli/cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Add Tasks (Priority: P1)

**Goal**: Enable users to create new tasks with title, priority, description, and due date, with sequential ID assignment and accurate remaining time display

**Independent Test**: Can be fully tested by adding a new task with all required and optional fields, and verifying the task is created with correct details and assigned ID.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T030 [P] [US3] Unit test for task creation in tests/unit/test_task_creation.py
- [X] T031 [P] [US3] Integration test for add task functionality in tests/integration/test_add_task.py

### Implementation for User Story 3

- [X] T032 [P] [US3] Update Task model with priority, description, due date, and status fields in src/todo_cli/models.py
- [X] T033 [US3] Implement task creation with sequential ID assignment in src/todo_cli/state.py
- [X] T034 [US3] Implement due date calculation and remaining time display in src/todo_cli/models.py
- [X] T035 [US3] Implement add task command in src/todo_cli/cli.py
- [X] T036 [US3] Implement task creation endpoint in src/todo_cli/service.py
- [X] T037 [US3] Add validation for required title and optional fields in src/todo_cli/models.py
- [X] T038 [US3] Implement task confirmation and display in src/todo_cli/cli.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - View Tasks (Priority: P1)

**Goal**: Enable users to see all their tasks displayed with relevant information including ID, due date, status, title, and description

**Independent Test**: Can be fully tested by creating several tasks and then viewing the task list to verify all tasks are displayed with correct information.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T039 [P] [US4] Unit test for task listing in tests/unit/test_task_listing.py
- [X] T040 [P] [US4] Integration test for view tasks functionality in tests/integration/test_view_tasks.py

### Implementation for User Story 4

- [X] T041 [P] [US4] Implement task listing with all required fields in src/todo_cli/state.py
- [X] T042 [US4] Implement view tasks command in src/todo_cli/cli.py
- [X] T043 [US4] Implement task listing endpoint in src/todo_cli/service.py
- [X] T044 [US4] Format task display with ID, due date, status, title, and description in src/todo_cli/cli.py
- [X] T045 [US4] Handle case when no tasks exist in src/todo_cli/cli.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Update and Delete Tasks (Priority: P2)

**Goal**: Enable users to modify existing tasks (title and description) or remove tasks they no longer need, preserving unchanged fields

**Independent Test**: Can be fully tested by creating a task, updating its details, and then deleting it to verify both operations work correctly.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T046 [P] [US5] Unit test for task update/delete in tests/unit/test_task_update_delete.py
- [X] T047 [P] [US5] Integration test for update/delete functionality in tests/integration/test_update_delete.py

### Implementation for User Story 5

- [X] T048 [P] [US5] Implement task update functionality preserving unchanged fields in src/todo_cli/state.py
- [X] T049 [US5] Implement task deletion by ID in src/todo_cli/state.py
- [X] T050 [US5] Implement update task command in src/todo_cli/cli.py
- [X] T051 [US5] Implement delete task command in src/todo_cli/cli.py
- [X] T052 [US5] Implement update/delete endpoints in src/todo_cli/service.py
- [X] T053 [US5] Add validation for existing task IDs in src/todo_cli/service.py
- [X] T054 [US5] Handle invalid IDs gracefully in src/todo_cli/service.py

**Checkpoint**: At this point, User Stories 1-5 should all work independently

---

## Phase 8: User Story 6 - Mark Complete/Incomplete (Priority: P2)

**Goal**: Enable users to toggle the completion status of tasks to track which ones are done and which are pending

**Independent Test**: Can be fully tested by creating a task, marking it complete, then marking it incomplete again to verify the status can be toggled.

### Tests for User Story 6 (OPTIONAL - only if tests requested) ⚠️

- [X] T055 [P] [US6] Unit test for task completion toggle in tests/unit/test_task_completion.py
- [X] T056 [P] [US6] Integration test for mark complete/incomplete functionality in tests/integration/test_completion.py

### Implementation for User Story 6

- [X] T057 [P] [US6] Implement task status toggle functionality in src/todo_cli/state.py
- [X] T058 [US6] Implement mark complete/incomplete command in src/todo_cli/cli.py
- [X] T059 [US6] Implement completion endpoints in src/todo_cli/service.py
- [X] T060 [US6] Ensure status changes reflect in task list in src/todo_cli/state.py
- [X] T061 [US6] Add validation for existing task IDs in src/todo_cli/service.py

**Checkpoint**: At this point, User Stories 1-6 should all work independently

---

## Phase 9: User Story 7 - Search/Filter Tasks (Priority: P3)

**Goal**: Enable users to find specific tasks by searching for them by ID or title

**Independent Test**: Can be fully tested by creating multiple tasks and then searching for them by ID or title to verify only matching tasks are displayed.

### Tests for User Story 7 (OPTIONAL - only if tests requested) ⚠️

- [X] T062 [P] [US7] Unit test for task search/filter in tests/unit/test_task_search.py
- [X] T063 [P] [US7] Integration test for search/filter functionality in tests/integration/test_search.py

### Implementation for User Story 7

- [X] T064 [P] [US7] Implement search by ID functionality in src/todo_cli/state.py
- [X] T065 [US7] Implement search by title functionality in src/todo_cli/state.py
- [X] T066 [US7] Implement search/filter command in src/todo_cli/cli.py
- [X] T067 [US7] Implement search endpoints in src/todo_cli/service.py
- [X] T068 [US7] Format search results display showing only matching tasks in src/todo_cli/cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T069 [P] Documentation updates in README.md
- [X] T070 Code cleanup and refactoring
- [X] T071 Performance optimization across all stories
- [X] T072 [P] Additional unit tests (if requested) in tests/unit/
- [X] T073 Error handling for edge cases (invalid credentials, menu selections, etc.) in src/todo_cli/
- [X] T074 [P] Update quickstart guide with usage examples in docs/quickstart.md
- [X] T075 Validation for due date formats and past dates in src/todo_cli/models.py
- [X] T076 Handle empty titles and long text inputs in src/todo_cli/models.py

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable
- **User Story 6 (P6)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable
- **User Story 7 (P7)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for user authentication in tests/unit/test_auth.py"
Task: "Integration test for application startup flow in tests/integration/test_startup.py"

# Launch all models for User Story 1 together:
Task: "Create User model with username and password in src/todo_cli/models.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Add User Story 6 → Test independently → Deploy/Demo
8. Add User Story 7 → Test independently → Deploy/Demo
9. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
   - Developer F: User Story 6
   - Developer G: User Story 7
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence