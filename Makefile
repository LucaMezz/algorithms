VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
RUFF := $(VENV)/bin/ruff
MYPY := $(VENV)/bin/mypy
PYTEST := $(VENV)/bin/pytest
MKDOCS := $(VENV)/bin/mkdocs

.PHONY: help install install-bench install-docs test lint format typecheck check docs docs-serve clean

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Setup:"
	@echo "  install        Create .venv and install dev dependencies"
	@echo "  install-bench  Install benchmark dependencies into .venv"
	@echo "  install-docs   Install documentation dependencies into .venv"
	@echo ""
	@echo "Quality checks (also run automatically on git commit via Husky):"
	@echo "  format         Run ruff formatter"
	@echo "  lint           Run ruff linter"
	@echo "  typecheck      Run mypy type checker"
	@echo "  test           Run pytest"
	@echo "  check          Run all quality checks"
	@echo ""
	@echo "Docs:"
	@echo "  docs           Build documentation site"
	@echo "  docs-serve     Serve documentation with live reload"
	@echo ""
	@echo "Misc:"
	@echo "  clean          Remove .venv and build artifacts"

install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"
	npm install
	@echo ""
	@echo "Done. Pre-commit hooks are wired through Husky (.husky/pre-commit)."
	@echo "Run 'make check' to verify everything is working."

install-bench:
	$(PIP) install -e ".[bench]"

install-docs:
	$(PIP) install -e ".[docs]"

test:
	$(PYTEST)

lint:
	$(RUFF) check .

format:
	$(RUFF) format .

typecheck:
	$(MYPY) src

check: format lint typecheck test

docs:
	$(MKDOCS) build

docs-serve:
	$(MKDOCS) serve

clean:
	rm -rf $(VENV) build dist *.egg-info .pytest_cache .mypy_cache .ruff_cache
