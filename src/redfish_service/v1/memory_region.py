from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class MemoryChunk(RedfishModel):
    chunk_link: IdRef | None = None
    chunk_offset_mi_b: int | None = None


class MemoryExtent(RedfishModel):
    extent_offset_mi_b: int | None = None
    extent_size_mi_b: int | None = None
    sequence_number: int | None = None
    tag: str | None = None


class MemoryRegion(RedfishResource):
    actions: Actions | None = None
    block_size_mi_b: int | None = None
    description: str | None = None
    extents_count: int | None = None
    hardware_managed_coherency_region: bool | None = None
    memory_chunks: list[MemoryChunk] | None = None
    memory_extents: list[MemoryExtent] | None = None
    non_volatile_region: bool | None = None
    oem: dict[str, Any] | None = None
    region_base_offset_mi_b: int | None = None
    region_number: int | None = None
    region_size_mi_b: int | None = None
    region_type: RegionType
    sanitize_on_release: bool | None = None
    shareable_region: bool | None = None
    status: Status | None = None


class RegionType(StrEnum):
    STATIC = "Static"
    DYNAMIC = "Dynamic"
