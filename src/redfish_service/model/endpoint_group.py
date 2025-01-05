from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Identifier


class AccessState(StrEnum):
    OPTIMIZED = "Optimized"
    NON_OPTIMIZED = "NonOptimized"
    STANDBY = "Standby"
    UNAVAILABLE = "Unavailable"
    TRANSITIONING = "Transitioning"


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class EndpointGroup(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#EndpointGroup.v1_3_4.EndpointGroup")
    access_state: AccessState | None = None
    actions: Actions | None = None
    description: str | None = None
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    group_type: GroupType | None = None
    id: str
    identifier: Identifier | None = None
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    preferred: bool | None = None
    target_endpoint_group_identifier: int | None = None


class GroupType(StrEnum):
    CLIENT = "Client"
    SERVER = "Server"
    INITIATOR = "Initiator"
    TARGET = "Target"


class Links(RedfishModel):
    connections: list[IdRef] | None = None
    connections_odata_count: int | None = Field(alias="Connections@odata.count", default=None)
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    oem: dict[str, Any] | None = None
