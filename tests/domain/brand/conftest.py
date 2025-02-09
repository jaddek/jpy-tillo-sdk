from unittest.mock import Mock, AsyncMock

import pytest
from httpx import Response

from jaddek_tillo_sdk.http_client import HttpClient, AsyncHttpClient


@pytest.fixture
def mock_http_client():
    client = Mock(spec=HttpClient)
    client.request.return_value = Mock(spec=Response)
    return client


@pytest.fixture
def mock_async_http_client():
    client = AsyncMock(spec=AsyncHttpClient)
    client.request.return_value = Mock(spec=Response)
    return client
