from dataclasses import dataclass
from typing import Optional

from ...endpoint import Endpoint, QP
from ...enums import Currency


class CheckFloatsEndpoint(Endpoint):
    _method: str = "GET"
    _endpoint: str = "check-floats"
    _route: str = "/api/v2/check-floats"

    @dataclass(frozen=True)
    class QueryParams(QP):
        currency: Optional[Currency] = None

    @property
    def query(self) -> QueryParams|None:
        return self._query