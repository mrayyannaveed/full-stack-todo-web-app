# ADR-2: In-Memory Data Storage Architecture for Todo Application

**Status**: Accepted
**Date**: 2025-12-29

## Context

The application requires an in-memory storage solution for todo items that supports the core operations (add, list, update, delete, complete, reopen) while maintaining data integrity and efficient access patterns.

## Decision

We will implement in-memory storage using:

- **Storage Structure**: Python dictionary with UUID keys mapping to todo objects
- **Identifier Generation**: UUID4 for unique, random identifiers
- **Timestamp Management**: Python's datetime module with timezone-aware timestamps
- **Data Model**: Todo entity with id (UUID), title (string), description (optional string), completed (boolean), created_at (datetime), updated_at (datetime)

## Alternatives Considered

- **Storage Structure**: Alternatives included list-based storage, custom class - Dictionary with UUID keys chosen for efficient O(1) lookups and standard practice
- **Identifier Generation**: Alternatives included sequential IDs, custom ID generation - UUID4 chosen for guaranteed uniqueness and standard practice
- **Timestamp Management**: Alternatives included Unix timestamps, third-party libraries like Arrow - Standard datetime chosen for simplicity and built-in support

## Consequences

**Positive:**
- Dictionary provides O(1) average time complexity for lookups, insertions, and deletions
- UUID4 ensures globally unique identifiers without coordination
- Standard datetime module provides built-in timezone support and rich date operations
- Simple in-memory structure supports all required operations efficiently
- Clear data model with validation rules ensures data integrity

**Negative:**
- In-memory storage means data is lost when application terminates
- UUIDs are less human-readable than sequential IDs
- Memory usage grows linearly with number of todos

## References

- plan.md: Technical Context section on in-memory storage
- data-model.md: Complete data model specification
- research.md: Decision sections on storage implementation and UUID generation