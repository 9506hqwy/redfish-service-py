from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .circuit import NominalVoltageType, PhaseWiringType, PlugType
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Location, Status


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#PowerSupply.Reset", default=None)
    oem: dict[str, Any] | None = None


class EfficiencyRating(RedfishModel):
    efficiency_percent: float | None = None
    load_percent: float | None = None


class InputRange(RedfishModel):
    capacity_watts: float | None = None
    nominal_voltage_type: NominalVoltageType | None = None


class LineStatus(StrEnum):
    NORMAL = "Normal"
    LOSS_OF_INPUT = "LossOfInput"
    OUT_OF_RANGE = "OutOfRange"


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    outlet: IdRef | None = None
    power_outlets: list[IdRef] | None = None
    power_outlets_odata_count: int | None = Field(alias="PowerOutlets@odata.count", default=None)
    powering_chassis: list[IdRef] | None = None
    powering_chassis_odata_count: int | None = Field(
        alias="PoweringChassis@odata.count", default=None
    )


class OutputRail(RedfishModel):
    nominal_voltage: float | None = None
    physical_context: PhysicalContext | None = None


class PowerSupply(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    certificates: IdRef | None = None
    description: str | None = None
    efficiency_ratings: list[EfficiencyRating] | None = None
    electrical_source_manager_ur_is: list[str] | None = Field(
        alias="ElectricalSourceManagerURIs", default=None
    )
    electrical_source_names: list[str] | None = None
    firmware_version: str | None = None
    hot_pluggable: bool | None = None
    input_nominal_voltage_type: NominalVoltageType | None = None
    input_ranges: list[InputRange] | None = None
    line_input_status: LineStatus | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    metrics: IdRef | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    output_nominal_voltage_type: NominalVoltageType | None = None
    output_rails: list[OutputRail] | None = None
    part_number: str | None = None
    phase_wiring_type: PhaseWiringType | None = None
    plug_type: PlugType | None = None
    power_capacity_watts: float | None = None
    power_supply_type: PowerSupplyType | None = None
    production_date: str | None = None
    replaceable: bool | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    version: str | None = None


class PowerSupplyType(StrEnum):
    AC = "AC"
    DC = "DC"
    A_COR_DC = "ACorDC"
    DC_REGULATOR = "DCRegulator"


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
