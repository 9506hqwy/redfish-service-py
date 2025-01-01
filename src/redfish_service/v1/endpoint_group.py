from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
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


class EndpointGroup(RedfishResource):
    access_state: str | None = None
    actions: Actions | None = None
    description: str | None = None
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    group_type: str | None = None
    identifier: Identifier | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    preferred: str | None = None
    target_endpoint_group_identifier: str | None = None


class Links(RedfishModel):
    connections: list[IdRef] | None = None
    connections_odata_count: int | None = Field(alias="Connections@odata.count", default=None)
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    oem: dict[str, Any] | None = None
