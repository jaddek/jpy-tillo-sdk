from dataclasses import dataclass
from typing import Optional

from ...endpoint import QP, Endpoint


class BrandEndpoint(Endpoint):
    _method = "GET"
    _endpoint = "brands"
    _route = "/api/v2/brands"

    @dataclass(frozen=True)
    class QueryParams(QP):
        detail: Optional[bool] = None
        currency: Optional[str] = None
        country: Optional[str] = None
        brand: Optional[str] = None
        category: Optional[str] = None

    @property
    def query(self) -> QueryParams | None:
        return self._query


class TemplateListEndpoint(Endpoint):
    _method = "GET"
    _endpoint = "templates"
    _route = "/api/v2/templates"

    @dataclass(frozen=True)
    class QueryParams(QP):
        brand: Optional[str] = None

        def get_sign_attrs(self) -> tuple:
            return (self.brand,) if self.brand is not None else ()

    @property
    def query(self) -> QueryParams | None:
        return self._query


class TemplateEndpoint(Endpoint):
    _method = "GET"
    _endpoint = "template"
    _route = "/api/v2/template"

    @dataclass(frozen=True)
    class QueryParams(QP):
        brand: Optional[str] = None
        template: Optional[str] = None

        def get_sign_attrs(self) -> tuple:
            return (self.brand,) if self.brand else ()

    @property
    def query(self) -> QueryParams | None:
        return self._query
