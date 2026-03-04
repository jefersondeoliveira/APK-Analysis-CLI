# Research: APK Metadata CLI (Phase 0)

Decision: Language and primary libraries
- Decision: Use Python 3.11 as the implementation language.
- Rationale: Rapid development, strong ecosystem for APK parsing (`androguard`), cross-platform runtime availability, and test tooling (`pytest`, `mypy`, `ruff`).
- Alternatives considered: Go (fast, single binary) — rejected for slower iteration and smaller ecosystem for APK parsing; Node.js — viable but fewer mature APK parsers; Java/Kotlin with `aapt` — heavyweight and adds JNI/tooling complexity.

Decision: APK parsing library
- Decision: Use `androguard` to parse APKs and extract AndroidManifest values.
- Rationale: `androguard` provides high-level APIs to parse the manifest and type-safe access to attributes. It handles binary AndroidManifest parsing and common edge cases.
- Alternatives considered: `aapt`/`aapt2` (requires external binary), `apktool` (jar-based, heavier), manual ZIP + axml parsing (fragile). These alternatives increase external dependency complexity or implementation risk.

Decision: CLI framework
- Decision: Use `typer` for the CLI entrypoint.
- Rationale: Typer is built on Click, is type-friendly, produces good help/usage output, and supports argument validation.

Decision: Output serialization
- Decision: Use domain model -> `pydantic` or builtin `dataclasses.asdict` for JSON output. `pydantic` gives validation and serialization features; mark as optional dependency.

Testing and QA
- Unit tests: Mock `ApkParser` interface to unit-test application logic (`metadata_service`).
- Integration tests: Include one or two small, checked-in sample APKs (or download in CI via curated test data) and place them under `tests/integration/samples` (if repo size policy permits). Integration tests marked with `pytest` markers.

Security & Constraints
- Treat APKs as untrusted input, do not execute any code from the APK. Limit resource usage and validate manifest fields.

Dependency rationale summary
- `androguard`: robust binary manifest parsing without requiring external binaries.
- `typer`: ergonomic CLI creation and help text.
- `pytest`, `mypy`, `ruff`, `coverage`: standard Python tooling that supports requirements in the constitution.

Next steps after research (Phase 1): create data-model.md, CLI contracts (JSON schema), quickstart, and implement a small prototype.
