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


class PowerAllocation(RedfishResource):
    allocated_watts: str | None = None
    requested_watts: str | None = None


class PowerSubsystem(RedfishResource):
    actions: Actions | None = None
    allocation: PowerAllocation | None = None
    batteries: IdRef | None = None
    capacity_watts: str | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    power_supplies: IdRef | None = None
    power_supply_redundancy: list[RedundantGroup] | None = None
    status: Status | None = None
