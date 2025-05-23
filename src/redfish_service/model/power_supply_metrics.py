from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .resource import Status
from .sensor import (
    SensorCurrentExcerpt,
    SensorEnergykWhExcerpt,
    SensorExcerpt,
    SensorFanArrayExcerpt,
    SensorFanExcerpt,
    SensorPowerExcerpt,
    SensorVoltageExcerpt,
)


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        serialization_alias="#PowerSupplyMetrics.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class PowerSupplyMetrics(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#PowerSupplyMetrics.v1_1_2.PowerSupplyMetrics"
    )
    actions: Actions | None = None
    description: str | None = None
    energyk_wh: SensorEnergykWhExcerpt | None = None
    fan_speed_percent: SensorFanExcerpt | None = None
    fan_speeds_percent: list[SensorFanArrayExcerpt] | None = None
    fan_speeds_percent_odata_count: int | None = Field(
        serialization_alias="FanSpeedsPercent@odata.count", default=None
    )
    frequency_hz: SensorExcerpt | None = None
    id: str
    input_current_amps: SensorCurrentExcerpt | None = None
    input_power_watts: SensorPowerExcerpt | None = None
    input_voltage: SensorVoltageExcerpt | None = None
    name: str
    oem: dict[str, Any] | None = None
    output_power_watts: SensorPowerExcerpt | None = None
    rail_current_amps: list[SensorCurrentExcerpt] | None = None
    rail_current_amps_odata_count: int | None = Field(
        serialization_alias="RailCurrentAmps@odata.count", default=None
    )
    rail_power_watts: list[SensorPowerExcerpt] | None = None
    rail_power_watts_odata_count: int | None = Field(
        serialization_alias="RailPowerWatts@odata.count", default=None
    )
    rail_voltage: list[SensorVoltageExcerpt] | None = None
    rail_voltage_odata_count: int | None = Field(
        serialization_alias="RailVoltage@odata.count", default=None
    )
    status: Status | None = None
    temperature_celsius: SensorExcerpt | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)
