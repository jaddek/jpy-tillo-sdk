from typing import Any
from unittest.mock import Mock

import pytest
from httpx import URL, MockTransport, Request, Response

from jpy_tillo_sdk.endpoint import Endpoint
from jpy_tillo_sdk.http_client import AsyncHttpClient, ErrorHandler, HttpClient, RequestDataExtractor


class MockEndpoint(Endpoint):
    _method: str = "GET"
    _endpoint: str = "/test"
    _route: str = "https://api.test.com/test"

    def __init__(
        self,
        body: Any = None,
        query: Any = None,
    ) -> None:
        super().__init__(body=body, query=query)


# def test_get_request_headers(http_client: HttpClient) -> None:
#     headers = http_client.("GET", "/test", ())
#
#     assert headers["Accept"] == "application/json"
#     assert headers["Content-Type"] == "application/json"
#     assert headers["API-Key"] == "test_api_key"
#     assert headers["Signature"] == "test_signature"
#     assert headers["Timestamp"] == "test_timestamp"
#     assert headers["User-Agent"] == "JpyTilloSDKClient/0.2"


def test_http_client_request() -> None:
    def mock_handler(request: Request) -> Response:
        assert request.url == URL("https://api.test.com/test")
        assert request.method == "GET"
        return Response(200, json={"mocked": True})

    extractor = Mock(spec=RequestDataExtractor)
    extractor.extract_all.return_value = ({}, None, None)

    transport = MockTransport(mock_handler)  # type: ignore[arg-type]
    http_client = HttpClient(
        {},
        extractor=extractor,
        error_handler=Mock(spec=ErrorHandler),
        transport=transport,
    )

    response = http_client.request(MockEndpoint())

    assert response.status_code == 200
    assert response.json() == {"mocked": True}


@pytest.mark.asyncio
async def test_async_http_client_request():
    async def mock_handler(request: Request) -> Response:
        assert request.url == URL("https://api.test.com/test")
        assert request.method == "GET"
        return Response(200, json={"mocked": True})

    extractor = Mock(spec=RequestDataExtractor)
    extractor.extract_all.return_value = ({}, None, None)

    transport = MockTransport(mock_handler)  # type: ignore[arg-type]
    http_client = AsyncHttpClient(
        tillo_client_options={},
        extractor=extractor,
        error_handler=Mock(spec=ErrorHandler),
        transport=transport,
    )

    response = await http_client.request(MockEndpoint())

    assert response.status_code == 200
    assert response.json() == {"mocked": True}
