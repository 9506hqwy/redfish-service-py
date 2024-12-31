from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .resource import Health


class Actions(RedfishResource):
    oem: OemActions | None = None


class OemActions(RedfishResource):
    pass


class ServiceConditions(RedfishResource):
    actions: Actions | None = None
    conditions: list[str] | None = None
    description: str | None = None
    health_rollup: Health | None = None
    oem: dict[str, Any] | None = None
