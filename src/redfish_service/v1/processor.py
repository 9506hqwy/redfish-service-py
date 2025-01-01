from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .pcie_device import PcieInterface
from .resource import Location, Status
from .software_inventory import AdditionalVersions, MeasurementBlock


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#Processor.Reset", default=None)
    reset_to_defaults: ResetToDefaults | None = Field(
        alias="#Processor.ResetToDefaults", default=None
    )
    oem: dict[str, Any] | None = None


class EthernetInterface(RedfishModel):
    max_lanes: str | None = None
    max_speed_mbps: str | None = None
    oem: dict[str, Any] | None = None


class Fpga(RedfishModel):
    external_interfaces: list[ProcessorInterface] | None = None
    firmware_id: str | None = None
    firmware_manufacturer: str | None = None
    firmware_version: str | None = None
    fpga_type: FpgaType | None = None
    host_interface: ProcessorInterface | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    pcie_virtual_functions: int | None = Field(alias="PCIeVirtualFunctions", default=None)
    programmable_from_host: str | None = None
    reconfiguration_slots: list[FpgaReconfigurationSlot] | None = None


class FpgaReconfigurationSlot(RedfishModel):
    acceleration_function: IdRef | None = None
    programmable_from_host: str | None = None
    slot_id: str | None = None
    uuid: str | None = Field(alias="UUID", default=None)


class FpgaType(StrEnum):
    INTEGRATED = "Integrated"
    DISCRETE = "Discrete"


class Links(RedfishModel):
    chassis: IdRef | None = None
    connected_processors: list[IdRef] | None = None
    connected_processors_odata_count: int | None = Field(
        alias="ConnectedProcessors@odata.count", default=None
    )
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    fabric_adapters: list[IdRef] | None = None
    fabric_adapters_odata_count: int | None = Field(
        alias="FabricAdapters@odata.count", default=None
    )
    graphics_controller: str | None = None
    memory: list[IdRef] | None = None
    memory_odata_count: int | None = Field(alias="Memory@odata.count", default=None)
    network_device_functions: list[IdRef] | None = None
    network_device_functions_odata_count: int | None = Field(
        alias="NetworkDeviceFunctions@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_device: IdRef | None = Field(alias="PCIeDevice", default=None)
    pcie_functions: list[IdRef] | None = Field(alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(alias="PCIeFunctions@odata.count", default=None)


class MemorySummary(RedfishModel):
    eccmode_enabled: str | None = Field(alias="ECCModeEnabled", default=None)
    metrics: IdRef | None = None
    total_cache_size_mi_b: str | None = None
    total_memory_size_mi_b: str | None = None


class Processor(RedfishResource):
    acceleration_functions: IdRef | None = None
    actions: Actions | None = None
    additional_firmware_versions: AdditionalVersions | None = None
    applied_operating_config: IdRef | None = None
    assembly: IdRef | None = None
    base_speed_mhz: str | None = Field(alias="BaseSpeedMHz", default=None)
    base_speed_priority_state: str | None = None
    cache_memory: IdRef | None = None
    certificates: IdRef | None = None
    description: str | None = None
    enabled: bool | None = None
    environment_metrics: IdRef | None = None
    fpga: Fpga | None = Field(alias="FPGA", default=None)
    family: str | None = None
    firmware_version: str | None = None
    high_speed_core_ids: list[str] | None = Field(alias="HighSpeedCoreIDs", default=None)
    instruction_set: str | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    manufacturer: str | None = None
    max_speed_mhz: str | None = Field(alias="MaxSpeedMHz", default=None)
    max_tdpwatts: str | None = Field(alias="MaxTDPWatts", default=None)
    measurements: list[MeasurementBlock] | None = None
    memory_summary: MemorySummary | None = None
    metrics: IdRef | None = None
    min_speed_mhz: str | None = Field(alias="MinSpeedMHz", default=None)
    model: str | None = None
    oem: dict[str, Any] | None = None
    operating_configs: IdRef | None = None
    operating_speed_mhz: str | None = Field(alias="OperatingSpeedMHz", default=None)
    operating_speed_range_mhz: str | None = Field(alias="OperatingSpeedRangeMHz", default=None)
    part_number: str | None = None
    ports: IdRef | None = None
    power_state: str | None = None
    processor_architecture: str | None = None
    processor_id: ProcessorId | None = None
    processor_index: str | None = None
    processor_memory: list[ProcessorMemory] | None = None
    processor_type: str | None = None
    replaceable: str | None = None
    serial_number: str | None = None
    socket: str | None = None
    spare_part_number: str | None = None
    speed_limit_mhz: str | None = Field(alias="SpeedLimitMHz", default=None)
    speed_locked: str | None = None
    status: Status | None = None
    sub_processors: IdRef | None = None
    system_interface: ProcessorInterface | None = None
    tdpwatts: str | None = Field(alias="TDPWatts", default=None)
    throttle_causes: list[str] | None = None
    throttled: str | None = None
    total_cores: str | None = None
    total_enabled_cores: str | None = None
    total_threads: str | None = None
    turbo_state: str | None = None
    uuid: str | None = Field(alias="UUID", default=None)
    version: str | None = None


class ProcessorId(RedfishModel):
    effective_family: str | None = None
    effective_model: str | None = None
    identification_registers: str | None = None
    microcode_info: str | None = None
    protected_identification_number: str | None = None
    step: str | None = None
    vendor_id: str | None = None


class ProcessorInterface(RedfishModel):
    ethernet: EthernetInterface | None = None
    interface_type: str | None = None
    pcie: PcieInterface | None = Field(alias="PCIe", default=None)


class ProcessorMemory(RedfishModel):
    capacity_mi_b: str | None = None
    integrated_memory: str | None = None
    memory_type: str | None = None
    speed_mhz: str | None = Field(alias="SpeedMHz", default=None)


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ResetToDefaults(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
