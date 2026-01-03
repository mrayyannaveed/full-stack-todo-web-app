---
description: "Task list template for feature implementation"
---

# Tasks: In-Memory Todo CLI Application

**Input**: Design documents from `/specs/phase1/`
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

- [ ] T001 Create project structure per implementation plan in todo-cli/
- [ ] T002 Initialize Python project with uv dependencies in pyproject.toml
- [ ] T003 [P] Configure linting and formatting tools (black, flake8, mypy)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Setup basic project structure with src/todo_cli/ directory
- [ ] T005 [P] Create models module with Todo Pydantic model in src/todo_cli/models.py
- [ ] T006 Create state management module for in-memory storage in src/todo_cli/state.py
- [ ] T007 Create service layer with FastAPI app in src/todo_cli/service.py
- [ ] T008 Create CLI module structure in src/todo_cli/cli.py
- [ ] T009 Configure error handling and logging infrastructure in src/todo_cli/
- [ ] T010 Setup environment configuration management

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and List Todos (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks and view all existing tasks

**Independent Test**: Can be fully tested by adding a few todos and listing them. Delivers core value of task management.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T011 [P] [US1] Contract test for /todos endpoint in tests/contract/test_todos.py
- [ ] T012 [P] [US1] Integration test for add/list user journey in tests/integration/test_add_list.py

### Implementation for User Story 1

- [ ] T013 [P] [US1] Create Todo model with id, title, description, completed, timestamps in src/todo_cli/models.py
- [ ] T014 [US1] Implement in-memory storage with add_todo and list_todos functions in src/todo_cli/state.py
- [ ] T015 [US1] Implement create_todo and get_all_todos endpoints in src/todo_cli/service.py
- [ ] T016 [US1] Implement add and list commands in src/todo_cli/cli.py
- [ ] T017 [US1] Add validation for non-empty titles in src/todo_cli/models.py
- [ ] T018 [US1] Add logging for add/list operations in src/todo_cli/cli.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Update and Delete Todos (Priority: P2)

**Goal**: Enable users to modify or remove existing tasks as their needs change

**Independent Test**: Can be tested by creating a todo, updating its details, and then deleting it. Ensures data management capabilities.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T019 [P] [US2] Contract test for /todos/{id} endpoint in tests/contract/test_todos.py
- [ ] T020 [P] [US2] Integration test for update/delete user journey in tests/integration/test_update_delete.py

### Implementation for User Story 2

- [ ] T021 [P] [US2] Create UpdateTodoRequest model in src/todo_cli/models.py
- [ ] T022 [US2] Implement update_todo and delete_todo functions in src/todo_cli/state.py
- [ ] T023 [US2] Implement update_todo and delete_todo endpoints in src/todo_cli/service.py
- [ ] T024 [US2] Implement update and delete commands in src/todo_cli/cli.py
- [ ] T025 [US2] Add validation for existing todo IDs in src/todo_cli/service.py
- [ ] T026 [US2] Add logging for update/delete operations in src/todo_cli/cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Complete and Reopen Todos (Priority: P3)

**Goal**: Provide essential workflow functionality for tracking task completion status

**Independent Test**: Can be tested by creating a todo, marking it complete, and then reopening it. Delivers task lifecycle management.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T027 [P] [US3] Contract test for /todos/{id}/complete and /todos/{id}/reopen endpoints in tests/contract/test_todos.py
- [ ] T028 [P] [US3] Integration test for complete/reopen user journey in tests/integration/test_complete_reopen.py

### Implementation for User Story 3

- [ ] T029 [P] [US3] Implement mark_complete and mark_reopen functions in src/todo_cli/state.py
- [ ] T030 [US3] Implement complete_todo and reopen_todo endpoints in src/todo_cli/service.py
- [ ] T031 [US3] Implement complete and reopen commands in src/todo_cli/cli.py
- [ ] T032 [US3] Add validation for existing todo IDs in src/todo_cli/service.py
- [ ] T033 [US3] Add logging for complete/reopen operations in src/todo_cli/cli.py

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T034 [P] Documentation updates in README.md
- [ ] T035 Code cleanup and refactoring
- [ ] T036 Performance optimization across all stories
- [ ] T037 [P] Additional unit tests (if requested) in tests/unit/
- [ ] T038 Error handling for edge cases (invalid IDs, empty titles) in src/todo_cli/service.py
- [ ] T039 [P] Update quickstart guide with usage examples in docs/quickstart.md

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
Task: "Contract test for /todos endpoint in tests/contract/test_todos.py"
Task: "Integration test for add/list user journey in tests/integration/test_add_list.py"

# Launch all models for User Story 1 together:
Task: "Create Todo model with id, title, description, completed, timestamps in src/todo_cli/models.py"
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
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
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