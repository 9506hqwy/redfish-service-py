from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishObjectId,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Redundancy(RedfishObjectId):
    actions: Actions | None = None
    max_num_supported: str | None = None
    member_id: str
    min_num_needed: str
    mode: str
    name: str
    oem: dict[str, Any] | None = None
    redundancy_enabled: str | None = None
    redundancy_set: list[IdRef]
    redundancy_set_odata_count: int | None = Field(alias="RedundancySet@odata.count", default=None)
    status: Status


class RedundantGroup(RedfishModel):
    max_supported_in_group: str | None = None
    min_needed_in_group: str
    redundancy_group: list[IdRef]
    redundancy_group_odata_count: int | None = Field(
        alias="RedundancyGroup@odata.count", default=None
    )
    redundancy_type: str
    status: Status
