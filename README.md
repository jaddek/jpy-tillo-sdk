# Tillo SDK for Python

A Python library providing tools to access the Tillo API, with comprehensive support for both synchronous and asynchronous operations.

## Table of Contents

1. [Installation](#installation)
2. [Features](#features)
3. [Usage](#usage)
4. [Error Handling](#error-handling)
5. [Rate Limiting](#rate-limiting)
6. [API Documentation](#api-documentation)
7. [License](#license)

## Features

- Complete Tillo API support
- Both synchronous and asynchronous clients
- Comprehensive error handling
- Rate limiting support
- Services supported:
  - Float Management
  - Brand Management
  - Template Management
  - Digital Card Operations (coming soon)
  - Physical Card Operations (coming soon)
  - Webhook Management (coming soon)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jaddek/jpy-tillo-sdk.git
    ```

2. Navigate to the project directory:
    ```bash
    cd jpy-tillo-sdk
    ```

3. Install dependencies:
   ```bash
   uv sync
   ```

4. Run tests:
   ```bash
   uv run pytest tests
   ```

## Usage

### Basic Example:

```python
from jpy_tillo_sdk import Tillo

# Initialize the client
client = Tillo(
    api_key="your_api_key",
    secret="your_secret",
)

# Synchronous usage
brands = client.brands.get_all()

# Asynchronous usage
async def get_brands():
    brands = await client.brands_async.get_all()
```

### Float Management Example:

```python
# Check float balance
balance = client.floats.get_balance()

# Async float operations
async def check_float():
    balance = await client.floats_async.get_balance()
```

### Brand Management Example:

```python
# Get brand details
brand = client.brands.get_brand_details(brand_id="123")

# Async brand operations
async def get_brand():
    brand = await client.brands_async.get_brand_details(brand_id="123")
```

## Error Handling

The SDK provides comprehensive error handling with specific exception classes:

```python
from jpy_tillo_sdk.errors import TilloException, AuthenticationError

try:
    result = client.brands.get_brand_details(brand_id="123")
except AuthenticationError as e:
    print(f"Authentication failed: {e.message}")
except TilloException as e:
    print(f"Error {e.tillo_error_code}: {e.message}")
```

## API Documentation

### Available Services

- `client.floats()` / `client.floats_async()`: Float management operations
- `client.brands()` / `client.brands_async()`: Brand management
- `client.templates()` / `client.templates_async()`: Template operations

### Coming Soon
- `client.digital_card()`: Digital card operations
- `client.physical_card()`: Physical card management
- `client.webhook()`: Webhook management


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
