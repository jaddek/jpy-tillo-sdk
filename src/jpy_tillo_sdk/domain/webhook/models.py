from dataclasses import dataclass, field
from typing import Union, List, Optional
from .enums import Types


@dataclass(frozen=True)
class Webhook:
    type: Union[str, Types]
    timestamp: str
    certificate: str
    version: int
    data: object


@dataclass(frozen=True)
class Status:
    code: Optional[str] = None
    reason: Optional[str] = None


@dataclass(frozen=True)
class Brand:
    name: Optional[str] = None
    slug: Optional[str] = None
    status: Status = field(default_factory=Status)


@dataclass(frozen=True)
class BrandList:
    brands: List[Brand] = field(default_factory=list)
