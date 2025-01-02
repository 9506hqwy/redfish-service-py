from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import RedfishModel
from .odata_v4 import IdRef
from .resource import PowerState, Status
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


class AutomaticRetryConfig(StrEnum):
    DISABLED = "Disabled"
    RETRY_ATTEMPTS = "RetryAttempts"
    RETRY_ALWAYS = "RetryAlways"


class Boot(RedfishModel):
    alias_boot_order: list[BootSource] | None = None
    automatic_retry_attempts: int | None = None
    automatic_retry_config: AutomaticRetryConfig | None = None
    boot_next: str | None = None
    boot_options: IdRef | None = None
    boot_order: list[str] | None = None
    boot_order_property_selection: BootOrderTypes | None = None
    boot_source_override_enabled: BootSourceOverrideEnabled | None = None
    boot_source_override_mode: BootSourceOverrideMode | None = None
    boot_source_override_target: BootSource | None = None
    certificates: IdRef | None = None
    http_boot_uri: str | None = None
    remaining_automatic_retry_attempts: int | None = None
    stop_boot_on_fault: StopBootOnFault | None = None
    trusted_module_required_to_boot: TrustedModuleRequiredToBoot | None = None
    uefi_target_boot_source_override: str | None = None


class BootOrderTypes(StrEnum):
    BOOT_ORDER = "BootOrder"
    ALIAS_BOOT_ORDER = "AliasBootOrder"


class BootProgress(RedfishModel):
    last_boot_time_seconds: float | None = None
    last_state: BootProgressTypes | None = None
    last_state_time: str | None = None
    oem: dict[str, Any] | None = None
    oem_last_state: str | None = None


class BootProgressTypes(StrEnum):
    NONE = "None"
    PRIMARY_PROCESSOR_INITIALIZATION_STARTED = "PrimaryProcessorInitializationStarted"
    BUS_INITIALIZATION_STARTED = "BusInitializationStarted"
    MEMORY_INITIALIZATION_STARTED = "MemoryInitializationStarted"
    SECONDARY_PROCESSOR_INITIALIZATION_STARTED = "SecondaryProcessorInitializationStarted"
    PCI_RESOURCE_CONFIG_STARTED = "PCIResourceConfigStarted"
    SYSTEM_HARDWARE_INITIALIZATION_COMPLETE = "SystemHardwareInitializationComplete"
    SETUP_ENTERED = "SetupEntered"
    OS_BOOT_STARTED = "OSBootStarted"
    OS_RUNNING = "OSRunning"
    OEM = "OEM"


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
    SD_CARD = "SDCard"
    UEFI_HTTP = "UefiHttp"
    REMOTE_DRIVE = "RemoteDrive"
    UEFI_BOOT_NEXT = "UefiBootNext"
    RECOVERY = "Recovery"


class BootSourceOverrideEnabled(StrEnum):
    DISABLED = "Disabled"
    ONCE = "Once"
    CONTINUOUS = "Continuous"


class BootSourceOverrideMode(StrEnum):
    LEGACY = "Legacy"
    UEFI = "UEFI"


class Composition(RedfishModel):
    use_cases: list[CompositionUseCase] | None = None


class CompositionUseCase(StrEnum):
    RESOURCE_BLOCK_CAPABLE = "ResourceBlockCapable"
    EXPANDABLE_SYSTEM = "ExpandableSystem"


