from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ApkMetadata:
    package_name: str
    version_name: Optional[str]
    version_code: Optional[int]
    min_sdk_version: Optional[int]
    target_sdk_version: Optional[int]

    def to_dict(self) -> dict:
        return {
            "packageName": self.package_name,
            "versionName": self.version_name,
            "versionCode": self.version_code,
            "minSdk": self.min_sdk_version,
            "targetSdk": self.target_sdk_version,
        }
