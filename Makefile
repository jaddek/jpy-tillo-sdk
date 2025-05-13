.PHONY: uvr-floats-check-floats, uvr-floats-transfer

all: help

tests:
    uv run pytests

uvr-floats-check-floats:
	 uv run examples/floats/check_floats.py

uvr-floats-request-transfer:
	uv run examples/floats/request_payment_transfer.py

help:
	@echo "Available requests:"
	@echo "  uvr-floats-check-floats   - Run examples/floats/check_floats.py (Tillo V2 GET - api/v2/float/check-floats)"
	@echo "  uvr-floats-transfer       - Run examples/floats/request_payment_transfer.py (Tillo V2 POST - api/v2/float/request-payment-transfer)"
	@echo "  help                      - Show this message"