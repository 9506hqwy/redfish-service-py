from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Redundancy(RedfishModel):
    odata_id: str = Field(serialization_alias="@odata.id")
    actions: Actions | None = None
    active_redundancy_set: list[IdRef] | None = None
    active_redundancy_set_odata_count: int | None = Field(
        serialization_alias="ActiveRedundancySet@odata.count", default=None
    )
    max_num_supported: int | None = None
    member_id: str
    min_num_needed: int | None = None
    min_num_needed_for_fault_tolerance: int | None = None
    mode: RedundancyMode | None = None
    name: str
    oem: dict[str, Any] | None = None
    redundancy_enabled: bool | None = None
    redundancy_set: list[IdRef]
    redundancy_set_odata_count: int | None = Field(
        serialization_alias="RedundancySet@odata.count", default=None
    )
    status: Status


class RedundancyMode(StrEnum):
    FAILOVER = "Failover"
    N_M = "N+m"
    SHARING = "Sharing"
    SPARING = "Sparing"
    NOT_REDUNDANT = "NotRedundant"


class RedundancyType(StrEnum):
    FAILOVER = "Failover"
    N_PLUS_M = "NPlusM"
    SHARING = "Sharing"
    SPARING = "Sparing"
    NOT_REDUNDANT = "NotRedundant"


class RedundantGroup(RedfishModel):
    active_redundancy_group: list[IdRef] | None = None
    active_redundancy_group_odata_count: int | None = Field(
        serialization_alias="ActiveRedundancyGroup@odata.count", default=None
    )
    group_name: str | None = None
    max_supported_in_group: int | None = None
    min_needed_for_fault_tolerance: int | None = None
    min_needed_in_group: int | None = None
    redundancy_group: list[IdRef]
    redundancy_group_odata_count: int | None = Field(
        serialization_alias="RedundancyGroup@odata.count", default=None
    )
    redundancy_type: RedundancyType | None = None
    status: Status
