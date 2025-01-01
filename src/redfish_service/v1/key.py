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


class Key(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    key_string: str | None = None
    key_type: KeyType | None = None
    nvmeo_f: NvmeoF | None = Field(alias="NVMeoF", default=None)
    oem: dict[str, Any] | None = None
    ssh: Sshtype | None = Field(alias="SSH", default=None)
    user_description: str | None = None


class KeyType(StrEnum):
    NVMEO_F = "NVMeoF"
    SSH = "SSH"


class NvmeoF(RedfishModel):
    host_key_id: str | None = None
    nqn: str | None = Field(alias="NQN", default=None)
    oemsecurity_protocol_type: str | None = Field(alias="OEMSecurityProtocolType", default=None)
    secure_hash_allow_list: list[NvmeoFsecureHashType] | None = None
    security_protocol_type: NvmeoFsecurityProtocolType | None = None


class NvmeoFsecureHashType(StrEnum):
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"


class NvmeoFsecurityProtocolType(StrEnum):
    DHHC = "DHHC"
    TLS__PSK = "TLS_PSK"
    OEM = "OEM"


class Sshtype(RedfishModel):
    comment: str | None = None
    fingerprint: str | None = None
    remote_server_host_name: str | None = None
