# Contracts: CLI Output JSON Schema

This schema defines the JSON object emitted by the CLI when `--json` is used.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "packageName": { "type": "string" },
    "versionName": { "type": ["string", "null"] },
    "versionCode": { "type": ["integer", "null"] },
    "minSdk": { "type": ["integer", "null"] },
    "targetSdk": { "type": ["integer", "null"] }
  },
  "required": ["packageName", "versionName", "versionCode", "minSdk", "targetSdk"],
  "additionalProperties": false
}
```

Notes:
Notes:
- `versionCode` MUST be an integer or `null` in the CLI JSON output. Implementations may accept string-encoded numeric values when parsing, but they should convert them to integers for the emitted JSON when possible.
