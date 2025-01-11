from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AuthenticationMode(StrEnum):
    AUTH_NONE = "AuthNone"
    BASIC_AUTH = "BasicAuth"
    REDFISH_SESSION_AUTH = "RedfishSessionAuth"
    OEM_AUTH = "OemAuth"


class CredentialBootstrapping(RedfishModel):
    enable_after_reset: bool | None = None
    enabled: bool | None = None
    role_id: str | None = None


class HostInterface(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#HostInterface.v1_3_2.HostInterface")
    actions: Actions | None = None
    auth_none_role_id: str | None = None
    authentication_modes: list[AuthenticationMode] | None = None
    credential_bootstrapping: CredentialBootstrapping | None = None
    description: str | None = None
    externally_accessible: bool | None = None
    firmware_auth_enabled: bool | None = None
    firmware_auth_role_id: str | None = None
    host_ethernet_interfaces: IdRef | None = None
    host_interface_type: HostInterfaceType | None = None
    id: str
    interface_enabled: bool | None = None
    kernel_auth_enabled: bool | None = None
    kernel_auth_role_id: str | None = None
    links: Links | None = None
    manager_ethernet_interface: IdRef | None = None
    name: str
    network_protocol: IdRef | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class HostInterfaceOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(
        alias="@odata.type", default="#HostInterface.v1_3_2.HostInterface"
    )
    actions: Actions | None = None
    auth_none_role_id: str | None = None
    authentication_modes: list[AuthenticationMode] | None = None
    credential_bootstrapping: CredentialBootstrapping | None = None
    description: str | None = None
    externally_accessible: bool | None = None
    firmware_auth_enabled: bool | None = None
    firmware_auth_role_id: str | None = None
    host_ethernet_interfaces: IdRef | None = None
    host_interface_type: HostInterfaceType | None = None
    id: str | None = None
    interface_enabled: bool | None = None
    kernel_auth_enabled: bool | None = None
    kernel_auth_role_id: str | None = None
    links: Links | None = None
    manager_ethernet_interface: IdRef | None = None
    name: str | None = None
    network_protocol: IdRef | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class HostInterfaceType(StrEnum):
    NETWORK_HOST_INTERFACE = "NetworkHostInterface"


class Links(RedfishModel):
    auth_none_role: IdRef | None = None
    computer_systems: list[IdRef] | None = None
    computer_systems_odata_count: int | None = Field(
        alias="ComputerSystems@odata.count", default=None
    )
    credential_bootstrapping_role: IdRef | None = None
    firmware_auth_role: IdRef | None = None
    kernel_auth_role: IdRef | None = None
    oem: dict[str, Any] | None = None
