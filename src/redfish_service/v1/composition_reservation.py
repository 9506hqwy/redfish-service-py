from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .manifest import Manifest
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CompositionReservation(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    client: str | None = None
    description: str | None = None
    id: str
    manifest: Manifest | None = None
    name: str
    oem: dict[str, Any] | None = None
    reservation_time: str | None = None
    reserved_resource_blocks: list[IdRef] | None = None
    reserved_resource_blocks_odata_count: int | None = Field(
        alias="ReservedResourceBlocks@odata.count", default=None
    )
