from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        alias="#ManagerDiagnosticData.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class BootTimeStatistics(RedfishModel):
    firmware_time_seconds: str | None = None
    initrd_time_seconds: str | None = None
    kernel_time_seconds: str | None = None
    loader_time_seconds: str | None = None
    user_space_time_seconds: str | None = None


class I2CbusStatistics(RedfishModel):
    bus_error_count: str | None = None
    i2_cbus_name: str | None = Field(alias="I2CBusName", default=None)
    nackcount: str | None = Field(alias="NACKCount", default=None)
    total_transaction_count: str | None = None


class ManagerDiagnosticData(RedfishResource):
    actions: Actions | None = None
    boot_time_statistics: BootTimeStatistics | None = None
    description: str | None = None
    free_storage_space_ki_b: str | None = None
    i2_cbuses: list[I2CbusStatistics] | None = Field(alias="I2CBuses", default=None)
    memory_eccstatistics: MemoryEccstatistics | None = Field(
        alias="MemoryECCStatistics", default=None
    )
    memory_statistics: MemoryStatistics | None = None
    oem: dict[str, Any] | None = None
    processor_statistics: ProcessorStatistics | None = None
    service_root_uptime_seconds: str | None = None
    top_processes: list[str] | None = None


class MemoryEccstatistics(RedfishModel):
    correctable_eccerror_count: str | None = Field(alias="CorrectableECCErrorCount", default=None)
    uncorrectable_eccerror_count: str | None = Field(
        alias="UncorrectableECCErrorCount", default=None
    )


class MemoryStatistics(RedfishModel):
    available_bytes: str | None = None
    buffers_and_cache_bytes: str | None = None
    free_bytes: str | None = None
    shared_bytes: str | None = None
    total_bytes: str | None = None
    used_bytes: str | None = None


class ProcessorStatistics(RedfishModel):
    kernel_percent: str | None = None
    user_percent: str | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
