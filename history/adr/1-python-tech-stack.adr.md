# ADR-1: Python Technology Stack for In-Memory CLI Todo Application

**Status**: Accepted
**Date**: 2025-12-29

## Context

The application requires a CLI-based Todo application that stores data in memory. We need to select the appropriate technology stack including programming language, CLI framework, service layer, and package management.

## Decision

We will use the following technology stack:

- **Language**: Python 3.13+
- **Package Manager**: UV for fast dependency resolution and virtual environment management
- **CLI Framework**: Click for command-line interface
- **Internal Service Layer**: FastAPI (used internally, not as HTTP server)
- **Testing Framework**: pytest

## Alternatives Considered

- **Package Manager**: Alternatives included standard pip/virtualenv, Poetry, Pipenv - UV was chosen for its speed and simplicity
- **CLI Framework**: Alternatives included argparse (built-in but less feature-rich), typer (built on Click with type hints), fire (Google's library) - Click chosen for its maturity and features
- **Service Layer**: Alternatives included pure function-based service layer, Flask - FastAPI chosen for its async support and built-in validation
- **Testing Framework**: Alternatives included unittest (built-in but more verbose), nose (deprecated) - pytest chosen for its features and community support

## Consequences

**Positive:**
- UV provides fast dependency resolution and virtual environment management
- Click provides rich CLI features including help generation, argument validation, and command organization
- FastAPI provides async support and built-in validation capabilities even when used as an internal service layer
- pytest offers extensive testing features with good support for fixtures and parameterized tests

**Negative:**
- FastAPI might be overkill for an internal service layer (though it provides good validation)
- UV is newer than pip and may have ecosystem compatibility issues (though generally resolved)

## References

- plan.md: Technical Context section
- research.md: Decision sections on Python version, CLI framework, FastAPI usage