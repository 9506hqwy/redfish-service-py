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


class Chassis(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    chassis_type: ChassisType
    depth_mm: str | None = None
    description: str | None = None
    environmental_class: str | None = None
    height_mm: str | None = None
    indicator_led: str | None = None
    links: Links | None = None
    location: Location | None = None
    log_services: IdRef | None = None
    manufacturer: str | None = None
    model: str | None = None
    network_adapters: IdRef | None = None
    oem: dict[str, Any] | None = None
    pcie_slots: IdRef | None = None
    part_number: str | None = None
    physical_security: PhysicalSecurity | None = None
    power: IdRef | None = None
    power_state: str | None = None
    sku: str | None = None
    sensors: IdRef | None = None
    serial_number: str | None = None
    status: Status | None = None
    thermal: IdRef | None = None
    uuid: str | None = None
    weight_kg: str | None = None
    width_mm: str | None = None


class ChassisType(StrEnum):
    RACK = "Rack"
    BLADE = "Blade"
    ENCLOSURE = "Enclosure"
    STAND_ALONE = "StandAlone"
    RACK_MOUNT = "RackMount"
    CARD = "Card"
    CARTRIDGE = "Cartridge"
    ROW = "Row"
    POD = "Pod"
    EXPANSION = "Expansion"
    SIDECAR = "Sidecar"
    ZONE = "Zone"
    SLED = "Sled"
    SHELF = "Shelf"
    DRAWER = "Drawer"
    MODULE = "Module"
    COMPONENT = "Component"
    IPBASED_DRIVE = "IPBasedDrive"
    RACK_GROUP = "RackGroup"
    STORAGE_ENCLOSURE = "StorageEnclosure"
    OTHER = "Other"


class Links(RedfishModel):
    computer_systems: list[IdRef] | None = None
    contained_by: IdRef | None = None
    contains: list[IdRef] | None = None
    cooled_by: list[IdRef] | None = None
    drives: list[IdRef] | None = None
    managed_by: list[IdRef] | None = None
    managers_in_chassis: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    pcie_devices: list[IdRef] | None = None
    powered_by: list[IdRef] | None = None
    processors: list[IdRef] | None = None
    resource_blocks: list[IdRef] | None = None
    storage: list[IdRef] | None = None
    switches: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass


class PhysicalSecurity(RedfishModel):
    intrusion_sensor: str | None = None
    intrusion_sensor_number: str | None = None
    intrusion_sensor_re_arm: str | None = None


class Reset(RedfishModel):
    target: str | None = None
    title: str | None = None
