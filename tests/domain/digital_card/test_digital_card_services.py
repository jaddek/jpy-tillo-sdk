from unittest.mock import AsyncMock, Mock

import pytest
from httpx import Response

from jpy_tillo_sdk.domain.digital_card.services import (
    DigitalCardService,
    DigitalCardServiceAsync,
)


class TestIssueDigitalCodeServiceAsync:
    @pytest.mark.asyncio
    async def test_issue_digital_code_async(self, mock_async_http_client: AsyncMock) -> None:
        service = DigitalCardServiceAsync(client=mock_async_http_client)
        response = await service.issue_digital_code()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_order_digital_code_async(self, mock_async_http_client: AsyncMock) -> None:
        service = DigitalCardServiceAsync(client=mock_async_http_client)
        response = await service.issue_digital_code()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_check_digital_order_async(self, mock_async_http_client: AsyncMock) -> None:
        service = DigitalCardServiceAsync(client=mock_async_http_client)
        response = await service.check_digital_order()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_top_up_digital_code(self, mock_async_http_client: AsyncMock) -> None:
        service = DigitalCardServiceAsync(client=mock_async_http_client)
        response = await service.top_up_digital_code()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_cancel_digital_url(self, mock_async_http_client: AsyncMock) -> None:
        service = DigitalCardServiceAsync(client=mock_async_http_client)
        response = await service.cancel_digital_url()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_cancel_digital_code(self, mock_async_http_client: AsyncMock) -> None:
        service = DigitalCardServiceAsync(client=mock_async_http_client)
        response = await service.cancel_digital_code()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_reverse_order_digital_code(self, mock_async_http_client: AsyncMock) -> None:
        service = DigitalCardServiceAsync(client=mock_async_http_client)
        response = await service.reverse_digital_code()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_check_stock(self, mock_async_http_client: AsyncMock) -> None:
        service = DigitalCardServiceAsync(client=mock_async_http_client)
        response = await service.check_stock()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.asyncio
    async def test_check_balance(self, mock_async_http_client: AsyncMock) -> None:
        service = DigitalCardServiceAsync(client=mock_async_http_client)
        response = await service.check_balance()

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)


class TestIssueDigitalCodeService:
    def test_issue_digital_code(self, mock_http_client: Mock) -> None:
        service = DigitalCardService(client=mock_http_client)
        response = service.issue_digital_code()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    def test_order_digital_code(self, mock_http_client: Mock) -> None:
        service = DigitalCardService(client=mock_http_client)
        response = service.order_digital_code()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    def test_check_digital_order(self, mock_http_client: Mock) -> None:
        service = DigitalCardService(client=mock_http_client)
        response = service.check_digital_order()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    def test_top_up_digital_code(self, mock_http_client: Mock) -> None:
        service = DigitalCardService(client=mock_http_client)
        response = service.top_up_digital_code()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    def test_cancel_digital_url(self, mock_http_client: Mock) -> None:
        service = DigitalCardService(client=mock_http_client)
        response = service.cancel_digital_url()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    def test_cancel_digital_code(self, mock_http_client: Mock) -> None:
        service = DigitalCardService(client=mock_http_client)
        response = service.cancel_digital_code()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    def test_reverse_order_digital_code(self, mock_http_client: Mock) -> None:
        service = DigitalCardService(client=mock_http_client)
        response = service.reverse_digital_code()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    def test_check_stock(self, mock_http_client: Mock) -> None:
        service = DigitalCardService(client=mock_http_client)
        response = service.check_stock()

        assert mock_http_client.request.called
        assert isinstance(response, Response)

    def test_check_balance(self, mock_http_client: Mock) -> None:
        service = DigitalCardService(client=mock_http_client)
        response = service.check_balance()

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)
