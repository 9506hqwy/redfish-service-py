from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Facility(RedfishResource):
    actions: Actions | None = None
    ambient_metrics: IdRef | None = None
    description: str | None = None
    environment_metrics: IdRef | None = None
    facility_type: FacilityType
    links: Links | None = None
    location: Location | None = None
    oem: dict[str, Any] | None = None
    power_domains: IdRef | None = None
    status: Status | None = None


class FacilityType(StrEnum):
    ROOM = "Room"
    FLOOR = "Floor"
    BUILDING = "Building"
    SITE = "Site"


class Links(RedfishModel):
    cdus: list[IdRef] | None = Field(alias="CDUs", default=None)
    cdus_odata_count: int | None = Field(alias="CDUs@odata.count", default=None)
    contained_by_facility: IdRef | None = None
    contains_chassis: list[IdRef] | None = None
    contains_chassis_odata_count: int | None = Field(
        alias="ContainsChassis@odata.count", default=None
    )
    contains_facilities: list[IdRef] | None = None
    contains_facilities_odata_count: int | None = Field(
        alias="ContainsFacilities@odata.count", default=None
    )
    cooling_loops: list[IdRef] | None = None
    cooling_loops_odata_count: int | None = Field(alias="CoolingLoops@odata.count", default=None)
    electrical_buses: list[IdRef] | None = None
    electrical_buses_odata_count: int | None = Field(
        alias="ElectricalBuses@odata.count", default=None
    )
    floor_pdus: list[IdRef] | None = Field(alias="FloorPDUs", default=None)
    floor_pdus_odata_count: int | None = Field(alias="FloorPDUs@odata.count", default=None)
    immersion_units: list[IdRef] | None = None
    immersion_units_odata_count: int | None = Field(
        alias="ImmersionUnits@odata.count", default=None
    )
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(alias="ManagedBy@odata.count", default=None)
    oem: dict[str, Any] | None = None
    power_shelves: list[IdRef] | None = None
    power_shelves_odata_count: int | None = Field(alias="PowerShelves@odata.count", default=None)
    rack_pdus: list[IdRef] | None = Field(alias="RackPDUs", default=None)
    rack_pdus_odata_count: int | None = Field(alias="RackPDUs@odata.count", default=None)
    switchgear: list[IdRef] | None = None
    switchgear_odata_count: int | None = Field(alias="Switchgear@odata.count", default=None)
    transfer_switches: list[IdRef] | None = None
    transfer_switches_odata_count: int | None = Field(
        alias="TransferSwitches@odata.count", default=None
    )
