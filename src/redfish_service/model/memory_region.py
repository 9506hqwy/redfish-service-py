from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class MemoryChunk(RedfishModel):
    chunk_link: IdRef | None = None
    chunk_offset_mib: int | None = Field(serialization_alias="ChunkOffsetMiB", default=None)


class MemoryExtent(RedfishModel):
    extent_offset_mib: int | None = Field(serialization_alias="ExtentOffsetMiB", default=None)
    extent_size_mib: int | None = Field(serialization_alias="ExtentSizeMiB", default=None)
    sequence_number: int | None = None
    tag: str | None = None


class MemoryRegion(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#MemoryRegion.v1_0_3.MemoryRegion"
    )
    actions: Actions | None = None
    block_size_mib: int | None = Field(serialization_alias="BlockSizeMiB", default=None)
    description: str | None = None
    extents_count: int | None = None
    hardware_managed_coherency_region: bool | None = None
    id: str
    memory_chunks: list[MemoryChunk] | None = None
    memory_extents: list[MemoryExtent] | None = None
    name: str
    non_volatile_region: bool | None = None
    oem: dict[str, Any] | None = None
    region_base_offset_mib: int | None = Field(
        serialization_alias="RegionBaseOffsetMiB", default=None
    )
    region_number: int | None = None
    region_size_mib: int | None = Field(serialization_alias="RegionSizeMiB", default=None)
    region_type: RegionType
    sanitize_on_release: bool | None = None
    shareable_region: bool | None = None
    status: Status | None = None


class MemoryRegionOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#MemoryRegion.v1_0_3.MemoryRegion"
    )
    actions: Actions | None = None
    block_size_mib: int | None = Field(serialization_alias="BlockSizeMiB", default=None)
    description: str | None = None
    extents_count: int | None = None
    hardware_managed_coherency_region: bool | None = None
    id: str | None = None
    memory_chunks: list[MemoryChunk] | None = None
    memory_extents: list[MemoryExtent] | None = None
    name: str | None = None
    non_volatile_region: bool | None = None
    oem: dict[str, Any] | None = None
    region_base_offset_mib: int | None = Field(
        serialization_alias="RegionBaseOffsetMiB", default=None
    )
    region_number: int | None = None
    region_size_mib: int | None = Field(serialization_alias="RegionSizeMiB", default=None)
    region_type: RegionType | None = None
    sanitize_on_release: bool | None = None
    shareable_region: bool | None = None
    status: Status | None = None


class MemoryRegionOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    block_size_mib: int | None = Field(serialization_alias="BlockSizeMiB", default=None)
    memory_chunks: list[MemoryChunk] | None = None
    memory_extents: list[MemoryExtent] | None = None
    oem: dict[str, Any] | None = None
    sanitize_on_release: bool | None = None
    status: Status | None = None


class RegionType(StrEnum):
    STATIC = "Static"
    DYNAMIC = "Dynamic"
