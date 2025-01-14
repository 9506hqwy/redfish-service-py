from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .sensor import SensorArrayExcerpt, SensorEnergykWhExcerpt, SensorExcerpt, SensorPowerExcerpt


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        serialization_alias="#ThermalMetrics.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class HeaterSummary(RedfishModel):
    total_pre_power_on_heating_time_seconds: int | None = None
    total_runtime_heating_time_seconds: int | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class TemperatureSummary(RedfishModel):
    ambient: SensorExcerpt | None = None
    exhaust: SensorExcerpt | None = None
    intake: SensorExcerpt | None = None
    internal: SensorExcerpt | None = None


class ThermalMetrics(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#ThermalMetrics.v1_3_2.ThermalMetrics"
    )
    actions: Actions | None = None
    air_flow_cubic_meters_per_minute: SensorExcerpt | None = None
    delta_pressurek_pa: SensorExcerpt | None = None
    description: str | None = None
    energyk_wh: SensorEnergykWhExcerpt | None = None
    heater_summary: HeaterSummary | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    power_watts: SensorPowerExcerpt | None = None
    temperature_readings_celsius: list[SensorArrayExcerpt] | None = None
    temperature_readings_celsius_odata_count: int | None = Field(
        serialization_alias="TemperatureReadingsCelsius@odata.count", default=None
    )
    temperature_summary_celsius: TemperatureSummary | None = None
