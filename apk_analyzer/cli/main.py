from __future__ import annotations

import json
import sys
from pathlib import Path

import typer

from apk_analyzer.application.metadata_service import MetadataService
from apk_analyzer.domain.errors import (
    ApkFileNotFoundError,
    ApkInvalidError,
    ApkParsingError,
)
from apk_analyzer.infrastructure.androguard_parser import AndroguardApkParser

app = typer.Typer(add_completion=False)


@app.command()
def main(path: Path | None = typer.Argument(None), json_out: bool = typer.Option(False, "--json", "-j")) -> None:
    if path is None:
        typer.echo("Error: missing APK file path", err=True)
        raise typer.Exit(code=2)
    try:
        parser = AndroguardApkParser()
    except RuntimeError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1)
    service = MetadataService(parser)
    try:
        meta = service.extract(path)
    except ApkFileNotFoundError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=3)
    except ApkInvalidError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=4)
    except ApkParsingError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=1)
    if json_out:
        typer.echo(json.dumps(meta.to_dict(), ensure_ascii=False))
    else:
        typer.echo(f"Package: {meta.package_name}")
        typer.echo(f"Version name: {meta.version_name if meta.version_name is not None else 'Unknown'}")
        typer.echo(f"Version code: {meta.version_code if meta.version_code is not None else 'Unknown'}")
        typer.echo(f"Min SDK: {meta.min_sdk_version if meta.min_sdk_version is not None else 'Unknown'}")
        typer.echo(f"Target SDK: {meta.target_sdk_version if meta.target_sdk_version is not None else 'Unknown'}")


if __name__ == "__main__":
    app()
