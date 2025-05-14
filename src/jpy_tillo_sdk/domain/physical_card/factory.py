from typing import List

from ...enums import Currency, Sector
from .endpoints import (
    ActivatePhysicalCardEndpoint,
    BalanceCheckPhysicalEndpoint,
    CancelTopUpOnPhysicalCardEndpoint,
    CashOutOriginalTransactionPhysicalCardEndpoint,
    FulfilPhysicalCardOrderEndpoint,
    OrderPhysicalCardEndpoint,
    PhysicalCardOrderStatusEndpoint,
    TopUpPhysicalCardEndpoint,
)
from .models import FaceValue


def create_activate_physical_card_request(
    client_request_id: str,
    brand: str,
    amount: str,
    code: str,
    pin: str,
    currency: Currency = Currency.EUR,
    sector: Sector = Sector.GIFT_CARD_MALL,
) -> ActivatePhysicalCardEndpoint.RequestBody:
    return ActivatePhysicalCardEndpoint.RequestBody(
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


def create_cash_out_original_transaction_request(
    client_request_id: str,
    original_client_request_id: str,
    brand: str,
    code: str,
    pin: str,
    sector: Sector = Sector.GIFT_CARD_MALL,
) -> CashOutOriginalTransactionPhysicalCardEndpoint.RequestBody:
    return CashOutOriginalTransactionPhysicalCardEndpoint.RequestBody(
        client_request_id=client_request_id,
        original_client_request_id=original_client_request_id,
        brand=brand,
        code=code,
        pin=pin,
        sector=sector.value,
    )


def create_top_up_physical_card_request(
    client_request_id: str,
    brand: str,
    amount: str,
    code: str,
    pin: str,
    currency: Currency = Currency.EUR,
    sector: Sector = Sector.GIFT_CARD_MALL,
) -> TopUpPhysicalCardEndpoint.RequestBody:
    return TopUpPhysicalCardEndpoint.RequestBody(
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


def create_cancel_top_up_physical_card_request(
    client_request_id: str,
    original_client_request_id: str,
    brand: str,
    amount: str,
    code: str,
    pin: str,
    currency: Currency = Currency.EUR,
    sector: Sector = Sector.GIFT_CARD_MALL,
) -> CancelTopUpOnPhysicalCardEndpoint.RequestBody:
    return CancelTopUpOnPhysicalCardEndpoint.RequestBody(
        client_request_id=client_request_id,
        original_client_request_id=original_client_request_id,
        brand=brand,
        face_value=FaceValue(
            currency=currency.value,
            amount=amount,
        ),
        code=code,
        pin=pin,
        sector=sector.value,
    )


def create_balance_check_request(
    client_request_id: str,
    brand: str,
    code: str,
    pin: str,
    currency: Currency = Currency.EUR,
    sector: Sector = Sector.GIFT_CARD_MALL,
) -> BalanceCheckPhysicalEndpoint.RequestBody:
    return BalanceCheckPhysicalEndpoint.RequestBody(
        client_request_id=client_request_id,
        brand=brand,
        face_value=FaceValue(
            currency=currency.value,
        ),
        code=code,
        pin=pin,
        sector=sector.value,
    )


def create_order_new_card_request(
    client_request_id: str,
    brand: str,
    amount: str,
    currency: Currency = Currency.EUR,
    fulfilment_parameters: OrderPhysicalCardEndpoint.RequestBody.FulfilmentParameters | None = None,
    personalisation: OrderPhysicalCardEndpoint.RequestBody.Personalisation | None = None,
    shipping_method: str = "standard",
    fulfilment_by: str = "rewardcloud",
    sector: Sector = Sector.GIFT_CARD_MALL,
    tags: List[str] | None = None,
) -> OrderPhysicalCardEndpoint.RequestBody:
    return OrderPhysicalCardEndpoint.RequestBody(
        client_request_id=client_request_id,
        face_value=FaceValue(
            amount=amount,
            currency=currency.value,
        ),
        brand=brand,
        fulfilment_parameters=fulfilment_parameters,
        personalisation=personalisation,
        shipping_method=shipping_method,
        fulfilment_by=fulfilment_by,
        sector=sector.value,
        tags=tags,
    )


def create_order_status_request(
    references: List[str],
) -> PhysicalCardOrderStatusEndpoint.RequestBody:
    return PhysicalCardOrderStatusEndpoint.RequestBody(references=references)


def create_fulfil_physical_card_order_request(
    client_request_id: str,
    brand: str,
    code: str,
    reference: str,
    amount: str,
    currency: Currency = Currency.EUR,
) -> FulfilPhysicalCardOrderEndpoint.RequestBody:
    return FulfilPhysicalCardOrderEndpoint.RequestBody(
        client_request_id=client_request_id,
        brand=brand,
        code=code,
        face_value=FaceValue(
            currency=currency.value,
            amount=amount,
        ),
        reference=reference,
    )
