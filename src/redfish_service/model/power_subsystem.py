from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .redundancy import RedundantGroup
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class PowerAllocation(RedfishModel):
    allocated_watts: float | None = None
    requested_watts: float | None = None


class PowerSubsystem(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#PowerSubsystem.v1_1_2.PowerSubsystem"
    )
    actions: Actions | None = None
    allocation: PowerAllocation | None = None
    batteries: IdRef | None = None
    capacity_watts: float | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    power_supplies: IdRef | None = None
    power_supply_redundancy: list[RedundantGroup] | None = None
    status: Status | None = None


class PowerSubsystemOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    allocation: PowerAllocation | None = None
    oem: dict[str, Any] | None = None
    power_supply_redundancy: list[RedundantGroup] | None = None
    status: Status | None = None
