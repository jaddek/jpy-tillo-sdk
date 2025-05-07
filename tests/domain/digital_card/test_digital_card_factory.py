from unittest.mock import AsyncMock, Mock

import pytest
from httpx import Response

from jpy_tillo_sdk.domain.digital_card.endpoints import (
    IssueDigitalCodeEndpoint,
    TopUpDigitalCodeEndpoint,
)
from jpy_tillo_sdk.domain.digital_card.factory import (
    create_standard_issue_request,
    create_personalised_issue_request,
    create_issue_request_fulfilment_by_tillo,
    create_issue_reward_pass_by_email,
    create_issue_reward_pass_by_url,
    create_card_top_up_request,
)
from jpy_tillo_sdk.enums import Currency, Sector, DeliveryMethod, FulfilmentType
from jpy_tillo_sdk.http_client import HttpClient, AsyncHttpClient


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
        fulfilment_by=FulfilmentType.PARTNER,
    )

    assert isinstance(request, IssueDigitalCodeEndpoint.RequestBody)

    assert request.client_request_id == "test-123"
    assert request.brand == "test-brand"
    assert request.face_value.amount == "100.00"
    assert request.face_value.currency == Currency.EUR.value
    assert request.sector == Sector.GIFT_CARD_MALL.value
    assert request.fulfilment_by == FulfilmentType.PARTNER.value
    assert request.delivery_method == DeliveryMethod.URL.value


def test_create_personalised_issue_request():
    personalisation = IssueDigitalCodeEndpoint.RequestBody.Personalisation(
        to_name="to Name",
        from_name="from Name",
        message="message",
    )

    request = create_personalised_issue_request(
        client_request_id="test-123",
        brand="test-brand",
        amount="100.00",
        personalisation=personalisation,
    )

    assert isinstance(request, IssueDigitalCodeEndpoint.RequestBody)

    assert request.client_request_id == "test-123"
    assert request.brand == "test-brand"
    assert request.personalisation == personalisation
    assert request.face_value.amount == "100.00"


def test_create_issue_request_fulfilment_by_tillo():
    personalisation = IssueDigitalCodeEndpoint.RequestBody.PersonalisationExtended(
        to_name="to Name",
        from_name="from Name",
        message="message",
    )

    fulfilment = IssueDigitalCodeEndpoint.RequestBody.FulfilmentParameters(
        to_name="to Name",
        from_name="from Name",
    )

    request = create_issue_request_fulfilment_by_tillo(
        client_request_id="test-123",
        brand="test-brand",
        amount="100.00",
        personalisation=personalisation,
        fulfilment_parameters=fulfilment,
        currency=Currency.EUR,
        sector=Sector.GIFT_CARD_MALL,
        delivery_method=DeliveryMethod.URL,
        fulfilment_by=FulfilmentType.PARTNER,
    )

    assert isinstance(request, IssueDigitalCodeEndpoint.RequestBody)

    assert request.client_request_id == "test-123"
    assert request.brand == "test-brand"
    assert request.face_value.amount == "100.00"
    assert request.face_value.currency == Currency.EUR.value
    assert request.delivery_method == DeliveryMethod.URL.value
    assert request.fulfilment_by == FulfilmentType.PARTNER.value
    assert request.personalisation == personalisation
    assert request.fulfilment_parameters == fulfilment


def test_create_issue_reward_pass_by_email():
    personalisation = IssueDigitalCodeEndpoint.RequestBody.PersonalisationExtended(
        to_name="to Name",
        from_name="from Name",
        message="message",
    )

    fulfilment = IssueDigitalCodeEndpoint.RequestBody.FulfilmentParametersForRewardPassUsingEmail(
        to_name="to Name",
        from_name="from Name",
    )

    request = create_issue_reward_pass_by_email(
        client_request_id="test-123",
        brand="test-brand",
        amount="100.00",
        personalisation=personalisation,
        fulfilment_parameters=fulfilment,
        currency=Currency.EUR,
        sector=Sector.GIFT_CARD_MALL,
        delivery_method=DeliveryMethod.URL,
        fulfilment_by=FulfilmentType.PARTNER,
    )

    assert isinstance(request, IssueDigitalCodeEndpoint.RequestBody)

    assert request.client_request_id == "test-123"
    assert request.brand == "test-brand"
    assert request.face_value.amount == "100.00"
    assert request.face_value.currency == Currency.EUR.value
    assert request.delivery_method == DeliveryMethod.URL.value
    assert request.fulfilment_by == FulfilmentType.PARTNER.value
    assert request.personalisation == personalisation
    assert request.fulfilment_parameters == fulfilment


def test_create_issue_reward_pass_by_url():
    personalisation = IssueDigitalCodeEndpoint.RequestBody.PersonalisationExtended(
        to_name="to Name",
        from_name="from Name",
        message="message",
    )

    fulfilment = (
        IssueDigitalCodeEndpoint.RequestBody.FulfilmentParametersForRewardPassUsingUrl(
            to_name="to Name",
        )
    )

    request = create_issue_reward_pass_by_url(
        client_request_id="test-123",
        brand="test-brand",
        amount="100.00",
        personalisation=personalisation,
        fulfilment_parameters=fulfilment,
        currency=Currency.EUR,
        sector=Sector.GIFT_CARD_MALL,
        delivery_method=DeliveryMethod.URL,
        fulfilment_by=FulfilmentType.PARTNER,
    )

    assert isinstance(request, IssueDigitalCodeEndpoint.RequestBody)

    assert request.client_request_id == "test-123"
    assert request.brand == "test-brand"
    assert request.face_value.amount == "100.00"
    assert request.face_value.currency == Currency.EUR.value
    assert request.delivery_method == DeliveryMethod.URL.value
    assert request.fulfilment_by == FulfilmentType.PARTNER.value
    assert request.personalisation == personalisation
    assert request.fulfilment_parameters == fulfilment


def test_create_card_top_up_request():
    request = create_card_top_up_request(
        client_request_id="test-123",
        brand="test-brand",
        amount="100.00",
        code="code",
        pin="123456",
        currency=Currency.EUR,
        sector=Sector.GIFT_CARD_MALL,
    )

    assert isinstance(request, TopUpDigitalCodeEndpoint.RequestBody)

    assert request.client_request_id == "test-123"
    assert request.brand == "test-brand"
    assert request.face_value.amount == "100.00"
    assert request.face_value.currency == Currency.EUR.value
    assert request.pin == "123456"
    assert request.code == "code"
    assert request.sector == Sector.GIFT_CARD_MALL.value
