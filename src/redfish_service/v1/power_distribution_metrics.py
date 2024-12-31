from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class PowerDistributionMetrics(RedfishResource):
    absolute_humidity: str | None = None
    actions: Actions | None = None
    description: str | None = None
    energyk_wh: str | None = None
    humidity_percent: str | None = None
    oem: dict[str, Any] | None = None
    power_load_percent: str | None = None
    power_watts: str | None = None
    temperature_celsius: str | None = None


class ResetMetrics(RedfishModel):
    target: str | None = None
    title: str | None = None
