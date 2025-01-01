from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .sensor import SensorArrayExcerpt, SensorPowerExcerpt


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(alias="#HeaterMetrics.ResetMetrics", default=None)
    oem: dict[str, Any] | None = None


class HeaterMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    power_watts: SensorPowerExcerpt | None = None
    pre_power_on_heating_time_seconds: int | None = None
    runtime_heating_time_seconds: int | None = None
    temperature_readings_celsius: list[SensorArrayExcerpt] | None = None
    temperature_readings_celsius_odata_count: int | None = Field(
        alias="TemperatureReadingsCelsius@odata.count", default=None
    )


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
