from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .sensor import SensorArrayExcerpt


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class HeaterSummary(RedfishModel):
    total_pre_power_on_heating_time_seconds: str | None = None
    total_runtime_heating_time_seconds: str | None = None


class ResetMetrics(RedfishModel):
    target: str | None = None
    title: str | None = None


class TemperatureSummary(RedfishModel):
    ambient: str | None = None
    exhaust: str | None = None
    intake: str | None = None
    internal: str | None = None


class ThermalMetrics(RedfishResource):
    actions: Actions | None = None
    air_flow_cubic_meters_per_minute: str | None = None
    delta_pressurek_pa: str | None = None
    description: str | None = None
    energyk_wh: str | None = None
    heater_summary: HeaterSummary | None = None
    oem: dict[str, Any] | None = None
    power_watts: str | None = None
    temperature_readings_celsius: list[SensorArrayExcerpt] | None = None
    temperature_summary_celsius: TemperatureSummary | None = None
