import dataclasses
from typing import Optional


@dataclasses.dataclass(frozen=True)
class RequestBody:

    @dataclasses.dataclass(frozen=True)
    class FaceValue1:
        current: str
        fiat: str

    face_value: Optional[FaceValue1] = None


RequestBody(**{})