from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .manager_account import AccountTypes
from .odata_v4 import IdRef
from .privileges import PrivilegeType
from .resource import Status


class AccountProviderTypes(StrEnum):
    REDFISH_SERVICE = "RedfishService"
    ACTIVE_DIRECTORY_SERVICE = "ActiveDirectoryService"
    LDAPSERVICE = "LDAPService"
    OEM = "OEM"
    TACACSPLUS = "TACACSplus"
    OAUTH2 = "OAuth2"


class AccountService(RedfishResource):
    account_lockout_counter_reset_after: int | None = None
    account_lockout_counter_reset_enabled: bool | None = None
    account_lockout_duration: int | None = None
    account_lockout_threshold: int | None = None
    accounts: IdRef | None = None
    actions: Actions | None = None
    active_directory: ExternalAccountProvider | None = None
    additional_external_account_providers: IdRef | None = None
    auth_failure_logging_threshold: int | None = None
    description: str | None = None
    httpbasic_auth: BasicAuthState | None = Field(alias="HTTPBasicAuth", default=None)
    ldap: ExternalAccountProvider | None = Field(alias="LDAP", default=None)
    local_account_auth: LocalAccountAuth | None = None
    max_password_length: int | None = None
    min_password_length: int | None = None
    multi_factor_auth: MultiFactorAuth | None = None
    oauth2: ExternalAccountProvider | None = Field(alias="OAuth2", default=None)
    oem: dict[str, Any] | None = None
    outbound_connections: IdRef | None = None
    password_expiration_days: int | None = None
    privilege_map: IdRef | None = None
    require_change_password_action: bool | None = None
    restricted_oem_privileges: list[str] | None = None
    restricted_privileges: list[PrivilegeType] | None = None
    roles: IdRef | None = None
    service_enabled: bool | None = None
    status: Status | None = None
    supported_account_types: list[AccountTypes] | None = None
    supported_oemaccount_types: list[str] | None = Field(
        alias="SupportedOEMAccountTypes", default=None
    )
    tacacsplus: ExternalAccountProvider | None = Field(alias="TACACSplus", default=None)


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


class BasicAuthState(StrEnum):
    ENABLED = "Enabled"
    UNADVERTISED = "Unadvertised"
    DISABLED = "Disabled"


class CertificateMappingAttribute(StrEnum):
    WHOLE = "Whole"
    COMMON_NAME = "CommonName"
    USER_PRINCIPAL_NAME = "UserPrincipalName"


class ClientCertificate(RedfishModel):
    certificate_mapping_attribute: CertificateMappingAttribute | None = None
    certificates: IdRef | None = None
    enabled: bool | None = None
    respond_to_unauthenticated_clients: bool | None = None


class ExternalAccountProvider(RedfishModel):
    account_provider_type: AccountProviderTypes | None = None
    authentication: Authentication | None = None
    certificates: IdRef | None = None
    ldapservice: Ldapservice | None = Field(alias="LDAPService", default=None)
    oauth2_service: Oauth2Service | None = Field(alias="OAuth2Service", default=None)
    password_set: bool | None = None
    priority: int | None = None
    remote_role_mapping: list[RoleMapping] | None = None
    retries: int | None = None
    service_addresses: list[str] | None = None
    service_enabled: bool | None = None
    tacacsplus_service: TacacsplusService | None = Field(alias="TACACSplusService", default=None)
    timeout_seconds: int | None = None


class GoogleAuthenticator(RedfishModel):
    enabled: bool | None = None
    secret_key: str | None = None
    secret_key_set: bool | None = None


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


class LocalAccountAuth(StrEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    FALLBACK = "Fallback"
    LOCAL_FIRST = "LocalFirst"


class Mfabypass(RedfishModel):
    bypass_types: list[MfabypassType] | None = None


class MfabypassType(StrEnum):
    ALL = "All"
    SECUR_ID = "SecurID"
    GOOGLE_AUTHENTICATOR = "GoogleAuthenticator"
    MICROSOFT_AUTHENTICATOR = "MicrosoftAuthenticator"
    CLIENT_CERTIFICATE = "ClientCertificate"
    ONE_TIME_PASSCODE = "OneTimePasscode"
    TIME_BASED_ONE_TIME_PASSWORD = "TimeBasedOneTimePassword"  # noqa: S105
    OEM = "OEM"


class MicrosoftAuthenticator(RedfishModel):
    enabled: bool | None = None
    secret_key: str | None = None
    secret_key_set: bool | None = None


class MultiFactorAuth(RedfishModel):
    client_certificate: ClientCertificate | None = None
    google_authenticator: GoogleAuthenticator | None = None
    microsoft_authenticator: MicrosoftAuthenticator | None = None
    one_time_passcode: OneTimePasscode | None = None
    secur_id: SecurId | None = Field(alias="SecurID", default=None)
    time_based_one_time_password: TimeBasedOneTimePassword | None = None


class Oauth2Mode(StrEnum):
    DISCOVERY = "Discovery"
    OFFLINE = "Offline"


class Oauth2Service(RedfishModel):
    audience: list[str] | None = None
    issuer: str | None = None
    mode: Oauth2Mode | None = None
    oauth_service_signing_keys: str | None = Field(alias="OAuthServiceSigningKeys", default=None)
    oem: dict[str, Any] | None = None


class OneTimePasscode(RedfishModel):
    enabled: bool | None = None


class RoleMapping(RedfishModel):
    local_account_types: list[AccountTypes] | None = None
    local_oemaccount_types: list[str] | None = Field(alias="LocalOEMAccountTypes", default=None)
    local_role: str | None = None
    mfabypass: Mfabypass | None = Field(alias="MFABypass", default=None)
    oem: dict[str, Any] | None = None
    remote_group: str | None = None
    remote_user: str | None = None


class SecurId(RedfishModel):
    certificates: IdRef | None = None
    client_id: str | None = None
    client_secret: str | None = None
    client_secret_set: bool | None = None
    enabled: bool | None = None
    server_uri: str | None = Field(alias="ServerURI", default=None)


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


class TimeBasedOneTimePassword(RedfishModel):
    enabled: bool | None = None
    time_step_seconds: int | None = None
