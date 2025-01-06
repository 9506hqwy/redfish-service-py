from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class RouteSetEntry(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#RouteSetEntry.v1_0_2.RouteSetEntry")
    actions: Actions | None = None
    description: str | None = None
    egress_identifier: int | None = None
    hop_count: int | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    vc_action: int | None = Field(alias="VCAction", default=None)
    valid: bool | None = None


class RouteSetEntryOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(
        alias="@odata.type", default="#RouteSetEntry.v1_0_2.RouteSetEntry"
    )
    actions: Actions | None = None
    description: str | None = None
    egress_identifier: int | None = None
    hop_count: int | None = None
    id: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    vc_action: int | None = Field(alias="VCAction", default=None)
    valid: bool | None = None
