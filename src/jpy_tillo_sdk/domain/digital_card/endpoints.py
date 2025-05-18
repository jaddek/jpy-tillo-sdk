from dataclasses import dataclass, field

from ...contracts import SignatureAttributesInterface
from ...endpoint import Endpoint
from .shared import FaceValue


@dataclass(frozen=True)
class IssueDigitalCodeRequestBody(SignatureAttributesInterface):
    @dataclass(frozen=True)
    class Personalisation:
        to_name: str | None = None
        from_name: str | None = None
        message: str | None = None
        template: str = "standard"

    @dataclass(frozen=True)
    class PersonalisationExtended(Personalisation):
        email_message: str | None = None
        redemption_message: str | None = None
        carrier_message: str | None = None

    @dataclass(frozen=True)
    class FulfilmentParameters:
        to_name: str | None = None
        to_email: str | None = None
        from_name: str | None = None
        from_email: str | None = None
        subject: str | None = None

    @dataclass(frozen=True)
    class FulfilmentParametersForRewardPassUsingEmail:
        to_name: str | None = None
        to_email: str | None = None
        from_name: str | None = None
        from_email: str | None = None
        subject: str | None = None
        language: str = "en"
        customer_id: str = ""
        to_first_name: str | None = None
        to_last_name: str | None = None

    @dataclass(frozen=True)
    class FulfilmentParametersForRewardPassUsingUrl:
        to_name: str | None = None
        to_first_name: str | None = None
        to_last_name: str | None = None
        address_1: str | None = None
        address_2: str | None = None
        city: str | None = None
        postal_code: str | None = None
        country: str | None = None
        language: str | None = None
        customer_id: str | None = None

    client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    delivery_method: str | None = None
    fulfilment_by: str | None = None
    fulfilment_parameters: (
        FulfilmentParameters
        | FulfilmentParametersForRewardPassUsingEmail
        | FulfilmentParametersForRewardPassUsingUrl
        | None
    ) = None
    sector: str | None = None
    personalisation: Personalisation | PersonalisationExtended | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        sign_attrs: list[str] = [
            self.client_request_id,
            self.brand,
        ]

        if self.face_value is not None:
            if self.face_value.currency is not None:
                sign_attrs.append(self.face_value.currency)

            if self.face_value.amount is not None:
                sign_attrs.append(self.face_value.amount)

        non_none_attrs = [attr for attr in sign_attrs if attr is not None]

        return tuple(non_none_attrs)


class IssueDigitalCodeEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "digital-issue"
    _route: str = "/api/v2/digital/issue"


@dataclass(frozen=True)
class TopUpDigitalCodeRequestBody(SignatureAttributesInterface):
    client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    code: str | None = None
    pin: str | None = None
    sector: str | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        sign_attrs: list[str] = [
            self.client_request_id,
            self.brand,
        ]

        if self.face_value is not None:
            if self.face_value.currency is not None:
                sign_attrs.append(self.face_value.currency)

            if self.face_value.amount is not None:
                sign_attrs.append(self.face_value.amount)

        non_none_attrs = [attr for attr in sign_attrs if attr is not None]

        return tuple(non_none_attrs)


class TopUpDigitalCodeEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "digital-top-up"
    _route: str = "/api/v2/digital/top-up"


@dataclass(frozen=True)
class CheckStockRequestQuery(SignatureAttributesInterface):
    @property
    def sign_attrs(self) -> tuple[str, ...]:
        return (self.brand,) if self.brand else ()

    brand: str


class CheckStockEndpoint(Endpoint):
    _method: str = "GET"
    _endpoint: str = "check-stock"
    _route: str = "/api/v2/check-stock"


@dataclass(frozen=True)
class CancelDigitalCodeRequestBody(SignatureAttributesInterface):
    client_request_id: str
    original_client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    code: str | None = None
    sector: str | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        sign_attrs: list[str] = [
            self.client_request_id,
            self.brand,
        ]

        if self.face_value is not None:
            if self.face_value.currency is not None:
                sign_attrs.append(self.face_value.currency)

            if self.face_value.amount is not None:
                sign_attrs.append(self.face_value.amount)

        non_none_attrs = [attr for attr in sign_attrs if attr is not None]

        return tuple(non_none_attrs)


