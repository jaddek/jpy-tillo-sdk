from dataclasses import dataclass
from typing import Optional

from ...endpoint import QP, AbstractBodyRequest, Endpoint
from ...enums import Currency


class CheckFloatsEndpoint(Endpoint):
    _method: str = "GET"
    _endpoint: str = "check-floats"
    _route: str = "/api/v2/check-floats"

    @dataclass(frozen=True)
    class QueryParams(QP):
        currency: Optional[Currency] = None

        def get_sign_attrs(self) -> tuple:
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
            company_name: Optional[str] = (None,)
            address_line_1: Optional[str] = (None,)
            address_line_2: Optional[str] = (None,)
            address_line_3: Optional[str] = (None,)
            address_line_4: Optional[str] = (None,)
            city: Optional[str] = (None,)
            post_code: Optional[str] = (None,)
            county: Optional[str] = (None,)
            country: Optional[str] = (None,)

        currency: Currency
        amount: str
        payment_reference: str
        finance_email: str
        proforma_invoice: Optional[ProformaInvoiceParams] = None
        float: str = Currency.UNIVERSAL_FLOAT.value

        def get_sign_attrs(self) -> tuple:
            return ()
