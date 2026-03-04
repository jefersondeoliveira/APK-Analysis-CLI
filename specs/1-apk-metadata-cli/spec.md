# APK Metadata CLI

**Summary**

Build a small CLI tool that analyzes an Android APK file and extracts basic metadata: package name, version name, version code, minimum SDK, and target SDK. The tool accepts a file path as input and prints results in a clear human-readable format, with an optional `--json` flag to output the same information as JSON. It must handle invalid files gracefully and return appropriate exit codes.

**Actors**

- User: runs the CLI locally to inspect APK files
- CI / automation: may call the CLI to extract metadata as part of a pipeline

**Goals**

- Quickly obtain basic APK metadata from a file path
- Provide both human-readable and machine-readable (JSON) output
- Fail gracefully for invalid input with clear messages and exit codes

**User Scenarios & Testing**

1. Analyze a valid APK
   - Given a valid APK file path, when the user runs `apk-analyzer path/to/app.apk`, then the tool prints package name, version name, version code, minSdk, and targetSdk in a readable table and exits with code `0`.

2. JSON output
   - Given a valid APK, when the user runs `apk-analyzer --json path/to/app.apk`, then the tool prints a single JSON object containing the same fields and exits with code `0`.

3. Missing file argument
   - When the user runs `apk-analyzer` without a file argument, the tool prints usage info and exits with code `2`.

4. File not found or unreadable
   - When the provided path does not exist or is unreadable, the tool prints an error and exits with code `3`.

5. Invalid or corrupt APK
   - When the provided file is not a valid APK, the tool prints a clear error and exits with code `4`.

6. Non-APK but readable file
   - When a readable file that is not an APK is supplied, the tool behaves like (5) and exits with code `4`.

**Functional Requirements**

1. CLI entrypoint
   - The tool exposes a CLI command `apk-analyzer <file>` with an optional `--json` (or `-j`) flag.
   - Behavior must be deterministic for the same input file.

2. Input validation
   - If no file path is provided, print usage/help and exit `2`.
   - If the file does not exist or cannot be read, print an error and exit `3`.

3. APK parsing
   - For a valid APK, extract and return these fields: `packageName`, `versionName`, `versionCode`, `minSdk`, `targetSdk`.
   - If any field is missing in the APK manifest, explicitly return `null` for that field in JSON or print `Unknown` in human-readable output.

4. Output formats
   - Human-readable: print labeled lines or a small table with each field on its own line.
   - JSON: when `--json` is provided, print a single JSON object with keys exactly: `packageName`, `versionName`, `versionCode`, `minSdk`, `targetSdk`.

5. Exit codes (machine-friendly)
   - `0` — success and metadata printed
   - `2` — missing file argument / usage error
   - `3` — file not found / cannot read
   - `4` — invalid/corrupt/non-APK file
   - `1` — general/unknown error

6. Error messages
   - Error messages must be concise and printed to stderr.

7. Cross-platform
   - The CLI must work on Windows, macOS, and Linux (no platform-specific behavior in outputs).

**Success Criteria**

- Users can run the CLI on a valid APK and read all required metadata in under 5 seconds for typical APKs (subjective; testable by measuring runtime).
- `--json` output is valid JSON and contains all required keys. 100% of valid APK runs return a JSON object with the keys present (values may be `null`).
- The CLI returns documented exit codes for the scenarios described above.
- Error messages are clear and let users correct input issues without inspecting internals.

**Key Entities**

- APK file: input artifact to analyze
- Manifest metadata: package name, version name, version code, minSdk, targetSdk
- CLI flags: `--json` / `-j`, `--help` / `-h`

**Assumptions**

- The tool will read the APK's AndroidManifest (APK is a zip archive) and parse the manifest to extract values.
- If multiple manifests or flavors exist in a file, the primary manifest is used (standard single-manifest APKs assumed).
- Default exit codes above are acceptable unless the project requires a different mapping.

**Acceptance Criteria**

- Given a valid APK path, the CLI prints all five fields and exits `0`.
- Given `--json`, the CLI emits a single, valid JSON object with the five keys and exits `0`.
- For missing argument, file-not-found, or invalid APK the CLI prints a helpful error and returns the documented exit code.

**Examples**

Human-readable:

    $ apk-analyzer path/to/app.apk
    Package: com.example.app
    Version name: 1.2.3
    Version code: 123
    Min SDK: 21
    Target SDK: 30

JSON:

    $ apk-analyzer --json path/to/app.apk
    {"packageName":"com.example.app","versionName":"1.2.3","versionCode":"123","minSdk":21,"targetSdk":30}

**Notes**

- Implementation details (language/tooling) are intentionally omitted from this spec. The focus is on expected behavior, inputs, outputs, error handling, and testable acceptance criteria.
