from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .resource import Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class MemoryRegion(RedfishResource):
    actions: Actions | None = None
    block_size_mi_b: int | None = None
    description: str | None = None
    extents_count: str | None = None
    hardware_managed_coherency_region: str | None = None
    memory_chunks: list[str] | None = None
    memory_extents: list[str] | None = None
    non_volatile_region: str | None = None
    oem: dict[str, Any] | None = None
    region_base_offset_mi_b: int | None = None
    region_number: int | None = None
    region_size_mi_b: int | None = None
    region_type: RegionType
    sanitize_on_release: str | None = None
    shareable_region: str | None = None
    status: Status | None = None


class OemActions(RedfishModel):
    pass


class RegionType(StrEnum):
    STATIC = "Static"
    DYNAMIC = "Dynamic"
