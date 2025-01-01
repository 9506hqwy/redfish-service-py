from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .sensor import SensorFanArrayExcerpt


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        alias="#EnvironmentMetrics.ResetMetrics", default=None
    )
    reset_to_defaults: ResetToDefaults | None = Field(
        alias="#EnvironmentMetrics.ResetToDefaults", default=None
    )
    oem: dict[str, Any] | None = None


class EnvironmentMetrics(RedfishResource):
    absolute_humidity: str | None = None
    actions: Actions | None = None
    description: str | None = None
    dew_point_celsius: str | None = None
    energy_joules: str | None = None
    energyk_wh: str | None = None
    fan_speeds_percent: list[SensorFanArrayExcerpt] | None = None
    fan_speeds_percent_odata_count: int | None = Field(
        alias="FanSpeedsPercent@odata.count", default=None
    )
    humidity_percent: str | None = None
    oem: dict[str, Any] | None = None
    power_limit_watts: str | None = None
    power_load_percent: str | None = None
    power_watts: str | None = None
    temperature_celsius: str | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ResetToDefaults(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
