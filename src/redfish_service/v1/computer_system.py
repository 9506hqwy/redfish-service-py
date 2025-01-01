from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status
from .software_inventory import MeasurementBlock


class Actions(RedfishModel):
    add_resource_block: AddResourceBlock | None = Field(
        alias="#ComputerSystem.AddResourceBlock", default=None
    )
    decommission: Decommission | None = Field(alias="#ComputerSystem.Decommission", default=None)
    remove_resource_block: RemoveResourceBlock | None = Field(
        alias="#ComputerSystem.RemoveResourceBlock", default=None
    )
    reset: Reset | None = Field(alias="#ComputerSystem.Reset", default=None)
    set_default_boot_order: SetDefaultBootOrder | None = Field(
        alias="#ComputerSystem.SetDefaultBootOrder", default=None
    )
    oem: dict[str, Any] | None = None


class AddResourceBlock(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Boot(RedfishModel):
    alias_boot_order: list[str] | None = None
    automatic_retry_attempts: str | None = None
    automatic_retry_config: str | None = None
    boot_next: str | None = None
    boot_options: IdRef | None = None
    boot_order: list[str] | None = None
    boot_order_property_selection: str | None = None
    boot_source_override_enabled: str | None = None
    boot_source_override_mode: str | None = None
    boot_source_override_target: str | None = None
    certificates: IdRef | None = None
    http_boot_uri: str | None = None
    remaining_automatic_retry_attempts: str | None = None
    stop_boot_on_fault: str | None = None
    trusted_module_required_to_boot: str | None = None
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
    boot_progress: str | None = None
    certificates: IdRef | None = None
    composition: str | None = None
    description: str | None = None
    ethernet_interfaces: IdRef | None = None
    fabric_adapters: IdRef | None = None
    graphical_console: HostGraphicalConsole | None = None
    graphics_controllers: IdRef | None = None
    host_name: str | None = None
    host_watchdog_timer: WatchdogTimer | None = None
    hosted_services: HostedServices | None = None
    hosting_roles: list[HostingRole] | None = None
    idle_power_saver: str | None = None
    indicator_led: str | None = Field(alias="IndicatorLED", default=None)
    key_management: str | None = None
    last_reset_cause: LastResetCauses | None = None
    last_reset_time: str | None = None
    links: Links | None = None
    location_indicator_active: str | None = None
    log_services: IdRef | None = None
    manufacturer: str | None = None
    manufacturing_mode: str | None = None
    measurements: list[MeasurementBlock] | None = None
    memory: IdRef | None = None
    memory_domains: IdRef | None = None
    memory_summary: MemorySummary | None = None
    model: str | None = None
    network_interfaces: IdRef | None = None
    oem: dict[str, Any] | None = None
    operating_system: IdRef | None = None
    pcie_devices: list[IdRef] | None = Field(alias="PCIeDevices", default=None)
    pcie_devices_odata_count: int | None = Field(alias="PCIeDevices@odata.count", default=None)
    pcie_functions: list[IdRef] | None = Field(alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(alias="PCIeFunctions@odata.count", default=None)
    part_number: str | None = None
    power_cycle_delay_seconds: str | None = None
    power_mode: str | None = None
    power_off_delay_seconds: str | None = None
    power_on_delay_seconds: str | None = None
    power_restore_policy: PowerRestorePolicyTypes | None = None
    power_state: str | None = None
    processor_summary: ProcessorSummary | None = None
    processors: IdRef | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(alias="Redundancy@odata.count", default=None)
    sku: str | None = Field(alias="SKU", default=None)
    secure_boot: IdRef | None = None
    serial_console: HostSerialConsole | None = None
    serial_number: str | None = None
    simple_storage: IdRef | None = None
    status: Status | None = None
    storage: IdRef | None = None
    sub_model: str | None = None
    system_type: SystemType | None = None
    trusted_modules: list[TrustedModules] | None = None
    usbcontrollers: IdRef | None = Field(alias="USBControllers", default=None)
    uuid: str | None = Field(alias="UUID", default=None)
    virtual_media: IdRef | None = None
    virtual_media_config: VirtualMediaConfig | None = None


class Decommission(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class GraphicalConnectTypesSupported(StrEnum):
    KVMIP = "KVMIP"
    OEM = "OEM"


class HostGraphicalConsole(RedfishModel):
    connect_types_supported: list[GraphicalConnectTypesSupported] | None = None
    max_concurrent_sessions: int | None = None
    port: str | None = None
    service_enabled: bool | None = None


class HostSerialConsole(RedfishModel):
    ipmi: SerialConsoleProtocol | None = Field(alias="IPMI", default=None)
    max_concurrent_sessions: int | None = None
    ssh: SerialConsoleProtocol | None = Field(alias="SSH", default=None)
    telnet: SerialConsoleProtocol | None = None


class HostedServices(RedfishModel):
    oem: dict[str, Any] | None = None
    storage_services: IdRef | None = None


class HostingRole(StrEnum):
    APPLICATION_SERVER = "ApplicationServer"
    STORAGE_SERVER = "StorageServer"
    SWITCH = "Switch"
    APPLIANCE = "Appliance"
    BARE_METAL_SERVER = "BareMetalServer"
    VIRTUAL_MACHINE_SERVER = "VirtualMachineServer"
    CONTAINER_SERVER = "ContainerServer"


class LastResetCauses(StrEnum):
    POWER_BUTTON_PRESS = "PowerButtonPress"
    MANAGEMENT_COMMAND = "ManagementCommand"
    POWER_RESTORE_POLICY = "PowerRestorePolicy"
    RTCWAKEUP = "RTCWakeup"
    WATCHDOG_EXPIRATION = "WatchdogExpiration"
    OSSOFT_RESTART = "OSSoftRestart"
    SYSTEM_CRASH = "SystemCrash"
    THERMAL_EVENT = "ThermalEvent"
    POWER_EVENT = "PowerEvent"
    UNKNOWN = "Unknown"


class Links(RedfishModel):
    chassis: list[IdRef] | None = None
    chassis_odata_count: int | None = Field(alias="Chassis@odata.count", default=None)
    consuming_computer_systems: list[IdRef] | None = None
    consuming_computer_systems_odata_count: int | None = Field(
        alias="ConsumingComputerSystems@odata.count", default=None
    )
    cooled_by: list[IdRef] | None = None
    cooled_by_odata_count: int | None = Field(alias="CooledBy@odata.count", default=None)
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    hosting_computer_system: str | None = None
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(alias="ManagedBy@odata.count", default=None)
    oem: dict[str, Any] | None = None
    offloaded_network_device_functions: list[IdRef] | None = None
    offloaded_network_device_functions_odata_count: int | None = Field(
        alias="OffloadedNetworkDeviceFunctions@odata.count", default=None
    )
    powered_by: list[IdRef] | None = None
    powered_by_odata_count: int | None = Field(alias="PoweredBy@odata.count", default=None)
    resource_blocks: list[IdRef] | None = None
    resource_blocks_odata_count: int | None = Field(
        alias="ResourceBlocks@odata.count", default=None
    )
    supplying_computer_systems: list[IdRef] | None = None
    supplying_computer_systems_odata_count: int | None = Field(
        alias="SupplyingComputerSystems@odata.count", default=None
    )
    trusted_components: list[IdRef] | None = None
    trusted_components_odata_count: int | None = Field(
        alias="TrustedComponents@odata.count", default=None
    )
    virtual_machines: list[IdRef] | None = None
    virtual_machines_odata_count: int | None = Field(
        alias="VirtualMachines@odata.count", default=None
    )


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
    core_count: str | None = None
    count: str | None = None
    logical_processor_count: str | None = None
    metrics: IdRef | None = None
    model: str | None = None
    status: Status | None = None
    threading_enabled: bool | None = None


class RemoveResourceBlock(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SerialConsoleProtocol(RedfishModel):
    console_entry_command: str | None = None
    hot_key_sequence_display: str | None = None
    port: str | None = None
    service_enabled: bool | None = None
    shared_with_manager_cli: bool | None = Field(alias="SharedWithManagerCLI", default=None)


class SetDefaultBootOrder(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SystemType(StrEnum):
    PHYSICAL = "Physical"
    VIRTUAL = "Virtual"
    OS = "OS"
    PHYSICALLY_PARTITIONED = "PhysicallyPartitioned"
    VIRTUALLY_PARTITIONED = "VirtuallyPartitioned"
    COMPOSED = "Composed"
    DPU = "DPU"


class TrustedModules(RedfishModel):
    firmware_version: str | None = None
    firmware_version2: str | None = None
    interface_type: str | None = None
    interface_type_selection: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class VirtualMediaConfig(RedfishModel):
    port: str | None = None
    service_enabled: bool | None = None


class WatchdogTimer(RedfishModel):
    function_enabled: str
    oem: dict[str, Any] | None = None
    status: Status | None = None
    timeout_action: str
    warning_action: str | None = None
