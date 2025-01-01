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
    oem: dict[str, Any] | None = None


class Fabric(RedfishResource):
    actions: Actions | None = None
    address_pools: IdRef | None = None
    connections: IdRef | None = None
    description: str | None = None
    endpoint_groups: IdRef | None = None
    endpoints: IdRef | None = None
    fabric_type: str | None = None
    links: Links | None = None
    max_zones: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    switches: IdRef | None = None
    uuid: str | None = Field(alias="UUID", default=None)
    zones: IdRef | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
