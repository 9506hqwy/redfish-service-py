from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Location, Status


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#PowerSupply.Reset", default=None)
    oem: dict[str, Any] | None = None


class InputRange(RedfishModel):
    capacity_watts: str | None = None
    nominal_voltage_type: str | None = None


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
    nominal_voltage: str | None = None
    physical_context: PhysicalContext | None = None


class PowerSupply(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    certificates: IdRef | None = None
    description: str | None = None
    efficiency_ratings: list[str] | None = None
    electrical_source_manager_uris: list[str] | None = Field(
        alias="ElectricalSourceManagerURIs", default=None
    )
    electrical_source_names: list[str] | None = None
    firmware_version: str | None = None
    hot_pluggable: str | None = None
    input_nominal_voltage_type: str | None = None
    input_ranges: list[InputRange] | None = None
    line_input_status: str | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    manufacturer: str | None = None
    metrics: IdRef | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    output_nominal_voltage_type: str | None = None
    output_rails: list[OutputRail] | None = None
    part_number: str | None = None
    phase_wiring_type: str | None = None
    plug_type: str | None = None
    power_capacity_watts: str | None = None
    power_supply_type: str | None = None
    production_date: str | None = None
    replaceable: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    version: str | None = None


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
