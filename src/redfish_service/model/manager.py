from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Location, PowerState, ResetType, Status
from .software_inventory import AdditionalVersions, MeasurementBlock


class Actions(RedfishModel):
    force_failover: ForceFailover | None = Field(
        serialization_alias="#Manager.ForceFailover", default=None
    )
    modify_redundancy_set: ModifyRedundancySet | None = Field(
        serialization_alias="#Manager.ModifyRedundancySet", default=None
    )
    reset: Reset | None = Field(serialization_alias="#Manager.Reset", default=None)
    reset_to_defaults: ResetToDefaults | None = Field(
        serialization_alias="#Manager.ResetToDefaults", default=None
    )
    update_security_mode: UpdateSecurityMode | None = Field(
        serialization_alias="#Manager.UpdateSecurityMode", default=None
    )
    oem: dict[str, Any] | None = None


class CommandConnectTypesSupported(StrEnum):
    SSH = "SSH"
    TELNET = "Telnet"
    IPMI = "IPMI"
    OEM = "Oem"


class CommandShell(RedfishModel):
    connect_types_supported: list[CommandConnectTypesSupported] | None = None
    max_concurrent_sessions: int | None = None
    service_enabled: bool | None = None


class DateTimeSource(StrEnum):
    RTC = "RTC"
    FIRMWARE = "Firmware"
    HOST = "Host"
    NTP = "NTP"
    PTP = "PTP"


class DaylightSavingTime(RedfishModel):
    end_date_time: str | None = None
    offset_minutes: int | None = None
    start_date_time: str | None = None
    time_zone_name: str | None = None


