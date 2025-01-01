from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    clear_current_period: ClearCurrentPeriod | None = Field(
        alias="#MemoryMetrics.ClearCurrentPeriod", default=None
    )
    oem: dict[str, Any] | None = None


class AlarmTrips(RedfishModel):
    address_parity_error: str | None = None
    correctable_eccerror: str | None = Field(alias="CorrectableECCError", default=None)
    spare_block: str | None = None
    temperature: str | None = None
    uncorrectable_eccerror: str | None = Field(alias="UncorrectableECCError", default=None)


class Cxl(RedfishModel):
    alert_capabilities: str | None = None


class ClearCurrentPeriod(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class CurrentPeriod(RedfishModel):
    blocks_read: str | None = None
    blocks_written: str | None = None
    correctable_eccerror_count: str | None = Field(alias="CorrectableECCErrorCount", default=None)
    indeterminate_correctable_error_count: str | None = None
    indeterminate_uncorrectable_error_count: str | None = None
    uncorrectable_eccerror_count: str | None = Field(
        alias="UncorrectableECCErrorCount", default=None
    )


class HealthData(RedfishModel):
    alarm_trips: AlarmTrips | None = None
    data_loss_detected: str | None = None
    last_shutdown_success: str | None = None
    performance_degraded: str | None = None
    predicted_media_life_left_percent: str | None = None
    remaining_spare_block_percentage: str | None = None


class LifeTime(RedfishModel):
    blocks_read: str | None = None
    blocks_written: str | None = None
    correctable_eccerror_count: str | None = Field(alias="CorrectableECCErrorCount", default=None)
    indeterminate_correctable_error_count: str | None = None
    indeterminate_uncorrectable_error_count: str | None = None
    uncorrectable_eccerror_count: str | None = Field(
        alias="UncorrectableECCErrorCount", default=None
    )


class MemoryMetrics(RedfishResource):
    actions: Actions | None = None
    bandwidth_percent: str | None = None
    block_size_bytes: str | None = None
    cxl: Cxl | None = Field(alias="CXL", default=None)
    capacity_utilization_percent: str | None = None
    corrected_persistent_error_count: str | None = None
    corrected_volatile_error_count: str | None = None
    current_period: CurrentPeriod | None = None
    description: str | None = None
    dirty_shutdown_count: str | None = None
    health_data: HealthData | None = None
    life_time: LifeTime | None = None
    oem: dict[str, Any] | None = None
    operating_speed_mhz: str | None = Field(alias="OperatingSpeedMHz", default=None)
