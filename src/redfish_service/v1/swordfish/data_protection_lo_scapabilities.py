from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier
from ..swordfish.storage_replica_info import ReplicaType


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DataProtectionLoScapabilities(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    identifier: Identifier | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    supported_lines_of_service: list[IdRef] | None = None
    supported_lines_of_service_odata_count: int | None = Field(
        alias="SupportedLinesOfService@odata.count", default=None
    )
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
        alias="SupportedReplicaOptions@odata.count", default=None
    )


class RecoveryAccessScope(StrEnum):
    ONLINE_ACTIVE = "OnlineActive"
    ONLINE_PASSIVE = "OnlinePassive"
    NEARLINE = "Nearline"
    OFFLINE = "Offline"
