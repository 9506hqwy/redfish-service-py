from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class VcatEntry(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#VCATEntry.v1_0_3.VCATEntry"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    raw_entry_hex: str | None = None
    vc_entries: list[VcaTableEntry] | None = Field(serialization_alias="VCEntries", default=None)


class VcatEntryOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#VCATEntry.v1_0_3.VCATEntry"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    raw_entry_hex: str | None = None
    vc_entries: list[VcaTableEntry] | None = Field(serialization_alias="VCEntries", default=None)


class VcatEntryOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    oem: dict[str, Any] | None = None
    raw_entry_hex: str | None = None
    vc_entries: list[VcaTableEntry] | None = Field(serialization_alias="VCEntries", default=None)


class VcaTableEntry(RedfishModel):
    threshold: str | None = None
    vc_mask: str | None = Field(serialization_alias="VCMask", default=None)
