from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .. import RedfishModel
from ..odata_v4 import IdRef
from ..resource import Status
from ..swordfish.storage_replica_info import ReplicaInfo


class Actions(RedfishModel):
    assign_replica_target: AssignReplicaTarget | None = Field(
        alias="#ConsistencyGroup.AssignReplicaTarget", default=None
    )
    create_replica_target: CreateReplicaTarget | None = Field(
        alias="#ConsistencyGroup.CreateReplicaTarget", default=None
    )
    remove_replica_relationship: RemoveReplicaRelationship | None = Field(
        alias="#ConsistencyGroup.RemoveReplicaRelationship", default=None
    )
    resume_replication: ResumeReplication | None = Field(
        alias="#ConsistencyGroup.ResumeReplication", default=None
    )
    reverse_replication_relationship: ReverseReplicationRelationship | None = Field(
        alias="#ConsistencyGroup.ReverseReplicationRelationship", default=None
    )
    split_replication: SplitReplication | None = Field(
        alias="#ConsistencyGroup.SplitReplication", default=None
    )
    suspend_replication: SuspendReplication | None = Field(
        alias="#ConsistencyGroup.SuspendReplication", default=None
    )
    oem: dict[str, Any] | None = None


class ApplicationConsistencyMethod(StrEnum):
    HOT_STANDBY = "HotStandby"
    VASA = "VASA"
    VDI = "VDI"
    VSS = "VSS"
    OTHER = "Other"


class AssignReplicaTarget(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ConsistencyGroup(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type", default="#ConsistencyGroup.v1_1_1.ConsistencyGroup"
    )
    actions: Actions | None = None
    consistency_method: ApplicationConsistencyMethod | None = None
    consistency_type: ConsistencyType | None = None
    description: str | None = None
    id: str
    is_consistent: bool | None = None
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    remote_replica_targets: list[str] | None = None
    replica_info: ReplicaInfo | None = None
    replica_targets: list[IdRef] | None = None
    replica_targets_odata_count: int | None = Field(
        alias="ReplicaTargets@odata.count", default=None
    )
    status: Status | None = None
    volumes: list[IdRef] | None = None
    volumes_odata_count: int | None = Field(alias="Volumes@odata.count", default=None)


class ConsistencyGroupOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(
        alias="@odata.type", default="#ConsistencyGroup.v1_1_1.ConsistencyGroup"
    )
    actions: Actions | None = None
    consistency_method: ApplicationConsistencyMethod | None = None
    consistency_type: ConsistencyType | None = None
    description: str | None = None
    id: str | None = None
    is_consistent: bool | None = None
    links: Links | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    remote_replica_targets: list[str] | None = None
    replica_info: ReplicaInfo | None = None
    replica_targets: list[IdRef] | None = None
    replica_targets_odata_count: int | None = Field(
        alias="ReplicaTargets@odata.count", default=None
    )
    status: Status | None = None
    volumes: list[IdRef] | None = None
    volumes_odata_count: int | None = Field(alias="Volumes@odata.count", default=None)


class ConsistencyType(StrEnum):
    CRASH_CONSISTENT = "CrashConsistent"
    APPLICATION_CONSISTENT = "ApplicationConsistent"


class CreateReplicaTarget(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Links(RedfishModel):
    oem: dict[str, Any] | None = None


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
