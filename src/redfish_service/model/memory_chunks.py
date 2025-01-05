from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
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
    offset_mib: int | None = Field(alias="OffsetMiB", default=None)
    region_id: str | None = None
    size_mib: int | None = Field(alias="SizeMiB", default=None)


class Links(RedfishModel):
    cxl_logical_devices: list[IdRef] | None = Field(alias="CXLLogicalDevices", default=None)
    cxl_logical_devices_odata_count: int | None = Field(
        alias="CXLLogicalDevices@odata.count", default=None
    )
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    memory_regions: list[IdRef] | None = None
    memory_regions_odata_count: int | None = Field(alias="MemoryRegions@odata.count", default=None)
    oem: dict[str, Any] | None = None


class MediaLocation(StrEnum):
    LOCAL = "Local"
    REMOTE = "Remote"
    MIXED = "Mixed"


class MemoryChunks(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#MemoryChunks.v1_6_2.MemoryChunks")
    actions: Actions | None = None
    address_range_offset_mib: int | None = Field(alias="AddressRangeOffsetMiB", default=None)
    address_range_type: AddressRangeType | None = None
    description: str | None = None
    display_name: str | None = None
    id: str
    interleave_sets: list[InterleaveSet] | None = None
    is_mirror_enabled: bool | None = None
    is_spare: bool | None = None
    links: Links | None = None
    media_location: MediaLocation | None = None
    memory_chunk_size_mib: int | None = Field(alias="MemoryChunkSizeMiB", default=None)
    name: str
    oem: dict[str, Any] | None = None
    requested_operational_state: OperationalState | None = None
    status: Status | None = None


class OperationalState(StrEnum):
    ONLINE = "Online"
    OFFLINE = "Offline"
