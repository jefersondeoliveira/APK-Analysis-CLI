# Contracts: CLI Output JSON Schema

This schema defines the JSON object emitted by the CLI when `--json` is used.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "packageName": { "type": "string" },
    "versionName": { "type": ["string", "null"] },
    "versionCode": { "type": ["integer", "string", "null"] },
    "minSdk": { "type": ["integer", "null"] },
    "targetSdk": { "type": ["integer", "null"] }
  },
  "required": ["packageName", "versionName", "versionCode", "minSdk", "targetSdk"],
  "additionalProperties": false
}
```

Notes:
- `versionCode` is allowed as string to be tolerant with some manifests that encode numeric codes as strings; the application should prefer integer conversion when possible.
