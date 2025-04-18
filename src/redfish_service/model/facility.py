from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Facility(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Facility.v1_4_2.Facility")
    actions: Actions | None = None
    ambient_metrics: IdRef | None = None
    description: str | None = None
    environment_metrics: IdRef | None = None
    facility_type: FacilityType
    id: str
    links: Links | None = None
    location: Location | None = None
    name: str
    oem: dict[str, Any] | None = None
    power_domains: IdRef | None = None
    status: Status | None = None


class FacilityOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#Facility.v1_4_2.Facility"
    )
    actions: Actions | None = None
    ambient_metrics: IdRef | None = None
    description: str | None = None
    environment_metrics: IdRef | None = None
    facility_type: FacilityType | None = None
    id: str | None = None
    links: Links | None = None
    location: Location | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    power_domains: IdRef | None = None
    status: Status | None = None


class FacilityOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    links: Links | None = None
    location: Location | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class FacilityType(StrEnum):
    ROOM = "Room"
    FLOOR = "Floor"
    BUILDING = "Building"
    SITE = "Site"


class Links(RedfishModel):
    cdus: list[IdRef] | None = Field(serialization_alias="CDUs", default=None)
    cdus_odata_count: int | None = Field(serialization_alias="CDUs@odata.count", default=None)
    contained_by_facility: IdRef | None = None
    contains_chassis: list[IdRef] | None = None
    contains_chassis_odata_count: int | None = Field(
        serialization_alias="ContainsChassis@odata.count", default=None
    )
    contains_facilities: list[IdRef] | None = None
    contains_facilities_odata_count: int | None = Field(
        serialization_alias="ContainsFacilities@odata.count", default=None
    )
    cooling_loops: list[IdRef] | None = None
    cooling_loops_odata_count: int | None = Field(
        serialization_alias="CoolingLoops@odata.count", default=None
    )
    electrical_buses: list[IdRef] | None = None
    electrical_buses_odata_count: int | None = Field(
        serialization_alias="ElectricalBuses@odata.count", default=None
    )
    floor_pd_us: list[IdRef] | None = Field(serialization_alias="FloorPDUs", default=None)
    floor_pd_us_odata_count: int | None = Field(
        serialization_alias="FloorPDUs@odata.count", default=None
    )
    immersion_units: list[IdRef] | None = None
    immersion_units_odata_count: int | None = Field(
        serialization_alias="ImmersionUnits@odata.count", default=None
    )
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(
        serialization_alias="ManagedBy@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    power_shelves: list[IdRef] | None = None
    power_shelves_odata_count: int | None = Field(
        serialization_alias="PowerShelves@odata.count", default=None
    )
    rack_pd_us: list[IdRef] | None = Field(serialization_alias="RackPDUs", default=None)
    rack_pd_us_odata_count: int | None = Field(
        serialization_alias="RackPDUs@odata.count", default=None
    )
    switchgear: list[IdRef] | None = None
    switchgear_odata_count: int | None = Field(
        serialization_alias="Switchgear@odata.count", default=None
    )
    transfer_switches: list[IdRef] | None = None
    transfer_switches_odata_count: int | None = Field(
        serialization_alias="TransferSwitches@odata.count", default=None
    )
