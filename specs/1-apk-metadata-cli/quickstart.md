# Quickstart: APK Metadata CLI (developer)

1. Create a Python virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows PowerShell
```

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
```

2. Install dependencies (example):

```bash
pip install androguard typer pydantic
pip install -D pytest ruff mypy coverage
```

3. Run the CLI (after implementation):

```bash
python -m apk_analyzer.cli.main path/to/app.apk
python -m apk_analyzer.cli.main --json path/to/app.apk
```

4. Run unit tests:

```bash
pytest -q
```

Notes:
- A `requirements.txt` or `pyproject.toml` will be added when implementation begins. CI should run linting and type checks prior to running tests.
