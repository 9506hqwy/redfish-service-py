from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .pcie_device import PcieInterface
from .resource import Location, Status


class Actions(RedfishModel):
    oem: OemActions | None = None


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
    pcie_virtual_functions: int | None = None
    programmable_from_host: str | None = None
    reconfiguration_slots: list[FpgaReconfigurationSlot] | None = None


class FpgaReconfigurationSlot(RedfishModel):
    acceleration_function: IdRef | None = None
    programmable_from_host: str | None = None
    slot_id: str | None = None
    uuid: str | None = None


class FpgaType(StrEnum):
    INTEGRATED = "Integrated"
    DISCRETE = "Discrete"


class Links(RedfishModel):
    chassis: IdRef | None = None
    connected_processors: list[IdRef] | None = None
    endpoints: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    pcie_device: IdRef | None = None
    pcie_functions: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass


class Processor(RedfishResource):
    acceleration_functions: IdRef | None = None
    actions: Actions | None = None
    applied_operating_config: IdRef | None = None
    assembly: IdRef | None = None
    base_speed_priority_state: str | None = None
    description: str | None = None
    fpga: Fpga | None = None
    firmware_version: str | None = None
    high_speed_core_ids: list[str] | None = None
    instruction_set: str | None = None
    links: Links | None = None
    location: Location | None = None
    manufacturer: str | None = None
    max_speed_mhz: str | None = None
    max_tdpwatts: str | None = None
    metrics: IdRef | None = None
    min_speed_mhz: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    operating_configs: IdRef | None = None
    operating_speed_mhz: str | None = None
    part_number: str | None = None
    processor_architecture: str | None = None
    processor_id: ProcessorId | None = None
    processor_memory: list[ProcessorMemory] | None = None
    processor_type: str | None = None
    serial_number: str | None = None
    socket: str | None = None
    status: Status | None = None
    sub_processors: IdRef | None = None
    system_interface: ProcessorInterface | None = None
    tdpwatts: str | None = None
    total_cores: str | None = None
    total_enabled_cores: str | None = None
    total_threads: str | None = None
    turbo_state: str | None = None
    uuid: str | None = None
    version: str | None = None


class ProcessorId(RedfishModel):
    effective_family: str | None = None
    effective_model: str | None = None
    identification_registers: str | None = None
    microcode_info: str | None = None
    step: str | None = None
    vendor_id: str | None = None


class ProcessorInterface(RedfishModel):
    ethernet: EthernetInterface | None = None
    interface_type: str | None = None
    pcie: PcieInterface | None = None


class ProcessorMemory(RedfishModel):
    capacity_mi_b: str | None = None
    integrated_memory: str | None = None
    memory_type: str | None = None
    speed_mhz: str | None = None


class Reset(RedfishModel):
    target: str | None = None
    title: str | None = None
