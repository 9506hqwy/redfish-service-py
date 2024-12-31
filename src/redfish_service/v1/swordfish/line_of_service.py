from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishResource,
)


class LineOfService(RedfishResource):
    description: str | None = None
    oem: dict[str, Any] | None = None
