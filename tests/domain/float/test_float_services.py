import pytest
from httpx import Response

from jpy_tillo_sdk.domain.float.endpoints import (
    RequestPaymentTransferEndpointRequestBody,
)
from jpy_tillo_sdk.domain.float.services import FloatService, FloatServiceAsync
from jpy_tillo_sdk.enums import Currency


def test_check_floats(mock_http_client):
    float_service = FloatService(client=mock_http_client)

    response = float_service.check_floats(mock_http_client)

    mock_http_client.request.assert_called_once()
    assert isinstance(response, Response)


@pytest.mark.asyncio
async def test_check_floats_async(mock_async_http_client):
    float_service = FloatServiceAsync(client=mock_async_http_client)

    response = await float_service.check_floats(mock_async_http_client)

    mock_async_http_client.request.assert_called_once()
    assert isinstance(response, Response)


def test_request_payment_transfer(mock_http_client):
    float_service = FloatService(client=mock_http_client)

    response = float_service.request_payment_transfer(
        RequestPaymentTransferEndpointRequestBody(
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
    float_service = FloatServiceAsync(client=mock_async_http_client)

    response = await float_service.request_payment_transfer(
        RequestPaymentTransferEndpointRequestBody(
            currency=Currency.EUR,
            amount="100",
            payment_reference="PAY_REF",
            finance_email="<EMAIL>",
        ),
    )

    mock_async_http_client.request.assert_called_once()
    assert isinstance(response, Response)
