from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    cxl_logical_devices: list[IdRef] | None = Field(
        serialization_alias="CXLLogicalDevices", default=None
    )
    cxl_logical_devices_odata_count: int | None = Field(
        serialization_alias="CXLLogicalDevices@odata.count", default=None
    )
    fabric_adapters: list[IdRef] | None = None
    fabric_adapters_odata_count: int | None = Field(
        serialization_alias="FabricAdapters@odata.count", default=None
    )
    media_controllers: list[IdRef] | None = None
    media_controllers_odata_count: int | None = Field(
        serialization_alias="MediaControllers@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = Field(serialization_alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(
        serialization_alias="PCIeFunctions@odata.count", default=None
    )


class MemoryDomain(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#MemoryDomain.v1_5_1.MemoryDomain"
    )
    actions: Actions | None = None
    allows_block_provisioning: bool | None = None
    allows_memory_chunk_creation: bool | None = None
    allows_mirroring: bool | None = None
    allows_sparing: bool | None = None
    description: str | None = None
    id: str
    interleavable_memory_sets: list[MemorySet] | None = None
    links: Links | None = None
    memory_chunk_increment_mib: int | None = Field(
        serialization_alias="MemoryChunkIncrementMiB", default=None
    )
    memory_chunks: IdRef | None = None
    memory_size_mib: int | None = Field(serialization_alias="MemorySizeMiB", default=None)
    min_memory_chunk_size_mib: int | None = Field(
        serialization_alias="MinMemoryChunkSizeMiB", default=None
    )
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None


class MemorySet(RedfishModel):
    memory_set: list[IdRef] | None = None
    memory_set_odata_count: int | None = Field(
        serialization_alias="MemorySet@odata.count", default=None
    )
