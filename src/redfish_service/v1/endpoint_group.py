from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

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
    oem: OemActions | None = None


class EndpointGroup(RedfishResource):
    access_state: str | None = None
    actions: Actions | None = None
    description: str | None = None
    endpoints: list[IdRef] | None = None
    group_type: str | None = None
    identifier: Identifier | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    preferred: str | None = None
    target_endpoint_group_identifier: str | None = None


class Links(RedfishModel):
    connections: list[IdRef] | None = None
    endpoints: list[IdRef] | None = None
    oem: dict[str, Any] | None = None


class OemActions(RedfishModel):
    pass
