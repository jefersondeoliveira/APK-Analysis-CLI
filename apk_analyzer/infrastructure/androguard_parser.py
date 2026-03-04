from __future__ import annotations

from pathlib import Path
from typing import Optional

from apk_analyzer.domain.models import ApkMetadata
from apk_analyzer.domain.errors import ApkInvalidError


class AndroguardApkParser:
    def __init__(self):
        try:
            from androguard.core.bytecodes.apk import APK

            self._APK = APK
        except Exception as exc:
            raise RuntimeError(
                "androguard is required for the androguard parser. Install with 'pip install androguard'"
            ) from exc

    def parse_apk(self, path: Path) -> ApkMetadata:
        apk = self._APK(str(path))
        package = apk.get_package()
        version_name = apk.get_androidversion_name()
        version_code_raw = apk.get_androidversion_code()
        try:
            version_code = int(version_code_raw) if version_code_raw is not None else None
        except Exception:
            version_code = None
        min_sdk_raw = apk.get_min_sdk_version()
        target_sdk_raw = apk.get_target_sdk_version()
        try:
            min_sdk = int(min_sdk_raw) if min_sdk_raw is not None else None
        except Exception:
            min_sdk = None
        try:
            target_sdk = int(target_sdk_raw) if target_sdk_raw is not None else None
        except Exception:
            target_sdk = None
        if not package:
            raise ApkInvalidError("Missing package name in manifest")
        return ApkMetadata(
            package_name=package,
            version_name=version_name,
            version_code=version_code,
            min_sdk_version=min_sdk,
            target_sdk_version=target_sdk,
        )
