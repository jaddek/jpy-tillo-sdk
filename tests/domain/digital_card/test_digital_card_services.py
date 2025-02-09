import pytest
from httpx import Response

from jaddek_tillo_sdk.domain.digital_card.services import IssueDigitalCodeService


class TestIssueDigitalCodeService:
    def test_issue_digital_code(self, mock_http_client):
        response = IssueDigitalCodeService.issue_digital_code(mock_http_client)

        mock_http_client.request.assert_called_once()
        assert isinstance(response, Response)


    @pytest.mark.asyncio
    async def test_issue_digital_code_async(self, mock_async_http_client):
        response = await IssueDigitalCodeService.issue_digital_code_async(mock_async_http_client)

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)

    @pytest.mark.skip(reason="Test not implemented yet.")
    def test_order_digital_code(self, mock_http_client):
        raise NotImplementedError

    @pytest.mark.skip(reason="Test not implemented yet.")
    @pytest.mark.asyncio
    async def test_order_digital_code_async(self, async_http_client):
        raise NotImplementedError

    @pytest.mark.skip(reason="Test not implemented yet.")
    def test_check_digital_order(self, mock_http_client):
        raise NotImplementedError

    @pytest.mark.skip(reason="Test not implemented yet.")
    @pytest.mark.asyncio
    async def test_check_digital_order_async(self, async_http_client):
        raise NotImplementedError

    @pytest.mark.skip(reason="Test not implemented yet.")
    def test_top_up_digital_code(self, mock_http_client):
        raise NotImplementedError

    @pytest.mark.skip(reason="Test not implemented yet.")
    @pytest.mark.asyncio
    async def test_top_up_digital_code_async(self, async_http_client):
        raise NotImplementedError

    @pytest.mark.skip(reason="Test not implemented yet.")
    def test_cancel_digital_url(self, mock_http_client):
        raise NotImplementedError

    @pytest.mark.skip(reason="Test not implemented yet.")
    @pytest.mark.asyncio
    async def test_cancel_digital_url_async(self, async_http_client):
        raise NotImplementedError

    @pytest.mark.skip(reason="Test not implemented yet.")
    def test_cancel_digital_code(self, mock_http_client):
        raise NotImplementedError

    @pytest.mark.skip(reason="Test not implemented yet.")
    @pytest.mark.asyncio
    async def test_cancel_digital_code_async(self, async_http_client):
        raise NotImplementedError

    @pytest.mark.skip(reason="Test not implemented yet.")
    def test_reverse_order_digital_code(self, mock_http_client):
        raise NotImplementedError

    @pytest.mark.skip(reason="Test not implemented yet.")
    @pytest.mark.asyncio
    async def test_reverse_order_digital_code_async(self, async_http_client):
        raise NotImplementedError


    def test_check_stock(self, mock_http_client):
        response = IssueDigitalCodeService.check_stock(mock_http_client)

        assert mock_http_client.request.called
        assert isinstance(response, Response)

    @pytest.mark.skip(reason="Test not implemented yet.")
    @pytest.mark.asyncio
    async def test_check_stock_async(self, mock_http_client):
        raise NotImplementedError

    @pytest.mark.skip(reason="Test not implemented yet.")
    def test_check_balance(self, mock_http_client):
        raise NotImplementedError

    @pytest.mark.asyncio
    async def test_check_balance_async(self, mock_async_http_client):
        response = await IssueDigitalCodeService.check_balance_async(mock_async_http_client)

        mock_async_http_client.request.assert_called_once()
        assert isinstance(response, Response)
