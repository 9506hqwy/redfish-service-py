from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import RedfishResource
from .cooling_loop import Coolant
from .odata_v4 import IdRef
from .redundancy import RedundantGroup
from .resource import Location, Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class CoolingEquipmentType(StrEnum):
    CDU = "CDU"
    HEAT_EXCHANGER = "HeatExchanger"
    IMMERSION_UNIT = "ImmersionUnit"


class CoolingUnit(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    coolant: Coolant | None = None
    coolant_connector_redundancy: list[RedundantGroup] | None = None
    cooling_capacity_watts: str | None = None
    description: str | None = None
    environment_metrics: IdRef | None = None
    equipment_type: CoolingEquipmentType
    filter_redundancy: list[RedundantGroup] | None = None
    filters: IdRef | None = None
    firmware_version: str | None = None
    leak_detection: IdRef | None = None
    links: Links | None = None
    location: Location | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    primary_coolant_connectors: IdRef | None = None
    production_date: str | None = None
    pump_redundancy: list[RedundantGroup] | None = None
    pumps: IdRef | None = None
    reservoirs: IdRef | None = None
    secondary_coolant_connectors: IdRef | None = None
    serial_number: str | None = None
    status: Status | None = None
    user_label: str | None = None
    version: str | None = None


class Links(RedfishResource):
    chassis: list[IdRef] | None = None
    facility: IdRef | None = None
    managed_by: list[IdRef] | None = None
    oem: dict[str, Any] | None = None


class OemActions(RedfishResource):
    pass
