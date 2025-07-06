from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .control import ControlRangeExcerpt
from .odata_v4 import IdRef
from .resource import Location, ResetType, Status
from .software_inventory import MeasurementBlock


class Actions(RedfishModel):
    disable_master_passphrase: DisableMasterPassphrase | None = Field(
        serialization_alias="#Memory.DisableMasterPassphrase", default=None
    )
    disable_passphrase: DisablePassphrase | None = Field(
        serialization_alias="#Memory.DisablePassphrase", default=None
    )
    freeze_security_state: FreezeSecurityState | None = Field(
        serialization_alias="#Memory.FreezeSecurityState", default=None
    )
    inject_persistent_poison: InjectPersistentPoison | None = Field(
        serialization_alias="#Memory.InjectPersistentPoison", default=None
    )
    overwrite_unit: OverwriteUnit | None = Field(
        serialization_alias="#Memory.OverwriteUnit", default=None
    )
    reset: Reset | None = Field(serialization_alias="#Memory.Reset", default=None)
    reset_to_defaults: ResetToDefaults | None = Field(
        serialization_alias="#Memory.ResetToDefaults", default=None
    )
    scan_media: ScanMedia | None = Field(serialization_alias="#Memory.ScanMedia", default=None)
    secure_erase_unit: SecureEraseUnit | None = Field(
        serialization_alias="#Memory.SecureEraseUnit", default=None
    )
    set_master_passphrase: SetMasterPassphrase | None = Field(
        serialization_alias="#Memory.SetMasterPassphrase", default=None
    )
    set_passphrase: SetPassphrase | None = Field(
        serialization_alias="#Memory.SetPassphrase", default=None
    )
    unlock_unit: UnlockUnit | None = Field(serialization_alias="#Memory.UnlockUnit", default=None)
    oem: dict[str, Any] | None = None


class BaseModuleType(StrEnum):
    RDIMM = "RDIMM"
    UDIMM = "UDIMM"
    S_O_DIMM = "SO_DIMM"
    LRDIMM = "LRDIMM"
    MINI_RDIMM = "Mini_RDIMM"
    MINI_UDIMM = "Mini_UDIMM"
    S_O_RDIM_M_72B = "SO_RDIMM_72b"
    S_O_UDIM_M_72B = "SO_UDIMM_72b"
    S_O_DIM_M_16B = "SO_DIMM_16b"
    S_O_DIM_M_32B = "SO_DIMM_32b"
    DIE = "Die"
    CAMM = "CAMM"


class Cxl(RedfishModel):
    label_storage_size_bytes: int | None = None
    staged_non_volatile_size_mib: int | None = Field(
        serialization_alias="StagedNonVolatileSizeMiB", default=None
    )
    staged_volatile_size_mib: int | None = Field(
        serialization_alias="StagedVolatileSizeMiB", default=None
    )


