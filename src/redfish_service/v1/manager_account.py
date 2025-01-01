from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

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
    change_password: ChangePassword | None = Field(
        alias="#ManagerAccount.ChangePassword", default=None
    )
    clear_secret_key: ClearSecretKey | None = Field(
        alias="#ManagerAccount.ClearSecretKey", default=None
    )
    generate_secret_key: GenerateSecretKey | None = Field(
        alias="#ManagerAccount.GenerateSecretKey", default=None
    )
    verify_time_based_one_time_password: VerifyTimeBasedOneTimePassword | None = Field(
        alias="#ManagerAccount.VerifyTimeBasedOneTimePassword", default=None
    )
    oem: dict[str, Any] | None = None


class ChangePassword(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ClearSecretKey(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class GenerateSecretKey(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    role: IdRef | None = None


class ManagerAccount(RedfishResource):
    account_expiration: str | None = None
    account_types: list[str]
    actions: Actions | None = None
    certificates: IdRef | None = None
    description: str | None = None
    email_address: str | None = None
    enabled: bool | None = None
    host_bootstrap_account: bool | None = None
    keys: IdRef | None = None
    links: Links | None = None
    locked: bool | None = None
    mfabypass: str | None = Field(alias="MFABypass", default=None)
    oemaccount_types: list[str] | None = Field(alias="OEMAccountTypes", default=None)
    oem: dict[str, Any] | None = None
    one_time_passcode_delivery_address: str | None = None
    password: str | None = None
    password_change_required: str | None = None
    password_expiration: str | None = None
    phone_number: str | None = None
    role_id: str | None = None
    snmp: str | None = Field(alias="SNMP", default=None)
    secret_key_set: bool | None = None
    strict_account_types: str | None = None
    user_name: str | None = None


class VerifyTimeBasedOneTimePassword(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
