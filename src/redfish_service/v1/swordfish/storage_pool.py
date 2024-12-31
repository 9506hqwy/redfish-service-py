from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier, Status
from ..swordfish.capacity import Capacity
from ..swordfish.iostatistics import Iostatistics


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AddDrives(RedfishModel):
    target: str | None = None
    title: str | None = None


class Links(RedfishModel):
    dedicated_spare_drives: list[IdRef] | None = None
    default_class_of_service: IdRef | None = None
    oem: dict[str, Any] | None = None
    owning_storage_resource: IdRef | None = None
    spare_resource_sets: list[IdRef] | None = None


class NvmePoolType(StrEnum):
    ENDURANCE_GROUP = "EnduranceGroup"
    NVMSET = "NVMSet"


class PoolType(StrEnum):
    BLOCK = "Block"
    FILE = "File"
    OBJECT = "Object"
    POOL = "Pool"


class RemoveDrives(RedfishModel):
    target: str | None = None
    title: str | None = None


class SetCompressionState(RedfishModel):
    target: str | None = None
    title: str | None = None


class SetDeduplicationState(RedfishModel):
    target: str | None = None
    title: str | None = None


class SetEncryptionState(RedfishModel):
    target: str | None = None
    title: str | None = None


class StoragePool(RedfishResource):
    actions: Actions | None = None
    allocated_pools: IdRef | None = None
    allocated_volumes: IdRef | None = None
    block_size_bytes: str | None = None
    capacity: Capacity | None = None
    capacity_sources: list[IdRef] | None = None
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
    iostatistics: Iostatistics | None = None
    identifier: Identifier | None = None
    links: Links | None = None
    low_space_warning_threshold_percents: list[str] | None = None
    max_block_size_bytes: str | None = None
    metrics: str | None = None
    nvme_endurance_group_properties: str | None = None
    nvme_properties: str | None = None
    nvme_set_properties: str | None = None
    oem: dict[str, Any] | None = None
    pool_type: list[str] | None = None
    recoverable_capacity_source_count: str | None = None
    remaining_capacity_percent: str | None = None
    replication_enabled: str | None = None
    status: Status | None = None
    supported_pool_types: list[str] | None = None
    supported_provisioning_policies: list[str] | None = None
    supported_raidtypes: list[str] | None = None