class DisableMasterPassphrase(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class DisableMasterPassphraseRequest(RedfishModel):
    passphrase: str
    region_id: str


class DisablePassphrase(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class DisablePassphraseRequest(RedfishModel):
    passphrase: str
    region_id: str


class ErrorCorrection(StrEnum):
    NO_ECC = "NoECC"
    SINGLE_BIT_ECC = "SingleBitECC"
    MULTI_BIT_ECC = "MultiBitECC"
    ADDRESS_PARITY = "AddressParity"


class FreezeSecurityState(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class HealthData(RedfishModel):
    predicted_media_life_left_percent: float | None = None


class InjectPersistentPoison(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class InjectPersistentPoisonRequest(RedfishModel):
    physical_address: str


class Links(RedfishModel):
    batteries: list[IdRef] | None = None
    batteries_odata_count: int | None = Field(
        serialization_alias="Batteries@odata.count", default=None
    )
    chassis: IdRef | None = None
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(
        serialization_alias="Endpoints@odata.count", default=None
    )
    memory_media_sources: list[IdRef] | None = None
    memory_media_sources_odata_count: int | None = Field(
        serialization_alias="MemoryMediaSources@odata.count", default=None
    )
    memory_region_media_sources: list[IdRef] | None = None
    memory_region_media_sources_odata_count: int | None = Field(
        serialization_alias="MemoryRegionMediaSources@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    processors: list[IdRef] | None = None
    processors_odata_count: int | None = Field(
        serialization_alias="Processors@odata.count", default=None
    )


class Memory(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Memory.v1_21_0.Memory")
    actions: Actions | None = None
    allocation_alignment_mib: int | None = Field(
        serialization_alias="AllocationAlignmentMiB", default=None
    )
    allocation_increment_mib: int | None = Field(
        serialization_alias="AllocationIncrementMiB", default=None
    )
    allowed_speeds_mhz: list[int] | None = Field(
        serialization_alias="AllowedSpeedsMHz", default=None
    )
    assembly: IdRef | None = None
    base_module_type: BaseModuleType | None = None
    bus_width_bits: int | None = None
    cxl: Cxl | None = Field(serialization_alias="CXL", default=None)
    cache_level: int | None = None
    cache_size_mib: int | None = Field(serialization_alias="CacheSizeMiB", default=None)
    capacity_mib: int | None = Field(serialization_alias="CapacityMiB", default=None)
    certificates: IdRef | None = None
    configuration_locked: bool | None = None
    data_width_bits: int | None = None
    description: str | None = None
    device_id: str | None = Field(serialization_alias="DeviceID", default=None)
    device_locator: str | None = None
    enabled: bool | None = None
    environment_metrics: IdRef | None = None
    error_correction: ErrorCorrection | None = None
    firmware_api_version: str | None = None
    firmware_revision: str | None = None
    function_classes: list[str] | None = None
    health_data: HealthData | None = None
    id: str
    is_rank_spare_enabled: bool | None = None
    is_spare_device_enabled: bool | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    log: IdRef | None = None
    logical_size_mib: int | None = Field(serialization_alias="LogicalSizeMiB", default=None)
    manufacturer: str | None = None
    max_tdp_milli_watts: list[int] | None = Field(
        serialization_alias="MaxTDPMilliWatts", default=None
    )
    measurements: list[MeasurementBlock] | None = None
    memory_device_type: MemoryDeviceType | None = None
    memory_location: MemoryLocation | None = None
    memory_media: list[MemoryMedia] | None = None
    memory_subsystem_controller_manufacturer_id: str | None = Field(
        serialization_alias="MemorySubsystemControllerManufacturerID", default=None
    )
    memory_subsystem_controller_product_id: str | None = Field(
        serialization_alias="MemorySubsystemControllerProductID", default=None
    )
    memory_type: MemoryType | None = None
    metrics: IdRef | None = None
    model: str | None = None
    module_manufacturer_id: str | None = Field(
        serialization_alias="ModuleManufacturerID", default=None
    )
    module_product_id: str | None = Field(serialization_alias="ModuleProductID", default=None)
    name: str
    non_volatile_size_limit_mib: int | None = Field(
        serialization_alias="NonVolatileSizeLimitMiB", default=None
    )
    non_volatile_size_mib: int | None = Field(
        serialization_alias="NonVolatileSizeMiB", default=None
    )
    oem: dict[str, Any] | None = None
    operating_memory_modes: list[OperatingMemoryModes] | None = None
    operating_speed_mhz: int | None = None
    operating_speed_range_mhz: ControlRangeExcerpt | None = Field(
        serialization_alias="OperatingSpeedRangeMHz", default=None
    )
    part_number: str | None = None
    persistent_region_number_limit: int | None = None
    persistent_region_size_limit_mib: int | None = Field(
        serialization_alias="PersistentRegionSizeLimitMiB", default=None
    )
    persistent_region_size_max_mib: int | None = Field(
        serialization_alias="PersistentRegionSizeMaxMiB", default=None
    )
    poison_list_max_media_error_records: int | None = None
    power_management_ic_manufacturer_id: str | None = Field(
        serialization_alias="PowerManagementICManufacturerID", default=None
    )
    power_management_ic_revision_id: str | None = Field(
        serialization_alias="PowerManagementICRevisionID", default=None
    )
    power_management_policy: PowerManagementPolicy | None = None
    rank_count: int | None = None
    regions: list[RegionSet] | None = None
    security_capabilities: SecurityCapabilities | None = None
    security_state: SecurityStates | None = None
    security_states: SecurityStateInfo | None = None
    serial_number: str | None = None
    spare_device_count: int | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    subsystem_device_id: str | None = Field(serialization_alias="SubsystemDeviceID", default=None)
    subsystem_vendor_id: str | None = Field(serialization_alias="SubsystemVendorID", default=None)
    vendor_id: str | None = Field(serialization_alias="VendorID", default=None)
    volatile_region_number_limit: int | None = None
    volatile_region_size_limit_mib: int | None = Field(
        serialization_alias="VolatileRegionSizeLimitMiB", default=None
    )
    volatile_region_size_max_mib: int | None = Field(
        serialization_alias="VolatileRegionSizeMaxMiB", default=None
    )
    volatile_size_limit_mib: int | None = Field(
        serialization_alias="VolatileSizeLimitMiB", default=None
    )
    volatile_size_mib: int | None = Field(serialization_alias="VolatileSizeMiB", default=None)


class MemoryOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    cxl: Cxl | None = Field(serialization_alias="CXL", default=None)
    enabled: bool | None = None
    health_data: HealthData | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    measurements: list[MeasurementBlock] | None = None
    memory_location: MemoryLocation | None = None
    non_volatile_size_limit_mib: int | None = Field(
        serialization_alias="NonVolatileSizeLimitMiB", default=None
    )
    oem: dict[str, Any] | None = None
    operating_speed_range_mhz: ControlRangeExcerpt | None = Field(
        serialization_alias="OperatingSpeedRangeMHz", default=None
    )
    poison_list_max_media_error_records: int | None = None
    power_management_policy: PowerManagementPolicy | None = None
    regions: list[RegionSet] | None = None
    security_capabilities: SecurityCapabilities | None = None
    security_state: SecurityStates | None = None
    security_states: SecurityStateInfo | None = None
    status: Status | None = None
    volatile_size_limit_mib: int | None = Field(
        serialization_alias="VolatileSizeLimitMiB", default=None
    )


class MemoryClassification(StrEnum):
    VOLATILE = "Volatile"
    BYTE_ACCESSIBLE_PERSISTENT = "ByteAccessiblePersistent"
    BLOCK = "Block"


class MemoryDeviceType(StrEnum):
    DDR = "DDR"
    DDR2 = "DDR2"
    DDR3 = "DDR3"
    DDR4 = "DDR4"
    DD_R4_SDRAM = "DDR4_SDRAM"
    DDR4_E_SDRAM = "DDR4E_SDRAM"
    LPDD_R4_SDRAM = "LPDDR4_SDRAM"
    DD_R3_SDRAM = "DDR3_SDRAM"
    LPDD_R3_SDRAM = "LPDDR3_SDRAM"
    DD_R2_SDRAM = "DDR2_SDRAM"
    DD_R2_SDRA_M_F_B_DIMM = "DDR2_SDRAM_FB_DIMM"
    DD_R2_SDRA_M_F_B_DIM_M_PROBE = "DDR2_SDRAM_FB_DIMM_PROBE"
    DD_R_SGRAM = "DDR_SGRAM"
    DD_R_SDRAM = "DDR_SDRAM"
    ROM = "ROM"
    SDRAM = "SDRAM"
    EDO = "EDO"
    FAST_PAGE_MODE = "FastPageMode"
    PIPELINED_NIBBLE = "PipelinedNibble"
    LOGICAL = "Logical"
    HBM = "HBM"
    HBM2 = "HBM2"
    HBM2_E = "HBM2E"
    HBM3 = "HBM3"
    GDDR = "GDDR"
    GDDR2 = "GDDR2"
    GDDR3 = "GDDR3"
    GDDR4 = "GDDR4"
    GDDR5 = "GDDR5"
    GDDR5_X = "GDDR5X"
    GDDR6 = "GDDR6"
    DDR5 = "DDR5"
    OEM = "OEM"
    LPDD_R5_SDRAM = "LPDDR5_SDRAM"
    DD_R5_MRDIMM = "DDR5_MRDIMM"


class MemoryLocation(RedfishModel):
    channel: int | None = None
    memory_controller: int | None = None
    slot: int | None = None
    socket: int | None = None


class MemoryMedia(StrEnum):
    DRAM = "DRAM"
    NAND = "NAND"
    INTEL3_DX_POINT = "Intel3DXPoint"
    PROPRIETARY = "Proprietary"


class MemoryType(StrEnum):
    DRAM = "DRAM"
    NVDIM_M_N = "NVDIMM_N"
    NVDIM_M_F = "NVDIMM_F"
    NVDIM_M_P = "NVDIMM_P"
    INTEL_OPTANE = "IntelOptane"
    CACHE = "Cache"


class OperatingMemoryModes(StrEnum):
    VOLATILE = "Volatile"
    PMEM = "PMEM"
    BLOCK = "Block"


class OverwriteUnit(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class OverwriteUnitRequest(RedfishModel):
    passphrase: str
    region_id: str


class PowerManagementPolicy(RedfishModel):
    average_power_budget_milli_watts: int | None = None
    max_tdp_milli_watts: int | None = Field(serialization_alias="MaxTDPMilliWatts", default=None)
    peak_power_budget_milli_watts: int | None = None
    policy_enabled: bool | None = None


class RegionSet(RedfishModel):
    master_passphrase_enabled: bool | None = None
    memory_classification: MemoryClassification | None = None
    offset_mib: int | None = Field(serialization_alias="OffsetMiB", default=None)
    passphrase_enabled: bool | None = None
    passphrase_state: bool | None = None
    region_id: str | None = None
    size_mib: int | None = Field(serialization_alias="SizeMiB", default=None)


class Reset(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetRequest(RedfishModel):
    reset_type: ResetType | None = None


class ResetToDefaults(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ScanMedia(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ScanMediaRequest(RedfishModel):
    length: int
    no_event_log: bool | None = None
    physical_address: str


class SecureEraseUnit(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SecureEraseUnitRequest(RedfishModel):
    passphrase: str
    region_id: str


class SecurityCapabilities(RedfishModel):
    configuration_lock_capable: bool | None = None
    data_lock_capable: bool | None = None
    max_passphrase_count: int | None = None
    passphrase_capable: bool | None = None
    passphrase_lock_limit: int | None = None
    security_states: list[SecurityStates] | None = None


class SecurityStateInfo(RedfishModel):
    master_passphrase_attempt_count_reached: bool | None = None
    user_passphrase_attempt_count_reached: bool | None = None


class SecurityStates(StrEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    UNLOCKED = "Unlocked"
    LOCKED = "Locked"
    FROZEN = "Frozen"
    PASSPHRASELIMIT = "Passphraselimit"


class SetMasterPassphrase(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SetMasterPassphraseRequest(RedfishModel):
    passphrase: str
    region_id: str


class SetPassphrase(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SetPassphraseRequest(RedfishModel):
    passphrase: str
    region_id: str


class UnlockUnit(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class UnlockUnitRequest(RedfishModel):
    passphrase: str
    region_id: str
