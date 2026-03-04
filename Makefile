PY=python
PIP=$(PY) -m pip
VENV_DIR=.venv

.PHONY: venv install install-dev test lint typecheck run

venv:
	$(PY) -m venv $(VENV_DIR)

install: venv
	$(PIP) install -r requirements.txt

install-dev: venv
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-dev.txt

test:
	$(VENV_DIR)/Scripts/pytest -q

lint:
	$(VENV_DIR)/Scripts/ruff check .

typecheck:
	$(VENV_DIR)/Scripts/mypy apk_analyzer

run:
	$(PY) -m apk_analyzer.cli.main
