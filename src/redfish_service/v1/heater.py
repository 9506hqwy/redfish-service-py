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
    oem: OemActions | None = None


class Heater(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    description: str | None = None
    hot_pluggable: str | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    manufacturer: str | None = None
    metrics: IdRef | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None


class Links(RedfishModel):
    managers: list[IdRef] | None = None
    memory: list[IdRef] | None = None
    network_adapters: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    processors: list[IdRef] | None = None
    storage_controllers: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass
