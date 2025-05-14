from dataclasses import dataclass

from ...endpoint import QP, Endpoint


class BrandEndpoint(Endpoint):
    _method = "GET"
    _endpoint = "brands"
    _route = "/api/v2/brands"

    @dataclass(frozen=True)
    class QueryParams(QP):
        detail: bool | None = None
        currency: str | None = None
        country: str | None = None
        brand: str | None = None
        category: str | None = None

    @property
    def query(self) -> QueryParams | None:
        return self._query


class TemplateListEndpoint(Endpoint):
    _method = "GET"
    _endpoint = "templates"
    _route = "/api/v2/templates"

    @dataclass(frozen=True)
    class QueryParams(QP):
        brand: str | None = None

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
        brand: str | None = None
        template: str | None = None

        def get_sign_attrs(self) -> tuple:
            return (self.brand,) if self.brand else ()

    @property
    def query(self) -> QueryParams | None:
        return self._query
