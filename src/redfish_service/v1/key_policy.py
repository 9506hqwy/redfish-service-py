from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource


class Actions(RedfishResource):
    oem: OemActions | None = None


class KeyPolicy(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    is_default: str | None = None
    key_policy_type: str | None = None
    nvmeo_f: NvmeoF | None = None
    oem: dict[str, Any] | None = None


class NvmeoF(RedfishResource):
    cipher_suite_allow_list: list[str] | None = None
    dhgroup_allow_list: list[str] | None = None
    oemsecurity_protocol_allow_list: list[str] | None = None
    secure_hash_allow_list: list[str] | None = None
    security_protocol_allow_list: list[str] | None = None
    security_transport_allow_list: list[str] | None = None


class OemActions(RedfishResource):
    pass
