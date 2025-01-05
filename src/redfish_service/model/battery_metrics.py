from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .resource import Status
from .sensor import SensorCurrentExcerpt, SensorExcerpt, SensorVoltageExcerpt


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class BatteryMetrics(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#BatteryMetrics.v1_0_4.BatteryMetrics")
    actions: Actions | None = None
    cell_voltages: list[SensorVoltageExcerpt] | None = None
    cell_voltages_odata_count: int | None = Field(alias="CellVoltages@odata.count", default=None)
    charge_percent: SensorExcerpt | None = None
    description: str | None = None
    discharge_cycles: float | None = None
    id: str
    input_current_amps: SensorCurrentExcerpt | None = None
    input_voltage: SensorVoltageExcerpt | None = None
    name: str
    oem: dict[str, Any] | None = None
    output_current_amps: list[SensorCurrentExcerpt] | None = None
    output_current_amps_odata_count: int | None = Field(
        alias="OutputCurrentAmps@odata.count", default=None
    )
    output_voltages: list[SensorVoltageExcerpt] | None = None
    output_voltages_odata_count: int | None = Field(
        alias="OutputVoltages@odata.count", default=None
    )
    status: Status | None = None
    stored_charge_amp_hours: SensorExcerpt | None = None
    stored_energy_watt_hours: SensorExcerpt | None = None
    temperature_celsius: SensorExcerpt | None = None
