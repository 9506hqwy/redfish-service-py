from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .account_service import MfaBypass
from .manager_account import AccountTypes
from .odata_v4 import IdRef


class AccountProviderTypes(StrEnum):
    REDFISH_SERVICE = "RedfishService"
    ACTIVE_DIRECTORY_SERVICE = "ActiveDirectoryService"
    LDAP_SERVICE = "LDAPService"
    OEM = "OEM"
    TACACS_PLUS = "TACACSplus"
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


class ExternalAccountProvider(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    account_provider_type: AccountProviderTypes | None = None
    actions: Actions | None = None
    authentication: Authentication | None = None
    certificates: IdRef | None = None
    description: str | None = None
    id: str
    ldap_service: LdapService | None = Field(alias="LDAPService", default=None)
    links: Links | None = None
    name: str
    oauth2_service: Oauth2Service | None = Field(alias="OAuth2Service", default=None)
    oem: dict[str, Any] | None = None
    priority: int | None = None
    remote_role_mapping: list[RoleMapping] | None = None
    retries: int | None = None
    service_addresses: list[str] | None = None
    service_enabled: bool | None = None
    tacacs_plus_service: TacacsPlusService | None = Field(alias="TACACSplusService", default=None)
    timeout_seconds: int | None = None


class LdapSearchSettings(RedfishModel):
    base_distinguished_names: list[str] | None = None
    email_attribute: str | None = None
    group_name_attribute: str | None = None
    groups_attribute: str | None = None
    ssh_key_attribute: str | None = Field(alias="SSHKeyAttribute", default=None)
    username_attribute: str | None = None


class LdapService(RedfishModel):
    oem: dict[str, Any] | None = None
    search_settings: LdapSearchSettings | None = None


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
    local_oem_account_types: list[str] | None = Field(alias="LocalOEMAccountTypes", default=None)
    local_role: str | None = None
    mfa_bypass: MfaBypass | None = Field(alias="MFABypass", default=None)
    oem: dict[str, Any] | None = None
    remote_group: str | None = None
    remote_user: str | None = None


class TacacsPlusPasswordExchangeProtocol(StrEnum):
    ASCII = "ASCII"
    PAP = "PAP"
    CHAP = "CHAP"
    MSCHA_PV1 = "MSCHAPv1"
    MSCHA_PV2 = "MSCHAPv2"


class TacacsPlusService(RedfishModel):
    authorization_service: str | None = None
    oem: dict[str, Any] | None = None
    password_exchange_protocols: list[TacacsPlusPasswordExchangeProtocol] | None = None
    privilege_level_argument: str | None = None
