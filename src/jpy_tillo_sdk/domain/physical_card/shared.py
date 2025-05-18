from dataclasses import dataclass

from jpy_tillo_sdk.enums import Currency


@dataclass(frozen=True)
class FaceValue:
    amount: str | None = None
    currency: Currency | None = None
