from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        serialization_alias="#ManagerDiagnosticData.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class BootTimeStatistics(RedfishModel):
    firmware_time_seconds: float | None = None
    initrd_time_seconds: float | None = None
    kernel_time_seconds: float | None = None
    loader_time_seconds: float | None = None
    user_space_time_seconds: float | None = None


class I2cBusStatistics(RedfishModel):
    bus_error_count: int | None = None
    i2c_bus_name: str | None = Field(serialization_alias="I2CBusName", default=None)
    nack_count: int | None = Field(serialization_alias="NACKCount", default=None)
    total_transaction_count: int | None = None


class ManagerDiagnosticData(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#ManagerDiagnosticData.v1_2_3.ManagerDiagnosticData",
    )
    actions: Actions | None = None
    boot_time_statistics: BootTimeStatistics | None = None
    description: str | None = None
    free_storage_space_kib: int | None = Field(
        serialization_alias="FreeStorageSpaceKiB", default=None
    )
    i2c_buses: list[I2cBusStatistics] | None = Field(serialization_alias="I2CBuses", default=None)
    id: str
    memory_ecc_statistics: MemoryEccStatistics | None = Field(
        serialization_alias="MemoryECCStatistics", default=None
    )
    memory_statistics: MemoryStatistics | None = None
    name: str
    oem: dict[str, Any] | None = None
    processor_statistics: ProcessorStatistics | None = None
    service_root_uptime_seconds: float | None = None
    top_processes: list[ProcessStatistics] | None = None


class MemoryEccStatistics(RedfishModel):
    correctable_ecc_error_count: int | None = Field(
        serialization_alias="CorrectableECCErrorCount", default=None
    )
    uncorrectable_ecc_error_count: int | None = Field(
        serialization_alias="UncorrectableECCErrorCount", default=None
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
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)
