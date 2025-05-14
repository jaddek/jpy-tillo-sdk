from dataclasses import dataclass

from ...endpoint import QP, AbstractBodyRequest, Endpoint
from ...enums import Currency


class CheckFloatsEndpoint(Endpoint):
    _method: str = "GET"
    _endpoint: str = "check-floats"
    _route: str = "/api/v2/check-floats"

    @dataclass(frozen=True)
    class QueryParams(QP):
        currency: Currency | None = None

        def get_sign_attrs(self) -> tuple[str, ...]:
            return ()

    @property
    def query(self) -> QueryParams | None:
        return self._query


class RequestPaymentTransferEndpoint(Endpoint):
    _method: str = "POST"
    _endpoint: str = "float-request-payment-transfer"
    _route: str = "/api/v2/float/request-payment-transfer"

    @dataclass(frozen=True)
    class RequestBody(AbstractBodyRequest):
        @dataclass(frozen=True)
        class ProformaInvoiceParams:
            company_name: str | None = None
            address_line_1: str | None = None
            address_line_2: str | None = None
            address_line_3: str | None = None
            address_line_4: str | None = None
            city: str | None = None
            post_code: str | None = None
            county: str | None = None
            country: str | None = None

        currency: Currency
        amount: str
        payment_reference: str
        finance_email: str
        proforma_invoice: ProformaInvoiceParams | None = None
        float: str = Currency.UNIVERSAL_FLOAT.value

        def get_sign_attrs(self) -> tuple[str, ...]:
            return ()
