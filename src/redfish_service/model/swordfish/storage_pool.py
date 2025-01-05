from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .. import RedfishModel
from ..odata_v4 import IdRef
from ..resource import Identifier, Status
from ..swordfish.capacity import Capacity
from ..swordfish.data_storage_los_capabilities import ProvisioningPolicy
from ..swordfish.io_statistics import IoStatistics
from ..swordfish.volume import RaidType


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


class EndGrpLifetime(RedfishModel):
    data_units_read: int | None = None
    data_units_written: int | None = None
    endurance_estimate: int | None = None
    error_information_log_entry_count: int | None = None
    host_read_command_count: int | None = None
    host_write_command_count: int | None = None
    media_and_data_integrity_error_count: int | None = None
    media_units_written: int | None = None
    percent_used: int | None = None


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


class NvmeEnduranceGroupProperties(RedfishModel):
    end_grp_lifetime: EndGrpLifetime | None = None
    predicted_media_life_left_percent: float | None = None


class NvmePoolType(StrEnum):
    ENDURANCE_GROUP = "EnduranceGroup"
    NVM_SET = "NVMSet"


class NvmeProperties(RedfishModel):
    nvme_pool_type: NvmePoolType | None = Field(alias="NVMePoolType", default=None)


class NvmeSetProperties(RedfishModel):
    endurance_group_identifier: str | None = None
    optimal_write_size_bytes: int | None = None
    random4k_read_typical_nano_seconds: int | None = None
    set_identifier: str | None = None
    unallocated_nvm_namespace_capacity_bytes: int | None = Field(
        alias="UnallocatedNVMNamespaceCapacityBytes", default=None
    )


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


class StoragePool(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#StoragePool.v1_9_1.StoragePool")
    actions: Actions | None = None
    allocated_pools: IdRef | None = None
    allocated_volumes: IdRef | None = None
    block_size_bytes: int | None = None
    capacity: Capacity | None = None
    capacity_sources: list[IdRef] | None = None
    capacity_sources_odata_count: int | None = Field(
        alias="CapacitySources@odata.count", default=None
    )
    classes_of_service: IdRef | None = None
    compressed: bool | None = None
    compression_enabled: bool | None = None
    deduplicated: bool | None = None
    deduplication_enabled: bool | None = None
    default_class_of_service: IdRef | None = None
    default_compression_behavior: bool | None = None
    default_deduplication_behavior: bool | None = None
    default_encryption_behavior: bool | None = None
    description: str | None = None
    encrypted: bool | None = None
    encryption_enabled: bool | None = None
    io_statistics: IoStatistics | None = Field(alias="IOStatistics", default=None)
    id: str
    identifier: Identifier | None = None
    links: Links | None = None
    low_space_warning_threshold_percents: list[int] | None = None
    max_block_size_bytes: int | None = None
    metrics: IdRef | None = None
    nvme_endurance_group_properties: NvmeEnduranceGroupProperties | None = Field(
        alias="NVMeEnduranceGroupProperties", default=None
    )
    nvme_properties: NvmeProperties | None = Field(alias="NVMeProperties", default=None)
    nvme_set_properties: NvmeSetProperties | None = Field(alias="NVMeSetProperties", default=None)
    name: str
    oem: dict[str, Any] | None = None
    pool_type: list[PoolType] | None = None
    recoverable_capacity_source_count: int | None = None
    remaining_capacity_percent: int | None = None
    replication_enabled: bool | None = None
    status: Status | None = None
    supported_pool_types: list[PoolType] | None = None
    supported_provisioning_policies: list[ProvisioningPolicy] | None = None
    supported_raid_types: list[RaidType] | None = Field(alias="SupportedRAIDTypes", default=None)
