---
description: "Generated task list for APK Metadata CLI"
---

# Tasks: APK Metadata CLI

**Input**: Design documents from `/specs/1-apk-metadata-cli/` (spec.md, plan.md, data-model.md, contracts)

## Phase 1: Setup (Shared Infrastructure)

Purpose: Project initialization and minimal developer setup.

- [ ] T001 [P] Create package layout and module files: create `apk_analyzer/` with subpackages `domain/`, `interfaces/`, `infrastructure/`, `application/`, `cli/` and `tests/` directories. Files: `apk_analyzer/__init__.py`, `apk_analyzer/domain/__init__.py`, `apk_analyzer/interfaces/__init__.py`, `apk_analyzer/infrastructure/__init__.py`, `apk_analyzer/application/__init__.py`, `apk_analyzer/cli/__init__.py`, `tests/unit/__init__.py`, `tests/integration/__init__.py`
- [ ] T002 Create Python project definition and dependencies: `pyproject.toml` (include `typer`, `androguard` as runtime deps and `pytest`, `ruff`, `mypy`, `coverage` as dev deps)
- [ ] T003 Create README and basic usage docs: `README.md` and reference `specs/1-apk-metadata-cli/quickstart.md`
- [ ] T004 [P] Add tooling configs: `.gitignore`, `pyproject.toml` tool sections or `ruff.toml`, `mypy.ini`, `pytest.ini`
- [ ] T005 [P] Add placeholder sample directory for integration tests: `tests/integration/samples/` (add `.gitkeep` or note for real sample APK)

---

## Phase 2: Foundational (Blocking Prerequisites)

Purpose: Implement domain + interfaces + application skeleton that all stories depend on.

- [ ] T006 Create domain model `ApkMetadata` in `apk_analyzer/domain/models.py` (immutable dataclass with `to_dict()`)
- [ ] T007 Create domain error classes in `apk_analyzer/domain/errors.py` (`ApkParsingError`, `ApkFileNotFoundError`, `ApkInvalidError`)
- [ ] T008 Define `ApkParser` protocol in `apk_analyzer/interfaces/apk_parser.py` (methods: `parse_apk(path: Path) -> ApkMetadata`)
- [ ] T009 Implement `MetadataService` in `apk_analyzer/application/metadata_service.py` (accepts an `ApkParser`, orchestrates parsing and error mapping)
- [ ] T010 Create infrastructure parser using androguard in `apk_analyzer/infrastructure/androguard_parser.py` (implement `ApkParser` protocol; initial version may raise `NotImplementedError` for missing pieces)
- [ ] T011 [P] Create CLI entrypoint skeleton in `apk_analyzer/cli/main.py` (Typer app, basic argument parsing)
- [ ] T012 [P] Add unit test scaffold for `MetadataService` using a mocked `ApkParser`: `tests/unit/test_metadata_service.py`
- [ ] T013 [ ] T-CHECK Foundation: Verify domain is independent of infrastructure and CLI, tests scaffold run (files: `apk_analyzer/domain/*.py`, `apk_analyzer/interfaces/*.py`, `apk_analyzer/application/*.py`, `tests/unit/test_metadata_service.py`)

---

## Phase 3: User Story 1 - Analyze APK (Priority: P1) 🎯 MVP

Goal: Given a valid APK path, extract `packageName`, `versionName`, `versionCode`, `minSdk`, `targetSdk` and print human-readable output. Exit `0` on success.

Independent Test: Run `python -m apk_analyzer.cli.main path/to/sample.apk` and confirm stdout contains labeled lines for each field and process exits with code `0`.

- [ ] T014 [P] [US1] Implement human-readable output formatting in `apk_analyzer/cli/main.py` (use `MetadataService` to obtain `ApkMetadata` and print labeled lines)
- [ ] T015 [US1] Integrate `MetadataService` with CLI wiring in `apk_analyzer/cli/main.py` (create service instance, wire `androguard_parser` by default)
- [ ] T016 [P] [US1] Add integration test `tests/integration/test_human_readable_output.py` (uses sample APK or a mocked runner; verifies stdout and exit code)
- [ ] T017 [US1] Add sample valid APK placeholder at `tests/integration/samples/sample_valid.apk` or document how to provide one during CI

---

## Phase 4: User Story 2 - JSON Output (Priority: P1)

Goal: Provide `--json` (`-j`) flag to emit a single JSON object with keys `packageName`, `versionName`, `versionCode`, `minSdk`, `targetSdk`.

