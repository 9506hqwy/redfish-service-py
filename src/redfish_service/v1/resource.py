from enum import StrEnum
from typing import Any


class Health(StrEnum):
    OK = "OK"
    WARNING = "Warning"
    CRITIAL = "Critical"


Oem = dict[str, Any]
