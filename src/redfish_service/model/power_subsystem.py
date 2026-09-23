from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .control import ControlSingleExcerpt
from .odata_v4 import IdRef
from .redundancy import RedundantGroup
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    power_brake_load_percent_sensor: IdRef | None = None
    power_brake_temperature_sensor: IdRef | None = None


class PowerAllocation(RedfishModel):
    allocated_watts: float | None = None
    requested_watts: float | None = None


class PowerBrake(RedfishModel):
    applied: bool | None = None
    enabled: bool | None = None
    load_percent_threshold: ThresholdLevel | None = None
    temperature_threshold: ThresholdLevel | None = None


class PowerSubsystem(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#PowerSubsystem.v1_2_0.PowerSubsystem"
    )
    actions: Actions | None = None
    allocation: PowerAllocation | None = None
    batteries: IdRef | None = None
    capacity_watts: float | None = None
    description: str | None = None
    id: str
    links: Links | None = None
    max_ramp_rate_watts_per_second: ControlSingleExcerpt | None = None
    name: str
    oem: dict[str, Any] | None = None
    power_brake: PowerBrake | None = None
    power_supplies: IdRef | None = None
    power_supply_redundancy: list[RedundantGroup] | None = None
    status: Status | None = None


class PowerSubsystemOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    allocation: PowerAllocation | None = None
    links: Links | None = None
    max_ramp_rate_watts_per_second: ControlSingleExcerpt | None = None
    oem: dict[str, Any] | None = None
    power_brake: PowerBrake | None = None
    power_supply_redundancy: list[RedundantGroup] | None = None
    status: Status | None = None


class ThresholdLevel(StrEnum):
    DISABLED = "Disabled"
    UPPER_CAUTION = "UpperCaution"
    UPPER_CRITICAL = "UpperCritical"
