from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .sensor import SensorEnergykWhExcerpt, SensorExcerpt, SensorPowerExcerpt


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        serialization_alias="#PowerDistributionMetrics.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class PowerDistributionMetrics(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#PowerDistributionMetrics.v1_4_0.PowerDistributionMetrics",
    )
    absolute_humidity: SensorExcerpt | None = None
    actions: Actions | None = None
    ambient_temperature_celsius: SensorExcerpt | None = None
    description: str | None = None
    energyk_wh: SensorEnergykWhExcerpt | None = None
    humidity_percent: SensorExcerpt | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    power_load_percent: SensorExcerpt | None = None
    power_watts: SensorPowerExcerpt | None = None
    temperature_celsius: SensorExcerpt | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)
