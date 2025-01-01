from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .resource import Status
from .sensor import SensorCurrentExcerpt, SensorExcerpt, SensorVoltageExcerpt


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class BatteryMetrics(RedfishResource):
    actions: Actions | None = None
    cell_voltages: list[SensorVoltageExcerpt] | None = None
    cell_voltages_odata_count: int | None = Field(alias="CellVoltages@odata.count", default=None)
    charge_percent: SensorExcerpt | None = None
    description: str | None = None
    discharge_cycles: str | None = None
    input_current_amps: SensorCurrentExcerpt | None = None
    input_voltage: SensorVoltageExcerpt | None = None
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
