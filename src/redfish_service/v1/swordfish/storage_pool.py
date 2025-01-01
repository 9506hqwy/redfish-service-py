from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier, Status
from ..swordfish.capacity import Capacity
from ..swordfish.iostatistics import Iostatistics


class Actions(RedfishModel):
    add_drives: AddDrives | None = Field(alias="#StoragePool.AddDrives", default=None)
    remove_drives: RemoveDrives | None = Field(alias="#StoragePool.RemoveDrives", default=None)
    set_compression_state: SetCompressionState | None = Field(
        alias="#StoragePool.SetCompressionState", default=None
    )
    set_deduplication_state: SetDeduplicationState | None = Field(
        alias="#StoragePool.SetDeduplicationState", default=None
    )
    set_encryption_state: SetEncryptionState | None = Field(
        alias="#StoragePool.SetEncryptionState", default=None
    )
    oem: dict[str, Any] | None = None


class AddDrives(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Links(RedfishModel):
    dedicated_spare_drives: list[IdRef] | None = None
    dedicated_spare_drives_odata_count: int | None = Field(
        alias="DedicatedSpareDrives@odata.count", default=None
    )
    default_class_of_service: IdRef | None = None
    oem: dict[str, Any] | None = None
    owning_storage_resource: IdRef | None = None
    spare_resource_sets: list[IdRef] | None = None
    spare_resource_sets_odata_count: int | None = Field(
        alias="SpareResourceSets@odata.count", default=None
    )


class NvmePoolType(StrEnum):
    ENDURANCE_GROUP = "EnduranceGroup"
    NVMSET = "NVMSet"


class PoolType(StrEnum):
    BLOCK = "Block"
    FILE = "File"
    OBJECT = "Object"
    POOL = "Pool"


class RemoveDrives(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SetCompressionState(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SetDeduplicationState(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SetEncryptionState(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class StoragePool(RedfishResource):
    actions: Actions | None = None
    allocated_pools: IdRef | None = None
    allocated_volumes: IdRef | None = None
    block_size_bytes: str | None = None
    capacity: Capacity | None = None
    capacity_sources: list[IdRef] | None = None
    capacity_sources_odata_count: int | None = Field(
        alias="CapacitySources@odata.count", default=None
    )
    classes_of_service: IdRef | None = None
    compressed: str | None = None
    compression_enabled: str | None = None
    deduplicated: str | None = None
    deduplication_enabled: str | None = None
    default_class_of_service: IdRef | None = None
    default_compression_behavior: str | None = None
    default_deduplication_behavior: str | None = None
    default_encryption_behavior: str | None = None
    description: str | None = None
    encrypted: str | None = None
    encryption_enabled: str | None = None
    iostatistics: Iostatistics | None = Field(alias="IOStatistics", default=None)
    identifier: Identifier | None = None
    links: Links | None = None
    low_space_warning_threshold_percents: list[str] | None = None
    max_block_size_bytes: str | None = None
    metrics: str | None = None
    nvme_endurance_group_properties: str | None = Field(
        alias="NVMeEnduranceGroupProperties", default=None
    )
    nvme_properties: str | None = Field(alias="NVMeProperties", default=None)
    nvme_set_properties: str | None = Field(alias="NVMeSetProperties", default=None)
    oem: dict[str, Any] | None = None
    pool_type: list[str] | None = None
    recoverable_capacity_source_count: str | None = None
    remaining_capacity_percent: str | None = None
    replication_enabled: str | None = None
    status: Status | None = None
    supported_pool_types: list[str] | None = None
    supported_provisioning_policies: list[str] | None = None
    supported_raidtypes: list[str] | None = Field(alias="SupportedRAIDTypes", default=None)