class ForceFailover(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ForceFailoverRequest(RedfishModel):
    new_manager: IdRef


class GraphicalConnectTypesSupported(StrEnum):
    KVMIP = "KVMIP"
    OEM = "Oem"


class GraphicalConsole(RedfishModel):
    connect_types_supported: list[GraphicalConnectTypesSupported] | None = None
    max_concurrent_sessions: int | None = None
    service_enabled: bool | None = None


class Links(RedfishModel):
    active_software_image: IdRef | None = None
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(
        serialization_alias="ManagedBy@odata.count", default=None
    )
    manager_for_chassis: list[IdRef] | None = None
    manager_for_chassis_odata_count: int | None = Field(
        serialization_alias="ManagerForChassis@odata.count", default=None
    )
    manager_for_fabrics: list[IdRef] | None = None
    manager_for_fabrics_odata_count: int | None = Field(
        serialization_alias="ManagerForFabrics@odata.count", default=None
    )
    manager_for_managers: list[IdRef] | None = None
    manager_for_managers_odata_count: int | None = Field(
        serialization_alias="ManagerForManagers@odata.count", default=None
    )
    manager_for_servers: list[IdRef] | None = None
    manager_for_servers_odata_count: int | None = Field(
        serialization_alias="ManagerForServers@odata.count", default=None
    )
    manager_for_switches: list[IdRef] | None = None
    manager_for_switches_odata_count: int | None = Field(
        serialization_alias="ManagerForSwitches@odata.count", default=None
    )
    manager_in_chassis: IdRef | None = None
    oem: dict[str, Any] | None = None
    selected_network_port: IdRef | None = None
    software_images: list[IdRef] | None = None
    software_images_odata_count: int | None = Field(
        serialization_alias="SoftwareImages@odata.count", default=None
    )


class Manager(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Manager.v1_24_0.Manager")
    actions: Actions | None = None
    additional_firmware_versions: AdditionalVersions | None = None
    auto_dst_enabled: bool | None = Field(serialization_alias="AutoDSTEnabled", default=None)
    certificates: IdRef | None = None
    command_shell: CommandShell | None = None
    date_time: str | None = None
    date_time_local_offset: str | None = None
    date_time_source: DateTimeSource | None = None
    daylight_saving_time: DaylightSavingTime | None = None
    dedicated_network_ports: IdRef | None = None
    description: str | None = None
    ethernet_interfaces: IdRef | None = None
    firmware_version: str | None = None
    graphical_console: GraphicalConsole | None = None
    host_interfaces: IdRef | None = None
    id: str
    last_reset_time: str | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    log_services: IdRef | None = None
    manager_diagnostic_data: IdRef | None = None
    manager_type: ManagerType | None = None
    manufacturer: str | None = None
    measurements: list[MeasurementBlock] | None = None
    model: str | None = None
    name: str
    network_protocol: IdRef | None = None
    oem_security_mode: str | None = Field(serialization_alias="OEMSecurityMode", default=None)
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    power_state: PowerState | None = None
    ready_to_remove: bool | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(
        serialization_alias="Redundancy@odata.count", default=None
    )
    remote_account_service: IdRef | None = None
    remote_redfish_service_uri: str | None = None
    security_mode: SecurityModeTypes | None = None
    security_policy: IdRef | None = None
    serial_console: SerialConsole | None = None
    serial_interfaces: IdRef | None = None
    serial_number: str | None = None
    service_entry_point_uuid: str | None = Field(
        serialization_alias="ServiceEntryPointUUID", default=None
    )
    service_identification: str | None = None
    service_use_notification: str | None = None
    shared_network_ports: IdRef | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    time_zone_name: str | None = None
    usb_ports: IdRef | None = Field(serialization_alias="USBPorts", default=None)
    uuid: str | None = Field(serialization_alias="UUID", default=None)
    version: str | None = None
    virtual_media: IdRef | None = None


class ManagerOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    additional_firmware_versions: AdditionalVersions | None = None
    auto_dst_enabled: bool | None = Field(serialization_alias="AutoDSTEnabled", default=None)
    command_shell: CommandShell | None = None
    date_time: str | None = None
    date_time_local_offset: str | None = None
    date_time_source: DateTimeSource | None = None
    daylight_saving_time: DaylightSavingTime | None = None
    dedicated_network_ports: IdRef | None = None
    graphical_console: GraphicalConsole | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    measurements: list[MeasurementBlock] | None = None
    oem: dict[str, Any] | None = None
    ready_to_remove: bool | None = None
    redundancy: list[IdRef] | None = None
    serial_console: SerialConsole | None = None
    service_identification: str | None = None
    service_use_notification: str | None = None
    shared_network_ports: IdRef | None = None
    status: Status | None = None
    time_zone_name: str | None = None
    usb_ports: IdRef | None = Field(serialization_alias="USBPorts", default=None)


class ManagerType(StrEnum):
    MANAGEMENT_CONTROLLER = "ManagementController"
    ENCLOSURE_MANAGER = "EnclosureManager"
    BMC = "BMC"
    RACK_MANAGER = "RackManager"
    AUXILIARY_CONTROLLER = "AuxiliaryController"
    SERVICE = "Service"
    FABRIC_MANAGER = "FabricManager"


class ModifyRedundancySet(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ModifyRedundancySetRequest(RedfishModel):
    add: list[IdRef] | None = None
    remove: list[IdRef] | None = None


class Reset(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetRequest(RedfishModel):
    reset_type: ResetType | None = None


class ResetToDefaults(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetToDefaultsRequest(RedfishModel):
    reset_type: ResetToDefaultsType


class ResetToDefaultsType(StrEnum):
    RESET_ALL = "ResetAll"
    PRESERVE_NETWORK_AND_USERS = "PreserveNetworkAndUsers"
    PRESERVE_NETWORK = "PreserveNetwork"


class SecurityModeTypes(StrEnum):
    FIP_S_140_2 = "FIPS_140_2"
    FIP_S_140_3 = "FIPS_140_3"
    CNS_A_1_0 = "CNSA_1_0"
    CNS_A_2_0 = "CNSA_2_0"
    SUITE_B = "SuiteB"
    OEM = "OEM"
    DEFAULT = "Default"


class SerialConnectTypesSupported(StrEnum):
    SSH = "SSH"
    TELNET = "Telnet"
    IPMI = "IPMI"
    OEM = "Oem"


class SerialConsole(RedfishModel):
    connect_types_supported: list[SerialConnectTypesSupported] | None = None
    max_concurrent_sessions: int | None = None
    service_enabled: bool | None = None


class UpdateSecurityMode(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class UpdateSecurityModeRequest(RedfishModel):
    oem_security_mode: str | None = Field(serialization_alias="OEMSecurityMode", default=None)
    security_mode: SecurityModeTypes
