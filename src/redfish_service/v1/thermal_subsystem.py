from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .redundancy import RedundantGroup
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class OemActions(RedfishResource):
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
