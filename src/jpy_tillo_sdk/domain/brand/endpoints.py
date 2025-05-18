from dataclasses import dataclass
from typing import final

from ...contracts import SignatureAttributesInterface
from ...endpoint import Endpoint


@final
@dataclass(frozen=True)
class BrandEndpointRequestQuery(SignatureAttributesInterface):
    detail: bool | None = None
    currency: str | None = None
    country: str | None = None
    brand: str | None = None
    category: str | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        return (self.brand,) if self.brand else ()


class BrandEndpoint(Endpoint):
    _method = "GET"
    _endpoint = "brands"
    _route = "/api/v2/brands"


@final
@dataclass(frozen=True)
class TemplatesListEndpointRequestQuery(SignatureAttributesInterface):
    brand: str | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        return (self.brand,) if self.brand else ()


@final
class TemplatesListEndpoint(Endpoint):
    _method = "GET"
    _endpoint = "templates"
    _route = "/api/v2/templates"


@final
@dataclass(frozen=True)
class DownloadBrandTemplateEndpointRequestQuery(SignatureAttributesInterface):
    brand: str | None = None
    template: str | None = None

    @property
    def sign_attrs(self) -> tuple[str, ...]:
        sign_attrs = []

        if self.brand:
            sign_attrs.append(self.brand)

        return tuple(sign_attrs)


@final
class DownloadBrandTemplateEndpoint(Endpoint):
    _method = "GET"
    _endpoint = "template"
    _route = "/api/v2/template"
