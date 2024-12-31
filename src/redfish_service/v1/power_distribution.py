from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .redundancy import RedundantGroup
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    chassis: list[IdRef] | None = None
    facility: IdRef | None = None
    managed_by: list[IdRef] | None = None
    oem: dict[str, Any] | None = None


class PowerDistribution(RedfishResource):
    actions: Actions | None = None
    asset_tag: str | None = None
    branches: IdRef | None = None
    description: str | None = None
    equipment_type: PowerEquipmentType
    feeders: IdRef | None = None
    firmware_version: str | None = None
    links: Links | None = None
    location: Location | None = None
    mains: IdRef | None = None
    mains_redundancy: RedundantGroup | None = None
    manufacturer: str | None = None
    metrics: IdRef | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    outlet_groups: IdRef | None = None
    outlets: IdRef | None = None
    part_number: str | None = None
    power_capacity_va: str | None = None
    power_supplies: IdRef | None = None
    power_supply_redundancy: list[RedundantGroup] | None = None
    production_date: str | None = None
    sensors: IdRef | None = None
    serial_number: str | None = None
    status: Status | None = None
    subfeeds: IdRef | None = None
    transfer_configuration: str | None = None
    transfer_criteria: str | None = None
    uuid: str | None = None
    user_label: str | None = None
    version: str | None = None


class PowerEquipmentType(StrEnum):
    RACK_PDU = "RackPDU"
    FLOOR_PDU = "FloorPDU"
    MANUAL_TRANSFER_SWITCH = "ManualTransferSwitch"
    AUTOMATIC_TRANSFER_SWITCH = "AutomaticTransferSwitch"
    SWITCHGEAR = "Switchgear"
    POWER_SHELF = "PowerShelf"
    BUS = "Bus"
    BATTERY_SHELF = "BatteryShelf"


class TransferControl(RedfishModel):
    target: str | None = None
    title: str | None = None
