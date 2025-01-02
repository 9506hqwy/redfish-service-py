from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from ..base import RedfishModel
from ..odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ConsistencyState(StrEnum):
    CONSISTENT = "Consistent"
    INCONSISTENT = "Inconsistent"


class ConsistencyStatus(StrEnum):
    CONSISTENT = "Consistent"
    IN_PROGRESS = "InProgress"
    DISABLED = "Disabled"
    IN_ERROR = "InError"


class ConsistencyType(StrEnum):
    SEQUENTIALLY_CONSISTENT = "SequentiallyConsistent"


class ReplicaFaultDomain(StrEnum):
    LOCAL = "Local"
    REMOTE = "Remote"


class ReplicaInfo(RedfishModel):
    consistency_enabled: bool | None = None
    consistency_state: ConsistencyState | None = None
    consistency_status: ConsistencyStatus | None = None
    consistency_type: ConsistencyType | None = None
    data_protection_line_of_service: IdRef | None = None
    failed_copy_stops_host_io: bool | None = Field(alias="FailedCopyStopsHostIO", default=None)
    percent_synced: int | None = None
    remote_source_replica: str | None = None
    replica: IdRef | None = None
    replica_fault_domain: ReplicaFaultDomain | None = None
    replica_priority: ReplicaPriority | None = None
    replica_progress_status: ReplicaProgressStatus | None = None
    replica_read_only_access: ReplicaReadOnlyAccess | None = None
    replica_recovery_mode: ReplicaRecoveryMode | None = None
    replica_role: ReplicaRole | None = None
    replica_skew_bytes: int | None = None
    replica_state: ReplicaState | None = None
    replica_type: ReplicaType | None = None
    replica_update_mode: ReplicaUpdateMode | None = None
    requested_replica_state: ReplicaState | None = None
    source_replica: IdRef | None = None
    sync_maintained: bool | None = None
    undiscovered_element: UndiscoveredElement | None = None
    when_activated: str | None = None
    when_deactivated: str | None = None
    when_established: str | None = None
    when_suspended: str | None = None
    when_synced: str | None = None
    when_synchronized: str | None = None


class ReplicaPriority(StrEnum):
    LOW = "Low"
    SAME = "Same"
    HIGH = "High"
    URGENT = "Urgent"


class ReplicaProgressStatus(StrEnum):
    COMPLETED = "Completed"
    DORMANT = "Dormant"
    INITIALIZING = "Initializing"
    PREPARING = "Preparing"
    SYNCHRONIZING = "Synchronizing"
    RESYNCING = "Resyncing"
    RESTORING = "Restoring"
    FRACTURING = "Fracturing"
    SPLITTING = "Splitting"
    FAILING_OVER = "FailingOver"
    FAILING_BACK = "FailingBack"
    DETACHING = "Detaching"
    ABORTING = "Aborting"
    MIXED = "Mixed"
    SUSPENDING = "Suspending"
    REQUIRES_FRACTURE = "RequiresFracture"
    REQUIRES_RESYNC = "RequiresResync"
    REQUIRES_ACTIVATE = "RequiresActivate"
    PENDING = "Pending"
    REQUIRES_DETACH = "RequiresDetach"
    TERMINATING = "Terminating"
    REQUIRES_SPLIT = "RequiresSplit"
    REQUIRES_RESUME = "RequiresResume"


class ReplicaReadOnlyAccess(StrEnum):
    SOURCE_ELEMENT = "SourceElement"
    REPLICA_ELEMENT = "ReplicaElement"
    BOTH = "Both"


class ReplicaRecoveryMode(StrEnum):
    AUTOMATIC = "Automatic"
    MANUAL = "Manual"


class ReplicaRole(StrEnum):
    SOURCE = "Source"
    TARGET = "Target"


class ReplicaState(StrEnum):
    INITIALIZED = "Initialized"
    UNSYNCHRONIZED = "Unsynchronized"
    SYNCHRONIZED = "Synchronized"
    BROKEN = "Broken"
    FRACTURED = "Fractured"
    SPLIT = "Split"
    INACTIVE = "Inactive"
    SUSPENDED = "Suspended"
    FAILEDOVER = "Failedover"
    PREPARED = "Prepared"
    ABORTED = "Aborted"
    SKEWED = "Skewed"
    MIXED = "Mixed"
    PARTITIONED = "Partitioned"
    INVALID = "Invalid"
    RESTORED = "Restored"


class ReplicaType(StrEnum):
    MIRROR = "Mirror"
    SNAPSHOT = "Snapshot"
    CLONE = "Clone"
    TOKENIZED_CLONE = "TokenizedClone"


class ReplicaUpdateMode(StrEnum):
    ACTIVE = "Active"
    SYNCHRONOUS = "Synchronous"
    ASYNCHRONOUS = "Asynchronous"
    ADAPTIVE = "Adaptive"


class StorageReplicaInfo(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None


class UndiscoveredElement(StrEnum):
    SOURCE_ELEMENT = "SourceElement"
    REPLICA_ELEMENT = "ReplicaElement"
