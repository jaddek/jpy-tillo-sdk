from .models import FaceValue
from .endpoints import IssueDigitalCodeEndpoint, TopUpDigitalCodeEndpoint
from ...enums import Currency, Sector, DeliveryMethod, FulfilmentType


def create_standard_issue_request(
    client_request_id: str,
    brand: str,
    amount: str,
    currency: Currency = Currency.EUR,
    sector: Sector = Sector.GIFT_CARD_MALL,
    delivery_method: DeliveryMethod = DeliveryMethod.URL,
    fulfilment_by: FulfilmentType = FulfilmentType.PARTNER,
) -> IssueDigitalCodeEndpoint.RequestBody:
    return IssueDigitalCodeEndpoint.RequestBody(
        client_request_id=client_request_id,
        brand=brand,
        face_value=FaceValue(
            currency=currency.value,
            amount=amount,
        ),
        sector=sector.value,
        delivery_method=delivery_method.value,
        fulfilment_by=fulfilment_by.value,
    )


def create_personalised_issue_request(
    client_request_id: str,
    brand: str,
    amount: str,
    personalisation: IssueDigitalCodeEndpoint.RequestBody.Personalisation,
    currency: Currency = Currency.EUR,
    sector: Sector = Sector.GIFT_CARD_MALL,
    delivery_method: DeliveryMethod = DeliveryMethod.URL,
    fulfilment_by: FulfilmentType = FulfilmentType.PARTNER,
) -> IssueDigitalCodeEndpoint.RequestBody:
    return IssueDigitalCodeEndpoint.RequestBody(
        client_request_id=client_request_id,
        brand=brand,
        face_value=FaceValue(
            currency=currency.value,
            amount=amount,
        ),
        delivery_method=delivery_method.value,
        fulfilment_by=fulfilment_by.value,
        personalisation=personalisation,
        sector=sector.value,
    )


def create_issue_request_fulfilment_by_tillo(
    client_request_id: str,
    brand: str,
    amount: str,
    personalisation: IssueDigitalCodeEndpoint.RequestBody.PersonalisationExtended,
    fulfilment_parameters: IssueDigitalCodeEndpoint.RequestBody.FulfilmentParameters,
    currency: Currency = Currency.EUR,
    sector: Sector = Sector.GIFT_CARD_MALL,
    delivery_method: DeliveryMethod = DeliveryMethod.URL,
    fulfilment_by: FulfilmentType = FulfilmentType.PARTNER,
) -> IssueDigitalCodeEndpoint.RequestBody:
    return IssueDigitalCodeEndpoint.RequestBody(
        client_request_id=client_request_id,
        brand=brand,
        face_value=FaceValue(
            currency=currency.value,
            amount=amount,
        ),
        delivery_method=delivery_method.value,
        fulfilment_by=fulfilment_by.value,
        fulfilment_parameters=fulfilment_parameters,
        personalisation=personalisation,
        sector=sector.value,
    )


def create_issue_reward_pass_by_email(
    client_request_id: str,
    brand: str,
    amount: str,
    personalisation: IssueDigitalCodeEndpoint.RequestBody.PersonalisationExtended,
    fulfilment_parameters: IssueDigitalCodeEndpoint.RequestBody.FulfilmentParametersForRewardPassUsingEmail,
    currency: Currency = Currency.EUR,
    sector: Sector = Sector.GIFT_CARD_MALL,
    delivery_method: DeliveryMethod = DeliveryMethod.URL,
    fulfilment_by: FulfilmentType = FulfilmentType.PARTNER,
) -> IssueDigitalCodeEndpoint.RequestBody:
    return IssueDigitalCodeEndpoint.RequestBody(
        client_request_id=client_request_id,
        brand=brand,
        face_value=FaceValue(
            currency=currency.value,
            amount=amount,
        ),
        delivery_method=delivery_method.value,
        fulfilment_by=fulfilment_by.value,
        fulfilment_parameters=fulfilment_parameters,
        personalisation=personalisation,
        sector=sector.value,
    )


def create_issue_reward_pass_by_url(
    client_request_id: str,
    brand: str,
    amount: str,
    personalisation: IssueDigitalCodeEndpoint.RequestBody.Personalisation,
    fulfilment_parameters: IssueDigitalCodeEndpoint.RequestBody.FulfilmentParametersForRewardPassUsingUrl,
    currency: Currency = Currency.EUR,
    sector: Sector = Sector.GIFT_CARD_MALL,
    delivery_method: DeliveryMethod = DeliveryMethod.URL,
    fulfilment_by: FulfilmentType = FulfilmentType.PARTNER,
) -> IssueDigitalCodeEndpoint.RequestBody:
    return IssueDigitalCodeEndpoint.RequestBody(
        client_request_id=client_request_id,
        brand=brand,
        face_value=FaceValue(
            currency=currency.value,
            amount=amount,
        ),
        delivery_method=delivery_method.value,
        fulfilment_by=fulfilment_by.value,
        fulfilment_parameters=fulfilment_parameters,
        personalisation=personalisation,
        sector=sector.value,
    )


def create_card_top_up_request(
    client_request_id: str,
    brand: str,
    amount: str,
    code: str,
    pin: str,
    currency: Currency = Currency.EUR,
    sector: Sector = Sector.GIFT_CARD_MALL,
) -> TopUpDigitalCodeEndpoint.RequestBody:
    return TopUpDigitalCodeEndpoint.RequestBody(
        client_request_id=client_request_id,
        brand=brand,
        face_value=FaceValue(
            currency=currency.value,
            amount=amount,
        ),
        code=code,
        pin=pin,
        sector=sector.value,
    )
