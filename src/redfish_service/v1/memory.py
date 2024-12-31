from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Location, Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class DisablePassphrase(RedfishResource):
    target: str | None = None
    title: str | None = None


class Links(RedfishResource):
    chassis: IdRef | None = None
    oem: dict[str, Any] | None = None


class Memory(RedfishResource):
    actions: Actions | None = None
    allocation_alignment_mi_b: str | None = None
    allocation_increment_mi_b: str | None = None
    allowed_speeds_mhz: list[int] | None = None
    assembly: IdRef | None = None
    base_module_type: str | None = None
    bus_width_bits: str | None = None
    cache_size_mi_b: str | None = None
    capacity_mi_b: str | None = None
    configuration_locked: str | None = None
    data_width_bits: str | None = None
    description: str | None = None
    device_id: str | None = None
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
    max_tdpmilli_watts: list[int] | None = None
    memory_device_type: str | None = None
    memory_location: MemoryLocation | None = None
    memory_media: list[MemoryMedia] | None = None
    memory_subsystem_controller_manufacturer_id: str | None = None
    memory_subsystem_controller_product_id: str | None = None
    memory_type: str | None = None
    metrics: IdRef | None = None
    module_manufacturer_id: str | None = None
    module_product_id: str | None = None
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
    subsystem_device_id: str | None = None
    subsystem_vendor_id: str | None = None
    vendor_id: str | None = None
    volatile_region_number_limit: str | None = None
    volatile_region_size_limit_mi_b: str | None = None
    volatile_region_size_max_mi_b: str | None = None
    volatile_size_mi_b: str | None = None


class MemoryLocation(RedfishResource):
    channel: str | None = None
    memory_controller: str | None = None
    slot: str | None = None
    socket: str | None = None


class MemoryMedia(StrEnum):
    DRAM = "DRAM"
    NAND = "NAND"
    INTEL3_DXPOINT = "Intel3DXPoint"
    PROPRIETARY = "Proprietary"


class OemActions(RedfishResource):
    pass


class OperatingMemoryModes(StrEnum):
    VOLATILE = "Volatile"
    PMEM = "PMEM"
    BLOCK = "Block"


class OverwriteUnit(RedfishResource):
    target: str | None = None
    title: str | None = None


class PowerManagementPolicy(RedfishResource):
    average_power_budget_milli_watts: str | None = None
    max_tdpmilli_watts: str | None = None
    peak_power_budget_milli_watts: str | None = None
    policy_enabled: str | None = None


class RegionSet(RedfishResource):
    memory_classification: str | None = None
    offset_mi_b: str | None = None
    passphrase_enabled: str | None = None
    passphrase_state: str | None = None
    region_id: str | None = None
    size_mi_b: str | None = None


class Reset(RedfishResource):
    target: str | None = None
    title: str | None = None


class SecureEraseUnit(RedfishResource):
    target: str | None = None
    title: str | None = None


class SecurityCapabilities(RedfishResource):
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


class SetPassphrase(RedfishResource):
    target: str | None = None
    title: str | None = None


class UnlockUnit(RedfishResource):
    target: str | None = None
    title: str | None = None
