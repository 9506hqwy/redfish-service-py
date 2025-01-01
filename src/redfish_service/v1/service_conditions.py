from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .resource import Condition, Health


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ServiceConditions(RedfishResource):
    actions: Actions | None = None
    conditions: list[Condition] | None = None
    description: str | None = None
    health_rollup: Health | None = None
    oem: dict[str, Any] | None = None
