from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .sensor import SensorArrayExcerpt


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class HeaterMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    power_watts: str | None = None
    pre_power_on_heating_time_seconds: str | None = None
    runtime_heating_time_seconds: str | None = None
    temperature_readings_celsius: list[SensorArrayExcerpt] | None = None


class ResetMetrics(RedfishModel):
    target: str | None = None
    title: str | None = None
