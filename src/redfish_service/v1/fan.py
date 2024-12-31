from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Fan(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    description: str | None = None
    fan_diameter_mm: str | None = None
    hot_pluggable: str | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    power_watts: str | None = None
    replaceable: str | None = None
    secondary_speed_percent: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    speed_percent: str | None = None
    status: Status | None = None


class Links(RedfishModel):
    cooling_chassis: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
