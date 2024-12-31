from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Status
from ..swordfish.storage_replica_info import ReplicaInfo


class Actions(RedfishModel):
    oem: OemActions | None = None


class ApplicationConsistencyMethod(StrEnum):
    HOT_STANDBY = "HotStandby"
    VASA = "VASA"
    VDI = "VDI"
    VSS = "VSS"
    OTHER = "Other"


class AssignReplicaTarget(RedfishModel):
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


class CreateReplicaTarget(RedfishModel):
    target: str | None = None
    title: str | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None


class OemActions(RedfishModel):
    pass


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
