from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .sensor import SensorFanArrayExcerpt


class Actions(RedfishModel):
    oem: OemActions | None = None


class EnvironmentMetrics(RedfishResource):
    absolute_humidity: str | None = None
    actions: Actions | None = None
    description: str | None = None
    dew_point_celsius: str | None = None
    energy_joules: str | None = None
    energyk_wh: str | None = None
    fan_speeds_percent: list[SensorFanArrayExcerpt] | None = None
    humidity_percent: str | None = None
    oem: dict[str, Any] | None = None
    power_limit_watts: str | None = None
    power_load_percent: str | None = None
    power_watts: str | None = None
    temperature_celsius: str | None = None


class OemActions(RedfishModel):
    pass


class ResetMetrics(RedfishModel):
    target: str | None = None
    title: str | None = None


class ResetToDefaults(RedfishModel):
    target: str | None = None
    title: str | None = None
