# Data Model: APK Metadata

Entity: `ApkMetadata`
- `package_name`: str
- `version_name`: Optional[str]
- `version_code`: Optional[int]
- `min_sdk_version`: Optional[int]
- `target_sdk_version`: Optional[int]

Representation
- Implement as an immutable `dataclass(frozen=True)` named `ApkMetadata` in `apk_analyzer/domain/models.py`.
- JSON serialization: provide a `to_dict()` method that returns keys: `packageName`, `versionName`, `versionCode`, `minSdk`, `targetSdk`. `None` values should be serialized as `null`.

Validation rules
- `package_name`: non-empty string; if missing in manifest treat as error at parsing stage.
- `version_code`: if present, coerce to int; if unparsable, keep `None` and surface a parse warning.
- SDK versions: parse as ints when present; otherwise `None`.

Relationships
- `ApkMetadata` is a leaf/domain object used by `MetadataService` (application layer) and produced by `ApkParser` (infrastructure).

State transitions
- No complex state machine; creation occurs after successful parsing. Errors raise domain exceptions defined in `domain/errors.py`.

Files to create
- `apk_analyzer/domain/models.py` — `ApkMetadata` dataclass
- `apk_analyzer/domain/errors.py` — domain exceptions (`ApkParsingError`, `ApkFileNotFound`, etc.)
