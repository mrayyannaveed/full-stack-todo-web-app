<!--
SYNC IMPACT REPORT
Version change: 0.1.0 → 1.0.0 (Initial full constitution implementation)
Modified principles:
- [PRINCIPLE_1_NAME] → I. Spec First
- [PRINCIPLE_2_NAME] → II. Progressive Enhancement
- [PRINCIPLE_3_NAME] → III. Deterministic Core, Probabilistic Edge
- [PRINCIPLE_4_NAME] → IV. Infrastructure as Capability
- [PRINCIPLE_5_NAME] → V. Observability Over Guessing
- [PRINCIPLE_6_NAME] → VI. Authoritative Source Mandate

Added sections: Domain Model and API Rules, Development Workflow and Quality Gates, Security & Compliance
Removed sections: None (replaced template placeholders)
Templates requiring updates: ✅ All checked and consistent
Follow-up TODOs: None
-->
# Full-Stack Todo Web App Constitution

## Core Principles

### I. Spec First
Every phase must begin with a spec before implementation; Specs are authoritative; Ambiguity in specs must be resolved before coding

### II. Progressive Enhancement
Each phase extends, never replaces, prior capabilities; Backward compatibility is preserved unless explicitly deprecated

### III. Deterministic Core, Probabilistic Edge
Core Todo logic must be deterministic; AI capabilities are layered at the edge (Phase III+); AI must never silently mutate persistent state

### IV. Infrastructure as Capability
Infrastructure choices are treated as product features; Local parity with cloud environments is mandatory

### V. Observability Over Guessing
Every deployed system must expose logs, metrics, and health signals

### VI. Authoritative Source Mandate
Agents MUST prioritize and use MCP tools and CLI commands for all information gathering and execution; NEVER assume a solution from internal knowledge; all methods require external verification

## Domain Model and API Rules
This section defines the canonical domain model and API contract rules for the Todo application.

Todo Entity:
- id (UUID)
- title (string)
- description (optional string)
- completed (boolean)
- created_at (timestamp)
- updated_at (timestamp)

API & Contract Rules:
- APIs are versioned
- Breaking changes require deprecation period
- OpenAPI specs are mandatory

## Development Workflow and Quality Gates
This section outlines the development workflow, quality requirements, and change management processes.

Development Guidelines:
- Clarify and plan first - keep business understanding separate from technical plan and carefully architect and implement
- Do not invent APIs, data, or contracts; ask targeted clarifiers if missing
- Never hardcode secrets or tokens; use `.env` and docs
- Prefer the smallest viable diff; do not refactor unrelated code
- Cite existing code with code references; propose new code in fenced blocks

Quality Gates:
- A phase is complete only if: Specs are written and reviewed, Tests map directly to specs, Deployment is reproducible
- All outputs strictly follow the user intent
- Prompt History Records (PHRs) are created automatically and accurately for every user prompt

Change Management:
- Constitution changes require a version bump
- All downstream specs must be reconciled
- This document overrides: Implementation preferences, Tool limitations, Time constraints
- If code and spec conflict, the spec wins

## Security & Compliance
This section defines security and compliance requirements.

- No secrets in source code
- Environment-based configuration only
- Principle of least privilege applies
- AI responses must be explainable
- Tool calls are logged
- Human-readable reasoning summaries are required
- AI failures must degrade gracefully

## Governance
This constitution acts as the highest-authority specification that governs all features, architecture decisions, AI usage, and deployment strategies. All implementation artifacts must conform to this constitution. Amendments to this constitution require documentation, approval, and migration plan. All PRs/reviews must verify compliance with these principles. Complexity must be justified with clear reasoning.

**Version**: 1.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28