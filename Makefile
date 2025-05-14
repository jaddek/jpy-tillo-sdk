.PHONY: uvr-mype, uvr-black-check, uvr-black-format, uvr-coverage, uvr-tests, uvrr, uvrr-check, uvrr-format, uvr-floats-check-floats, uvr-floats-transfer

all: help

uvrr: uvrr-check uvrr-format uvr-black-format uvr-tests

uvr-tests:
	uv run pytest .

uvrr-check:
	uv run ruff check . --fix

uvrr-format:
	uv run ruff format

uvr-floats-check-floats:
	 uv run examples/floats/check_floats.py

uvr-floats-request-transfer:
	uv run examples/floats/request_payment_transfer.py

uvr-coverage:
	uv run coverage run -m pytest & uv run coverage run report

uvr-black-check:
	uv run black . --check --diff

uvr-black-format:
	uv run black . --diff

uvr-mypy:
	uv run mypy src/

help:
	@echo "Run UV:"
	@echo "  uvrr-check                - uv run ruff check - Ruff Check"
	@echo "  uvrr-format               - uv run ruff format - Ruff Format"
	@echo "  uvrp-tests                - uv run pytest - Tests"
	@echo "Run MyPy:"
	@echo "  uvrb-mypy                - uv run mype src/"
	@echo "Run Black:"
	@echo "  uvrb-check                - uv run black . --diff"
	@echo "  uvrb-format               - uv run black . --check --diff"
	@echo "Available requests:"
	@echo "  uvr-floats-check-floats   - Run examples/floats/check_floats.py (Tillo V2 GET - api/v2/float/check-floats)"
	@echo "  uvr-floats-transfer       - Run examples/floats/request_payment_transfer.py (Tillo V2 POST - api/v2/float/request-payment-transfer)"
	@echo "  help                      - Show this message"