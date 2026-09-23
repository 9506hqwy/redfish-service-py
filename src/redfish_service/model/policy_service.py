from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .policy import ConditionType, ResponseAction
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None


class OperatingMode(StrEnum):
    DISABLED = "Disabled"
    ALERT_ONLY = "AlertOnly"
    ENABLED = "Enabled"


class PolicyService(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#PolicyService.v1_0_0.PolicyService"
    )
    actions: Actions | None = None
    actions_supported: list[ResponseAction] | None = None
    condition_types_supported: list[ConditionType] | None = None
    description: str | None = None
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    operating_mode: OperatingMode | None = None
    policies: IdRef | None = None
    resource_types_supported: list[str] | None = None
    status: Status | None = None


class PolicyServiceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    operating_mode: OperatingMode | None = None
    status: Status | None = None
