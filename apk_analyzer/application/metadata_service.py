from __future__ import annotations

from pathlib import Path
from typing import Optional

from apk_analyzer.domain.errors import (
    ApkFileNotFoundError,
    ApkInvalidError,
    ApkParsingError,
)
from apk_analyzer.interfaces.apk_parser import ApkParser


class MetadataService:
    def __init__(self, parser: ApkParser):
        self._parser = parser

    def extract(self, path: Path):
        if path is None:
            raise ApkParsingError("No path provided")
        if not path.exists():
            raise ApkFileNotFoundError(f"File not found: {path}")
        if not path.is_file():
            raise ApkFileNotFoundError(f"Not a file: {path}")
        try:
            return self._parser.parse_apk(path)
        except ApkInvalidError:
            raise
        except Exception as exc:
            raise ApkParsingError(str(exc)) from exc
