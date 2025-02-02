from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AddressRangeType(StrEnum):
    VOLATILE = "Volatile"
    PMEM = "PMEM"
    BLOCK = "Block"


class InterleaveSet(RedfishModel):
    memory: IdRef | None = None
    memory_level: int | None = None
    offset_mib: int | None = Field(serialization_alias="OffsetMiB", default=None)
    region_id: str | None = None
    size_mib: int | None = Field(serialization_alias="SizeMiB", default=None)


class Links(RedfishModel):
    cxl_logical_devices: list[IdRef] | None = Field(
        serialization_alias="CXLLogicalDevices", default=None
    )
    cxl_logical_devices_odata_count: int | None = Field(
        serialization_alias="CXLLogicalDevices@odata.count", default=None
    )
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(
        serialization_alias="Endpoints@odata.count", default=None
    )
    memory_regions: list[IdRef] | None = None
    memory_regions_odata_count: int | None = Field(
        serialization_alias="MemoryRegions@odata.count", default=None
    )
    oem: dict[str, Any] | None = None


class MediaLocation(StrEnum):
    LOCAL = "Local"
    REMOTE = "Remote"
    MIXED = "Mixed"


class MemoryChunks(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#MemoryChunks.v1_6_2.MemoryChunks"
    )
    actions: Actions | None = None
    address_range_offset_mib: int | None = Field(
        serialization_alias="AddressRangeOffsetMiB", default=None
    )
    address_range_type: AddressRangeType | None = None
    description: str | None = None
    display_name: str | None = None
    id: str
    interleave_sets: list[InterleaveSet] | None = None
    is_mirror_enabled: bool | None = None
    is_spare: bool | None = None
    links: Links | None = None
    media_location: MediaLocation | None = None
    memory_chunk_size_mib: int | None = Field(
        serialization_alias="MemoryChunkSizeMiB", default=None
    )
    name: str
    oem: dict[str, Any] | None = None
    requested_operational_state: OperationalState | None = None
    status: Status | None = None


class MemoryChunksOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#MemoryChunks.v1_6_2.MemoryChunks"
    )
    actions: Actions | None = None
    address_range_offset_mib: int | None = Field(
        serialization_alias="AddressRangeOffsetMiB", default=None
    )
    address_range_type: AddressRangeType | None = None
    description: str | None = None
    display_name: str | None = None
    id: str | None = None
    interleave_sets: list[InterleaveSet] | None = None
    is_mirror_enabled: bool | None = None
    is_spare: bool | None = None
    links: Links | None = None
    media_location: MediaLocation | None = None
    memory_chunk_size_mib: int | None = Field(
        serialization_alias="MemoryChunkSizeMiB", default=None
    )
    name: str | None = None
    oem: dict[str, Any] | None = None
    requested_operational_state: OperationalState | None = None
    status: Status | None = None


class MemoryChunksOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    display_name: str | None = None
    interleave_sets: list[InterleaveSet] | None = None
    links: Links | None = None
    media_location: MediaLocation | None = None
    oem: dict[str, Any] | None = None
    requested_operational_state: OperationalState | None = None
    status: Status | None = None


class OperationalState(StrEnum):
    ONLINE = "Online"
    OFFLINE = "Offline"
