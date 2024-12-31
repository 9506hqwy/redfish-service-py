from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .circuit import PowerRestorePolicyTypes
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    outlet_groups: list[IdRef] | None = None
    outlets: list[IdRef] | None = None


class OutletGroup(RedfishResource):
    actions: Actions | None = None
    configuration_locked: bool | None = None
    created_by: str | None = None
    description: str | None = None
    energyk_wh: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    outlet_group_type: OutletGroupType | None = None
    power_control_locked: bool | None = None
    power_cycle_delay_seconds: str | None = None
    power_enabled: str | None = None
    power_off_delay_seconds: str | None = None
    power_on_delay_seconds: str | None = None
    power_restore_delay_seconds: str | None = None
    power_restore_policy: PowerRestorePolicyTypes | None = None
    power_state: str | None = None
    power_state_in_transition: bool | None = None
    power_watts: str | None = None
    status: Status | None = None


class OutletGroupType(StrEnum):
    HARDWARE_DEFINED = "HardwareDefined"
    USER_DEFINED = "UserDefined"


class PowerControl(RedfishModel):
    target: str | None = None
    title: str | None = None


class PowerState(StrEnum):
    ON = "On"
    OFF = "Off"
    POWER_CYCLE = "PowerCycle"


class ResetMetrics(RedfishModel):
    target: str | None = None
    title: str | None = None
