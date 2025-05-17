from unittest.mock import Mock

import httpx
import pytest

from jpy_tillo_sdk.http_client import AsyncHttpClient, ErrorHandler, HttpClient
from jpy_tillo_sdk.signature import SignatureBridge, SignatureGenerator


@pytest.fixture
def mock_signer():
    signer = Mock(spec=SignatureBridge)
    signer.sign.return_value = ("test_api_key", "test_signature", "test_timestamp")
    return signer


@pytest.fixture
def client_options():
    return {"base_url": "https://api.test.com"}


@pytest.fixture
def http_client(mock_signer, client_options) -> HttpClient:
    async def mock_handler(request: httpx.Request) -> httpx.Response:
        assert request.url == httpx.URL("https://api.example.com/data")
        return httpx.Response(200, json={"mocked": True})

    transport = httpx.MockTransport(mock_handler)
    eh = ErrorHandler()
    http_client = HttpClient(client_options, mock_signer, transport=transport, error_handler=eh)
    return http_client


@pytest.fixture
def async_http_client(mock_signer, client_options, httpx_mock_async) -> AsyncHttpClient:
    async def mock_handler(request: httpx.Request) -> httpx.Response:
        assert request.url == httpx.URL("https://api.example.com/data")
        return httpx.Response(200, json={"mocked": True})

    transport = httpx.MockTransport(mock_handler)
    http_client = AsyncHttpClient(client_options, mock_signer, transport=transport)  # type: ignore[arg-type]

    return http_client


@pytest.fixture
def api_key():
    return "test_api_key"


@pytest.fixture
def secret_key():
    return "test_secret_key"


@pytest.fixture
def signature_generator(api_key, secret_key):
    return SignatureGenerator(api_key, secret_key)


@pytest.fixture
def signature_bridge(signature_generator):
    return SignatureBridge(signature_generator)
