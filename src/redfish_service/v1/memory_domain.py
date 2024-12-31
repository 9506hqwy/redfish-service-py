from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    cxllogical_devices: list[IdRef] | None = None
    fabric_adapters: list[IdRef] | None = None
    media_controllers: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = None


class MemoryDomain(RedfishResource):
    actions: Actions | None = None
    allows_block_provisioning: str | None = None
    allows_memory_chunk_creation: str | None = None
    allows_mirroring: str | None = None
    allows_sparing: str | None = None
    description: str | None = None
    interleavable_memory_sets: list[MemorySet] | None = None
    links: Links | None = None
    memory_chunk_increment_mi_b: str | None = None
    memory_chunks: IdRef | None = None
    memory_size_mi_b: str | None = None
    min_memory_chunk_size_mi_b: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class MemorySet(RedfishModel):
    memory_set: list[IdRef] | None = None
