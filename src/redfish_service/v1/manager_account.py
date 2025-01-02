from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .account_service import MfaBypass
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
    account_types: list[AccountTypes]
    actions: Actions | None = None
    certificates: IdRef | None = None
    description: str | None = None
    email_address: str | None = None
    enabled: bool | None = None
    host_bootstrap_account: bool | None = None
    keys: IdRef | None = None
    links: Links | None = None
    locked: bool | None = None
    mfa_bypass: MfaBypass | None = Field(alias="MFABypass", default=None)
    oem_account_types: list[str] | None = Field(alias="OEMAccountTypes", default=None)
    oem: dict[str, Any] | None = None
    one_time_passcode_delivery_address: str | None = None
    password: str | None = None
    password_change_required: bool | None = None
    password_expiration: str | None = None
    phone_number: str | None = None
    role_id: str | None = None
    snmp: SnmpUserInfo | None = Field(alias="SNMP", default=None)
    secret_key_set: bool | None = None
    strict_account_types: bool | None = None
    user_name: str | None = None


class SnmpAuthenticationProtocols(StrEnum):
    NONE = "None"
    HMA_C_MD5 = "HMAC_MD5"
    HMA_C_SHA96 = "HMAC_SHA96"
    HMA_C128_SHA224 = "HMAC128_SHA224"
    HMA_C192_SHA256 = "HMAC192_SHA256"
    HMA_C256_SHA384 = "HMAC256_SHA384"
    HMA_C384_SHA512 = "HMAC384_SHA512"


class SnmpEncryptionProtocols(StrEnum):
    NONE = "None"
    CB_C_DES = "CBC_DES"
    CF_B128_AES128 = "CFB128_AES128"
    CF_B128_AES192 = "CFB128_AES192"
    CF_B128_AES256 = "CFB128_AES256"


class SnmpUserInfo(RedfishModel):
    authentication_key: str | None = None
    authentication_key_set: bool | None = None
    authentication_protocol: SnmpAuthenticationProtocols | None = None
    encryption_key: str | None = None
    encryption_key_set: bool | None = None
    encryption_protocol: SnmpEncryptionProtocols | None = None


class VerifyTimeBasedOneTimePassword(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
