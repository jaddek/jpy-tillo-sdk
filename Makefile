.PHONY: uvr-mype, uvr-black-check, uvr-black-format, uvr-coverage, uvr-tests, uvrr, uvrr-check, uvrr-format

all: help

uvrr: uvrr-check uvrr-format uvr-black-format uvr-tests

uvr-tests:
	uv run pytest .

uvrr-check:
	uv run ruff check . --fix

uvrr-format:
	uv run ruff format

uvr-coverage:
	uv run coverage run -m pytest & uv run coverage run report

uvr-black-check:
	uv run black . --check --diff

uvr-black-format:
	uv run black . --diff

uvr-mypy:
	uv run mypy src/ --strict --ignore-missing-imports --check-untyped-defs

help:
	@echo "Run UV:"
	@echo "  uvrr-check                - uv run ruff check - Ruff Check"
	@echo "  uvrr-format               - uv run ruff format - Ruff Format"
	@echo "  uvr-tests                - uv run pytest - Tests"
	@echo "Run MyPy:"
	@echo "  uvrb-mypy                - uv run mype src/"
	@echo "Run Black:"
	@echo "  uvrb-check                - uv run black . --diff"
	@echo "  uvrb-format               - uv run black . --check --diff"
	@echo "  help                      - Show this message"
