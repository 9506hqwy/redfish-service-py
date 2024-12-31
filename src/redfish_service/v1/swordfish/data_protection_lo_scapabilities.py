from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from ..base import RedfishResource
from ..odata_v4 import IdRef
from ..resource import Identifier


class Actions(RedfishResource):
    oem: OemActions | None = None


class DataProtectionLoScapabilities(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    identifier: Identifier | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    supported_lines_of_service: list[IdRef] | None = None
    supported_min_lifetimes: list[str] | None = None
    supported_recovery_geographic_objectives: list[str] | None = None
    supported_recovery_point_objective_times: list[str] | None = None
    supported_recovery_time_objectives: list[str] | None = None
    supported_replica_types: list[str] | None = None
    supports_isolated: str | None = None


class FailureDomainScope(StrEnum):
    SERVER = "Server"
    RACK = "Rack"
    RACK_GROUP = "RackGroup"
    ROW = "Row"
    DATACENTER = "Datacenter"
    REGION = "Region"


class Links(RedfishResource):
    oem: dict[str, Any] | None = None
    supported_replica_options: list[IdRef] | None = None


class OemActions(RedfishResource):
    pass


class RecoveryAccessScope(StrEnum):
    ONLINE_ACTIVE = "OnlineActive"
    ONLINE_PASSIVE = "OnlinePassive"
    NEARLINE = "Nearline"
    OFFLINE = "Offline"
