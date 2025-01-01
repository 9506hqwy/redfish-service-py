from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .account_service import Mfabypass
from .base import (
    RedfishModel,
    RedfishResource,
)
from .manager_account import AccountTypes
from .odata_v4 import IdRef


class AccountProviderTypes(StrEnum):
    REDFISH_SERVICE = "RedfishService"
    ACTIVE_DIRECTORY_SERVICE = "ActiveDirectoryService"
    LDAPSERVICE = "LDAPService"
    OEM = "OEM"
    TACACSPLUS = "TACACSplus"
    OAUTH2 = "OAuth2"


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Authentication(RedfishModel):
    authentication_type: AuthenticationTypes | None = None
    encryption_key: str | None = None
    encryption_key_set: bool | None = None
    kerberos_keytab: str | None = None
    oem: dict[str, Any] | None = None
    password: str | None = None
    token: str | None = None
    username: str | None = None


class AuthenticationTypes(StrEnum):
    TOKEN = "Token"  # noqa: S105
    KERBEROS_KEYTAB = "KerberosKeytab"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"  # noqa: S105
    OEM = "OEM"


class ExternalAccountProvider(RedfishResource):
    account_provider_type: AccountProviderTypes | None = None
    actions: Actions | None = None
    authentication: Authentication | None = None
    certificates: IdRef | None = None
    description: str | None = None
    ldapservice: Ldapservice | None = Field(alias="LDAPService", default=None)
    links: Links | None = None
    oauth2_service: Oauth2Service | None = Field(alias="OAuth2Service", default=None)
    oem: dict[str, Any] | None = None
    priority: int | None = None
    remote_role_mapping: list[RoleMapping] | None = None
    retries: int | None = None
    service_addresses: list[str] | None = None
    service_enabled: bool | None = None
    tacacsplus_service: TacacsplusService | None = Field(alias="TACACSplusService", default=None)
    timeout_seconds: int | None = None


class LdapsearchSettings(RedfishModel):
    base_distinguished_names: list[str] | None = None
    email_attribute: str | None = None
    group_name_attribute: str | None = None
    groups_attribute: str | None = None
    sshkey_attribute: str | None = Field(alias="SSHKeyAttribute", default=None)
    username_attribute: str | None = None


class Ldapservice(RedfishModel):
    oem: dict[str, Any] | None = None
    search_settings: LdapsearchSettings | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None


class Oauth2Mode(StrEnum):
    DISCOVERY = "Discovery"
    OFFLINE = "Offline"


class Oauth2Service(RedfishModel):
    audience: list[str] | None = None
    issuer: str | None = None
    mode: Oauth2Mode | None = None
    oauth_service_signing_keys: str | None = Field(alias="OAuthServiceSigningKeys", default=None)
    oem: dict[str, Any] | None = None


class RoleMapping(RedfishModel):
    local_account_types: list[AccountTypes] | None = None
    local_oemaccount_types: list[str] | None = Field(alias="LocalOEMAccountTypes", default=None)
    local_role: str | None = None
    mfabypass: Mfabypass | None = Field(alias="MFABypass", default=None)
    oem: dict[str, Any] | None = None
    remote_group: str | None = None
    remote_user: str | None = None


class TacacsplusPasswordExchangeProtocol(StrEnum):
    ASCII = "ASCII"
    PAP = "PAP"
    CHAP = "CHAP"
    MSCHAPV1 = "MSCHAPv1"
    MSCHAPV2 = "MSCHAPv2"


class TacacsplusService(RedfishModel):
    authorization_service: str | None = None
    oem: dict[str, Any] | None = None
    password_exchange_protocols: list[TacacsplusPasswordExchangeProtocol] | None = None
    privilege_level_argument: str | None = None
