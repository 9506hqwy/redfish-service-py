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


class EcdsacurveType(StrEnum):
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


class Key(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    key_string: str | None = None
    key_type: str | None = None
    nvmeo_f: NvmeoF | None = Field(alias="NVMeoF", default=None)
    oem: dict[str, Any] | None = None
    ssh: Sshtype | None = Field(alias="SSH", default=None)
    user_description: str | None = None


class NvmeoF(RedfishModel):
    host_key_id: str | None = None
    nqn: str | None = Field(alias="NQN", default=None)
    oemsecurity_protocol_type: str | None = Field(alias="OEMSecurityProtocolType", default=None)
    secure_hash_allow_list: list[str] | None = None
    security_protocol_type: str | None = None


class SshkeyType(StrEnum):
    RSA = "RSA"
    DSA = "DSA"
    ECDSA = "ECDSA"
    ED25519 = "Ed25519"


class Sshtype(RedfishModel):
    comment: str | None = None
    fingerprint: str | None = None
    remote_server_host_name: str | None = None
