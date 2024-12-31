from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Location, Status


class Actions(RedfishModel):
    oem: OemActions | None = None


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
    cdus: list[IdRef] | None = None
    contained_by_facility: IdRef | None = None
    contains_chassis: list[IdRef] | None = None
    contains_facilities: list[IdRef] | None = None
    cooling_loops: list[IdRef] | None = None
    electrical_buses: list[IdRef] | None = None
    floor_pdus: list[IdRef] | None = None
    immersion_units: list[IdRef] | None = None
    managed_by: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    power_shelves: list[IdRef] | None = None
    rack_pdus: list[IdRef] | None = None
    switchgear: list[IdRef] | None = None
    transfer_switches: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass
