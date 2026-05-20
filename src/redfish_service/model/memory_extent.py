from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    memory_regions: list[IdRef] | None = None
    memory_regions_odata_count: int | None = Field(
        serialization_alias="MemoryRegions@odata.count", default=None
    )
    oem: dict[str, Any] | None = None


class MemoryChunk(RedfishModel):
    chunk_link: IdRef | None = None
    chunk_offset_mib: int | None = Field(serialization_alias="ChunkOffsetMiB", default=None)


class MemoryExtent(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#MemoryExtent.v1_0_0.MemoryExtent"
    )
    actions: Actions | None = None
    description: str | None = None
    extent_offset_mib: int | None = Field(serialization_alias="ExtentOffsetMiB", default=None)
    extent_size_mib: int | None = Field(serialization_alias="ExtentSizeMiB", default=None)
    fm_referenced_extent: bool | None = Field(
        serialization_alias="FMReferencedExtent", default=None
    )
    id: str
    links: Links | None = None
    memory_chunks: list[MemoryChunk] | None = None
    name: str
    oem: dict[str, Any] | None = None
    sequence_number: int | None = None
    status: Status | None = None
    tag: str | None = None


class MemoryExtentOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#MemoryExtent.v1_0_0.MemoryExtent"
    )
    actions: Actions | None = None
    description: str | None = None
    extent_offset_mib: int | None = Field(serialization_alias="ExtentOffsetMiB", default=None)
    extent_size_mib: int | None = Field(serialization_alias="ExtentSizeMiB", default=None)
    fm_referenced_extent: bool | None = Field(
        serialization_alias="FMReferencedExtent", default=None
    )
    id: str | None = None
    links: Links | None = None
    memory_chunks: list[MemoryChunk] | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    sequence_number: int | None = None
    status: Status | None = None
    tag: str | None = None
