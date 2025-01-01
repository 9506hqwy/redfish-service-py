from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .resource import Status
from .sensor import (
    SensorCurrentExcerpt,
    SensorFanArrayExcerpt,
    SensorPowerExcerpt,
    SensorVoltageExcerpt,
)


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        alias="#PowerSupplyMetrics.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class PowerSupplyMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    energyk_wh: str | None = None
    fan_speed_percent: str | None = None
    fan_speeds_percent: list[SensorFanArrayExcerpt] | None = None
    fan_speeds_percent_odata_count: int | None = Field(
        alias="FanSpeedsPercent@odata.count", default=None
    )
    frequency_hz: str | None = None
    input_current_amps: str | None = None
    input_power_watts: str | None = None
    input_voltage: str | None = None
    oem: dict[str, Any] | None = None
    output_power_watts: str | None = None
    rail_current_amps: list[SensorCurrentExcerpt] | None = None
    rail_current_amps_odata_count: int | None = Field(
        alias="RailCurrentAmps@odata.count", default=None
    )
    rail_power_watts: list[SensorPowerExcerpt] | None = None
    rail_power_watts_odata_count: int | None = Field(
        alias="RailPowerWatts@odata.count", default=None
    )
    rail_voltage: list[SensorVoltageExcerpt] | None = None
    rail_voltage_odata_count: int | None = Field(alias="RailVoltage@odata.count", default=None)
    status: Status | None = None
    temperature_celsius: str | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
