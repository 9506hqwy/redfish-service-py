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
    firmware_time_seconds: float | None = None
    initrd_time_seconds: float | None = None
    kernel_time_seconds: float | None = None
    loader_time_seconds: float | None = None
    user_space_time_seconds: float | None = None


class I2CbusStatistics(RedfishModel):
    bus_error_count: int | None = None
    i2_cbus_name: str | None = Field(alias="I2CBusName", default=None)
    nackcount: int | None = Field(alias="NACKCount", default=None)
    total_transaction_count: int | None = None


class ManagerDiagnosticData(RedfishResource):
    actions: Actions | None = None
    boot_time_statistics: BootTimeStatistics | None = None
    description: str | None = None
    free_storage_space_ki_b: int | None = None
    i2_cbuses: list[I2CbusStatistics] | None = Field(alias="I2CBuses", default=None)
    memory_eccstatistics: MemoryEccstatistics | None = Field(
        alias="MemoryECCStatistics", default=None
    )
    memory_statistics: MemoryStatistics | None = None
    oem: dict[str, Any] | None = None
    processor_statistics: ProcessorStatistics | None = None
    service_root_uptime_seconds: float | None = None
    top_processes: list[ProcessStatistics] | None = None


class MemoryEccstatistics(RedfishModel):
    correctable_eccerror_count: int | None = Field(alias="CorrectableECCErrorCount", default=None)
    uncorrectable_eccerror_count: int | None = Field(
        alias="UncorrectableECCErrorCount", default=None
    )


class MemoryStatistics(RedfishModel):
    available_bytes: int | None = None
    buffers_and_cache_bytes: int | None = None
    free_bytes: int | None = None
    shared_bytes: int | None = None
    total_bytes: int | None = None
    used_bytes: int | None = None


class ProcessStatistics(RedfishModel):
    command_line: str | None = None
    kernel_time_seconds: float | None = None
    resident_set_size_bytes: int | None = None
    restart_after_failure_count: int | None = None
    restart_count: int | None = None
    uptime_seconds: float | None = None
    user_time_seconds: float | None = None


class ProcessorStatistics(RedfishModel):
    kernel_percent: float | None = None
    user_percent: float | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
