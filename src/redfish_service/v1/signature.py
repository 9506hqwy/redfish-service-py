from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import RedfishResource


class Actions(RedfishResource):
    oem: OemActions | None = None


class OemActions(RedfishResource):
    pass


class Signature(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    signature_string: str | None = None
    signature_type: str | None = None
    signature_type_registry: str | None = None
    uefi_signature_owner: str | None = None


class SignatureTypeRegistry(StrEnum):
    UEFI = "UEFI"
