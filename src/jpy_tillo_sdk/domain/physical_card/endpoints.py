from dataclasses import dataclass

from ...contracts import SignatureAttributesInterface
from ...endpoint import Endpoint
from ...enums import Sector
from .shared import FaceValue


@dataclass(frozen=True)
class ActivatePhysicalCardERequestBody(SignatureAttributesInterface):
    client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    code: str | None = None
    pin: str | None = None
    sector: Sector | None = Sector.GIFT_CARD_MALL

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        sign_attrs: list[str] = [
            self.client_request_id,
            self.brand,
        ]

        if self.face_value is not None:
            if self.face_value.currency is not None:
                sign_attrs.append(self.face_value.currency.value)

            if self.face_value.amount is not None:
                sign_attrs.append(self.face_value.amount)

        non_none_attrs = [attr for attr in sign_attrs if attr is not None]

        return tuple(non_none_attrs)


class ActivatePhysicalCardEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-activate"
    _route: str = "/api/v2/physical/activate"


@dataclass(frozen=True)
class CancelActivateRequestBody(SignatureAttributesInterface):
    client_request_id: str
    original_client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    code: str | None = None
    pin: str | None = None
    sector: Sector | None = Sector.GIFT_CARD_MALL
    tags: list[str] | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        sign_attrs: list[str] = [
            self.client_request_id,
            self.brand,
        ]

        if self.face_value is not None:
            if self.face_value.currency is not None:
                sign_attrs.append(self.face_value.currency.value)

            if self.face_value.amount is not None:
                sign_attrs.append(self.face_value.amount)

        non_none_attrs = [attr for attr in sign_attrs if attr is not None]

        return tuple(non_none_attrs)


class CancelActivateEndpoint(Endpoint):
    _method: str = "DELETE"
    _endpoint: str = "physical-activate"
    _route: str = "/api/v2/physical/activate"


@dataclass(frozen=True)
class CashOutOriginalTransactionRequestBody(SignatureAttributesInterface):
    client_request_id: str
    original_client_request_id: str
    brand: str
    code: str | None = None
    pin: str | None = None
    sector: Sector | None = Sector.GIFT_CARD_MALL

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        return (
            self.client_request_id,
            self.brand,
        )


class CashOutOriginalTransactionEndpoint(Endpoint):
    _method: str = "DELETE"
    _endpoint: str = "cash-out-original-transaction"
    _route: str = "/api/v2/physical/cash-out-original-transaction"


@dataclass(frozen=True)
class TopUpPhysicalCardRequestBody(SignatureAttributesInterface):
    client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    code: str | None = None
    pin: str | None = None
    sector: Sector | None = Sector.GIFT_CARD_MALL

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        sign_attrs: list[str] = [
            self.client_request_id,
            self.brand,
        ]

        if self.face_value is not None:
            if self.face_value.currency is not None:
                sign_attrs.append(self.face_value.currency.value)

            if self.face_value.amount is not None:
                sign_attrs.append(self.face_value.amount)

        non_none_attrs = [attr for attr in sign_attrs if attr is not None]

        return tuple(non_none_attrs)


class TopUpPhysicalCardEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-top-up"
    _route: str = "/api/v2/physical/top-up"


@dataclass(frozen=True)
class CancelTopUpRequestBody(SignatureAttributesInterface):
    client_request_id: str
    original_client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    code: str | None = None
    pin: str | None = None
    sector: Sector | None = Sector.GIFT_CARD_MALL

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        return ()


class CancelTopUpEndpoint(Endpoint):
    _method: str = "DELETE"
    _endpoint: str = "physical-top-up"
    _route: str = "/api/v2/physical/top-up"


@dataclass(frozen=True)
class OrderPhysicalCardRequestBody(SignatureAttributesInterface):
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

    client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    shipping_method: str | None = None
    fulfilment_by: str | None = None
    fulfilment_parameters: FulfilmentParameters | None = None
    personalisation: Personalisation | None = None
    sector: Sector | None = Sector.GIFT_CARD_MALL
    tags: list[str] | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        attrs = [
            self.client_request_id,
            self.brand,
        ]

        non_none_attrs = [attr for attr in attrs if attr is not None]

        return tuple(non_none_attrs)


class OrderPhysicalCardEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-order-card"
    _route: str = "/api/v2/physical/order-card"


@dataclass(frozen=True)
class PhysicalCardOrderStatusRequestBody(SignatureAttributesInterface):
    references: list[str] | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        return ()


class PhysicalCardOrderStatusEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-order-status"
    _route: str = "/api/v2/physical/order-status"


@dataclass(frozen=True)
class FulfilPhysicalCardOrderEndpointRequestBody(SignatureAttributesInterface):
    client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    code: str | None = None
    reference: str | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        return ()


class FulfilPhysicalCardOrderEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-fulfil-order"
    _route: str = "/api/v2/physical/fulfil-order"


@dataclass(frozen=True)
class BalanceCheckPhysicalRequestBody(SignatureAttributesInterface):
    client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    code: str | None = None
    pin: str | None = None
    sector: Sector | None = Sector.GIFT_CARD_MALL

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        sign_attrs: list[str] = [
            self.client_request_id,
            self.brand,
        ]

        if self.face_value is not None:
            if self.face_value.currency is not None:
                sign_attrs.append(self.face_value.currency.value)

            if self.face_value.amount is not None:
                sign_attrs.append(self.face_value.amount)

        non_none_attrs = [attr for attr in sign_attrs if attr is not None]

        return tuple(non_none_attrs)


class BalanceCheckPhysicalEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "physical-check-balance"
    _route: str = "/api/v2/physical/check-balance"
