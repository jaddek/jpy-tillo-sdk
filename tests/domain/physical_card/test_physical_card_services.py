import pytest
from httpx import Response
from unittest.mock import Mock, AsyncMock
from jpy_tillo_sdk.http_client import HttpClient, AsyncHttpClient
from jpy_tillo_sdk.domain.physical_card.services import PhysicalGiftCardsService

@pytest.fixture
def mock_async_http_client():
    client = AsyncMock(spec=AsyncHttpClient)
    client.request.return_value = Mock(spec=Response)
    return client

@pytest.fixture
def mock_http_client():
    client = Mock(spec=HttpClient)
    client.request.return_value = Mock(spec=Response)
    return client


def test_activate_physical_card(mock_http_client):
    response = PhysicalGiftCardsService.activate_physical_card(mock_http_client)

    mock_http_client.request.assert_called_once()
    assert isinstance(response, Response)


@pytest.mark.asyncio
async def test_activate_physical_card_async(mock_async_http_client):
    response = await PhysicalGiftCardsService.activate_physical_card_async(mock_async_http_client)

    mock_async_http_client.request.assert_called_once()
    assert isinstance(response, Response)


@pytest.mark.skip(reason="Test not implemented yet.")
def test_cancel_activate_physical_card(mock_http_client):
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
@pytest.mark.asyncio
async def test_cancel_activate_physical_card_async(mock_async_http_client):
    raise NotImplementedError


@pytest.mark.skip(reason="Test not implemented yet.")
def test_cash_out_original_transaction_physical_card(mock_http_client):
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
@pytest.mark.asyncio
async def test_cash_out_original_transaction_physical_card_async(mock_async_http_client):
    raise NotImplementedError


@pytest.mark.skip(reason="Test not implemented yet.")
def test_top_up_physical_card(mock_http_client):
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
@pytest.mark.asyncio
def test_top_up_physical_card_async(mock_async_http_client):
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
def test_cancel_top_up_on_physical_card(mock_http_client):
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
@pytest.mark.asyncio
def test_cancel_top_up_on_physical_card_async(mock_async_http_client):
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
def test_order_physical_card(mock_http_client):
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
@pytest.mark.asyncio
def test_order_physical_card_async(mock_async_http_client):
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
def test_physical_card_order_status(mock_http_client):
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
@pytest.mark.asyncio
def test_physical_card_order_status_async(mock_async_http_client):
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
def test_fulfil_physical_card_order(mock_http_client):
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
@pytest.mark.asyncio
def test_fulfil_physical_card_order_async(mock_async_http_client):
    raise NotImplementedError


def test_balance_check_physical(mock_http_client):
    response = PhysicalGiftCardsService.balance_check_physical(mock_http_client)

    mock_http_client.request.assert_called_once()
    assert isinstance(response, Response)

@pytest.mark.asyncio
async def test_balance_check_physical_async(mock_async_http_client):
    response = await PhysicalGiftCardsService.balance_check_physical_async(mock_async_http_client)

    mock_async_http_client.request.assert_called_once()
    assert isinstance(response, Response)
