from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    generate_ssh_identity_key_pair: GenerateSshIdentityKeyPair | None = Field(
        alias="#AggregationSource.GenerateSSHIdentityKeyPair", default=None
    )
    remove_ssh_identity_key_pair: RemoveSshIdentityKeyPair | None = Field(
        alias="#AggregationSource.RemoveSSHIdentityKeyPair", default=None
    )
    oem: dict[str, Any] | None = None


class AggregationSource(RedfishResource):
    actions: Actions | None = None
    aggregation_type: AggregationType | None = None
    description: str | None = None
    host_name: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    password: str | None = None
    snmp: SnmpSettings | None = Field(alias="SNMP", default=None)
    ssh_settings: SshSettingsType | None = Field(alias="SSHSettings", default=None)
    status: Status | None = None
    user_name: str | None = None


class AggregationType(StrEnum):
    NOTIFICATIONS_ONLY = "NotificationsOnly"
    FULL = "Full"


class GenerateSshIdentityKeyPair(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Links(RedfishModel):
    connection_method: IdRef | None = None
    oem: dict[str, Any] | None = None
    resources_accessed: list[IdRef] | None = None
    resources_accessed_odata_count: int | None = Field(
        alias="ResourcesAccessed@odata.count", default=None
    )


class RemoveSshIdentityKeyPair(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SnmpAuthenticationProtocols(StrEnum):
    NONE = "None"
    COMMUNITY_STRING = "CommunityString"
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


class SnmpSettings(RedfishModel):
    authentication_key: str | None = None
    authentication_key_set: bool | None = None
    authentication_protocol: SnmpAuthenticationProtocols | None = None
    encryption_key: str | None = None
    encryption_key_set: bool | None = None
    encryption_protocol: SnmpEncryptionProtocols | None = None
    trap_community: str | None = None


class SshSettingsType(RedfishModel):
    presented_public_host_key: IdRef | None = None
    presented_public_host_key_timestamp: str | None = None
    public_identity_key: IdRef | None = None
    trusted_public_host_keys: IdRef | None = None
    user_authentication_method: UserAuthenticationMethod | None = None


class UserAuthenticationMethod(StrEnum):
    PUBLIC_KEY = "PublicKey"
    PASSWORD = "Password"  # noqa: S105
