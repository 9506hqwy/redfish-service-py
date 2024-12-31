from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class IoconnectivityLineOfService(RedfishResource):
    access_protocols: list[str] | None = None
    actions: Actions | None = None
    description: str | None = None
    max_bytes_per_second: str | None = None
    max_iops: str | None = None
    oem: dict[str, Any] | None = None
