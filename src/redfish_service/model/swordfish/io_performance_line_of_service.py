from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel
from ..swordfish.io_performance_los_capabilities import IoWorkload


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class IoPerformanceLineOfService(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type",
        default="#IOPerformanceLineOfService.v1_1_1.IOPerformanceLineOfService",
    )
    actions: Actions | None = None
    average_io_operation_latency_microseconds: int | None = Field(
        alias="AverageIOOperationLatencyMicroseconds", default=None
    )
    description: str | None = None
    io_operations_per_second_is_limited: bool | None = Field(
        alias="IOOperationsPerSecondIsLimited", default=None
    )
    io_workload: IoWorkload | None = Field(alias="IOWorkload", default=None)
    id: str
    max_io_operations_per_second_per_terabyte: int | None = Field(
        alias="MaxIOOperationsPerSecondPerTerabyte", default=None
    )
    name: str
    oem: dict[str, Any] | None = None
    sample_period: str | None = None


class IoPerformanceLineOfServiceOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(
        alias="@odata.type",
        default="#IOPerformanceLineOfService.v1_1_1.IOPerformanceLineOfService",
    )
    actions: Actions | None = None
    average_io_operation_latency_microseconds: int | None = Field(
        alias="AverageIOOperationLatencyMicroseconds", default=None
    )
    description: str | None = None
    io_operations_per_second_is_limited: bool | None = Field(
        alias="IOOperationsPerSecondIsLimited", default=None
    )
    io_workload: IoWorkload | None = Field(alias="IOWorkload", default=None)
    id: str | None = None
    max_io_operations_per_second_per_terabyte: int | None = Field(
        alias="MaxIOOperationsPerSecondPerTerabyte", default=None
    )
    name: str | None = None
    oem: dict[str, Any] | None = None
    sample_period: str | None = None
