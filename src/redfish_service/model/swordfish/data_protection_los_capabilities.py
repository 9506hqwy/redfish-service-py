from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .. import RedfishModel, RedfishModelOnUpdate
from ..odata_v4 import IdRef
from ..resource import Identifier
from ..swordfish.storage_replica_info import ReplicaType


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DataProtectionLosCapabilities(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#DataProtectionLoSCapabilities.v1_2_0.DataProtectionLoSCapabilities",
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    identifier: Identifier | None = None
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    supported_lines_of_service: list[IdRef] | None = None
    supported_lines_of_service_odata_count: int | None = Field(
        serialization_alias="SupportedLinesOfService@odata.count", default=None
    )
    supported_min_lifetimes: list[str] | None = None
    supported_recovery_geographic_objectives: list[FailureDomainScope] | None = None
    supported_recovery_point_objective_times: list[str] | None = None
    supported_recovery_time_objectives: list[RecoveryAccessScope] | None = None
    supported_replica_types: list[ReplicaType] | None = None
    supports_isolated: bool | None = None


class DataProtectionLosCapabilitiesOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    identifier: Identifier | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    supported_lines_of_service: list[IdRef] | None = None
    supported_min_lifetimes: list[str] | None = None
    supported_recovery_geographic_objectives: list[FailureDomainScope] | None = None
    supported_recovery_point_objective_times: list[str] | None = None
    supported_recovery_time_objectives: list[RecoveryAccessScope] | None = None
    supported_replica_types: list[ReplicaType] | None = None
    supports_isolated: bool | None = None


class FailureDomainScope(StrEnum):
    SERVER = "Server"
    RACK = "Rack"
    RACK_GROUP = "RackGroup"
    ROW = "Row"
    DATACENTER = "Datacenter"
    REGION = "Region"


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    supported_replica_options: list[IdRef] | None = None
    supported_replica_options_odata_count: int | None = Field(
        serialization_alias="SupportedReplicaOptions@odata.count", default=None
    )


class RecoveryAccessScope(StrEnum):
    ONLINE_ACTIVE = "OnlineActive"
    ONLINE_PASSIVE = "OnlinePassive"
    NEARLINE = "Nearline"
    OFFLINE = "Offline"
