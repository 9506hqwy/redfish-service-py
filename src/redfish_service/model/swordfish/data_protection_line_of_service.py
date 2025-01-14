from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel, RedfishModelOnUpdate
from ..odata_v4 import IdRef
from ..resource import Location
from ..schedule import Schedule
from ..swordfish.data_protection_los_capabilities import FailureDomainScope, RecoveryAccessScope
from ..swordfish.storage_replica_info import ReplicaType


class Actions(RedfishModel):
    create_replicas: CreateReplicas | None = Field(
        alias="#DataProtectionLineOfService.CreateReplicas", default=None
    )
    oem: dict[str, Any] | None = None


class CreateReplicas(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class CreateReplicasRequest(RedfishModel):
    replica_line_of_service: IdRef
    replica_requests: list[ReplicaRequest] | None = None


class DataProtectionLineOfService(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type",
        default="#DataProtectionLineOfService.v1_3_0.DataProtectionLineOfService",
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    is_isolated: bool | None = None
    min_lifetime: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    recovery_geographic_objective: FailureDomainScope | None = None
    recovery_point_objective_time: str | None = None
    recovery_time_objective: RecoveryAccessScope | None = None
    replica_access_location: Location | None = None
    replica_class_of_service: IdRef | None = None
    replica_type: ReplicaType | None = None
    schedule: Schedule | None = None


class DataProtectionLineOfServiceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    is_isolated: bool | None = None
    min_lifetime: str | None = None
    oem: dict[str, Any] | None = None
    recovery_geographic_objective: FailureDomainScope | None = None
    recovery_point_objective_time: str | None = None
    recovery_time_objective: RecoveryAccessScope | None = None
    replica_class_of_service: IdRef | None = None
    replica_type: ReplicaType | None = None
    schedule: Schedule | None = None


class ReplicaRequest(RedfishModel):
    replica_name: str | None = None
    replica_source: IdRef | None = None
