from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..swordfish.io_performance_los_capabilities import IoWorkload


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class IoPerformanceLineOfService(RedfishResource):
    actions: Actions | None = None
    average_io_operation_latency_microseconds: int | None = Field(
        alias="AverageIOOperationLatencyMicroseconds", default=None
    )
    description: str | None = None
    io_operations_per_second_is_limited: bool | None = Field(
        alias="IOOperationsPerSecondIsLimited", default=None
    )
    io_workload: IoWorkload | None = Field(alias="IOWorkload", default=None)
    max_io_operations_per_second_per_terabyte: int | None = Field(
        alias="MaxIOOperationsPerSecondPerTerabyte", default=None
    )
    oem: dict[str, Any] | None = None
    sample_period: str | None = None
