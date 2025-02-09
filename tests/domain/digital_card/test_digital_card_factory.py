from unittest.mock import AsyncMock, Mock

import pytest
from httpx import Response

from jaddek_tillo_sdk.domain.digital_card.endpoints import IssueDigitalCodeEndpoint
from jaddek_tillo_sdk.domain.digital_card.factory import (
    create_standard_issue_request,
    create_personalised_issue_request
)
from jaddek_tillo_sdk.enums import Currency, Sector, DeliveryMethod, FulfilmentType
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


def test_create_standard_issue_request():
    request = create_standard_issue_request(
        client_request_id="test-123",
        brand="test-brand",
        amount="100.00",
        currency=Currency.EUR,
        sector=Sector.GIFT_CARD_MALL,
        delivery_method=DeliveryMethod.URL,
        fulfilment_by=FulfilmentType.PARTNER
    )

    assert request.client_request_id == "test-123"
    assert request.brand == "test-brand"
    assert request.face_value.amount == "100.00"
    assert request.face_value.currency == Currency.EUR.value
    assert request.sector == Sector.GIFT_CARD_MALL.value
    assert request.fulfilment_by == FulfilmentType.PARTNER.value
    assert request.delivery_method == DeliveryMethod.URL.value


def test_create_personalised_issue_request():
    personalisation = IssueDigitalCodeEndpoint.RequestBody.Personalisation(
        to_name='to Name',
        from_name='from Name',
        message='message',
    )

    request = create_personalised_issue_request(
        client_request_id="test-123",
        brand="test-brand",
        amount="100.00",
        personalisation=personalisation
    )

    assert request.client_request_id == "test-123"
    assert request.brand == "test-brand"
    assert request.personalisation == personalisation
    assert request.face_value.amount == "100.00"
    assert request.face_value.amount == "100.00"


@pytest.mark.skip(reason="Test not implemented yet.")
def test_create_issue_request_fulfilment_by_tillo():
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
def create_issue_reward_pass_by_email():
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
def create_issue_reward_pass_by_url():
    raise NotImplementedError

@pytest.mark.skip(reason="Test not implemented yet.")
def create_card_top_up_request():
    raise NotImplementedError
