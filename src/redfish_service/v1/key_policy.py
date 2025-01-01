from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class KeyPolicy(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    is_default: bool | None = None
    key_policy_type: KeyPolicyType | None = None
    nvmeo_f: NvmeoF | None = Field(alias="NVMeoF", default=None)
    oem: dict[str, Any] | None = None


class KeyPolicyType(StrEnum):
    NVMEO_F = "NVMeoF"


class NvmeoF(RedfishModel):
    cipher_suite_allow_list: list[NvmeoFcipherSuiteType] | None = None
    dhgroup_allow_list: list[NvmeoFdhgroupType] | None = Field(
        alias="DHGroupAllowList", default=None
    )
    oemsecurity_protocol_allow_list: list[str] | None = Field(
        alias="OEMSecurityProtocolAllowList", default=None
    )
    secure_hash_allow_list: list[NvmeoFsecureHashType] | None = None
    security_protocol_allow_list: list[NvmeoFsecurityProtocolType] | None = None
    security_transport_allow_list: list[NvmeoFsecurityTransportType] | None = None


class NvmeoFcipherSuiteType(StrEnum):
    TLS__AES_128__GCM__SHA256 = "TLS_AES_128_GCM_SHA256"
    TLS__AES_256__GCM__SHA384 = "TLS_AES_256_GCM_SHA384"


class NvmeoFdhgroupType(StrEnum):
    FFDHE2048 = "FFDHE2048"
    FFDHE3072 = "FFDHE3072"
    FFDHE4096 = "FFDHE4096"
    FFDHE6144 = "FFDHE6144"
    FFDHE8192 = "FFDHE8192"


class NvmeoFsecureHashType(StrEnum):
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"


class NvmeoFsecurityProtocolType(StrEnum):
    DHHC = "DHHC"
    TLS__PSK = "TLS_PSK"
    OEM = "OEM"


class NvmeoFsecurityTransportType(StrEnum):
    TLSV2 = "TLSv2"
    TLSV3 = "TLSv3"
