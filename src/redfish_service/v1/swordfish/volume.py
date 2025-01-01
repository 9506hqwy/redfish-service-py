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
from ..swordfish.data_storage_lo_scapabilities import ProvisioningPolicy, StorageAccessCapability
from ..swordfish.iostatistics import Iostatistics
from ..swordfish.storage_replica_info import ReplicaInfo


class Alua(RedfishModel):
    anagroup_id: float | None = Field(alias="ANAGroupId", default=None)


class Actions(RedfishModel):
    assign_replica_target: AssignReplicaTarget | None = Field(
        alias="#Volume.AssignReplicaTarget", default=None
    )
    change_raidlayout: ChangeRaidlayout | None = Field(
        alias="#Volume.ChangeRAIDLayout", default=None
    )
    check_consistency: CheckConsistency | None = Field(
        alias="#Volume.CheckConsistency", default=None
    )
    create_replica_target: CreateReplicaTarget | None = Field(
        alias="#Volume.CreateReplicaTarget", default=None
    )
    force_enable: ForceEnable | None = Field(alias="#Volume.ForceEnable", default=None)
    initialize: Initialize | None = Field(alias="#Volume.Initialize", default=None)
    remove_replica_relationship: RemoveReplicaRelationship | None = Field(
        alias="#Volume.RemoveReplicaRelationship", default=None
    )
    resume_replication: ResumeReplication | None = Field(
        alias="#Volume.ResumeReplication", default=None
    )
    reverse_replication_relationship: ReverseReplicationRelationship | None = Field(
        alias="#Volume.ReverseReplicationRelationship", default=None
    )
    split_replication: SplitReplication | None = Field(
        alias="#Volume.SplitReplication", default=None
    )
    suspend_replication: SuspendReplication | None = Field(
        alias="#Volume.SuspendReplication", default=None
    )
    oem: dict[str, Any] | None = None


class AssignReplicaTarget(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ChangeRaidlayout(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class CheckConsistency(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class CreateReplicaTarget(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class EncryptionTypes(StrEnum):
    NATIVE_DRIVE_ENCRYPTION = "NativeDriveEncryption"
    CONTROLLER_ASSISTED = "ControllerAssisted"
    SOFTWARE_ASSISTED = "SoftwareAssisted"


class ForceEnable(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Initialize(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class InitializeMethod(StrEnum):
    SKIP = "Skip"
    BACKGROUND = "Background"
    FOREGROUND = "Foreground"


class Lbaformat(RedfishModel):
    lbadata_size_bytes: int | None = Field(alias="LBADataSizeBytes", default=None)
    lbaformat_type: LbaformatType | None = Field(alias="LBAFormatType", default=None)
    lbametadata_size_bytes: int | None = Field(alias="LBAMetadataSizeBytes", default=None)
    relative_performance: LbarelativePerformanceType | None = None


class LbaformatType(StrEnum):
    LBAFORMAT0 = "LBAFormat0"
    LBAFORMAT1 = "LBAFormat1"
    LBAFORMAT2 = "LBAFormat2"
    LBAFORMAT3 = "LBAFormat3"
    LBAFORMAT4 = "LBAFormat4"
    LBAFORMAT5 = "LBAFormat5"
    LBAFORMAT6 = "LBAFormat6"
    LBAFORMAT7 = "LBAFormat7"
    LBAFORMAT8 = "LBAFormat8"
    LBAFORMAT9 = "LBAFormat9"
    LBAFORMAT10 = "LBAFormat10"
    LBAFORMAT11 = "LBAFormat11"
    LBAFORMAT12 = "LBAFormat12"
    LBAFORMAT13 = "LBAFormat13"
    LBAFORMAT14 = "LBAFormat14"
    LBAFORMAT15 = "LBAFormat15"


class LbarelativePerformanceType(StrEnum):
    BEST = "Best"
    BETTER = "Better"
    GOOD = "Good"
    DEGRADED = "Degraded"


class Links(RedfishModel):
    cache_data_volumes: list[IdRef] | None = None
    cache_data_volumes_odata_count: int | None = Field(
        alias="CacheDataVolumes@odata.count", default=None
    )
    cache_volume_source: IdRef | None = None
    class_of_service: IdRef | None = None
    client_endpoints: list[IdRef] | None = None
    client_endpoints_odata_count: int | None = Field(
        alias="ClientEndpoints@odata.count", default=None
    )
    consistency_groups: list[IdRef] | None = None
    consistency_groups_odata_count: int | None = Field(
        alias="ConsistencyGroups@odata.count", default=None
    )
    controllers: list[IdRef] | None = None
    controllers_odata_count: int | None = Field(alias="Controllers@odata.count", default=None)
    dedicated_spare_drives: list[IdRef] | None = None
    dedicated_spare_drives_odata_count: int | None = Field(
        alias="DedicatedSpareDrives@odata.count", default=None
    )
    drives: list[IdRef] | None = None
    drives_odata_count: int | None = Field(alias="Drives@odata.count", default=None)
    journaling_media: IdRef | None = None
    oem: dict[str, Any] | None = None
    owning_storage_resource: IdRef | None = None
    owning_storage_service: IdRef | None = None
    providing_storage_pool: IdRef | None = None
    server_endpoints: list[IdRef] | None = None
    server_endpoints_odata_count: int | None = Field(
        alias="ServerEndpoints@odata.count", default=None
    )
    spare_resource_sets: list[IdRef] | None = None
    spare_resource_sets_odata_count: int | None = Field(
        alias="SpareResourceSets@odata.count", default=None
    )
    storage_groups: list[IdRef] | None = None
    storage_groups_odata_count: int | None = Field(alias="StorageGroups@odata.count", default=None)


class NvmeNamespaceProperties(RedfishModel):
    formatted_lbasize: str | None = Field(alias="FormattedLBASize", default=None)
    is_shareable: bool | None = None
    lbaformat: Lbaformat | None = Field(alias="LBAFormat", default=None)
    lbaformats: list[Lbaformat] | None = Field(alias="LBAFormats", default=None)
    lbaformats_supported: list[LbaformatType] | None = Field(
        alias="LBAFormatsSupported", default=None
    )
    metadata_transferred_at_end_of_data_lba: bool | None = Field(
        alias="MetadataTransferredAtEndOfDataLBA", default=None
    )
    nvme_version: str | None = Field(alias="NVMeVersion", default=None)
    namespace_features: NamespaceFeatures | None = None
    namespace_id: str | None = None
    namespace_type: NamespaceType | None = None
    number_lbaformats: int | None = Field(alias="NumberLBAFormats", default=None)
    supports_ioperformance_hints: bool | None = Field(
        alias="SupportsIOPerformanceHints", default=None
    )
    supports_multiple_namespace_attachments: bool | None = None
    type: NamespaceType | None = None


class NamespaceFeatures(RedfishModel):
    supports_atomic_transaction_size: bool | None = None
    supports_deallocated_or_unwritten_lberror: bool | None = Field(
        alias="SupportsDeallocatedOrUnwrittenLBError", default=None
    )
    supports_ioperformance_hints: bool | None = Field(
        alias="SupportsIOPerformanceHints", default=None
    )
    supports_nguidreuse: bool | None = Field(alias="SupportsNGUIDReuse", default=None)
    supports_thin_provisioning: bool | None = None


class NamespaceType(StrEnum):
    BLOCK = "Block"
    KEY_VALUE = "KeyValue"
    ZNS = "ZNS"
    COMPUTATIONAL = "Computational"


class Operation(RedfishModel):
    associated_features_registry: IdRef | None = None
    operation: OperationType | None = None
    operation_name: str | None = None
    percentage_complete: int | None = None


class OperationType(StrEnum):
    DEDUPLICATE = "Deduplicate"
    CHECK_CONSISTENCY = "CheckConsistency"
    INITIALIZE = "Initialize"
    REPLICATE = "Replicate"
    DELETE = "Delete"
    CHANGE_RAIDTYPE = "ChangeRAIDType"
    REBUILD = "Rebuild"
    ENCRYPT = "Encrypt"
    DECRYPT = "Decrypt"
    RESIZE = "Resize"
    COMPRESS = "Compress"
    SANITIZE = "Sanitize"
    FORMAT = "Format"
    CHANGE_STRIP_SIZE = "ChangeStripSize"


class Raidtype(StrEnum):
    RAID0 = "RAID0"
    RAID1 = "RAID1"
    RAID3 = "RAID3"
    RAID4 = "RAID4"
    RAID5 = "RAID5"
    RAID6 = "RAID6"
    RAID10 = "RAID10"
    RAID01 = "RAID01"
    RAID6_TP = "RAID6TP"
    RAID1_E = "RAID1E"
    RAID50 = "RAID50"
    RAID60 = "RAID60"
    RAID00 = "RAID00"
    RAID10_E = "RAID10E"
    RAID1_TRIPLE = "RAID1Triple"
    RAID10_TRIPLE = "RAID10Triple"
    NONE = "None"


class ReadCachePolicyType(StrEnum):
    READ_AHEAD = "ReadAhead"
    ADAPTIVE_READ_AHEAD = "AdaptiveReadAhead"
    OFF = "Off"


class RemoveReplicaRelationship(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ResumeReplication(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ReverseReplicationRelationship(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SplitReplication(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SuspendReplication(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Volume(RedfishResource):
    alua: Alua | None = Field(alias="ALUA", default=None)
    access_capabilities: list[StorageAccessCapability] | None = None
    actions: Actions | None = None
    allocated_pools: IdRef | None = None
    block_size_bytes: int | None = None
    capacity: Capacity | None = None
    capacity_bytes: int | None = None
    capacity_sources: list[IdRef] | None = None
    capacity_sources_odata_count: int | None = Field(
        alias="CapacitySources@odata.count", default=None
    )
    compressed: bool | None = None
    connections: list[IdRef] | None = None
    connections_odata_count: int | None = Field(alias="Connections@odata.count", default=None)
    deduplicated: bool | None = None
    description: str | None = None
    display_name: str | None = None
    encrypted: bool | None = None
    encryption_types: list[EncryptionTypes] | None = None
    ioperf_mode_enabled: bool | None = Field(alias="IOPerfModeEnabled", default=None)
    iostatistics: Iostatistics | None = Field(alias="IOStatistics", default=None)
    identifiers: list[Identifier] | None = None
    initialize_method: InitializeMethod | None = None
    is_boot_capable: bool | None = None
    links: Links | None = None
    logical_unit_number: int | None = None
    low_space_warning_threshold_percents: list[int] | None = None
    manufacturer: str | None = None
    max_block_size_bytes: int | None = None
    media_span_count: int | None = None
    metrics: IdRef | None = None
    model: str | None = None
    nvme_namespace_properties: NvmeNamespaceProperties | None = Field(
        alias="NVMeNamespaceProperties", default=None
    )
    oem: dict[str, Any] | None = None
    operations: list[Operation] | None = None
    optimum_iosize_bytes: int | None = Field(alias="OptimumIOSizeBytes", default=None)
    provisioning_policy: ProvisioningPolicy | None = None
    raidtype: Raidtype | None = Field(alias="RAIDType", default=None)
    read_cache_policy: ReadCachePolicyType | None = None
    recoverable_capacity_source_count: int | None = None
    remaining_capacity_percent: int | None = None
    remote_replica_targets: list[str] | None = None
    replica_info: ReplicaInfo | None = None
    replica_targets: list[IdRef] | None = None
    replica_targets_odata_count: int | None = Field(
        alias="ReplicaTargets@odata.count", default=None
    )
    replication_enabled: bool | None = None
    status: Status | None = None
    storage_groups: IdRef | None = None
    strip_size_bytes: int | None = None
    volume_type: VolumeType | None = None
    volume_usage: VolumeUsageType | None = None
    write_cache_policy: WriteCachePolicyType | None = None
    write_cache_state: WriteCacheStateType | None = None
    write_hole_protection_policy: WriteHoleProtectionPolicyType | None = None


class VolumeType(StrEnum):
    RAW_DEVICE = "RawDevice"
    NON_REDUNDANT = "NonRedundant"
    MIRRORED = "Mirrored"
    STRIPED_WITH_PARITY = "StripedWithParity"
    SPANNED_MIRRORS = "SpannedMirrors"
    SPANNED_STRIPES_WITH_PARITY = "SpannedStripesWithParity"


class VolumeUsageType(StrEnum):
    DATA = "Data"
    SYSTEM_DATA = "SystemData"
    CACHE_ONLY = "CacheOnly"
    SYSTEM_RESERVE = "SystemReserve"
    REPLICATION_RESERVE = "ReplicationReserve"


class WriteCachePolicyType(StrEnum):
    WRITE_THROUGH = "WriteThrough"
    PROTECTED_WRITE_BACK = "ProtectedWriteBack"
    UNPROTECTED_WRITE_BACK = "UnprotectedWriteBack"
    OFF = "Off"


class WriteCacheStateType(StrEnum):
    UNPROTECTED = "Unprotected"
    PROTECTED = "Protected"
    DEGRADED = "Degraded"


class WriteHoleProtectionPolicyType(StrEnum):
    OFF = "Off"
    JOURNALING = "Journaling"
    DISTRIBUTED_LOG = "DistributedLog"
    OEM = "Oem"
