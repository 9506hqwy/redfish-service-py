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
    address_parity_error: bool | None = None
    correctable_eccerror: bool | None = Field(alias="CorrectableECCError", default=None)
    spare_block: bool | None = None
    temperature: bool | None = None
    uncorrectable_eccerror: bool | None = Field(alias="UncorrectableECCError", default=None)


class AlertCapabilities(RedfishModel):
    correctable_eccerror: bool | None = Field(alias="CorrectableECCError", default=None)
    spare_block: bool | None = None
    temperature: bool | None = None
    uncorrectable_eccerror: bool | None = Field(alias="UncorrectableECCError", default=None)


class Cxl(RedfishModel):
    alert_capabilities: AlertCapabilities | None = None


class ClearCurrentPeriod(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class CurrentPeriod(RedfishModel):
    blocks_read: int | None = None
    blocks_written: int | None = None
    correctable_eccerror_count: int | None = Field(alias="CorrectableECCErrorCount", default=None)
    indeterminate_correctable_error_count: int | None = None
    indeterminate_uncorrectable_error_count: int | None = None
    uncorrectable_eccerror_count: int | None = Field(
        alias="UncorrectableECCErrorCount", default=None
    )


class HealthData(RedfishModel):
    alarm_trips: AlarmTrips | None = None
    data_loss_detected: bool | None = None
    last_shutdown_success: bool | None = None
    performance_degraded: bool | None = None
    predicted_media_life_left_percent: float | None = None
    remaining_spare_block_percentage: float | None = None


class LifeTime(RedfishModel):
    blocks_read: int | None = None
    blocks_written: int | None = None
    correctable_eccerror_count: int | None = Field(alias="CorrectableECCErrorCount", default=None)
    indeterminate_correctable_error_count: int | None = None
    indeterminate_uncorrectable_error_count: int | None = None
    uncorrectable_eccerror_count: int | None = Field(
        alias="UncorrectableECCErrorCount", default=None
    )


class MemoryMetrics(RedfishResource):
    actions: Actions | None = None
    bandwidth_percent: float | None = None
    block_size_bytes: int | None = None
    cxl: Cxl | None = Field(alias="CXL", default=None)
    capacity_utilization_percent: float | None = None
    corrected_persistent_error_count: int | None = None
    corrected_volatile_error_count: int | None = None
    current_period: CurrentPeriod | None = None
    description: str | None = None
    dirty_shutdown_count: int | None = None
    health_data: HealthData | None = None
    life_time: LifeTime | None = None
    oem: dict[str, Any] | None = None
    operating_speed_mhz: int | None = Field(alias="OperatingSpeedMHz", default=None)
