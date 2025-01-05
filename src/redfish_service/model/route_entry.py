from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class RouteEntry(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#RouteEntry.v1_0_2.RouteEntry")
    actions: Actions | None = None
    description: str | None = None
    id: str
    minimum_hop_count: int | None = None
    name: str
    oem: dict[str, Any] | None = None
    raw_entry_hex: str | None = None
    route_set: IdRef | None = None
