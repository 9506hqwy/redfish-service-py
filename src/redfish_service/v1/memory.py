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


class Actions(RedfishModel):
    disable_passphrase: DisablePassphrase | None = Field(
        alias="#Memory.DisablePassphrase", default=None
    )
    overwrite_unit: OverwriteUnit | None = Field(alias="#Memory.OverwriteUnit", default=None)
    reset: Reset | None = Field(alias="#Memory.Reset", default=None)
    secure_erase_unit: SecureEraseUnit | None = Field(
        alias="#Memory.SecureEraseUnit", default=None
    )
    set_passphrase: SetPassphrase | None = Field(alias="#Memory.SetPassphrase", default=None)
    unlock_unit: UnlockUnit | None = Field(alias="#Memory.UnlockUnit", default=None)
    oem: dict[str, Any] | None = None


class DisablePassphrase(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Links(RedfishModel):
    chassis: IdRef | None = None
    oem: dict[str, Any] | None = None


class Memory(RedfishResource):
    actions: Actions | None = None
    allocation_alignment_mi_b: str | None = None
    allocation_increment_mi_b: str | None = None
    allowed_speeds_mhz: list[int] | None = Field(alias="AllowedSpeedsMHz", default=None)
    assembly: IdRef | None = None
    base_module_type: str | None = None
    bus_width_bits: str | None = None
    cache_size_mi_b: str | None = None
    capacity_mi_b: str | None = None
    configuration_locked: str | None = None
    data_width_bits: str | None = None
    description: str | None = None
    device_id: str | None = Field(alias="DeviceID", default=None)
    device_locator: str | None = None
    error_correction: str | None = None
    firmware_api_version: str | None = None
    firmware_revision: str | None = None
    function_classes: list[str] | None = None
    is_rank_spare_enabled: str | None = None
    is_spare_device_enabled: str | None = None
    links: Links | None = None
    location: Location | None = None
    logical_size_mi_b: str | None = None
    manufacturer: str | None = None
    max_tdpmilli_watts: list[int] | None = Field(alias="MaxTDPMilliWatts", default=None)
    memory_device_type: str | None = None
    memory_location: MemoryLocation | None = None
    memory_media: list[MemoryMedia] | None = None
    memory_subsystem_controller_manufacturer_id: str | None = Field(
        alias="MemorySubsystemControllerManufacturerID", default=None
    )
    memory_subsystem_controller_product_id: str | None = Field(
        alias="MemorySubsystemControllerProductID", default=None
    )
    memory_type: str | None = None
    metrics: IdRef | None = None
    module_manufacturer_id: str | None = Field(alias="ModuleManufacturerID", default=None)
    module_product_id: str | None = Field(alias="ModuleProductID", default=None)
    non_volatile_size_mi_b: str | None = None
    oem: dict[str, Any] | None = None
    operating_memory_modes: list[OperatingMemoryModes] | None = None
    operating_speed_mhz: str | None = None
    part_number: str | None = None
    persistent_region_number_limit: str | None = None
    persistent_region_size_limit_mi_b: str | None = None
    persistent_region_size_max_mi_b: str | None = None
    power_management_policy: PowerManagementPolicy | None = None
    rank_count: str | None = None
    regions: list[RegionSet] | None = None
    security_capabilities: SecurityCapabilities | None = None
    security_state: str | None = None
    serial_number: str | None = None
    spare_device_count: str | None = None
    status: Status | None = None
    subsystem_device_id: str | None = Field(alias="SubsystemDeviceID", default=None)
    subsystem_vendor_id: str | None = Field(alias="SubsystemVendorID", default=None)
    vendor_id: str | None = Field(alias="VendorID", default=None)
    volatile_region_number_limit: str | None = None
    volatile_region_size_limit_mi_b: str | None = None
    volatile_region_size_max_mi_b: str | None = None
    volatile_size_mi_b: str | None = None


class MemoryLocation(RedfishModel):
    channel: str | None = None
    memory_controller: str | None = None
    slot: str | None = None
    socket: str | None = None


class MemoryMedia(StrEnum):
    DRAM = "DRAM"
    NAND = "NAND"
    INTEL3_DXPOINT = "Intel3DXPoint"
    PROPRIETARY = "Proprietary"


class OperatingMemoryModes(StrEnum):
    VOLATILE = "Volatile"
    PMEM = "PMEM"
    BLOCK = "Block"


class OverwriteUnit(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class PowerManagementPolicy(RedfishModel):
    average_power_budget_milli_watts: str | None = None
    max_tdpmilli_watts: str | None = Field(alias="MaxTDPMilliWatts", default=None)
    peak_power_budget_milli_watts: str | None = None
    policy_enabled: str | None = None


class RegionSet(RedfishModel):
    memory_classification: str | None = None
    offset_mi_b: str | None = None
    passphrase_enabled: str | None = None
    passphrase_state: str | None = None
    region_id: str | None = None
    size_mi_b: str | None = None


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SecureEraseUnit(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SecurityCapabilities(RedfishModel):
    configuration_lock_capable: str | None = None
    data_lock_capable: str | None = None
    max_passphrase_count: str | None = None
    passphrase_capable: str | None = None
    passphrase_lock_limit: str | None = None
    security_states: list[SecurityStates] | None = None


class SecurityStates(StrEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    UNLOCKED = "Unlocked"
    LOCKED = "Locked"
    FROZEN = "Frozen"
    PASSPHRASELIMIT = "Passphraselimit"


class SetPassphrase(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class UnlockUnit(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