Independent Test: Run `python -m apk_analyzer.cli.main --json path/to/sample.apk` and confirm output is valid JSON matching contract `specs/1-apk-metadata-cli/contracts/cli-output-schema.md` and exit `0`.

- [ ] T018 [P] [US2] Implement `--json` flag parsing in `apk_analyzer/cli/main.py` and output JSON using `ApkMetadata.to_dict()` (or `pydantic` if used)
- [ ] T019 [US2] Implement `to_dict()` / JSON serialization in `apk_analyzer/domain/models.py` (ensure `None` -> `null` and keys match contract)
- [ ] T020 [P] [US2] Add integration test `tests/integration/test_json_output.py` to validate JSON structure against the contract in `specs/1-apk-metadata-cli/contracts/cli-output-schema.md`

---

## Phase 5: User Story 3 - CLI Usage & Missing Argument (Priority: P2)

Goal: If the user omits the file argument, print usage/help and exit with code `2`.

Independent Test: Run `python -m apk_analyzer.cli.main` with no args and assert exit code `2` and usage text on stderr.

- [ ] T021 [US3] Enforce required positional argument in `apk_analyzer/cli/main.py` and map missing argument to exit code `2`
- [ ] T022 [P] [US3] Add unit test `tests/unit/test_cli_missing_argument.py` validating exit code and stderr message

---

## Phase 6: User Story 4 - File Not Found / Unreadable (Priority: P2)

Goal: If the file path doesn't exist or is unreadable, print an error to stderr and exit `3`.

Independent Test: Run CLI with a non-existent path and assert exit code `3` and a concise error message on stderr.

- [ ] T023 [US4] Implement file existence/readability checks in `apk_analyzer/application/metadata_service.py` or `cli/main.py`, map to `ApkFileNotFoundError`
- [ ] T024 [P] [US4] Add unit test `tests/unit/test_file_not_found.py`

---

## Phase 7: User Story 5 - Invalid / Corrupt APK (Priority: P2)

Goal: If the provided file is not a valid APK or parsing fails, print concise error and exit `4`.

Independent Test: Supply a known non-APK file (or corrupt APK) and assert exit code `4` and clear stderr message.

- [ ] T025 [US5] Map infrastructure parsing errors to `ApkInvalidError` in `apk_analyzer/application/metadata_service.py`
- [ ] T026 [P] [US5] Add unit test `tests/unit/test_invalid_apk.py` and integration test `tests/integration/test_invalid_apk.py`

---

## Phase 8: User Story 6 - Non-APK Readable File (Priority: P2)

Goal: If a readable file that isn't an APK is given, behave like invalid APK (exit `4`).

Independent Test: Provide a plain-text file, verify exit `4` and stderr message.

- [ ] T027 [US6] Ensure `apk_analyzer/infrastructure/androguard_parser.py` raises `ApkInvalidError` for non-APK files
- [ ] T028 [P] [US6] Add unit test `tests/unit/test_non_apk_file.py`

---

## Phase 9: Polish & Cross-Cutting Concerns

- [ ] T029 [P] Add CI workflow `/.github/workflows/ci.yml` to run lint, type-check, and tests
- [ ] T030 [P] Add console entrypoint packaging in `pyproject.toml` (`[project.scripts]` or `tool.poetry.scripts`) so users can install `apk-analyzer` CLI
- [ ] T031 [P] Update `README.md` and `specs/1-apk-metadata-cli/quickstart.md` with installation and usage examples
- [ ] T032 [ ] T-CHECK Final: Verify constitution compliance (domain isolation, tests present, contracts implemented) before merge (files: see foundation T-CHECK and new artifacts)

---

## Dependencies & Execution Order

- **Setup** (Phase 1): T001-T005 — can run immediately and in parallel where marked [P]
- **Foundational** (Phase 2): T006-T013 — MUST complete before user story implementation
- **User Stories** (Phases 3-8): follow priority order but can be worked in parallel after foundation completes
- **Polish** (Phase 9): T029-T032 — run after stories complete

## Parallel execution examples

- While Phase 2 foundation is being completed, the team can implement `apk_analyzer/cli/main.py` (T011) and tests scaffolding (T012) in parallel.
- After foundation: Developer A implements US1 (T014-T017), Developer B implements US2 (T018-T020), Developer C writes tests and CI (T023-T031).

## Implementation strategy

- MVP first: complete Phase 1 & 2, then implement US1 and US2 to deliver a working CLI (human + JSON) before polishing.

*** End Patch