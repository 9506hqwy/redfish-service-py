from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


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


class ExternalAccountProvider(RedfishResource):
    account_provider_type: str | None = None
    actions: Actions | None = None
    authentication: Authentication | None = None
    certificates: IdRef | None = None
    description: str | None = None
    ldapservice: Ldapservice | None = Field(alias="LDAPService", default=None)
    links: Links | None = None
    oauth2_service: str | None = Field(alias="OAuth2Service", default=None)
    oem: dict[str, Any] | None = None
    priority: str | None = None
    remote_role_mapping: list[str] | None = None
    retries: str | None = None
    service_addresses: list[str] | None = None
    service_enabled: str | None = None
    tacacsplus_service: str | None = Field(alias="TACACSplusService", default=None)
    timeout_seconds: str | None = None


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
