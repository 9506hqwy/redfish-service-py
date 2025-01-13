from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class EcdsaCurveType(StrEnum):
    NISTP256 = "NISTP256"
    NISTP384 = "NISTP384"
    NISTP521 = "NISTP521"
    NISTK163 = "NISTK163"
    NISTP192 = "NISTP192"
    NISTP224 = "NISTP224"
    NISTK233 = "NISTK233"
    NISTB233 = "NISTB233"
    NISTK283 = "NISTK283"
    NISTK409 = "NISTK409"
    NISTB409 = "NISTB409"
    NISTT571 = "NISTT571"


class Key(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#Key.v1_4_1.Key")
    actions: Actions | None = None
    description: str | None = None
    id: str
    key_string: str | None = None
    key_type: KeyType | None = None
    nvme_of: NvmeOf | None = Field(alias="NVMeoF", default=None)
    name: str
    oem: dict[str, Any] | None = None
    ssh: SshType | None = Field(alias="SSH", default=None)
    user_description: str | None = None


class KeyOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#Key.v1_4_1.Key")
    actions: Actions | None = None
    description: str | None = None
    id: str | None = None
    key_string: str | None = None
    key_type: KeyType | None = None
    nvme_of: NvmeOf | None = Field(alias="NVMeoF", default=None)
    name: str | None = None
    oem: dict[str, Any] | None = None
    ssh: SshType | None = Field(alias="SSH", default=None)
    user_description: str | None = None


class KeyOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#Key.v1_4_1.Key")
    actions: Actions | None = None
    description: str | None = None
    id: str | None = None
    key_string: str | None = None
    key_type: KeyType | None = None
    nvme_of: NvmeOf | None = Field(alias="NVMeoF", default=None)
    name: str | None = None
    oem: dict[str, Any] | None = None
    ssh: SshType | None = Field(alias="SSH", default=None)
    user_description: str | None = None


class KeyType(StrEnum):
    NVME_OF = "NVMeoF"
    SSH = "SSH"


class NvmeOf(RedfishModel):
    host_key_id: str | None = None
    nqn: str | None = Field(alias="NQN", default=None)
    oem_security_protocol_type: str | None = Field(alias="OEMSecurityProtocolType", default=None)
    secure_hash_allow_list: list[NvmeOfSecureHashType] | None = None
    security_protocol_type: NvmeOfSecurityProtocolType | None = None


class NvmeOfSecureHashType(StrEnum):
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"


class NvmeOfSecurityProtocolType(StrEnum):
    DHHC = "DHHC"
    TL_S_PSK = "TLS_PSK"
    OEM = "OEM"


class SshKeyType(StrEnum):
    RSA = "RSA"
    DSA = "DSA"
    ECDSA = "ECDSA"
    ED25519 = "Ed25519"


class SshType(RedfishModel):
    comment: str | None = None
    fingerprint: str | None = None
    remote_server_host_name: str | None = None
