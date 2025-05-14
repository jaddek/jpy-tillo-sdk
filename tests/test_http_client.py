import dataclasses
from unittest.mock import AsyncMock, Mock

import pytest
from httpx import Response

from jpy_tillo_sdk.endpoint import AbstractBodyRequest, Endpoint


class MockEndpoint(Endpoint):
    def __init__(self, method="GET", endpoint="/test", route="https://api.test.com/test", body=None):
        super().__init__()
        self._method = method
        self._endpoint = endpoint
        self._route = route
        self._params = {}
        self._body = body or Mock(get_sign_attrs=Mock(return_value=()))
        self._query = Mock(get_sign_attrs=Mock(return_value=()))

    def is_body_not_empty(self):
        return False


def test_get_request_headers(http_client):
    headers = http_client._get_request_headers("GET", "/test", ())

    assert headers["Accept"] == "application/json"
    assert headers["Content-Type"] == "application/json"
    assert headers["API-Key"] == "test_api_key"
    assert headers["Signature"] == "test_signature"
    assert headers["Timestamp"] == "test_timestamp"
    assert headers["User-Agent"] == "JpyTilloSDKClient/0.2"


def test_http_client_request(http_client, monkeypatch):
    endpoint = MockEndpoint()
    mock_response = Mock(spec=Response)
    mock_response.status_code = 200
    mock_client = Mock()
    mock_client.request.return_value = mock_response

    class MockClientContext:
        def __enter__(self):
            return mock_client

        def __exit__(self, *args):
            pass

    monkeypatch.setattr("jpy_tillo_sdk.http_client.Client", lambda **kwargs: MockClientContext())

    response = http_client.request(endpoint)

    assert response == mock_response
    mock_client.request.assert_called_once_with(
        url=endpoint.route,
        method=endpoint.method,
        params=endpoint.params,
        json=None,
        headers=http_client._get_request_headers(endpoint.method, endpoint.endpoint),
    )


@pytest.mark.asyncio
async def test_async_http_client_request(async_http_client, monkeypatch):
    endpoint = MockEndpoint()
    mock_response = Mock(spec=Response)
    mock_response.status_code = 200
    mock_client = AsyncMock()
    mock_client.request.return_value = mock_response

    class MockAsyncClientContext:
        async def __aenter__(self):
            return mock_client

        async def __aexit__(self, *args):
            pass

    monkeypatch.setattr(
        "jpy_tillo_sdk.http_client.AsyncClient",
        lambda **kwargs: MockAsyncClientContext(),
    )

    response = await async_http_client.request(endpoint)

    assert response == mock_response
    mock_client.request.assert_called_once_with(
        url=endpoint.route,
        method=endpoint.method,
        params=endpoint.params,
        json=None,
        headers=async_http_client._get_request_headers(endpoint.method, endpoint.endpoint),
    )


def test_request_with_body(http_client, monkeypatch):
    @dataclasses.dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        test: str = "data"

        def get_sign_attrs(self):
            return ()

    endpoint = MockEndpoint(body=RequestBody())

    mock_response = Mock(spec=Response)
    mock_response.status_code = 200
    mock_client = Mock()
    mock_client.request.return_value = mock_response

    class MockClientContext:
        def __enter__(self):
            return mock_client

        def __exit__(self, *args):
            pass

    monkeypatch.setattr("jpy_tillo_sdk.http_client.Client", lambda **kwargs: MockClientContext())

    response = http_client.request(endpoint)

    assert response == mock_response
    mock_client.request.assert_called_once_with(
        url=endpoint.route,
        method=endpoint.method,
        params=endpoint.params,
        json={"test": "data"},
        headers=http_client._get_request_headers(endpoint.method, endpoint.endpoint, endpoint.body.get_sign_attrs()),
    )
