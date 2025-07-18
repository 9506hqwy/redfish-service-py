from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .protocol import Protocol
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Fabric(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Fabric.v1_4_0.Fabric")
    actions: Actions | None = None
    address_pools: IdRef | None = None
    connections: IdRef | None = None
    description: str | None = None
    endpoint_groups: IdRef | None = None
    endpoints: IdRef | None = None
    fabric_type: Protocol | None = None
    id: str
    links: Links | None = None
    max_zones: int | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None
    switches: IdRef | None = None
    uuid: str | None = Field(serialization_alias="UUID", default=None)
    zones: IdRef | None = None


class FabricOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    uuid: str | None = Field(serialization_alias="UUID", default=None)


class Links(RedfishModel):
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(
        serialization_alias="ManagedBy@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
