import pytest
from httpx import Response

from jpy_tillo_sdk.domain.float.endpoints import RequestPaymentTransferEndpoint
from jpy_tillo_sdk.domain.float.services import FloatService
from jpy_tillo_sdk.enums import Currency


def test_check_floats(mock_http_client):
    response = FloatService.check_floats(mock_http_client)

    mock_http_client.request.assert_called_once()
    assert isinstance(response, Response)


@pytest.mark.asyncio
async def test_check_floats_async(mock_async_http_client):
    response = await FloatService.check_floats_async(mock_async_http_client)

    mock_async_http_client.request.assert_called_once()
    assert isinstance(response, Response)


def test_request_payment_transfer(mock_http_client):
    response = FloatService.request_payment_transfer(
        mock_http_client,
        RequestPaymentTransferEndpoint.RequestBody(
            currency=Currency.EUR,
            amount="100",
            payment_reference="PAY_REF",
            finance_email="<EMAIL>",
        ),
    )
    mock_http_client.request.assert_called_once()
    assert isinstance(response, Response)


@pytest.mark.asyncio
async def test_request_payment_transfer_async(mock_async_http_client):
    response = await FloatService.request_payment_transfer_async(
        mock_async_http_client,
        RequestPaymentTransferEndpoint.RequestBody(
            currency=Currency.EUR,
            amount="100",
            payment_reference="PAY_REF",
            finance_email="<EMAIL>",
        ),
    )

    mock_async_http_client.request.assert_called_once()
    assert isinstance(response, Response)
