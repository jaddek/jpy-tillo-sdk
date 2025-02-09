from typing import Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class FaceValue:
    amount: Optional[str] = None
    currency: Optional[str] = None
