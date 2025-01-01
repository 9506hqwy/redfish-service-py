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


class Connection(RedfishResource):
    actions: Actions | None = None
    connection_keys: ConnectionKey | None = None
    connection_type: str | None = None
    description: str | None = None
    links: Links | None = None
    memory_chunk_info: list[MemoryChunkInfo] | None = None
    memory_region_info: list[MemoryRegionInfo] | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    volume_info: list[str] | None = None


class ConnectionKey(RedfishModel):
    chap: str | None = Field(alias="CHAP", default=None)
    dhchap: str | None = Field(alias="DHCHAP", default=None)
    gen_z: str | None = None


class Links(RedfishModel):
    initiator_endpoint_groups: list[IdRef] | None = None
    initiator_endpoint_groups_odata_count: int | None = Field(
        alias="InitiatorEndpointGroups@odata.count", default=None
    )
    initiator_endpoints: list[IdRef] | None = None
    initiator_endpoints_odata_count: int | None = Field(
        alias="InitiatorEndpoints@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    target_endpoint_groups: list[IdRef] | None = None
    target_endpoint_groups_odata_count: int | None = Field(
        alias="TargetEndpointGroups@odata.count", default=None
    )
    target_endpoints: list[IdRef] | None = None
    target_endpoints_odata_count: int | None = Field(
        alias="TargetEndpoints@odata.count", default=None
    )


class MemoryChunkInfo(RedfishModel):
    access_capabilities: list[str] | None = None
    access_state: str | None = None
    memory_chunk: str | None = None


class MemoryRegionInfo(RedfishModel):
    access_capabilities: list[str] | None = None
    access_state: str | None = None
    memory_region: str | None = None
