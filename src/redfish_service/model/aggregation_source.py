from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .key import EcdsaCurveType, SshKeyType
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    generate_ssh_identity_key_pair: GenerateSshIdentityKeyPair | None = Field(
        serialization_alias="#AggregationSource.GenerateSSHIdentityKeyPair", default=None
    )
    remove_ssh_identity_key_pair: RemoveSshIdentityKeyPair | None = Field(
        serialization_alias="#AggregationSource.RemoveSSHIdentityKeyPair", default=None
    )
    oem: dict[str, Any] | None = None


class AggregationSource(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#AggregationSource.v1_5_0.AggregationSource"
    )
    actions: Actions | None = None
    aggregation_type: AggregationType | None = None
    description: str | None = None
    host_name: str | None = None
    id: str
    links: Links | None = None
    modbus_target_server_id: int | None = None
    name: str
    oem: dict[str, Any] | None = None
    password: str | None = None
    port: int | None = None
    snmp: SnmpSettings | None = Field(serialization_alias="SNMP", default=None)
    ssh_settings: SshSettingsType | None = Field(serialization_alias="SSHSettings", default=None)
    status: Status | None = None
    user_name: str | None = None


class AggregationSourceOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#AggregationSource.v1_5_0.AggregationSource"
    )
    actions: Actions | None = None
    aggregation_type: AggregationType | None = None
    description: str | None = None
    host_name: str | None = None
    id: str | None = None
    links: Links | None = None
    modbus_target_server_id: int | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    password: str | None = None
    port: int | None = None
    snmp: SnmpSettings | None = Field(serialization_alias="SNMP", default=None)
    ssh_settings: SshSettingsType | None = Field(serialization_alias="SSHSettings", default=None)
    status: Status | None = None
    user_name: str | None = None


class AggregationSourceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    aggregation_type: AggregationType | None = None
    host_name: str | None = None
    links: Links | None = None
    modbus_target_server_id: int | None = None
    oem: dict[str, Any] | None = None
    password: str | None = None
    port: int | None = None
    snmp: SnmpSettings | None = Field(serialization_alias="SNMP", default=None)
    ssh_settings: SshSettingsType | None = Field(serialization_alias="SSHSettings", default=None)
    status: Status | None = None
    user_name: str | None = None


class AggregationType(StrEnum):
    NOTIFICATIONS_ONLY = "NotificationsOnly"
    FULL = "Full"


class GenerateSshIdentityKeyPair(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class GenerateSshIdentityKeyPairRequest(RedfishModel):
    curve: EcdsaCurveType | None = None
    key_length: int | None = None
    key_type: SshKeyType


class Links(RedfishModel):
    connection_method: IdRef | None = None
    oem: dict[str, Any] | None = None
    resources_accessed: list[IdRef] | None = None
    resources_accessed_odata_count: int | None = Field(
        serialization_alias="ResourcesAccessed@odata.count", default=None
    )


class RemoveSshIdentityKeyPair(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


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
