from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel, RedfishModelOnUpdate
from ..swordfish.io_performance_los_capabilities import IoWorkload


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class IoPerformanceLineOfService(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#IOPerformanceLineOfService.v1_1_1.IOPerformanceLineOfService",
    )
    actions: Actions | None = None
    average_io_operation_latency_microseconds: int | None = Field(
        serialization_alias="AverageIOOperationLatencyMicroseconds", default=None
    )
    description: str | None = None
    io_operations_per_second_is_limited: bool | None = Field(
        serialization_alias="IOOperationsPerSecondIsLimited", default=None
    )
    io_workload: IoWorkload | None = Field(serialization_alias="IOWorkload", default=None)
    id: str
    max_io_operations_per_second_per_terabyte: int | None = Field(
        serialization_alias="MaxIOOperationsPerSecondPerTerabyte", default=None
    )
    name: str
    oem: dict[str, Any] | None = None
    sample_period: str | None = None


class IoPerformanceLineOfServiceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    average_io_operation_latency_microseconds: int | None = Field(
        serialization_alias="AverageIOOperationLatencyMicroseconds", default=None
    )
    io_operations_per_second_is_limited: bool | None = Field(
        serialization_alias="IOOperationsPerSecondIsLimited", default=None
    )
    io_workload: IoWorkload | None = Field(serialization_alias="IOWorkload", default=None)
    max_io_operations_per_second_per_terabyte: int | None = Field(
        serialization_alias="MaxIOOperationsPerSecondPerTerabyte", default=None
    )
    oem: dict[str, Any] | None = None
    sample_period: str | None = None
