from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Location, PowerState, ResetType, Status
from .software_inventory import MeasurementBlock


class Actions(RedfishModel):
    reset: Reset | None = Field(serialization_alias="#Chassis.Reset", default=None)
    oem: dict[str, Any] | None = None


class Chassis(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Chassis.v1_25_2.Chassis")
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    certificates: IdRef | None = None
    chassis_type: ChassisType
    controls: IdRef | None = None
    depth_mm: float | None = None
    description: str | None = None
    doors: Doors | None = None
    drives: IdRef | None = None
    electrical_source_manager_ur_is: list[str] | None = Field(
        serialization_alias="ElectricalSourceManagerURIs", default=None
    )
    electrical_source_names: list[str] | None = None
    environment_metrics: IdRef | None = None
    environmental_class: EnvironmentalClass | None = None
    fabric_adapters: IdRef | None = None
    heating_cooling_equipment_names: list[str] | None = None
    heating_cooling_manager_ur_is: list[str] | None = Field(
        serialization_alias="HeatingCoolingManagerURIs", default=None
    )
    height_mm: float | None = None
    hot_pluggable: bool | None = None
    id: str
    indicator_led: IndicatorLed | None = Field(serialization_alias="IndicatorLED", default=None)
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    log_services: IdRef | None = None
    manufacturer: str | None = None
    max_power_watts: float | None = None
    measurements: list[MeasurementBlock] | None = None
    media_controllers: IdRef | None = None
    memory: IdRef | None = None
    memory_domains: IdRef | None = None
    min_power_watts: float | None = None
    model: str | None = None
    name: str
    network_adapters: IdRef | None = None
    oem: dict[str, Any] | None = None
    pcie_devices: IdRef | None = Field(serialization_alias="PCIeDevices", default=None)
    pcie_slots: IdRef | None = Field(serialization_alias="PCIeSlots", default=None)
    part_number: str | None = None
    physical_security: PhysicalSecurity | None = None
    power: IdRef | None = None
    power_state: PowerState | None = None
    power_subsystem: IdRef | None = None
    powered_by_parent: bool | None = None
    processors: IdRef | None = None
    replaceable: bool | None = None
    sku: str | None = Field(serialization_alias="SKU", default=None)
    sensors: IdRef | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    thermal: IdRef | None = None
    thermal_direction: ThermalDirection | None = None
    thermal_managed_by_parent: bool | None = None
    thermal_subsystem: IdRef | None = None
    trusted_components: IdRef | None = None
    uuid: str | None = Field(serialization_alias="UUID", default=None)
    version: str | None = None
    weight_kg: float | None = None
    width_mm: float | None = None


class ChassisOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#Chassis.v1_25_2.Chassis"
    )
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    certificates: IdRef | None = None
    chassis_type: ChassisType | None = None
    controls: IdRef | None = None
    depth_mm: float | None = None
    description: str | None = None
    doors: Doors | None = None
    drives: IdRef | None = None
    electrical_source_manager_ur_is: list[str] | None = Field(
        serialization_alias="ElectricalSourceManagerURIs", default=None
    )
    electrical_source_names: list[str] | None = None
    environment_metrics: IdRef | None = None
    environmental_class: EnvironmentalClass | None = None
    fabric_adapters: IdRef | None = None
    heating_cooling_equipment_names: list[str] | None = None
    heating_cooling_manager_ur_is: list[str] | None = Field(
        serialization_alias="HeatingCoolingManagerURIs", default=None
    )
    height_mm: float | None = None
    hot_pluggable: bool | None = None
    id: str | None = None
    indicator_led: IndicatorLed | None = Field(serialization_alias="IndicatorLED", default=None)
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    log_services: IdRef | None = None
    manufacturer: str | None = None
    max_power_watts: float | None = None
    measurements: list[MeasurementBlock] | None = None
    media_controllers: IdRef | None = None
    memory: IdRef | None = None
    memory_domains: IdRef | None = None
    min_power_watts: float | None = None
    model: str | None = None
    name: str | None = None
    network_adapters: IdRef | None = None
    oem: dict[str, Any] | None = None
    pcie_devices: IdRef | None = Field(serialization_alias="PCIeDevices", default=None)
    pcie_slots: IdRef | None = Field(serialization_alias="PCIeSlots", default=None)
    part_number: str | None = None
    physical_security: PhysicalSecurity | None = None
    power: IdRef | None = None
    power_state: PowerState | None = None
    power_subsystem: IdRef | None = None
    powered_by_parent: bool | None = None
    processors: IdRef | None = None
    replaceable: bool | None = None
    sku: str | None = Field(serialization_alias="SKU", default=None)
    sensors: IdRef | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    thermal: IdRef | None = None
    thermal_direction: ThermalDirection | None = None
    thermal_managed_by_parent: bool | None = None
    thermal_subsystem: IdRef | None = None
    trusted_components: IdRef | None = None
    uuid: str | None = Field(serialization_alias="UUID", default=None)
    version: str | None = None
    weight_kg: float | None = None
    width_mm: float | None = None


class ChassisOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    asset_tag: str | None = None
    doors: Doors | None = None
    drives: IdRef | None = None
    electrical_source_manager_ur_is: list[str] | None = Field(
        serialization_alias="ElectricalSourceManagerURIs", default=None
    )
    electrical_source_names: list[str] | None = None
    environmental_class: EnvironmentalClass | None = None
    heating_cooling_equipment_names: list[str] | None = None
    heating_cooling_manager_ur_is: list[str] | None = Field(
        serialization_alias="HeatingCoolingManagerURIs", default=None
    )
    indicator_led: IndicatorLed | None = Field(serialization_alias="IndicatorLED", default=None)
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    measurements: list[MeasurementBlock] | None = None
    oem: dict[str, Any] | None = None
    physical_security: PhysicalSecurity | None = None
    status: Status | None = None


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
    IP_BASED_DRIVE = "IPBasedDrive"
    RACK_GROUP = "RackGroup"
    STORAGE_ENCLOSURE = "StorageEnclosure"
    IMMERSION_TANK = "ImmersionTank"
    HEAT_EXCHANGER = "HeatExchanger"
    POWER_STRIP = "PowerStrip"
    OTHER = "Other"


class Door(RedfishModel):
    door_state: DoorState | None = None
    locked: bool | None = None
    user_label: str | None = None


class DoorState(StrEnum):
    LOCKED = "Locked"
    CLOSED = "Closed"
    LOCKED_AND_OPEN = "LockedAndOpen"
    OPEN = "Open"


class Doors(RedfishModel):
    front: Door | None = None
    rear: Door | None = None


class EnvironmentalClass(StrEnum):
    A1 = "A1"
    A2 = "A2"
    A3 = "A3"
    A4 = "A4"


class IndicatorLed(StrEnum):
    UNKNOWN = "Unknown"
    LIT = "Lit"
    BLINKING = "Blinking"
    OFF = "Off"


class IntrusionSensor(StrEnum):
    NORMAL = "Normal"
    HARDWARE_INTRUSION = "HardwareIntrusion"
    TAMPERING_DETECTED = "TamperingDetected"


class IntrusionSensorReArm(StrEnum):
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"


class Links(RedfishModel):
    cables: list[IdRef] | None = None
    cables_odata_count: int | None = Field(serialization_alias="Cables@odata.count", default=None)
    computer_systems: list[IdRef] | None = None
    computer_systems_odata_count: int | None = Field(
        serialization_alias="ComputerSystems@odata.count", default=None
    )
    connected_cooling_loops: list[IdRef] | None = None
    connected_cooling_loops_odata_count: int | None = Field(
        serialization_alias="ConnectedCoolingLoops@odata.count", default=None
    )
    contained_by: IdRef | None = None
    contains: list[IdRef] | None = None
    contains_odata_count: int | None = Field(
        serialization_alias="Contains@odata.count", default=None
    )
    cooled_by: list[IdRef] | None = None
    cooled_by_odata_count: int | None = Field(
        serialization_alias="CooledBy@odata.count", default=None
    )
    cooling_units: list[IdRef] | None = None
    cooling_units_odata_count: int | None = Field(
        serialization_alias="CoolingUnits@odata.count", default=None
    )
    drives: list[IdRef] | None = None
    drives_odata_count: int | None = Field(serialization_alias="Drives@odata.count", default=None)
    facility: IdRef | None = None
    fans: list[IdRef] | None = None
    fans_odata_count: int | None = Field(serialization_alias="Fans@odata.count", default=None)
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(
        serialization_alias="ManagedBy@odata.count", default=None
    )
    managers_in_chassis: list[IdRef] | None = None
    managers_in_chassis_odata_count: int | None = Field(
        serialization_alias="ManagersInChassis@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_devices: list[IdRef] | None = Field(serialization_alias="PCIeDevices", default=None)
    pcie_devices_odata_count: int | None = Field(
        serialization_alias="PCIeDevices@odata.count", default=None
    )
    power_distribution: IdRef | None = None
    power_outlets: list[IdRef] | None = None
    power_outlets_odata_count: int | None = Field(
        serialization_alias="PowerOutlets@odata.count", default=None
    )
    power_supplies: list[IdRef] | None = None
    power_supplies_odata_count: int | None = Field(
        serialization_alias="PowerSupplies@odata.count", default=None
    )
    powered_by: list[IdRef] | None = None
    powered_by_odata_count: int | None = Field(
        serialization_alias="PoweredBy@odata.count", default=None
    )
    processors: list[IdRef] | None = None
    processors_odata_count: int | None = Field(
        serialization_alias="Processors@odata.count", default=None
    )
    resource_blocks: list[IdRef] | None = None
    resource_blocks_odata_count: int | None = Field(
        serialization_alias="ResourceBlocks@odata.count", default=None
    )
    storage: list[IdRef] | None = None
    storage_odata_count: int | None = Field(
        serialization_alias="Storage@odata.count", default=None
    )
    switches: list[IdRef] | None = None
    switches_odata_count: int | None = Field(
        serialization_alias="Switches@odata.count", default=None
    )


class PhysicalSecurity(RedfishModel):
    intrusion_sensor: IntrusionSensor | None = None
    intrusion_sensor_number: int | None = None
    intrusion_sensor_re_arm: IntrusionSensorReArm | None = None


class Reset(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetRequest(RedfishModel):
    reset_type: ResetType | None = None


class ThermalDirection(StrEnum):
    FRONT_TO_BACK = "FrontToBack"
    BACK_TO_FRONT = "BackToFront"
    TOP_EXHAUST = "TopExhaust"
    SEALED = "Sealed"
