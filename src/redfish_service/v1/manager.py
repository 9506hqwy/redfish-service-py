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
    oem: OemActions | None = None


class CommandConnectTypesSupported(StrEnum):
    SSH = "SSH"
    TELNET = "Telnet"
    IPMI = "IPMI"
    OEM = "Oem"


class CommandShell(RedfishModel):
    connect_types_supported: list[CommandConnectTypesSupported] | None = None
    max_concurrent_sessions: int | None = None
    service_enabled: bool | None = None


class ForceFailover(RedfishModel):
    target: str | None = None
    title: str | None = None


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
    manager_for_chassis: list[IdRef] | None = None
    manager_for_managers: list[IdRef] | None = None
    manager_for_servers: list[IdRef] | None = None
    manager_for_switches: list[IdRef] | None = None
    manager_in_chassis: IdRef | None = None
    oem: dict[str, Any] | None = None
    software_images: list[IdRef] | None = None


class Manager(RedfishResource):
    actions: Actions | None = None
    auto_dstenabled: bool | None = None
    command_shell: CommandShell | None = None
    date_time: str | None = None
    date_time_local_offset: str | None = None
    description: str | None = None
    ethernet_interfaces: IdRef | None = None
    firmware_version: str | None = None
    graphical_console: GraphicalConsole | None = None
    host_interfaces: IdRef | None = None
    last_reset_time: str | None = None
    links: Links | None = None
    log_services: IdRef | None = None
    manager_type: ManagerType | None = None
    manufacturer: str | None = None
    model: str | None = None
    network_protocol: IdRef | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    power_state: str | None = None
    redundancy: list[IdRef] | None = None
    remote_account_service: IdRef | None = None
    remote_redfish_service_uri: str | None = None
    serial_console: SerialConsole | None = None
    serial_interfaces: IdRef | None = None
    serial_number: str | None = None
    service_entry_point_uuid: str | None = None
    status: Status | None = None
    uuid: str | None = None
    virtual_media: IdRef | None = None


class ManagerType(StrEnum):
    MANAGEMENT_CONTROLLER = "ManagementController"
    ENCLOSURE_MANAGER = "EnclosureManager"
    BMC = "BMC"
    RACK_MANAGER = "RackManager"
    AUXILIARY_CONTROLLER = "AuxiliaryController"
    SERVICE = "Service"


class ModifyRedundancySet(RedfishModel):
    target: str | None = None
    title: str | None = None


class OemActions(RedfishModel):
    pass


class Reset(RedfishModel):
    target: str | None = None
    title: str | None = None


class ResetToDefaults(RedfishModel):
    target: str | None = None
    title: str | None = None


class SerialConnectTypesSupported(StrEnum):
    SSH = "SSH"
    TELNET = "Telnet"
    IPMI = "IPMI"
    OEM = "Oem"


class SerialConsole(RedfishModel):
    connect_types_supported: list[SerialConnectTypesSupported] | None = None
    max_concurrent_sessions: int | None = None
    service_enabled: bool | None = None
