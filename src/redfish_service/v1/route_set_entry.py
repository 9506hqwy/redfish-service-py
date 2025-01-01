from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class RouteSetEntry(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    egress_identifier: int | None = None
    hop_count: int | None = None
    oem: dict[str, Any] | None = None
    vcaction: int | None = Field(alias="VCAction", default=None)
    valid: bool | None = None
