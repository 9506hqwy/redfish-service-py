from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .control import ControlRangeExcerpt
from .odata_v4 import IdRef
from .pcie_device import PcieInterface
from .resource import Location, PowerState, Status
from .software_inventory import AdditionalVersions, MeasurementBlock


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#Processor.Reset", default=None)
    reset_to_defaults: ResetToDefaults | None = Field(
        alias="#Processor.ResetToDefaults", default=None
    )
    oem: dict[str, Any] | None = None


class BaseSpeedPriorityState(StrEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class EthernetInterface(RedfishModel):
    max_lanes: int | None = None
    max_speed_mbps: int | None = None
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
    programmable_from_host: bool | None = None
    reconfiguration_slots: list[FpgaReconfigurationSlot] | None = None


class FpgaReconfigurationSlot(RedfishModel):
    acceleration_function: IdRef | None = None
    programmable_from_host: bool | None = None
    slot_id: str | None = None
    uuid: str | None = Field(alias="UUID", default=None)


class FpgaType(StrEnum):
    INTEGRATED = "Integrated"
    DISCRETE = "Discrete"


class InstructionSet(StrEnum):
    X86 = "x86"
    X86_64 = "x86-64"
    I_A_64 = "IA-64"
    AR_M_A32 = "ARM-A32"
    AR_M_A64 = "ARM-A64"
    MIPS32 = "MIPS32"
    MIPS64 = "MIPS64"
    POWER_ISA = "PowerISA"
    RV32 = "RV32"
    RV64 = "RV64"
    OEM = "OEM"


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
    graphics_controller: IdRef | None = None
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
    ecc_mode_enabled: bool | None = Field(alias="ECCModeEnabled", default=None)
    metrics: IdRef | None = None
    total_cache_size_mib: int | None = Field(alias="TotalCacheSizeMiB", default=None)
    total_memory_size_mib: int | None = Field(alias="TotalMemorySizeMiB", default=None)


class Processor(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#Processor.v1_20_1.Processor")
    acceleration_functions: IdRef | None = None
    actions: Actions | None = None
    additional_firmware_versions: AdditionalVersions | None = None
    applied_operating_config: IdRef | None = None
    assembly: IdRef | None = None
    base_speed_mhz: int | None = Field(alias="BaseSpeedMHz", default=None)
    base_speed_priority_state: BaseSpeedPriorityState | None = None
    cache_memory: IdRef | None = None
    certificates: IdRef | None = None
    description: str | None = None
    enabled: bool | None = None
    environment_metrics: IdRef | None = None
    fpga: Fpga | None = Field(alias="FPGA", default=None)
    family: str | None = None
    firmware_version: str | None = None
    high_speed_core_ids: list[int] | None = Field(alias="HighSpeedCoreIDs", default=None)
    id: str
    instruction_set: InstructionSet | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    max_speed_mhz: int | None = Field(alias="MaxSpeedMHz", default=None)
    max_tdp_watts: int | None = Field(alias="MaxTDPWatts", default=None)
    measurements: list[MeasurementBlock] | None = None
    memory_summary: MemorySummary | None = None
    metrics: IdRef | None = None
    min_speed_mhz: int | None = Field(alias="MinSpeedMHz", default=None)
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    operating_configs: IdRef | None = None
    operating_speed_mhz: int | None = Field(alias="OperatingSpeedMHz", default=None)
    operating_speed_range_mhz: ControlRangeExcerpt | None = Field(
        alias="OperatingSpeedRangeMHz", default=None
    )
    part_number: str | None = None
    ports: IdRef | None = None
    power_state: PowerState | None = None
    processor_architecture: ProcessorArchitecture | None = None
    processor_id: ProcessorId | None = None
    processor_index: int | None = None
    processor_memory: list[ProcessorMemory] | None = None
    processor_type: ProcessorType | None = None
    replaceable: bool | None = None
    serial_number: str | None = None
    socket: str | None = None
    spare_part_number: str | None = None
    speed_limit_mhz: int | None = Field(alias="SpeedLimitMHz", default=None)
    speed_locked: bool | None = None
    status: Status | None = None
    sub_processors: IdRef | None = None
    system_interface: ProcessorInterface | None = None
    tdp_watts: int | None = Field(alias="TDPWatts", default=None)
    throttle_causes: list[ThrottleCause] | None = None
    throttled: bool | None = None
    total_cores: int | None = None
    total_enabled_cores: int | None = None
    total_threads: int | None = None
    turbo_state: TurboState | None = None
    uuid: str | None = Field(alias="UUID", default=None)
    version: str | None = None


class ProcessorOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#Processor.v1_20_1.Processor")
    acceleration_functions: IdRef | None = None
    actions: Actions | None = None
    additional_firmware_versions: AdditionalVersions | None = None
    applied_operating_config: IdRef | None = None
    assembly: IdRef | None = None
    base_speed_mhz: int | None = Field(alias="BaseSpeedMHz", default=None)
    base_speed_priority_state: BaseSpeedPriorityState | None = None
    cache_memory: IdRef | None = None
    certificates: IdRef | None = None
    description: str | None = None
    enabled: bool | None = None
    environment_metrics: IdRef | None = None
    fpga: Fpga | None = Field(alias="FPGA", default=None)
    family: str | None = None
    firmware_version: str | None = None
    high_speed_core_ids: list[int] | None = Field(alias="HighSpeedCoreIDs", default=None)
    id: str | None = None
    instruction_set: InstructionSet | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    max_speed_mhz: int | None = Field(alias="MaxSpeedMHz", default=None)
    max_tdp_watts: int | None = Field(alias="MaxTDPWatts", default=None)
    measurements: list[MeasurementBlock] | None = None
    memory_summary: MemorySummary | None = None
    metrics: IdRef | None = None
    min_speed_mhz: int | None = Field(alias="MinSpeedMHz", default=None)
    model: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    operating_configs: IdRef | None = None
    operating_speed_mhz: int | None = Field(alias="OperatingSpeedMHz", default=None)
    operating_speed_range_mhz: ControlRangeExcerpt | None = Field(
        alias="OperatingSpeedRangeMHz", default=None
    )
    part_number: str | None = None
    ports: IdRef | None = None
    power_state: PowerState | None = None
    processor_architecture: ProcessorArchitecture | None = None
    processor_id: ProcessorId | None = None
    processor_index: int | None = None
    processor_memory: list[ProcessorMemory] | None = None
    processor_type: ProcessorType | None = None
    replaceable: bool | None = None
    serial_number: str | None = None
    socket: str | None = None
    spare_part_number: str | None = None
    speed_limit_mhz: int | None = Field(alias="SpeedLimitMHz", default=None)
    speed_locked: bool | None = None
    status: Status | None = None
    sub_processors: IdRef | None = None
    system_interface: ProcessorInterface | None = None
    tdp_watts: int | None = Field(alias="TDPWatts", default=None)
    throttle_causes: list[ThrottleCause] | None = None
    throttled: bool | None = None
    total_cores: int | None = None
    total_enabled_cores: int | None = None
    total_threads: int | None = None
    turbo_state: TurboState | None = None
    uuid: str | None = Field(alias="UUID", default=None)
    version: str | None = None


class ProcessorArchitecture(StrEnum):
    X86 = "x86"
    I_A_64 = "IA-64"
    ARM = "ARM"
    MIPS = "MIPS"
    POWER = "Power"
    RIS_C_V = "RISC-V"
    OEM = "OEM"


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
    interface_type: SystemInterfaceType | None = None
    pcie: PcieInterface | None = Field(alias="PCIe", default=None)


class ProcessorMemory(RedfishModel):
    capacity_mib: int | None = Field(alias="CapacityMiB", default=None)
    integrated_memory: bool | None = None
    memory_type: ProcessorMemoryType | None = None
    speed_mhz: int | None = Field(alias="SpeedMHz", default=None)


class ProcessorMemoryType(StrEnum):
    CACHE = "Cache"
    L1_CACHE = "L1Cache"
    L2_CACHE = "L2Cache"
    L3_CACHE = "L3Cache"
    L4_CACHE = "L4Cache"
    L5_CACHE = "L5Cache"
    L6_CACHE = "L6Cache"
    L7_CACHE = "L7Cache"
    HBM1 = "HBM1"
    HBM2 = "HBM2"
    HBM2_E = "HBM2E"
    HBM3 = "HBM3"
    SGRAM = "SGRAM"
    GDDR = "GDDR"
    GDDR2 = "GDDR2"
    GDDR3 = "GDDR3"
    GDDR4 = "GDDR4"
    GDDR5 = "GDDR5"
    GDDR5_X = "GDDR5X"
    GDDR6 = "GDDR6"
    DDR = "DDR"
    DDR2 = "DDR2"
    DDR3 = "DDR3"
    DDR4 = "DDR4"
    DDR5 = "DDR5"
    SDRAM = "SDRAM"
    SRAM = "SRAM"
    FLASH = "Flash"
    OEM = "OEM"


class ProcessorType(StrEnum):
    CPU = "CPU"
    GPU = "GPU"
    FPGA = "FPGA"
    DSP = "DSP"
    ACCELERATOR = "Accelerator"
    CORE = "Core"
    THREAD = "Thread"
    PARTITION = "Partition"
    OEM = "OEM"


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ResetToDefaults(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SystemInterfaceType(StrEnum):
    QPI = "QPI"
    UPI = "UPI"
    PCIE = "PCIe"
    ETHERNET = "Ethernet"
    AMBA = "AMBA"
    CCIX = "CCIX"
    CXL = "CXL"
    OEM = "OEM"


class ThrottleCause(StrEnum):
    POWER_LIMIT = "PowerLimit"
    THERMAL_LIMIT = "ThermalLimit"
    CLOCK_LIMIT = "ClockLimit"
    MANAGEMENT_DETECTED_FAULT = "ManagementDetectedFault"
    UNKNOWN = "Unknown"
    OEM = "OEM"


class TurboState(StrEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"
