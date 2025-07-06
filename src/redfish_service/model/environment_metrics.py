from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .control import ControlSingleExcerpt
from .sensor import (
    SensorCurrentExcerpt,
    SensorEnergykWhExcerpt,
    SensorExcerpt,
    SensorFanArrayExcerpt,
    SensorPowerExcerpt,
    SensorVoltageExcerpt,
)


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        serialization_alias="#EnvironmentMetrics.ResetMetrics", default=None
    )
    reset_to_defaults: ResetToDefaults | None = Field(
        serialization_alias="#EnvironmentMetrics.ResetToDefaults", default=None
    )
    oem: dict[str, Any] | None = None


class EnvironmentMetrics(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#EnvironmentMetrics.v1_5_0.EnvironmentMetrics"
    )
    absolute_humidity: SensorExcerpt | None = None
    actions: Actions | None = None
    ambient_temperature_celsius: SensorExcerpt | None = None
    current_amps: SensorCurrentExcerpt | None = None
    description: str | None = None
    dew_point_celsius: SensorExcerpt | None = None
    energy_joules: SensorExcerpt | None = None
    energyk_wh: SensorEnergykWhExcerpt | None = None
    fan_speeds_percent: list[SensorFanArrayExcerpt] | None = None
    fan_speeds_percent_odata_count: int | None = Field(
        serialization_alias="FanSpeedsPercent@odata.count", default=None
    )
    humidity_percent: SensorExcerpt | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    power_limit_watts: ControlSingleExcerpt | None = None
    power_load_percent: SensorExcerpt | None = None
    power_watts: SensorPowerExcerpt | None = None
    temperature_celsius: SensorExcerpt | None = None
    voltage: SensorVoltageExcerpt | None = None


class EnvironmentMetricsOnUpdate(RedfishModelOnUpdate):
    absolute_humidity: SensorExcerpt | None = None
    actions: Actions | None = None
    ambient_temperature_celsius: SensorExcerpt | None = None
    current_amps: SensorCurrentExcerpt | None = None
    dew_point_celsius: SensorExcerpt | None = None
    energy_joules: SensorExcerpt | None = None
    energyk_wh: SensorEnergykWhExcerpt | None = None
    fan_speeds_percent: list[SensorFanArrayExcerpt] | None = None
    humidity_percent: SensorExcerpt | None = None
    oem: dict[str, Any] | None = None
    power_limit_watts: ControlSingleExcerpt | None = None
    power_load_percent: SensorExcerpt | None = None
    power_watts: SensorPowerExcerpt | None = None
    temperature_celsius: SensorExcerpt | None = None
    voltage: SensorVoltageExcerpt | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetToDefaults(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)
