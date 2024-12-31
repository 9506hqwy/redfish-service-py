from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .physical_context import PhysicalContext
from .resource import Location, Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class Assembly(RedfishResource):
    actions: Actions | None = None
    assemblies: list[AssemblyData] | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None


class AssemblyData(RedfishResource):
    actions: AssemblyDataActions | None = None
    binary_data_uri: str | None = None
    description: str | None = None
    engineering_change_level: str | None = None
    isocountry_code_of_origin: str | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    member_id: str
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    producer: str | None = None
    production_date: str | None = None
    replaceable: str | None = None
    sku: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    vendor: str | None = None
    version: str | None = None


class AssemblyDataActions(RedfishResource):
    oem: AssemblyDataOemActions | None = None


class AssemblyDataOemActions(RedfishResource):
    pass


class OemActions(RedfishResource):
    pass
