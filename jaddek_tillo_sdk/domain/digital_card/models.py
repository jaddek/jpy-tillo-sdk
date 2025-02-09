from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class FaceValue:
    amount: Optional[str] = None
    currency: Optional[str] = None