class ComputerSystem(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    asset_tag: str | None = None
    bios: IdRef | None = None
    bios_version: str | None = None
    boot: Boot | None = None
    boot_progress: BootProgress | None = None
    certificates: IdRef | None = None
    composition: Composition | None = None
    description: str | None = None
    ethernet_interfaces: IdRef | None = None
    fabric_adapters: IdRef | None = None
    graphical_console: HostGraphicalConsole | None = None
    graphics_controllers: IdRef | None = None
    host_name: str | None = None
    host_watchdog_timer: WatchdogTimer | None = None
    hosted_services: HostedServices | None = None
    hosting_roles: list[HostingRole] | None = None
    id: str
    idle_power_saver: IdlePowerSaver | None = None
    indicator_led: IndicatorLed | None = Field(alias="IndicatorLED", default=None)
    key_management: KeyManagement | None = None
    last_reset_cause: LastResetCauses | None = None
    last_reset_time: str | None = None
    links: Links | None = None
    location_indicator_active: bool | None = None
    log_services: IdRef | None = None
    manufacturer: str | None = None
    manufacturing_mode: bool | None = None
    measurements: list[MeasurementBlock] | None = None
    memory: IdRef | None = None
    memory_domains: IdRef | None = None
    memory_summary: MemorySummary | None = None
    model: str | None = None
    name: str
    network_interfaces: IdRef | None = None
    oem: dict[str, Any] | None = None
    operating_system: IdRef | None = None
    pcie_devices: list[IdRef] | None = Field(alias="PCIeDevices", default=None)
    pcie_devices_odata_count: int | None = Field(alias="PCIeDevices@odata.count", default=None)
    pcie_functions: list[IdRef] | None = Field(alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(alias="PCIeFunctions@odata.count", default=None)
    part_number: str | None = None
    power_cycle_delay_seconds: float | None = None
    power_mode: PowerMode | None = None
    power_off_delay_seconds: float | None = None
    power_on_delay_seconds: float | None = None
    power_restore_policy: PowerRestorePolicyTypes | None = None
    power_state: PowerState | None = None
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
    usb_controllers: IdRef | None = Field(alias="USBControllers", default=None)
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
    port: int | None = None
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


class IdlePowerSaver(RedfishModel):
    enabled: bool | None = None
    enter_dwell_time_seconds: int | None = None
    enter_utilization_percent: float | None = None
    exit_dwell_time_seconds: int | None = None
    exit_utilization_percent: float | None = None


class IndicatorLed(StrEnum):
    UNKNOWN = "Unknown"
    LIT = "Lit"
    BLINKING = "Blinking"
    OFF = "Off"


class InterfaceType(StrEnum):
    TP_M1_2 = "TPM1_2"
    TP_M2_0 = "TPM2_0"
    TC_M1_0 = "TCM1_0"


class InterfaceTypeSelection(StrEnum):
    NONE = "None"
    FIRMWARE_UPDATE = "FirmwareUpdate"
    BIOS_SETTING = "BiosSetting"
    OEM_METHOD = "OemMethod"


class KmipCachePolicy(StrEnum):
    NONE = "None"
    AFTER_FIRST_USE = "AfterFirstUse"


class KmipServer(RedfishModel):
    address: str | None = None
    cache_duration: str | None = None
    cache_policy: KmipCachePolicy | None = None
    password: str | None = None
    port: int | None = None
    username: str | None = None


class KeyManagement(RedfishModel):
    kmip_certificates: IdRef | None = Field(alias="KMIPCertificates", default=None)
    kmip_servers: list[KmipServer] | None = Field(alias="KMIPServers", default=None)


class LastResetCauses(StrEnum):
    POWER_BUTTON_PRESS = "PowerButtonPress"
    MANAGEMENT_COMMAND = "ManagementCommand"
    POWER_RESTORE_POLICY = "PowerRestorePolicy"
    RTC_WAKEUP = "RTCWakeup"
    WATCHDOG_EXPIRATION = "WatchdogExpiration"
    OS_SOFT_RESTART = "OSSoftRestart"
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
    hosting_computer_system: IdRef | None = None
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


class MemoryMirroring(StrEnum):
    SYSTEM = "System"
    DIMM = "DIMM"
    HYBRID = "Hybrid"
    NONE = "None"


class MemorySummary(RedfishModel):
    memory_mirroring: MemoryMirroring | None = None
    metrics: IdRef | None = None
    status: Status | None = None
    total_system_memory_gib: float | None = Field(alias="TotalSystemMemoryGiB", default=None)
    total_system_persistent_memory_gib: float | None = Field(
        alias="TotalSystemPersistentMemoryGiB", default=None
    )


class PowerMode(StrEnum):
    MAXIMUM_PERFORMANCE = "MaximumPerformance"
    BALANCED_PERFORMANCE = "BalancedPerformance"
    POWER_SAVING = "PowerSaving"
    STATIC = "Static"
    OS_CONTROLLED = "OSControlled"
    OEM = "OEM"
    EFFICIENCY_FAVOR_POWER = "EfficiencyFavorPower"
    EFFICIENCY_FAVOR_PERFORMANCE = "EfficiencyFavorPerformance"


class PowerRestorePolicyTypes(StrEnum):
    ALWAYS_ON = "AlwaysOn"
    ALWAYS_OFF = "AlwaysOff"
    LAST_STATE = "LastState"


class ProcessorSummary(RedfishModel):
    core_count: int | None = None
    count: int | None = None
    logical_processor_count: int | None = None
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
    port: int | None = None
    service_enabled: bool | None = None
    shared_with_manager_cli: bool | None = Field(alias="SharedWithManagerCLI", default=None)


class SetDefaultBootOrder(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class StopBootOnFault(StrEnum):
    NEVER = "Never"
    ANY_FAULT = "AnyFault"


class SystemType(StrEnum):
    PHYSICAL = "Physical"
    VIRTUAL = "Virtual"
    OS = "OS"
    PHYSICALLY_PARTITIONED = "PhysicallyPartitioned"
    VIRTUALLY_PARTITIONED = "VirtuallyPartitioned"
    COMPOSED = "Composed"
    DPU = "DPU"


class TrustedModuleRequiredToBoot(StrEnum):
    DISABLED = "Disabled"
    REQUIRED = "Required"


class TrustedModules(RedfishModel):
    firmware_version: str | None = None
    firmware_version2: str | None = None
    interface_type: InterfaceType | None = None
    interface_type_selection: InterfaceTypeSelection | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class VirtualMediaConfig(RedfishModel):
    port: int | None = None
    service_enabled: bool | None = None


class WatchdogTimeoutActions(StrEnum):
    NONE = "None"
    RESET_SYSTEM = "ResetSystem"
    POWER_CYCLE = "PowerCycle"
    POWER_DOWN = "PowerDown"
    OEM = "OEM"


class WatchdogTimer(RedfishModel):
    function_enabled: bool | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    timeout_action: WatchdogTimeoutActions | None = None
    warning_action: WatchdogWarningActions | None = None


class WatchdogWarningActions(StrEnum):
    NONE = "None"
    DIAGNOSTIC_INTERRUPT = "DiagnosticInterrupt"
    SMI = "SMI"
    MESSAGING_INTERRUPT = "MessagingInterrupt"
    SCI = "SCI"
    OEM = "OEM"
