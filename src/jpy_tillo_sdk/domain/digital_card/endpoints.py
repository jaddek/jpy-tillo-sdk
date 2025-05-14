from dataclasses import dataclass, field
from typing import Optional, Union

from ...endpoint import QP, AbstractBodyRequest, Endpoint
from .models import FaceValue


class IssueDigitalCodeEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "digital-issue"
    _route: str = "/api/v2/digital/issue"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        @dataclass(frozen=True)
        class Personalisation:
            to_name: Optional[str] = None
            from_name: Optional[str] = None
            message: Optional[str] = None
            template: str = "standard"

        @dataclass(frozen=True)
        class PersonalisationExtended(Personalisation):
            email_message: Optional[str] = None
            redemption_message: Optional[str] = None
            carrier_message: Optional[str] = None

        @dataclass(frozen=True)
        class FulfilmentParameters:
            to_name: Optional[str] = None
            to_email: Optional[str] = None
            from_name: Optional[str] = None
            from_email: Optional[str] = None
            subject: Optional[str] = None

        @dataclass(frozen=True)
        class FulfilmentParametersForRewardPassUsingEmail:
            to_name: Optional[str] = None
            to_email: Optional[str] = None
            from_name: Optional[str] = None
            from_email: Optional[str] = None
            subject: Optional[str] = None
            language: str = "en"
            customer_id: str = ""
            to_first_name: Optional[str] = None
            to_last_name: Optional[str] = None

        @dataclass(frozen=True)
        class FulfilmentParametersForRewardPassUsingUrl:
            to_name: Optional[str] = None
            to_first_name: Optional[str] = None
            to_last_name: Optional[str] = None
            address_1: Optional[str] = None
            address_2: Optional[str] = None
            city: Optional[str] = None
            postal_code: Optional[str] = None
            country: Optional[str] = None
            language: Optional[str] = None
            customer_id: Optional[str] = None

        client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        delivery_method: Optional[str] = None
        fulfilment_by: Optional[str] = None
        fulfilment_parameters: Optional[
            Union[
                FulfilmentParameters,
                FulfilmentParametersForRewardPassUsingEmail,
                FulfilmentParametersForRewardPassUsingUrl,
            ]
        ] = None
        sector: Optional[str] = None
        personalisation: Optional[Union[Personalisation, PersonalisationExtended]] = None

        def get_sign_attrs(self) -> tuple:
            if self.client_request_id and self.brand and self.face_value:
                return (
                    self.client_request_id,
                    self.brand,
                    self.face_value.currency,
                    self.face_value.amount,
                )

            return ()


class TopUpDigitalCodeEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "digital-top-up"
    _route: str = "/api/v2/digital/top-up"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        code: Optional[str] = None
        pin: Optional[str] = None
        sector: Optional[str] = None

        def get_sign_attrs(self) -> tuple:
            if self.client_request_id and self.brand and self.face_value:
                return (
                    self.client_request_id,
                    self.brand,
                    self.face_value.currency,
                    self.face_value.amount,
                )

            return ()


class CheckStockEndpoint(Endpoint):
    _method: str = "GET"
    _endpoint: str = "check-stock"
    _route: str = "/api/v2/check-stock"

    @dataclass(frozen=True)
    class QueryParams(QP):
        brand: str | None = None

        def get_sign_attrs(self) -> tuple:
            return (self.brand,) if self.brand is not None else ()

    @property
    def query(self) -> QueryParams | None:
        return self._query


class CancelDigitalCodeEndpoint(Endpoint):
    _method: str = "DELETE"
    _endpoint: str = "digital-issue"
    _route: str = "/api/v2/digital/issue"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: Optional[str] = None
        original_client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        code: Optional[str] = None
        sector: Optional[str] = None

        def get_sign_attrs(self) -> tuple:
            if self.client_request_id and self.brand and self.face_value:
                return (
                    self.client_request_id,
                    self.brand,
                    self.face_value.currency,
                    self.face_value.amount,
                )

            return ()


class CancelDigitalUrlEndpoint(Endpoint):
    _method: str = "DELETE"
    _endpoint: str = "digital-issue"
    _route: str = "/api/v2/digital/issue"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: Optional[str] = None
        original_client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        url: Optional[str] = None
        sector: Optional[str] = None

        def get_sign_attrs(self) -> tuple:
            if self.client_request_id and self.brand and self.face_value:
                return (
                    self.client_request_id,
                    self.brand,
                    self.face_value.currency,
                    self.face_value.amount,
                )

            return ()


class ReverseDigitalCodeEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "digital-reverse"
    _route: str = "/api/v2/digital/reverse"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: Optional[str] = None
        original_client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        sector: Optional[str] = None

        def get_sign_attrs(self) -> tuple:
            if self.client_request_id and self.brand and self.face_value:
                return (
                    self.client_request_id,
                    self.brand,
                    self.face_value.currency,
                    self.face_value.amount,
                )

            return ()


class CheckBalanceEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "digital-check-balance"
    _route: str = "/api/v2/digital/check-balance"

    @dataclass(frozen=True)
    class QueryParams(QP):
        pass

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        reference: Optional[str] = None

        def get_sign_attrs(self) -> tuple:
            if self.client_request_id and self.brand and self.face_value:
                return (
                    self.client_request_id,
                    self.brand,
                    self.face_value.currency,
                )

            return ()


class OrderDigitalCodeAsyncEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "digital-order-card"
    _route: str = "/api/v2/digital/order-card"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        @dataclass(frozen=True)
        class Personalisation:
            to_name: Optional[str] = None
            from_name: Optional[str] = None
            message: Optional[str] = None
            template: Optional[str] = "standard"
            email_message: Optional[str] = None
            redemption_message: Optional[str] = None
            carrier_message: Optional[str] = None

        @dataclass(frozen=True)
        class FulfilmentParameters:
            to_name: Optional[str] = None
            to_email: Optional[str] = None
            from_name: Optional[str] = None
            from_email: Optional[str] = None
            subject: Optional[str] = None
            language: str = "en"
            customer_id: Optional[str] = ""
            to_first_name: Optional[str] = None
            to_last_name: Optional[str] = None

        client_request_id: Optional[str] = None
        brand: Optional[str] = None
        face_value: Optional[FaceValue] = None
        delivery_method: Optional[str] = None
        fulfilment_by: Optional[str] = None
        fulfilment_parameters: Optional[FulfilmentParameters] = field(default=None)
        sector: Optional[str] = None
        personalisation: Optional[Personalisation] = None

        def get_sign_attrs(self) -> tuple:
            if self.client_request_id and self.brand and self.face_value:
                return (
                    self.client_request_id,
                    self.brand,
                    self.face_value.currency,
                    self.face_value.amount,
                )

            return ()


class CheckDigitalOrderStatusAsyncEndpoint(Endpoint):
    _method: str = "GET"
    _endpoint: str = "digital-order-status"
    _route: str = "/api/v2/digital/order-status"

    @dataclass(frozen=True)
    class QueryParams(QP):
        reference: Optional[str] = None

        def get_sign_attrs(self) -> tuple:
            return ()

    @property
    def query(self) -> QueryParams | None:
        return self._query
