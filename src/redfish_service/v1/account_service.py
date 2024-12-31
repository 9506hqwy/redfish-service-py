from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .manager_account import AccountTypes
from .odata_v4 import IdRef
from .privileges import PrivilegeType
from .resource import Status


class AccountService(RedfishResource):
    account_lockout_counter_reset_after: int | None = None
    account_lockout_counter_reset_enabled: bool | None = None
    account_lockout_duration: str | None = None
    account_lockout_threshold: str | None = None
    accounts: IdRef | None = None
    actions: Actions | None = None
    active_directory: ExternalAccountProvider | None = None
    additional_external_account_providers: IdRef | None = None
    auth_failure_logging_threshold: int | None = None
    description: str | None = None
    ldap: ExternalAccountProvider | None = None
    local_account_auth: LocalAccountAuth | None = None
    max_password_length: int | None = None
    min_password_length: int | None = None
    oem: dict[str, Any] | None = None
    password_expiration_days: str | None = None
    privilege_map: IdRef | None = None
    restricted_oem_privileges: list[str] | None = None
    restricted_privileges: list[PrivilegeType] | None = None
    roles: IdRef | None = None
    service_enabled: str | None = None
    status: Status | None = None
    supported_account_types: list[AccountTypes] | None = None
    supported_oemaccount_types: list[str] | None = None
    tacacsplus: str | None = None


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Authentication(RedfishModel):
    authentication_type: str | None = None
    encryption_key: str | None = None
    encryption_key_set: str | None = None
    kerberos_keytab: str | None = None
    oem: dict[str, Any] | None = None
    password: str | None = None
    token: str | None = None
    username: str | None = None


class ExternalAccountProvider(RedfishModel):
    account_provider_type: str | None = None
    authentication: Authentication | None = None
    certificates: IdRef | None = None
    ldapservice: Ldapservice | None = None
    password_set: bool | None = None
    priority: str | None = None
    remote_role_mapping: list[str] | None = None
    service_addresses: list[str] | None = None
    service_enabled: str | None = None
    tacacsplus_service: str | None = None


class LdapsearchSettings(RedfishModel):
    base_distinguished_names: list[str] | None = None
    group_name_attribute: str | None = None
    groups_attribute: str | None = None
    username_attribute: str | None = None


class Ldapservice(RedfishModel):
    oem: dict[str, Any] | None = None
    search_settings: LdapsearchSettings | None = None


class LocalAccountAuth(StrEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    FALLBACK = "Fallback"
    LOCAL_FIRST = "LocalFirst"


class Mfabypass(RedfishModel):
    bypass_types: list[str] | None = None


class MfabypassType(StrEnum):
    ALL = "All"
    SECUR_ID = "SecurID"
    GOOGLE_AUTHENTICATOR = "GoogleAuthenticator"
    MICROSOFT_AUTHENTICATOR = "MicrosoftAuthenticator"
    CLIENT_CERTIFICATE = "ClientCertificate"
    ONE_TIME_PASSCODE = "OneTimePasscode"
    TIME_BASED_ONE_TIME_PASSWORD = "TimeBasedOneTimePassword"  # noqa: S105
    OEM = "OEM"
