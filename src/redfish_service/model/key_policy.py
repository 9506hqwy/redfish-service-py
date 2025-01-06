from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class KeyPolicy(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#KeyPolicy.v1_0_1.KeyPolicy")
    actions: Actions | None = None
    description: str | None = None
    id: str
    is_default: bool | None = None
    key_policy_type: KeyPolicyType | None = None
    nvme_of: NvmeOf | None = Field(alias="NVMeoF", default=None)
    name: str
    oem: dict[str, Any] | None = None


class KeyPolicyOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#KeyPolicy.v1_0_1.KeyPolicy")
    actions: Actions | None = None
    description: str | None = None
    id: str | None = None
    is_default: bool | None = None
    key_policy_type: KeyPolicyType | None = None
    nvme_of: NvmeOf | None = Field(alias="NVMeoF", default=None)
    name: str | None = None
    oem: dict[str, Any] | None = None


class KeyPolicyType(StrEnum):
    NVME_OF = "NVMeoF"


class NvmeOf(RedfishModel):
    cipher_suite_allow_list: list[NvmeOfCipherSuiteType] | None = None
    dh_group_allow_list: list[NvmeOfDhGroupType] | None = Field(
        alias="DHGroupAllowList", default=None
    )
    oem_security_protocol_allow_list: list[str] | None = Field(
        alias="OEMSecurityProtocolAllowList", default=None
    )
    secure_hash_allow_list: list[NvmeOfSecureHashType] | None = None
    security_protocol_allow_list: list[NvmeOfSecurityProtocolType] | None = None
    security_transport_allow_list: list[NvmeOfSecurityTransportType] | None = None


class NvmeOfCipherSuiteType(StrEnum):
    TL_S_AE_S_128_GC_M_SHA256 = "TLS_AES_128_GCM_SHA256"
    TL_S_AE_S_256_GC_M_SHA384 = "TLS_AES_256_GCM_SHA384"


class NvmeOfDhGroupType(StrEnum):
    FFDHE2048 = "FFDHE2048"
    FFDHE3072 = "FFDHE3072"
    FFDHE4096 = "FFDHE4096"
    FFDHE6144 = "FFDHE6144"
    FFDHE8192 = "FFDHE8192"


class NvmeOfSecureHashType(StrEnum):
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"


class NvmeOfSecurityProtocolType(StrEnum):
    DHHC = "DHHC"
    TL_S_PSK = "TLS_PSK"
    OEM = "OEM"


class NvmeOfSecurityTransportType(StrEnum):
    TL_SV2 = "TLSv2"
    TL_SV3 = "TLSv3"
