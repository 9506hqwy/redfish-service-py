from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Location, Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class OemActions(RedfishResource):
    pass


class Pump(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    description: str | None = None
    filters: IdRef | None = None
    firmware_version: str | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    production_date: str | None = None
    pump_speed_percent: str | None = None
    pump_type: str | None = None
    serial_number: str | None = None
    service_hours: str | None = None
    spare_part_number: str | None = None
    speed_control_percent: str | None = None
    status: Status | None = None
    user_label: str | None = None
    version: str | None = None
