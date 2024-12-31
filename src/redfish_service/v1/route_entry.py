from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: OemActions | None = None


class OemActions(RedfishModel):
    pass


class RouteEntry(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    minimum_hop_count: int | None = None
    oem: dict[str, Any] | None = None
    raw_entry_hex: str | None = None
    route_set: IdRef | None = None
