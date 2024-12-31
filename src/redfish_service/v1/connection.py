from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


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


class ConnectionKey(RedfishResource):
    chap: str | None = None
    dhchap: str | None = None
    gen_z: str | None = None


class Links(RedfishResource):
    initiator_endpoint_groups: list[IdRef] | None = None
    initiator_endpoints: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    target_endpoint_groups: list[IdRef] | None = None
    target_endpoints: list[IdRef] | None = None


class MemoryChunkInfo(RedfishResource):
    access_capabilities: list[str] | None = None
    access_state: str | None = None
    memory_chunk: str | None = None


class MemoryRegionInfo(RedfishResource):
    access_capabilities: list[str] | None = None
    access_state: str | None = None
    memory_region: str | None = None


class OemActions(RedfishResource):
    pass
