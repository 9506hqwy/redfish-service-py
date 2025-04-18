from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .sensor import SensorArrayExcerpt, SensorPowerExcerpt


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        serialization_alias="#HeaterMetrics.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class HeaterMetrics(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#HeaterMetrics.v1_0_2.HeaterMetrics"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    power_watts: SensorPowerExcerpt | None = None
    pre_power_on_heating_time_seconds: int | None = None
    runtime_heating_time_seconds: int | None = None
    temperature_readings_celsius: list[SensorArrayExcerpt] | None = None
    temperature_readings_celsius_odata_count: int | None = Field(
        serialization_alias="TemperatureReadingsCelsius@odata.count", default=None
    )


class ResetMetrics(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)
