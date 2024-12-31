from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .cooling_loop import Coolant
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Location, Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class OemActions(RedfishModel):
    pass


class Reservoir(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    capacity_liters: str | None = None
    coolant: Coolant | None = None
    description: str | None = None
    filters: IdRef | None = None
    fluid_level_percent: str | None = None
    fluid_level_status: str | None = None
    internal_pressurek_pa: str | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    reservoir_type: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    user_label: str | None = None
