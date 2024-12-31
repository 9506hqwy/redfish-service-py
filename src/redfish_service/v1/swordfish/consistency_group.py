from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from ..base import RedfishResource
from ..odata_v4 import IdRef
from ..resource import Status
from ..swordfish.storage_replica_info import ReplicaInfo


class Actions(RedfishResource):
    oem: OemActions | None = None


class ApplicationConsistencyMethod(StrEnum):
    HOT_STANDBY = "HotStandby"
    VASA = "VASA"
    VDI = "VDI"
    VSS = "VSS"
    OTHER = "Other"


class AssignReplicaTarget(RedfishResource):
    target: str | None = None
    title: str | None = None


class ConsistencyGroup(RedfishResource):
    actions: Actions | None = None
    consistency_method: str | None = None
    consistency_type: str | None = None
    description: str | None = None
    is_consistent: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    remote_replica_targets: list[str] | None = None
    replica_info: ReplicaInfo | None = None
    replica_targets: list[IdRef] | None = None
    status: Status | None = None
    volumes: list[IdRef] | None = None


class ConsistencyType(StrEnum):
    CRASH_CONSISTENT = "CrashConsistent"
    APPLICATION_CONSISTENT = "ApplicationConsistent"


class CreateReplicaTarget(RedfishResource):
    target: str | None = None
    title: str | None = None


class Links(RedfishResource):
    oem: dict[str, Any] | None = None


class OemActions(RedfishResource):
    pass


class RemoveReplicaRelationship(RedfishResource):
    target: str | None = None
    title: str | None = None


class ResumeReplication(RedfishResource):
    target: str | None = None
    title: str | None = None


class ReverseReplicationRelationship(RedfishResource):
    target: str | None = None
    title: str | None = None


class SplitReplication(RedfishResource):
    target: str | None = None
    title: str | None = None


class SuspendReplication(RedfishResource):
    target: str | None = None
    title: str | None = None
