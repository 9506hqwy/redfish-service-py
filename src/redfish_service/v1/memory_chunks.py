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


class InterleaveSet(RedfishModel):
    memory: IdRef | None = None
    memory_level: str | None = None
    offset_mi_b: str | None = None
    region_id: str | None = None
    size_mi_b: str | None = None


class Links(RedfishModel):
    cxllogical_devices: list[IdRef] | None = Field(alias="CXLLogicalDevices", default=None)
    cxllogical_devices_odata_count: int | None = Field(
        alias="CXLLogicalDevices@odata.count", default=None
    )
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    memory_regions: list[IdRef] | None = None
    memory_regions_odata_count: int | None = Field(alias="MemoryRegions@odata.count", default=None)
    oem: dict[str, Any] | None = None


class MemoryChunks(RedfishResource):
    actions: Actions | None = None
    address_range_offset_mi_b: str | None = None
    address_range_type: str
    description: str | None = None
    display_name: str | None = None
    interleave_sets: list[InterleaveSet] | None = None
    is_mirror_enabled: str | None = None
    is_spare: str | None = None
    links: Links | None = None
    media_location: str | None = None
    memory_chunk_size_mi_b: str | None = None
    oem: dict[str, Any] | None = None
    requested_operational_state: str | None = None
    status: Status | None = None
