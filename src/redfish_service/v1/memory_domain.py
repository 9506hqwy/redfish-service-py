from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    cxl_logical_devices: list[IdRef] | None = Field(alias="CXLLogicalDevices", default=None)
    cxl_logical_devices_odata_count: int | None = Field(
        alias="CXLLogicalDevices@odata.count", default=None
    )
    fabric_adapters: list[IdRef] | None = None
    fabric_adapters_odata_count: int | None = Field(
        alias="FabricAdapters@odata.count", default=None
    )
    media_controllers: list[IdRef] | None = None
    media_controllers_odata_count: int | None = Field(
        alias="MediaControllers@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = Field(alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(alias="PCIeFunctions@odata.count", default=None)


class MemoryDomain(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    allows_block_provisioning: bool | None = None
    allows_memory_chunk_creation: bool | None = None
    allows_mirroring: bool | None = None
    allows_sparing: bool | None = None
    description: str | None = None
    id: str
    interleavable_memory_sets: list[MemorySet] | None = None
    links: Links | None = None
    memory_chunk_increment_mib: int | None = Field(alias="MemoryChunkIncrementMiB", default=None)
    memory_chunks: IdRef | None = None
    memory_size_mib: int | None = Field(alias="MemorySizeMiB", default=None)
    min_memory_chunk_size_mib: int | None = Field(alias="MinMemoryChunkSizeMiB", default=None)
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None


class MemorySet(RedfishModel):
    memory_set: list[IdRef] | None = None
    memory_set_odata_count: int | None = Field(alias="MemorySet@odata.count", default=None)
