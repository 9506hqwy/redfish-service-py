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


class AuthenticationMode(StrEnum):
    AUTH_NONE = "AuthNone"
    BASIC_AUTH = "BasicAuth"
    REDFISH_SESSION_AUTH = "RedfishSessionAuth"
    OEM_AUTH = "OemAuth"


class CredentialBootstrapping(RedfishModel):
    enable_after_reset: str | None = None
    enabled: str | None = None
    role_id: str | None = None


class HostInterface(RedfishResource):
    actions: Actions | None = None
    auth_none_role_id: str | None = None
    authentication_modes: list[AuthenticationMode] | None = None
    credential_bootstrapping: CredentialBootstrapping | None = None
    description: str | None = None
    externally_accessible: str | None = None
    firmware_auth_enabled: str | None = None
    firmware_auth_role_id: str | None = None
    host_ethernet_interfaces: IdRef | None = None
    host_interface_type: str | None = None
    interface_enabled: str | None = None
    kernel_auth_enabled: str | None = None
    kernel_auth_role_id: str | None = None
    links: Links | None = None
    manager_ethernet_interface: IdRef | None = None
    network_protocol: IdRef | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class Links(RedfishModel):
    auth_none_role: IdRef | None = None
    computer_systems: list[IdRef] | None = None
    credential_bootstrapping_role: IdRef | None = None
    firmware_auth_role: IdRef | None = None
    kernel_auth_role: IdRef | None = None
    oem: dict[str, Any] | None = None


class OemActions(RedfishModel):
    pass