class CancelDigitalCodeEndpoint(Endpoint):
    _method: str = "DELETE"
    _endpoint: str = "digital-issue"
    _route: str = "/api/v2/digital/issue"


@dataclass(frozen=True)
class CancelDigitalUrlRequestBody(SignatureAttributesInterface):
    client_request_id: str
    original_client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    url: str | None = None
    sector: str | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        sign_attrs: list[str] = [
            self.client_request_id,
            self.brand,
        ]

        if self.face_value is not None:
            if self.face_value.currency is not None:
                sign_attrs.append(self.face_value.currency)

            if self.face_value.amount is not None:
                sign_attrs.append(self.face_value.amount)

        non_none_attrs = [attr for attr in sign_attrs if attr is not None]

        return tuple(non_none_attrs)


class CancelDigitalUrlEndpoint(Endpoint):
    _method: str = "DELETE"
    _endpoint: str = "digital-issue"
    _route: str = "/api/v2/digital/issue"


@dataclass(frozen=True)
class ReverseDigitalCodeRequestBody(SignatureAttributesInterface):
    client_request_id: str
    original_client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    sector: str | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        sign_attrs: list[str] = [
            self.client_request_id,
            self.brand,
        ]

        if self.face_value is not None:
            if self.face_value.currency is not None:
                sign_attrs.append(self.face_value.currency)

            if self.face_value.amount is not None:
                sign_attrs.append(self.face_value.amount)

        non_none_attrs = [attr for attr in sign_attrs if attr is not None]

        return tuple(non_none_attrs)


class ReverseDigitalCodeEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "digital-reverse"
    _route: str = "/api/v2/digital/reverse"


@dataclass(frozen=True)
class CheckBalanceRequestBody(SignatureAttributesInterface):
    client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    reference: str | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        sign_attrs: list[str] = [
            self.client_request_id,
            self.brand,
        ]

        if self.face_value is not None:
            if self.face_value.currency is not None:
                sign_attrs.append(self.face_value.currency)

            if self.face_value.amount is not None:
                sign_attrs.append(self.face_value.amount)

        non_none_attrs = [attr for attr in sign_attrs if attr is not None]

        return tuple(non_none_attrs)


class CheckBalanceEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "digital-check-balance"
    _route: str = "/api/v2/digital/check-balance"


@dataclass(frozen=True)
class OrderDigitalCodeAsyncRequestBody(SignatureAttributesInterface):
    @dataclass(frozen=True)
    class Personalisation:
        to_name: str | None = None
        from_name: str | None = None
        message: str | None = None
        template: str | None = "standard"
        email_message: str | None = None
        redemption_message: str | None = None
        carrier_message: str | None = None

    @dataclass(frozen=True)
    class FulfilmentParameters:
        to_name: str | None = None
        to_email: str | None = None
        from_name: str | None = None
        from_email: str | None = None
        subject: str | None = None
        language: str = "en"
        customer_id: str | None = ""
        to_first_name: str | None = None
        to_last_name: str | None = None

    client_request_id: str
    brand: str
    face_value: FaceValue | None = None
    delivery_method: str | None = None
    fulfilment_by: str | None = None
    fulfilment_parameters: FulfilmentParameters | None = field(default=None)
    sector: str | None = None
    personalisation: Personalisation | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        sign_attrs: list[str] = [
            self.client_request_id,
            self.brand,
        ]

        if self.face_value is not None:
            if self.face_value.currency is not None:
                sign_attrs.append(self.face_value.currency)

            if self.face_value.amount is not None:
                sign_attrs.append(self.face_value.amount)

        non_none_attrs = [attr for attr in sign_attrs if attr is not None]

        return tuple(non_none_attrs)


class OrderDigitalCodeAsyncEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "digital-order-card"
    _route: str = "/api/v2/digital/order-card"


@dataclass(frozen=True)
class CheckDigitalOrderStatusAsyncRequestQuery(SignatureAttributesInterface):
    reference: str | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        return ()


class CheckDigitalOrderStatusAsyncEndpoint(Endpoint):
    _method: str = "GET"
    _endpoint: str = "digital-order-status"
    _route: str = "/api/v2/digital/order-status"
