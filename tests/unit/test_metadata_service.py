from pathlib import Path

from apk_analyzer.application.metadata_service import MetadataService
from apk_analyzer.domain.models import ApkMetadata


class FakeParser:
    def parse_apk(self, path: Path) -> ApkMetadata:
        return ApkMetadata(
            package_name="com.example.app",
            version_name="1.2.3",
            version_code=123,
            min_sdk_version=21,
            target_sdk_version=30,
        )


def test_metadata_service_extract(tmp_path: Path):
    sample = tmp_path / "sample.apk"
    sample.write_text("dummy")
    service = MetadataService(FakeParser())
    meta = service.extract(sample)
    assert meta.package_name == "com.example.app"
    assert meta.version_code == 123
