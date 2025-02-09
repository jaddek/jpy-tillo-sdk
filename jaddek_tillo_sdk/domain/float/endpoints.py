from dataclasses import dataclass
from typing import Optional

from ...endpoint import Endpoint, QP


class CheckFloatsEndpoint(Endpoint):
    _method: str = "GET"
    _endpoint: str = "check-floats"
    _route: str = "/api/v2/check-floats"

    @dataclass(frozen=True)
    class QueryParams(QP):
        currency: Optional[str] = None
        template: Optional[str] = None