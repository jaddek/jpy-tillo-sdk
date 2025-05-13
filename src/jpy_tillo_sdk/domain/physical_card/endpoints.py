from dataclasses import dataclass
from typing import List, Optional

from ...endpoint import AbstractBodyRequest, Endpoint
from ...enums import Sector
from .models import FaceValue


class ActivatePhysicalCardEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-activate"
    _route: str = "/api/v2/physical/activate"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        code: Optional[str] = None
        pin: Optional[str] = None
        sector: Optional[Sector] = Sector.GIFT_CARD_MALL

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
        client_request_id: Optional[str] = None
        original_client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        code: Optional[str] = None
        pin: Optional[str] = None
        sector: Optional[Sector] = Sector.GIFT_CARD_MALL
        tags: Optional[List[str]] = None

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
        client_request_id: Optional[str] = None
        original_client_request_id: Optional[str] = None
        brand: Optional[str] = None
        code: Optional[str] = None
        pin: Optional[str] = None
        sector: Optional[Sector] = Sector.GIFT_CARD_MALL

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
        client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        code: Optional[str] = None
        pin: Optional[str] = None
        sector: Optional[Sector] = Sector.GIFT_CARD_MALL

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
        client_request_id: Optional[str] = None
        original_client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        code: Optional[str] = None
        pin: Optional[str] = None
        sector: Optional[Sector] = Sector.GIFT_CARD_MALL


class OrderPhysicalCardEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-order-card"
    _route: str = "/api/v2/physical/order-card"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        @dataclass(frozen=True)
        class FulfilmentParameters:
            to_name: Optional[str] = None
            company_name: Optional[str] = None
            address_1: Optional[str] = None
            address_2: str = ""
            address_3: str = ""
            address_4: str = ""
            city: Optional[str] = None
            postal_code: Optional[str] = None
            country: Optional[str] = None

        @dataclass(frozen=True)
        class Personalisation:
            message: Optional[str] = None

        client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        shipping_method: Optional[str] = None
        fulfilment_by: Optional[str] = None
        fulfilment_parameters: Optional[FulfilmentParameters] = None
        personalisation: Optional[Personalisation] = None
        sector: Optional[Sector] = Sector.GIFT_CARD_MALL
        tags: Optional[List[str]] = None

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
        references: Optional[List[str]] = None


class FulfilPhysicalCardOrderEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-fulfil-order"
    _route: str = "/api/v2/physical/fulfil-order"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        code: Optional[str] = None
        reference: Optional[str] = None


class BalanceCheckPhysicalEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-check-balance"
    _route: str = "/api/v2/physical/check-balance"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        code: Optional[str] = None
        pin: Optional[str] = None
        sector: Optional[Sector] = Sector.GIFT_CARD_MALL

        def get_sign_attrs(self) -> tuple:
            return (
                self.client_request_id,
                self.brand,
                self.face_value.currency,
                self.face_value.amount,
            )
