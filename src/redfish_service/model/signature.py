from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Signature(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#Signature.v1_0_3.Signature"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    signature_string: str | None = None
    signature_type: str | None = None
    signature_type_registry: SignatureTypeRegistry | None = None
    uefi_signature_owner: str | None = None


class SignatureOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#Signature.v1_0_3.Signature"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    signature_string: str | None = None
    signature_type: str | None = None
    signature_type_registry: SignatureTypeRegistry | None = None
    uefi_signature_owner: str | None = None


class SignatureTypeRegistry(StrEnum):
    UEFI = "UEFI"
