from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource


class Actions(RedfishResource):
    oem: OemActions | None = None


class AlarmTrips(RedfishResource):
    address_parity_error: str | None = None
    correctable_eccerror: str | None = None
    spare_block: str | None = None
    temperature: str | None = None
    uncorrectable_eccerror: str | None = None


class Cxl(RedfishResource):
    alert_capabilities: str | None = None


class ClearCurrentPeriod(RedfishResource):
    target: str | None = None
    title: str | None = None


class CurrentPeriod(RedfishResource):
    blocks_read: str | None = None
    blocks_written: str | None = None
    correctable_eccerror_count: str | None = None
    indeterminate_correctable_error_count: str | None = None
    indeterminate_uncorrectable_error_count: str | None = None
    uncorrectable_eccerror_count: str | None = None


class HealthData(RedfishResource):
    alarm_trips: AlarmTrips | None = None
    data_loss_detected: str | None = None
    last_shutdown_success: str | None = None
    performance_degraded: str | None = None
    predicted_media_life_left_percent: str | None = None
    remaining_spare_block_percentage: str | None = None


class LifeTime(RedfishResource):
    blocks_read: str | None = None
    blocks_written: str | None = None
    correctable_eccerror_count: str | None = None
    indeterminate_correctable_error_count: str | None = None
    indeterminate_uncorrectable_error_count: str | None = None
    uncorrectable_eccerror_count: str | None = None


class MemoryMetrics(RedfishResource):
    actions: Actions | None = None
    bandwidth_percent: str | None = None
    block_size_bytes: str | None = None
    cxl: Cxl | None = None
    capacity_utilization_percent: str | None = None
    corrected_persistent_error_count: str | None = None
    corrected_volatile_error_count: str | None = None
    current_period: CurrentPeriod | None = None
    description: str | None = None
    dirty_shutdown_count: str | None = None
    health_data: HealthData | None = None
    life_time: LifeTime | None = None
    oem: dict[str, Any] | None = None
    operating_speed_mhz: str | None = None


class OemActions(RedfishResource):
    pass
