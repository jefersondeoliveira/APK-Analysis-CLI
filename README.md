# APK Analyzer — Spec-Driven Development

This repository uses Spec-Driven Development. All features must originate from a written specification before implementation.

Key resources
- Constitution: `.specify/memory/constitution.md` — project principles, gates, and governance.
- Spec template: `.specify/templates/spec-template.md` — required sections for feature specs.
- Plan template: `.specify/templates/plan-template.md` — implementation plan and constitution gates.
- Tasks template: `.specify/templates/tasks-template.md` — task organization and constitution checks.

Workflow (summary)
1. Create a spec: add `specs/[###-short-name]/spec.md` using the spec template.
2. Run planning: generate `plan.md` from the spec and ensure the Constitution Check passes.
3. Implement: produce tasks from the plan, implement code in feature branch `[###-short-name]`.
4. Tests: write unit tests first (business logic), run CI checks, aim for ≥80% coverage on new modules.
5. Review: PR must reference the spec and include a short note on constitution compliance.

Developer notes
- All CLI outputs must support `--json` and human-readable modes.
- External tools (like `aapt2`) must be configurable via environment variables or CLI flags.
- Feature branches must follow the `[###-short-name]` convention.

Contributing
- See `.github/CONTRIBUTING.md` for PR guidelines (create if missing).

Contact
- Maintainership and ratification dates recorded in the constitution file.
# APK-Analysis-CLI
