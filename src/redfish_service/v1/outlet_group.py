from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .circuit import PowerRestorePolicyTypes
from .odata_v4 import IdRef
from .resource import PowerState, Status
from .sensor import SensorEnergykWhExcerpt, SensorPowerExcerpt


class Actions(RedfishModel):
    power_control: PowerControl | None = Field(alias="#OutletGroup.PowerControl", default=None)
    reset_metrics: ResetMetrics | None = Field(alias="#OutletGroup.ResetMetrics", default=None)
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    outlet_groups: list[IdRef] | None = None
    outlet_groups_odata_count: int | None = Field(alias="OutletGroups@odata.count", default=None)
    outlets: list[IdRef] | None = None
    outlets_odata_count: int | None = Field(alias="Outlets@odata.count", default=None)


class OutletGroup(RedfishResource):
    actions: Actions | None = None
    configuration_locked: bool | None = None
    created_by: str | None = None
    description: str | None = None
    energyk_wh: SensorEnergykWhExcerpt | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    outlet_group_type: OutletGroupType | None = None
    power_control_locked: bool | None = None
    power_cycle_delay_seconds: float | None = None
    power_enabled: bool | None = None
    power_off_delay_seconds: float | None = None
    power_on_delay_seconds: float | None = None
    power_restore_delay_seconds: float | None = None
    power_restore_policy: PowerRestorePolicyTypes | None = None
    power_state: PowerState | None = None
    power_state_in_transition: bool | None = None
    power_watts: SensorPowerExcerpt | None = None
    status: Status | None = None


class OutletGroupType(StrEnum):
    HARDWARE_DEFINED = "HardwareDefined"
    USER_DEFINED = "UserDefined"


class PowerControl(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
