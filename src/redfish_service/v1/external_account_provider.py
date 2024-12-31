from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef


class Actions(RedfishResource):
    oem: OemActions | None = None


class Authentication(RedfishResource):
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
    ldapservice: Ldapservice | None = None
    links: Links | None = None
    oauth2_service: str | None = None
    oem: dict[str, Any] | None = None
    priority: str | None = None
    remote_role_mapping: list[str] | None = None
    retries: str | None = None
    service_addresses: list[str] | None = None
    service_enabled: str | None = None
    tacacsplus_service: str | None = None
    timeout_seconds: str | None = None


class LdapsearchSettings(RedfishResource):
    base_distinguished_names: list[str] | None = None
    email_attribute: str | None = None
    group_name_attribute: str | None = None
    groups_attribute: str | None = None
    sshkey_attribute: str | None = None
    username_attribute: str | None = None


class Ldapservice(RedfishResource):
    oem: dict[str, Any] | None = None
    search_settings: LdapsearchSettings | None = None


class Links(RedfishResource):
    oem: dict[str, Any] | None = None


class OemActions(RedfishResource):
    pass
