from dataclasses import dataclass


@dataclass(frozen=True)
class FaceValue:
    amount: str | None = None
    currency: str | None = None
