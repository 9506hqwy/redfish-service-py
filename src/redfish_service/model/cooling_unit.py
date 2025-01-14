from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .cooling_loop import Coolant
from .odata_v4 import IdRef
from .redundancy import RedundantGroup
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CoolingEquipmentType(StrEnum):
    CDU = "CDU"
    HEAT_EXCHANGER = "HeatExchanger"
    IMMERSION_UNIT = "ImmersionUnit"


class CoolingUnit(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#CoolingUnit.v1_1_2.CoolingUnit")
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    coolant: Coolant | None = None
    coolant_connector_redundancy: list[RedundantGroup] | None = None
    cooling_capacity_watts: int | None = None
    description: str | None = None
    environment_metrics: IdRef | None = None
    equipment_type: CoolingEquipmentType
    filter_redundancy: list[RedundantGroup] | None = None
    filters: IdRef | None = None
    firmware_version: str | None = None
    id: str
    leak_detection: IdRef | None = None
    links: Links | None = None
    location: Location | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str
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


class CoolingUnitOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    asset_tag: str | None = None
    coolant: Coolant | None = None
    coolant_connector_redundancy: list[RedundantGroup] | None = None
    filter_redundancy: list[RedundantGroup] | None = None
    links: Links | None = None
    location: Location | None = None
    oem: dict[str, Any] | None = None
    pump_redundancy: list[RedundantGroup] | None = None
    status: Status | None = None
    user_label: str | None = None


class Links(RedfishModel):
    chassis: list[IdRef] | None = None
    chassis_odata_count: int | None = Field(alias="Chassis@odata.count", default=None)
    facility: IdRef | None = None
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(alias="ManagedBy@odata.count", default=None)
    oem: dict[str, Any] | None = None
