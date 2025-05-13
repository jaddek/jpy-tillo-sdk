from unittest.mock import Mock

import pytest

from jpy_tillo_sdk.http_client import AsyncHttpClient, HttpClient
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
def http_client(mock_signer, client_options):
    return HttpClient(client_options, mock_signer)


@pytest.fixture
def async_http_client(mock_signer, client_options):
    return AsyncHttpClient(client_options, mock_signer)


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
