from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .manifest import Manifest
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CompositionReservation(RedfishResource):
    actions: Actions | None = None
    client: str | None = None
    description: str | None = None
    manifest: Manifest | None = None
    oem: dict[str, Any] | None = None
    reservation_time: str | None = None
    reserved_resource_blocks: list[IdRef] | None = None
    reserved_resource_blocks_odata_count: int | None = Field(
        alias="ReservedResourceBlocks@odata.count", default=None
    )
