from __future__ import annotations  # PEP563 Forward References

from typing import Any

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
    oem: OemActions | None = None


class OemActions(RedfishModel):
    pass


class PowerSupplyMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    energyk_wh: str | None = None
    fan_speed_percent: str | None = None
    fan_speeds_percent: list[SensorFanArrayExcerpt] | None = None
    frequency_hz: str | None = None
    input_current_amps: str | None = None
    input_power_watts: str | None = None
    input_voltage: str | None = None
    oem: dict[str, Any] | None = None
    output_power_watts: str | None = None
    rail_current_amps: list[SensorCurrentExcerpt] | None = None
    rail_power_watts: list[SensorPowerExcerpt] | None = None
    rail_voltage: list[SensorVoltageExcerpt] | None = None
    status: Status | None = None
    temperature_celsius: str | None = None


class ResetMetrics(RedfishModel):
    target: str | None = None
    title: str | None = None
