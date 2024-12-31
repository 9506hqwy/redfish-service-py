from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: OemActions | None = None


class DataStorageLineOfService(RedfishResource):
    access_capabilities: list[str] | None = None
    actions: Actions | None = None
    description: str | None = None
    is_space_efficient: str | None = None
    oem: dict[str, Any] | None = None
    provisioning_policy: str | None = None
    recoverable_capacity_source_count: str | None = None
    recovery_time_objectives: str | None = None


class OemActions(RedfishModel):
    pass
