from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef


class Actions(RedfishModel):
    oem: OemActions | None = None


class OemActions(RedfishModel):
    pass


class ReplicaFaultDomain(StrEnum):
    LOCAL = "Local"
    REMOTE = "Remote"


class ReplicaInfo(RedfishModel):
    consistency_enabled: str | None = None
    consistency_state: str | None = None
    consistency_status: str | None = None
    consistency_type: str | None = None
    data_protection_line_of_service: IdRef | None = None
    failed_copy_stops_host_io: str | None = None
    percent_synced: str | None = None
    remote_source_replica: str | None = None
    replica: IdRef | None = None
    replica_fault_domain: str | None = None
    replica_priority: str | None = None
    replica_progress_status: str | None = None
    replica_read_only_access: str | None = None
    replica_recovery_mode: str | None = None
    replica_role: str | None = None
    replica_skew_bytes: str | None = None
    replica_state: str | None = None
    replica_type: str | None = None
    replica_update_mode: str | None = None
    requested_replica_state: str | None = None
    source_replica: IdRef | None = None
    sync_maintained: str | None = None
    undiscovered_element: str | None = None
    when_activated: str | None = None
    when_deactivated: str | None = None
    when_established: str | None = None
    when_suspended: str | None = None
    when_synced: str | None = None
    when_synchronized: str | None = None


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


class StorageReplicaInfo(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
