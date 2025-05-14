from dataclasses import dataclass
from typing import List

from ...endpoint import AbstractBodyRequest, Endpoint
from ...enums import Sector
from .models import FaceValue


class ActivatePhysicalCardEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-activate"
    _route: str = "/api/v2/physical/activate"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        code: str | None = None
        pin: str | None = None
        sector: Sector | None = Sector.GIFT_CARD_MALL

        def get_sign_attrs(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )


class CancelActivatePhysicalCardEndpoint(Endpoint):
    _method: str = "DELETE"
    _endpoint: str = "physical-activate"
    _route: str = "/api/v2/physical/activate"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None
        original_client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        code: str | None = None
        pin: str | None = None
        sector: Sector | None = Sector.GIFT_CARD_MALL
        tags: List[str] | None = None

        def get_sign_attrs(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )


class CashOutOriginalTransactionPhysicalCardEndpoint(Endpoint):
    _method: str = "DELETE"
    _endpoint: str = "cash-out-original-transaction"
    _route: str = "/api/v2/physical/cash-out-original-transaction"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None
        original_client_request_id: str | None = None
        brand: str | None = None
        code: str | None = None
        pin: str | None = None
        sector: Sector | None = Sector.GIFT_CARD_MALL

        def get_sign_attrs(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )


class TopUpPhysicalCardEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-top-up"
    _route: str = "/api/v2/physical/top-up"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        code: str | None = None
        pin: str | None = None
        sector: Sector | None = Sector.GIFT_CARD_MALL

        def get_sign_attrs(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )


class CancelTopUpOnPhysicalCardEndpoint(Endpoint):
    _method: str = "DELETE"
    _endpoint: str = "physical-top-up"
    _route: str = "/api/v2/physical/top-up"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None
        original_client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        code: str | None = None
        pin: str | None = None
        sector: Sector | None = Sector.GIFT_CARD_MALL


class OrderPhysicalCardEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-order-card"
    _route: str = "/api/v2/physical/order-card"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        @dataclass(frozen=True)
        class FulfilmentParameters:
            to_name: str | None = None
            company_name: str | None = None
            address_1: str | None = None
            address_2: str = ""
            address_3: str = ""
            address_4: str = ""
            city: str | None = None
            postal_code: str | None = None
            country: str | None = None

        @dataclass(frozen=True)
        class Personalisation:
            message: str | None = None

        client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        shipping_method: str | None = None
        fulfilment_by: str | None = None
        fulfilment_parameters: FulfilmentParameters | None = None
        personalisation: Personalisation | None = None
        sector: Sector | None = Sector.GIFT_CARD_MALL
        tags: List[str] | None = None

        def get_sign_attrs(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )


class PhysicalCardOrderStatusEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-order-status"
    _route: str = "/api/v2/physical/order-status"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        references: List[str] | None = None


class FulfilPhysicalCardOrderEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-fulfil-order"
    _route: str = "/api/v2/physical/fulfil-order"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        code: str | None = None
        reference: str | None = None


class BalanceCheckPhysicalEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-check-balance"
    _route: str = "/api/v2/physical/check-balance"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: str | None = None
        brand: str | None = None
        face_value: FaceValue | None = None
        code: str | None = None
        pin: str | None = None
        sector: Sector | None = Sector.GIFT_CARD_MALL

        def get_sign_attrs(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )
