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
from ..swordfish.storage_replica_info import ReplicaInfo


class Actions(RedfishModel):
    oem: OemActions | None = None


class AssignReplicaTarget(RedfishModel):
    target: str | None = None
    title: str | None = None


class ChangeRaidlayout(RedfishModel):
    target: str | None = None
    title: str | None = None


class CheckConsistency(RedfishModel):
    target: str | None = None
    title: str | None = None


class CreateReplicaTarget(RedfishModel):
    target: str | None = None
    title: str | None = None


class EncryptionTypes(StrEnum):
    NATIVE_DRIVE_ENCRYPTION = "NativeDriveEncryption"
    CONTROLLER_ASSISTED = "ControllerAssisted"
    SOFTWARE_ASSISTED = "SoftwareAssisted"


class ForceEnable(RedfishModel):
    target: str | None = None
    title: str | None = None


class Initialize(RedfishModel):
    target: str | None = None
    title: str | None = None


class InitializeMethod(StrEnum):
    SKIP = "Skip"
    BACKGROUND = "Background"
    FOREGROUND = "Foreground"


class InitializeType(StrEnum):
    FAST = "Fast"
    SLOW = "Slow"


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
    cache_volume_source: str | None = None
    class_of_service: IdRef | None = None
    client_endpoints: list[IdRef] | None = None
    consistency_groups: list[IdRef] | None = None
    controllers: list[IdRef] | None = None
    dedicated_spare_drives: list[IdRef] | None = None
    drives: list[IdRef] | None = None
    journaling_media: str | None = None
    oem: dict[str, Any] | None = None
    owning_storage_resource: IdRef | None = None
    owning_storage_service: IdRef | None = None
    server_endpoints: list[IdRef] | None = None
    spare_resource_sets: list[IdRef] | None = None
    storage_groups: list[IdRef] | None = None


class NamespaceType(StrEnum):
    BLOCK = "Block"
    KEY_VALUE = "KeyValue"
    ZNS = "ZNS"
    COMPUTATIONAL = "Computational"


class OemActions(RedfishModel):
    pass


class Operation(RedfishModel):
    associated_features_registry: IdRef | None = None
    operation: str | None = None
    operation_name: str | None = None
    percentage_complete: str | None = None


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
    target: str | None = None
    title: str | None = None


class ResumeReplication(RedfishModel):
    target: str | None = None
    title: str | None = None


class ReverseReplicationRelationship(RedfishModel):
    target: str | None = None
    title: str | None = None


class SplitReplication(RedfishModel):
    target: str | None = None
    title: str | None = None


class SuspendReplication(RedfishModel):
    target: str | None = None
    title: str | None = None


class Volume(RedfishResource):
    access_capabilities: list[str] | None = None
    actions: Actions | None = None
    allocated_pools: IdRef | None = None
    block_size_bytes: str | None = None
    capacity: Capacity | None = None
    capacity_bytes: str | None = None
    capacity_sources: list[IdRef] | None = None
    compressed: str | None = None
    connections: list[IdRef] | None = None
    deduplicated: str | None = None
    description: str | None = None
    display_name: str | None = None
    encrypted: str | None = None
    encryption_types: list[EncryptionTypes] | None = None
    ioperf_mode_enabled: str | None = None
    iostatistics: Iostatistics | None = None
    identifiers: list[Identifier] | None = None
    initialize_method: str | None = None
    is_boot_capable: str | None = None
    links: Links | None = None
    logical_unit_number: str | None = None
    low_space_warning_threshold_percents: list[str] | None = None
    manufacturer: str | None = None
    max_block_size_bytes: str | None = None
    media_span_count: str | None = None
    metrics: IdRef | None = None
    model: str | None = None
    nvme_namespace_properties: str | None = None
    oem: dict[str, Any] | None = None
    operations: list[Operation] | None = None
    optimum_iosize_bytes: str | None = None
    provisioning_policy: str | None = None
    raidtype: str | None = None
    read_cache_policy: str | None = None
    recoverable_capacity_source_count: str | None = None
    remaining_capacity_percent: str | None = None
    remote_replica_targets: list[str] | None = None
    replica_info: ReplicaInfo | None = None
    replica_targets: list[IdRef] | None = None
    replication_enabled: str | None = None
    status: Status | None = None
    storage_groups: IdRef | None = None
    strip_size_bytes: str | None = None
    volume_type: str | None = None
    volume_usage: str | None = None
    write_cache_policy: str | None = None
    write_cache_state: str | None = None
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
