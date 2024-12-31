from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: OemActions | None = None


class OemActions(RedfishModel):
    pass


class RouteSetEntry(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    egress_identifier: int | None = None
    hop_count: int | None = None
    oem: dict[str, Any] | None = None
    vcaction: int | None = None
    valid: bool | None = None
