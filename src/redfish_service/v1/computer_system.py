from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AddResourceBlock(RedfishModel):
    target: str | None = None
    title: str | None = None


class Boot(RedfishModel):
    alias_boot_order: list[str] | None = None
    boot_next: str | None = None
    boot_options: IdRef | None = None
    boot_order: list[str] | None = None
    boot_order_property_selection: str | None = None
    boot_source_override_enabled: str | None = None
    boot_source_override_mode: str | None = None
    boot_source_override_target: str | None = None
    certificates: IdRef | None = None
    http_boot_uri: str | None = None
    uefi_target_boot_source_override: str | None = None


class BootSource(StrEnum):
    NONE = "None"
    PXE = "Pxe"
    FLOPPY = "Floppy"
    CD = "Cd"
    USB = "Usb"
    HDD = "Hdd"
    BIOS_SETUP = "BiosSetup"
    UTILITIES = "Utilities"
    DIAGS = "Diags"
    UEFI_SHELL = "UefiShell"
    UEFI_TARGET = "UefiTarget"
    SDCARD = "SDCard"
    UEFI_HTTP = "UefiHttp"
    REMOTE_DRIVE = "RemoteDrive"
    UEFI_BOOT_NEXT = "UefiBootNext"
    RECOVERY = "Recovery"


class ComputerSystem(RedfishResource):
    actions: Actions | None = None
    asset_tag: str | None = None
    bios: IdRef | None = None
    bios_version: str | None = None
    boot: Boot | None = None
    description: str | None = None
    ethernet_interfaces: IdRef | None = None
    host_name: str | None = None
    host_watchdog_timer: WatchdogTimer | None = None
    hosted_services: HostedServices | None = None
    hosting_roles: list[HostingRole] | None = None
    indicator_led: str | None = None
    links: Links | None = None
    log_services: IdRef | None = None
    manufacturer: str | None = None
    memory: IdRef | None = None
    memory_domains: IdRef | None = None
    memory_summary: MemorySummary | None = None
    model: str | None = None
    network_interfaces: IdRef | None = None
    oem: dict[str, Any] | None = None
    pcie_devices: list[IdRef] | None = None
    pcie_functions: list[IdRef] | None = None
    part_number: str | None = None
    power_restore_policy: PowerRestorePolicyTypes | None = None
    power_state: str | None = None
    processor_summary: ProcessorSummary | None = None
    processors: IdRef | None = None
    redundancy: list[IdRef] | None = None
    sku: str | None = None
    secure_boot: IdRef | None = None
    serial_number: str | None = None
    simple_storage: IdRef | None = None
    status: Status | None = None
    storage: IdRef | None = None
    sub_model: str | None = None
    system_type: SystemType | None = None
    trusted_modules: list[TrustedModules] | None = None
    uuid: str | None = None


class HostedServices(RedfishModel):
    oem: dict[str, Any] | None = None
    storage_services: IdRef | None = None


class HostingRole(StrEnum):
    APPLICATION_SERVER = "ApplicationServer"
    STORAGE_SERVER = "StorageServer"
    SWITCH = "Switch"


class Links(RedfishModel):
    chassis: list[IdRef] | None = None
    consuming_computer_systems: list[IdRef] | None = None
    cooled_by: list[IdRef] | None = None
    endpoints: list[IdRef] | None = None
    managed_by: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    powered_by: list[IdRef] | None = None
    resource_blocks: list[IdRef] | None = None
    supplying_computer_systems: list[IdRef] | None = None


class MemorySummary(RedfishModel):
    memory_mirroring: str | None = None
    metrics: IdRef | None = None
    status: Status | None = None
    total_system_memory_gi_b: str | None = None
    total_system_persistent_memory_gi_b: str | None = None


class PowerRestorePolicyTypes(StrEnum):
    ALWAYS_ON = "AlwaysOn"
    ALWAYS_OFF = "AlwaysOff"
    LAST_STATE = "LastState"


class ProcessorSummary(RedfishModel):
    count: str | None = None
    logical_processor_count: str | None = None
    metrics: IdRef | None = None
    model: str | None = None
    status: Status | None = None


class RemoveResourceBlock(RedfishModel):
    target: str | None = None
    title: str | None = None


class Reset(RedfishModel):
    target: str | None = None
    title: str | None = None


class SetDefaultBootOrder(RedfishModel):
    target: str | None = None
    title: str | None = None


class SystemType(StrEnum):
    PHYSICAL = "Physical"
    VIRTUAL = "Virtual"
    OS = "OS"
    PHYSICALLY_PARTITIONED = "PhysicallyPartitioned"
    VIRTUALLY_PARTITIONED = "VirtuallyPartitioned"
    COMPOSED = "Composed"


class TrustedModules(RedfishModel):
    firmware_version: str | None = None
    firmware_version2: str | None = None
    interface_type: str | None = None
    interface_type_selection: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class WatchdogTimer(RedfishModel):
    function_enabled: str
    oem: dict[str, Any] | None = None
    status: Status | None = None
    timeout_action: str
    warning_action: str | None = None
