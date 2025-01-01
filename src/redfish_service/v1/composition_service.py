from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    compose: Compose | None = Field(alias="#CompositionService.Compose", default=None)
    oem: dict[str, Any] | None = None


class Compose(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class CompositionService(RedfishResource):
    actions: Actions | None = None
    active_pool: IdRef | None = None
    allow_overprovisioning: str | None = None
    allow_zone_affinity: str | None = None
    composition_reservations: IdRef | None = None
    description: str | None = None
    free_pool: IdRef | None = None
    oem: dict[str, Any] | None = None
    reservation_duration: str | None = None
    resource_blocks: IdRef | None = None
    resource_zones: IdRef | None = None
    service_enabled: str | None = None
    status: Status | None = None
