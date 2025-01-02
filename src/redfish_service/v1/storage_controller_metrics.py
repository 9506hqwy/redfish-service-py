from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .storage_controller import NvmeSmartCriticalWarnings


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class EgCriticalWarningSummary(RedfishModel):
    namespaces_in_read_only_mode: bool | None = None
    reliability_degraded: bool | None = None
    spare_capacity_under_threshold: bool | None = None


class NvmeSmartMetrics(RedfishModel):
    available_spare_percent: float | None = None
    available_spare_threshold_percent: float | None = None
    composite_temperature_celsius: float | None = None
    controller_busy_time_minutes: int | None = None
    critical_composite_temp_time_minutes: int | None = None
    critical_warnings: NvmeSmartCriticalWarnings | None = None
    data_units_read: int | None = None
    data_units_written: int | None = None
    eg_critical_warning_summary: EgCriticalWarningSummary | None = Field(
        alias="EGCriticalWarningSummary", default=None
    )
    host_read_commands: int | None = None
    host_write_commands: int | None = None
    media_and_data_integrity_errors: int | None = None
    number_of_error_information_log_entries: int | None = None
    percentage_used: float | None = None
    power_cycles: int | None = None
    power_on_hours: float | None = None
    temperature_sensors_celsius: list[float] | None = None
    thermal_mgmt_temp1_total_time_seconds: int | None = None
    thermal_mgmt_temp1_transition_count: int | None = None
    thermal_mgmt_temp2_total_time_seconds: int | None = None
    thermal_mgmt_temp2_transition_count: int | None = None
    unsafe_shutdowns: int | None = None
    warning_composite_temp_time_minutes: int | None = None


class StorageControllerMetrics(RedfishResource):
    actions: Actions | None = None
    correctable_ecc_error_count: int | None = Field(alias="CorrectableECCErrorCount", default=None)
    correctable_parity_error_count: int | None = None
    description: str | None = None
    nvme_smart: NvmeSmartMetrics | None = Field(alias="NVMeSMART", default=None)
    oem: dict[str, Any] | None = None
    state_change_count: int | None = None
    uncorrectable_ecc_error_count: int | None = Field(
        alias="UncorrectableECCErrorCount", default=None
    )
    uncorrectable_parity_error_count: int | None = None
