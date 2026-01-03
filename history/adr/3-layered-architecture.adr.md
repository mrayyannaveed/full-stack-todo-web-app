# ADR-3: Layered Application Architecture for CLI Todo Application

**Status**: Accepted
**Date**: 2025-12-29

## Context

The application needs a well-structured architecture that separates concerns between user interface, business logic, and data management while supporting all required CLI operations in an in-memory context.

## Decision

We will implement a layered architecture with three distinct layers:

- **CLI Layer**: Handles user input/output, menu navigation, and command processing (using Click framework)
- **Service Layer**: Contains business logic, validation, and orchestration (using FastAPI internally as service layer)
- **State Layer**: Manages in-memory data storage and retrieval operations

This architecture will be implemented as a single project with separate modules:
- `cli.py` for CLI interface
- `service.py` for business logic
- `state.py` for in-memory state management
- `models.py` for data models

## Alternatives Considered

- **Monolithic approach**: Single file or module for all functionality - rejected for poor maintainability and separation of concerns
- **Microservices**: Separate services for each layer - rejected as overkill for a single-user CLI application
- **Different layering**: Alternative approaches like MVC or domain-driven design - rejected in favor of simple layering appropriate for CLI application

## Consequences

**Positive:**
- Clear separation of concerns improves maintainability and testability
- Each layer can be developed and tested independently
- Business logic is centralized and reusable
- CLI interface can be changed without affecting core logic
- State management is isolated and can be modified independently

**Negative:**
- Additional complexity compared to monolithic approach
- Multiple files and dependencies to manage
- Potential over-engineering for simple application (mitigated by the need for clean architecture)

## References

- plan.md: Project Structure section and architecture description
- research.md: Decision on FastAPI as internal service layer