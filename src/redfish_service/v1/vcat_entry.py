from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class VcatEntry(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    raw_entry_hex: str | None = None
    vc_entries: list[VcaTableEntry] | None = Field(alias="VCEntries", default=None)


class VcaTableEntry(RedfishModel):
    threshold: str | None = None
    vc_mask: str | None = Field(alias="VCMask", default=None)
