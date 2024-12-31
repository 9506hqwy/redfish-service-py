from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .storage_controller import NvmeSmartcriticalWarnings


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class EgcriticalWarningSummary(RedfishModel):
    namespaces_in_read_only_mode: str | None = None
    reliability_degraded: str | None = None
    spare_capacity_under_threshold: str | None = None


class NvmeSmartmetrics(RedfishModel):
    available_spare_percent: str | None = None
    available_spare_threshold_percent: str | None = None
    composite_temperature_celsius: str | None = None
    controller_busy_time_minutes: str | None = None
    critical_composite_temp_time_minutes: str | None = None
    critical_warnings: NvmeSmartcriticalWarnings | None = None
    data_units_read: str | None = None
    data_units_written: str | None = None
    egcritical_warning_summary: EgcriticalWarningSummary | None = None
    host_read_commands: str | None = None
    host_write_commands: str | None = None
    media_and_data_integrity_errors: str | None = None
    number_of_error_information_log_entries: str | None = None
    percentage_used: str | None = None
    power_cycles: str | None = None
    power_on_hours: str | None = None
    temperature_sensors_celsius: list[str] | None = None
    thermal_mgmt_temp1_total_time_seconds: str | None = None
    thermal_mgmt_temp1_transition_count: str | None = None
    thermal_mgmt_temp2_total_time_seconds: str | None = None
    thermal_mgmt_temp2_transition_count: str | None = None
    unsafe_shutdowns: str | None = None
    warning_composite_temp_time_minutes: str | None = None


class StorageControllerMetrics(RedfishResource):
    actions: Actions | None = None
    correctable_eccerror_count: str | None = None
    correctable_parity_error_count: str | None = None
    description: str | None = None
    nvme_smart: NvmeSmartmetrics | None = None
    oem: dict[str, Any] | None = None
    state_change_count: str | None = None
    uncorrectable_eccerror_count: str | None = None
    uncorrectable_parity_error_count: str | None = None
