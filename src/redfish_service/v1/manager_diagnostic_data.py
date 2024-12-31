from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource


class Actions(RedfishResource):
    oem: OemActions | None = None


class BootTimeStatistics(RedfishResource):
    firmware_time_seconds: str | None = None
    initrd_time_seconds: str | None = None
    kernel_time_seconds: str | None = None
    loader_time_seconds: str | None = None
    user_space_time_seconds: str | None = None


class I2CbusStatistics(RedfishResource):
    bus_error_count: str | None = None
    i2_cbus_name: str | None = None
    nackcount: str | None = None
    total_transaction_count: str | None = None


class ManagerDiagnosticData(RedfishResource):
    actions: Actions | None = None
    boot_time_statistics: BootTimeStatistics | None = None
    description: str | None = None
    free_storage_space_ki_b: str | None = None
    i2_cbuses: list[I2CbusStatistics] | None = None
    memory_eccstatistics: MemoryEccstatistics | None = None
    memory_statistics: MemoryStatistics | None = None
    oem: dict[str, Any] | None = None
    processor_statistics: ProcessorStatistics | None = None
    service_root_uptime_seconds: str | None = None
    top_processes: list[str] | None = None


class MemoryEccstatistics(RedfishResource):
    correctable_eccerror_count: str | None = None
    uncorrectable_eccerror_count: str | None = None


class MemoryStatistics(RedfishResource):
    available_bytes: str | None = None
    buffers_and_cache_bytes: str | None = None
    free_bytes: str | None = None
    shared_bytes: str | None = None
    total_bytes: str | None = None
    used_bytes: str | None = None


class OemActions(RedfishResource):
    pass


class ProcessorStatistics(RedfishResource):
    kernel_percent: str | None = None
    user_percent: str | None = None


class ResetMetrics(RedfishResource):
    target: str | None = None
    title: str | None = None
