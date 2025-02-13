import pytest
from httpx import Response

from jpy_tillo_sdk.domain.float.services import FloatService


def test_check_floats(mock_http_client, mock_query_params):
    response = FloatService.check_floats(mock_http_client)

    mock_http_client.request.assert_called_once()
    assert isinstance(response, Response)


@pytest.mark.asyncio
async def test_check_floats_async(mock_async_http_client):
    response = await FloatService.check_floats_async(mock_async_http_client)

    mock_async_http_client.request.assert_called_once()
    assert isinstance(response, Response)


def test_request_payment_transfer():
    service = FloatService()
    with pytest.raises(NotImplementedError):
        service.request_payment_transfer()


@pytest.mark.asyncio
async def test_request_payment_transfer_async():
    service = FloatService()
    with pytest.raises(NotImplementedError):
        await service.request_payment_transfer_async()
