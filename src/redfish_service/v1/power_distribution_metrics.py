from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .sensor import SensorEnergykWhExcerpt, SensorExcerpt, SensorPowerExcerpt


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        alias="#PowerDistributionMetrics.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class PowerDistributionMetrics(RedfishResource):
    absolute_humidity: SensorExcerpt | None = None
    actions: Actions | None = None
    description: str | None = None
    energyk_wh: SensorEnergykWhExcerpt | None = None
    humidity_percent: SensorExcerpt | None = None
    oem: dict[str, Any] | None = None
    power_load_percent: SensorExcerpt | None = None
    power_watts: SensorPowerExcerpt | None = None
    temperature_celsius: SensorExcerpt | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
