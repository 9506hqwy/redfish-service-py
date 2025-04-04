from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class RouteSetEntry(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#RouteSetEntry.v1_0_2.RouteSetEntry"
    )
    actions: Actions | None = None
    description: str | None = None
    egress_identifier: int | None = None
    hop_count: int | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    vc_action: int | None = Field(serialization_alias="VCAction", default=None)
    valid: bool | None = None


class RouteSetEntryOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#RouteSetEntry.v1_0_2.RouteSetEntry"
    )
    actions: Actions | None = None
    description: str | None = None
    egress_identifier: int | None = None
    hop_count: int | None = None
    id: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    vc_action: int | None = Field(serialization_alias="VCAction", default=None)
    valid: bool | None = None


class RouteSetEntryOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    egress_identifier: int | None = None
    hop_count: int | None = None
    oem: dict[str, Any] | None = None
    vc_action: int | None = Field(serialization_alias="VCAction", default=None)
    valid: bool | None = None
