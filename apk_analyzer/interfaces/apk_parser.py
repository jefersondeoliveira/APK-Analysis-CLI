from __future__ import annotations

from pathlib import Path
from typing import Protocol

from apk_analyzer.domain.models import ApkMetadata


class ApkParser(Protocol):
    def parse_apk(self, path: Path) -> ApkMetadata:
        ...
