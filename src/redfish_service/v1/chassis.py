from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Location, Status
from .software_inventory import MeasurementBlock


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#Chassis.Reset", default=None)
    oem: dict[str, Any] | None = None


class Chassis(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    certificates: IdRef | None = None
    chassis_type: ChassisType
    controls: IdRef | None = None
    depth_mm: str | None = None
    description: str | None = None
    doors: Doors | None = None
    drives: IdRef | None = None
    electrical_source_manager_uris: list[str] | None = Field(
        alias="ElectricalSourceManagerURIs", default=None
    )
    electrical_source_names: list[str] | None = None
    environment_metrics: IdRef | None = None
    environmental_class: str | None = None
    fabric_adapters: IdRef | None = None
    heating_cooling_equipment_names: list[str] | None = None
    heating_cooling_manager_uris: list[str] | None = Field(
        alias="HeatingCoolingManagerURIs", default=None
    )
    height_mm: str | None = None
    hot_pluggable: str | None = None
    indicator_led: str | None = Field(alias="IndicatorLED", default=None)
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    log_services: IdRef | None = None
    manufacturer: str | None = None
    max_power_watts: str | None = None
    measurements: list[MeasurementBlock] | None = None
    media_controllers: IdRef | None = None
    memory: IdRef | None = None
    memory_domains: IdRef | None = None
    min_power_watts: str | None = None
    model: str | None = None
    network_adapters: IdRef | None = None
    oem: dict[str, Any] | None = None
    pcie_devices: IdRef | None = Field(alias="PCIeDevices", default=None)
    pcie_slots: IdRef | None = Field(alias="PCIeSlots", default=None)
    part_number: str | None = None
    physical_security: PhysicalSecurity | None = None
    power: IdRef | None = None
    power_state: str | None = None
    power_subsystem: IdRef | None = None
    powered_by_parent: str | None = None
    processors: IdRef | None = None
    replaceable: str | None = None
    sku: str | None = Field(alias="SKU", default=None)
    sensors: IdRef | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    thermal: IdRef | None = None
    thermal_direction: str | None = None
    thermal_managed_by_parent: str | None = None
    thermal_subsystem: IdRef | None = None
    trusted_components: IdRef | None = None
    uuid: str | None = Field(alias="UUID", default=None)
    version: str | None = None
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
    IMMERSION_TANK = "ImmersionTank"
    HEAT_EXCHANGER = "HeatExchanger"
    POWER_STRIP = "PowerStrip"
    OTHER = "Other"


class Doors(RedfishModel):
    front: str | None = None
    rear: str | None = None


class Links(RedfishModel):
    cables: list[IdRef] | None = None
    cables_odata_count: int | None = Field(alias="Cables@odata.count", default=None)
    computer_systems: list[IdRef] | None = None
    computer_systems_odata_count: int | None = Field(
        alias="ComputerSystems@odata.count", default=None
    )
    connected_cooling_loops: list[IdRef] | None = None
    connected_cooling_loops_odata_count: int | None = Field(
        alias="ConnectedCoolingLoops@odata.count", default=None
    )
    contained_by: IdRef | None = None
    contains: list[IdRef] | None = None
    contains_odata_count: int | None = Field(alias="Contains@odata.count", default=None)
    cooled_by: list[IdRef] | None = None
    cooled_by_odata_count: int | None = Field(alias="CooledBy@odata.count", default=None)
    cooling_units: list[IdRef] | None = None
    cooling_units_odata_count: int | None = Field(alias="CoolingUnits@odata.count", default=None)
    drives: list[IdRef] | None = None
    drives_odata_count: int | None = Field(alias="Drives@odata.count", default=None)
    facility: IdRef | None = None
    fans: list[IdRef] | None = None
    fans_odata_count: int | None = Field(alias="Fans@odata.count", default=None)
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(alias="ManagedBy@odata.count", default=None)
    managers_in_chassis: list[IdRef] | None = None
    managers_in_chassis_odata_count: int | None = Field(
        alias="ManagersInChassis@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_devices: list[IdRef] | None = Field(alias="PCIeDevices", default=None)
    pcie_devices_odata_count: int | None = Field(alias="PCIeDevices@odata.count", default=None)
    power_distribution: str | None = None
    power_outlets: list[IdRef] | None = None
    power_outlets_odata_count: int | None = Field(alias="PowerOutlets@odata.count", default=None)
    power_supplies: list[IdRef] | None = None
    power_supplies_odata_count: int | None = Field(alias="PowerSupplies@odata.count", default=None)
    powered_by: list[IdRef] | None = None
    powered_by_odata_count: int | None = Field(alias="PoweredBy@odata.count", default=None)
    processors: list[IdRef] | None = None
    processors_odata_count: int | None = Field(alias="Processors@odata.count", default=None)
    resource_blocks: list[IdRef] | None = None
    resource_blocks_odata_count: int | None = Field(
        alias="ResourceBlocks@odata.count", default=None
    )
    storage: list[IdRef] | None = None
    storage_odata_count: int | None = Field(alias="Storage@odata.count", default=None)
    switches: list[IdRef] | None = None
    switches_odata_count: int | None = Field(alias="Switches@odata.count", default=None)


class PhysicalSecurity(RedfishModel):
    intrusion_sensor: str | None = None
    intrusion_sensor_number: str | None = None
    intrusion_sensor_re_arm: str | None = None


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
