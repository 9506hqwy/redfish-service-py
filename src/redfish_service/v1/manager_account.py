from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class AccountTypes(StrEnum):
    REDFISH = "Redfish"
    SNMP = "SNMP"
    OEM = "OEM"
    HOST_CONSOLE = "HostConsole"
    MANAGER_CONSOLE = "ManagerConsole"
    IPMI = "IPMI"
    KVMIP = "KVMIP"
    VIRTUAL_MEDIA = "VirtualMedia"
    WEB_UI = "WebUI"


class Actions(RedfishModel):
    oem: OemActions | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    role: IdRef | None = None


class ManagerAccount(RedfishResource):
    account_expiration: str | None = None
    account_types: list[str]
    actions: Actions | None = None
    certificates: IdRef | None = None
    description: str | None = None
    enabled: bool | None = None
    host_bootstrap_account: bool | None = None
    keys: IdRef | None = None
    links: Links | None = None
    locked: bool | None = None
    oemaccount_types: list[str] | None = None
    oem: dict[str, Any] | None = None
    password: str | None = None
    password_change_required: str | None = None
    password_expiration: str | None = None
    role_id: str | None = None
    snmp: str | None = None
    strict_account_types: str | None = None
    user_name: str | None = None


class OemActions(RedfishModel):
    pass
