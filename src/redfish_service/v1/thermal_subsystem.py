from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .redundancy import RedundantGroup
from .resource import Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class OemActions(RedfishModel):
    pass


class ThermalSubsystem(RedfishResource):
    actions: Actions | None = None
    coolant_connector_redundancy: list[RedundantGroup] | None = None
    coolant_connectors: IdRef | None = None
    description: str | None = None
    fan_redundancy: list[RedundantGroup] | None = None
    fans: IdRef | None = None
    heaters: IdRef | None = None
    leak_detection: IdRef | None = None
    oem: dict[str, Any] | None = None
    pumps: IdRef | None = None
    status: Status | None = None
    thermal_metrics: IdRef | None = None
