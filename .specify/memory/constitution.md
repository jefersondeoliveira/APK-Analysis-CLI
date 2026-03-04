<!--
Sync Impact Report (2026-03-03)
- Version change: 0.0.0 → 1.0.0
- Modified principles: All template placeholders replaced
- Added sections: Platform Independence, Dependency Discipline
- Removed sections: None
- Templates requiring updates: plan-template.md (✅), spec-template.md (✅), tasks-template.md (✅)
- Follow-up TODOs: TODO(RATIFICATION_DATE): Original ratification date required
-->

# APK Analyzer CLI Constitution

## Core Principles

### I. Clean Architecture
The project MUST follow Clean Architecture principles. All layers must be clearly separated, with business logic isolated from frameworks and delivery mechanisms.
Rationale: Ensures maintainability, testability, and adaptability to future changes.

### II. Modular & Extensible CLI
The CLI MUST be modular and extensible. New commands and features must be addable without major refactoring.
Rationale: Supports growth and customizability for diverse user needs.

### III. Business Rule Independence
All business rules MUST be independent from the CLI framework. No business logic may depend on CLI-specific code or libraries.
Rationale: Enables reuse, easier testing, and framework migration.

### IV. Testability with Unit Tests
The tool MUST support testability with unit tests. All business logic and CLI modules must have independently runnable unit tests.
Rationale: Guarantees reliability and supports continuous integration.

### V. Output Formats
Output MUST support both human-readable and JSON formats. All CLI commands must provide both formats via flags or configuration.
Rationale: Facilitates automation, integration, and user accessibility.

### VI. Platform Independence
The project MUST be platform-independent (Windows, Mac, Linux). No code may assume a specific OS unless justified and documented.
Rationale: Maximizes user reach and reduces support burden.

### VII. Dependency Discipline
Dependencies MUST be minimal and well justified. Every external package must have a documented rationale for inclusion.
Rationale: Reduces attack surface, simplifies maintenance, and improves portability.

## Additional Constraints
- All code and documentation must be in English.
- Licensing must be OSI-approved and clearly stated in the repository.
- Security best practices must be followed for handling user input and file operations.

## Development Workflow
- All changes require code review by at least one other contributor.
- Unit tests must pass before merging.
- Feature branches must be named using the format `[###-feature-name]`.
- All new features require a specification and implementation plan.

## Governance
- This constitution supersedes all other project practices.
- Amendments require documentation, approval, and a migration plan.
- All PRs/reviews must verify compliance with these principles.
- Constitution versioning follows semantic versioning: MAJOR for principle changes, MINOR for additions, PATCH for clarifications.
- Use runtime guidance files for development best practices.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2026-03-03
