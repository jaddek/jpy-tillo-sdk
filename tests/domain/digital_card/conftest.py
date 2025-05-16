from unittest.mock import AsyncMock, Mock

import pytest
from httpx import Response

from jpy_tillo_sdk.http_client import AsyncHttpClient, HttpClient


@pytest.fixture
def mock_http_client() -> Mock:
    client = Mock(spec=HttpClient)
    client.request.return_value = Mock(spec=Response)
    return client


@pytest.fixture
def mock_async_http_client() -> AsyncMock:
    client = AsyncMock(spec=AsyncHttpClient)
    client.request.return_value = Mock(spec=Response)
    return client
