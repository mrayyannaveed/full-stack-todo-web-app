# Research: In-Memory Todo CLI Application

## Decision: Python Version and Environment
**Rationale**: Using Python 3.13+ as specified in the requirements. Using UV as the package manager for fast dependency resolution and virtual environment management.
**Alternatives considered**: Standard pip/virtualenv, Poetry, Pipenv - UV was chosen for its speed and simplicity.

## Decision: CLI Framework
**Rationale**: Using Click for the CLI framework as it's more feature-rich and user-friendly than argparse. Provides better help generation, argument validation, and command organization.
**Alternatives considered**: argparse (built-in but less feature-rich), typer (built on Click with type hints), fire (Google's library) - Click chosen for its maturity and features.

## Decision: FastAPI as Internal Service Layer
**Rationale**: Using FastAPI as specified in requirements, even though it's typically for web APIs. In this case, it will be used as an internal service layer that the CLI interacts with directly in-process, not exposed as an HTTP server.
**Alternatives considered**: Pure function-based service layer, Flask - FastAPI chosen for its async support and built-in validation.

## Decision: In-Memory Storage Implementation
**Rationale**: Using a simple Python dictionary/UUID mapping for in-memory storage as specified. This will be managed in a dedicated state module.
**Alternatives considered**: List-based storage, custom class - Dictionary with UUID keys chosen for efficient lookups and standard practice.

## Decision: UUID Generation
**Rationale**: Using Python's built-in `uuid` module to generate unique identifiers for todos, specifically UUID4 for random generation.
**Alternatives considered**: Sequential IDs, custom ID generation - UUID4 chosen for uniqueness and standard practice.

## Decision: Datetime Handling
**Rationale**: Using Python's `datetime` module with timezone-aware timestamps for created_at and updated_at fields.
**Alternatives considered**: Unix timestamps, third-party libraries like Arrow - Standard datetime chosen for simplicity and built-in support.

## Decision: Testing Framework
**Rationale**: Using pytest for testing as it's the most popular and feature-rich Python testing framework, with good support for fixtures and parameterized tests.
**Alternatives considered**: unittest (built-in but more verbose), nose (deprecated) - pytest chosen for its features and community support.