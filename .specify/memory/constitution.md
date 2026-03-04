<!--
Sync Impact Report (2026-03-03)
- Version change: 1.0.0 → 1.1.0
- Modified principles: expanded architecture, testability, performance, and documentation sections
- Added sections: Parsing abstraction, Performance constraints, Developer experience requirements
- Removed sections: None
- Templates requiring updates: .specify/templates/plan-template.md (✅), .specify/templates/spec-template.md (✅), .specify/templates/tasks-template.md (✅)
- Follow-up TODOs: TODO(RATIFICATION_DATE): original ratification date required
-->

# APK Analyzer CLI Constitution

## 1. Architectural Principles

1. The project MUST follow Clean Architecture principles.
2. Business rules MUST be independent of CLI frameworks and external tools.
3. The domain layer MUST NOT depend on infrastructure or presentation layers.
4. All parsing logic MUST be abstracted behind clear interfaces and injected into the domain layer.

Rationale: Enforces separation of concerns, enables testing, and allows swapping infrastructure implementations.

## 2. Modularity & Extensibility

1. The system MUST be modular and allow future analysis modules (e.g., security scoring, malware heuristics, diff comparison).
2. Each analysis feature MUST be implemented as an independent component with a clear interface.
3. Adding new output formats MUST NOT require modifying domain logic.

Rationale: Keeps the codebase adaptable and reduces risk when evolving features.

## 3. Testability

1. All business logic MUST be unit-testable.
2. External dependencies (e.g., `aapt2`, filesystem access) MUST be abstracted and injectable.
3. The project SHOULD aim for a minimum of 80% unit test coverage; coverage targets are reviewed per module.
4. Tests MUST NOT depend on real APK files unless explicitly marked as integration tests.

Rationale: High test coverage and isolation reduce regressions and increase confidence.

## 4. CLI Design Principles

1. The CLI MUST be intuitive and follow standard Unix conventions where applicable.
2. The tool MUST support both human-readable output and JSON structured output via flags.
3. Errors MUST be explicit and actionable; exit codes MUST follow standard CLI conventions.

Rationale: Clear CLI behavior improves UX and scriptability.

## 5. Performance & Constraints

1. The tool SHOULD process typical APK files (<200MB) in under 5 seconds on a modern developer machine; this is a target, not a hard guarantee.
2. Memory usage MUST remain predictable and the system MUST avoid loading entire APK contents into memory unnecessarily.

Rationale: Reasonable performance expectations for local developer use and CI.

## 6. Cross-Platform Compatibility

1. The tool MUST run on Windows, macOS, and Linux.
2. OS-specific logic MUST be isolated behind abstractions.
3. No platform-locked dependencies are allowed without an abstraction and documented justification.

Rationale: Ensures wide usability and simplified maintenance.

## 7. Dependency Management

1. Dependencies MUST be minimal and justified; each dependency entry in manifests must include a short rationale.
2. Security and maintenance status of dependencies MUST be considered during review.
3. External tools (e.g., `aapt2`) MUST be configurable (path/env) and not hardcoded.

Rationale: Limits attack surface and improves long-term sustainability.

## 8. Documentation & Developer Experience

1. The project MUST contain a clear and professional `README.md` with purpose, installation, usage, outputs, and roadmap.
2. Code SHOULD be self-documenting; architectural decisions MUST be recorded when significant changes occur.

Rationale: Reduces onboarding friction and preserves institutional knowledge.

## 9. Versioning & Releases

1. The project MUST follow Semantic Versioning.
2. Breaking changes REQUIRE a major version bump and an upgrade migration note.

Rationale: Predictable versioning for users and integrators.

## 10. Security & Integrity

1. Treat APK files as untrusted input; validate and fail safely on malformed content.
2. No external network calls SHOULD be made without explicit user request or configuration.

Rationale: Minimize security risks and accidental data exfiltration.

## Governance

- This constitution supersedes informal practices; amendments REQUIRE a documented rationale, review, and migration guidance.
- Constitution versioning follows SemVer: MAJOR for principle changes, MINOR for additions/expansions, PATCH for wording/typo fixes.

**Version**: 1.1.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2026-03-03
