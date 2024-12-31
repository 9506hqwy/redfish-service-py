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


class ThermalEquipment(RedfishResource):
    actions: Actions | None = None
    cdus: IdRef | None = None
    cooling_loop_redundancy: list[RedundantGroup] | None = None
    cooling_loops: IdRef | None = None
    description: str | None = None
    heat_exchangers: IdRef | None = None
    immersion_units: IdRef | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
