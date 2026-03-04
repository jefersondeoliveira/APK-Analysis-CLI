# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

[Extract from feature spec: primary requirement + technical approach from research]

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: [e.g., Python 3.11, Swift 5.9, Rust 1.75 or NEEDS CLARIFICATION]  
**Primary Dependencies**: [e.g., FastAPI, UIKit, LLVM or NEEDS CLARIFICATION]  
**Storage**: [if applicable, e.g., PostgreSQL, CoreData, files or N/A]  
**Testing**: [e.g., pytest, XCTest, cargo test or NEEDS CLARIFICATION]  
**Target Platform**: [e.g., Linux server, iOS 15+, WASM or NEEDS CLARIFICATION]
**Project Type**: [e.g., library/cli/web-service/mobile-app/compiler/desktop-app or NEEDS CLARIFICATION]  
**Performance Goals**: [domain-specific, e.g., 1000 req/s, 10k lines/sec, 60 fps or NEEDS CLARIFICATION]  
**Constraints**: [domain-specific, e.g., <200ms p95, <100MB memory, offline-capable or NEEDS CLARIFICATION]  
**Scale/Scope**: [domain-specific, e.g., 10k users, 1M LOC, 50 screens or NEEDS CLARIFICATION]

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*
## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify the plan complies with the project's constitution (.specify/memory/constitution.md). At minimum confirm:

- Clean Architecture: domain, application, and infrastructure separation is preserved.
- Business rules are independent of CLI/framework code.
- Parsing logic is behind interfaces and injectable into the domain.
- Testability: unit tests planned for business logic; integration tests separated and labeled.
- Outputs: human-readable and JSON formats supported by planned commands.
- Cross-platform considerations and OS abstractions are documented.
- Dependency rationale: external dependency list includes short justifications.

If any gate is violated, document the violation and include a justification in the "Complexity Tracking" section.

## Project Structure

# Implementation Plan: APK Metadata CLI

**Branch**: `1-apk-metadata-cli` | **Date**: 2026-03-04 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/1-apk-metadata-cli/spec.md`

## Summary

Create a small, cross-platform Python CLI that extracts basic APK metadata (package name, version name, version code, minSdk, targetSdk) from an APK file and prints it in human-readable or JSON form. Implementation follows Clean Architecture: domain models and application logic are independent from infrastructure (androguard) and the CLI layer (Typer).

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: `androguard` (APK parsing), `typer` (CLI), `pydantic` (optional validation/serialization), `pytest` (testing), `ruff` (linting), `mypy` (static types), `coverage.py` (coverage)
**Storage**: N/A (reads APK file, no persistent storage)
**Testing**: `pytest` for unit and integration tests; integration tests marked and isolated under `tests/integration`.
**Target Platform**: Cross-platform (Windows, macOS, Linux)
**Project Type**: CLI tool (library-style layout to enable reuse)
**Performance Goals**: Typical APKs (<200MB) should parse within 5 seconds on modern developer machines.
**Constraints**: Avoid loading entire APK into memory unnecessarily; treat APKs as untrusted input and validate manifest content.
**Scale/Scope**: Single-feature CLI focused on metadata extraction; designed to be extended by future analysis modules.

## Constitution Check

The plan is evaluated against `.specify/memory/constitution.md` and must satisfy the following gates:

- Clean Architecture: design keeps domain, application, and infrastructure separate.  (PASS)
- Business rules are independent of CLI/framework code (domain models + services have no Typer/androguard imports).  (PASS)
- Parsing logic behind interfaces: `interfaces/apk_parser.py` will define an `ApkParser` protocol implemented in `infrastructure/androguard_parser.py`.  (PASS)
- Testability: unit tests planned for domain and application layers; integration tests will exercise `infrastructure` with a small sample APK under `tests/integration`.  (PASS)
- Outputs: human-readable and JSON formats supported by CLI via `--json`.  (PASS)
- Cross-platform considerations: avoid platform-specific dependencies; file path handling via `pathlib`.  (PASS)
- Dependency rationale: `androguard` chosen for robust APK parsing; `typer` for ergonomic CLI. Rationale recorded in `research.md`.  (PASS)

No constitution violations detected that require exceptions. See `research.md` for dependency rationale and alternatives considered.

## Project Structure

Documentation (this feature):

```text
specs/1-apk-metadata-cli/
├── plan.md              # This file (generated)
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output (not created here)
```

Source layout (repository root):

```text
apk_analyzer/
├── domain/
│   ├── models.py       # `ApkMetadata` dataclass
+│   └── errors.py       # domain-specific exceptions
├── interfaces/
│   └── apk_parser.py   # `ApkParser` protocol
├── infrastructure/
│   └── androguard_parser.py
├── application/
│   └── metadata_service.py
├── cli/
│   └── main.py         # Typer CLI
tests/
├── unit/
└── integration/
```

**Structure Decision**: use single Python project with a clear domain/application/infrastructure/cli separation to satisfy the constitution and enable testability and reuse.

## Complexity Tracking

No constitution gates violated; no complexity exceptions required.
