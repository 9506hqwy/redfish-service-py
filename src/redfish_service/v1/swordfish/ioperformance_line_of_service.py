from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..swordfish.ioperformance_lo_scapabilities import Ioworkload


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class IoperformanceLineOfService(RedfishResource):
    actions: Actions | None = None
    average_iooperation_latency_microseconds: str | None = None
    description: str | None = None
    iooperations_per_second_is_limited: str | None = None
    ioworkload: Ioworkload | None = None
    max_iooperations_per_second_per_terabyte: str | None = None
    oem: dict[str, Any] | None = None
    sample_period: str | None = None
