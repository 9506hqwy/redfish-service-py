from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .circuit import CircuitPowerState, PowerRestorePolicyTypes
from .odata_v4 import IdRef
from .resource import PowerState, Status
from .sensor import SensorEnergykWhExcerpt, SensorPowerExcerpt


class Actions(RedfishModel):
    power_control: PowerControl | None = Field(
        serialization_alias="#OutletGroup.PowerControl", default=None
    )
    reset_metrics: ResetMetrics | None = Field(
        serialization_alias="#OutletGroup.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    outlet_groups: list[IdRef] | None = None
    outlet_groups_odata_count: int | None = Field(
        serialization_alias="OutletGroups@odata.count", default=None
    )
    outlets: list[IdRef] | None = None
    outlets_odata_count: int | None = Field(
        serialization_alias="Outlets@odata.count", default=None
    )


class OutletGroup(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#OutletGroup.v1_2_0.OutletGroup"
    )
    actions: Actions | None = None
    configuration_locked: bool | None = None
    created_by: str | None = None
    description: str | None = None
    energyk_wh: SensorEnergykWhExcerpt | None = None
    id: str
    links: Links | None = None
    name: str
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


class OutletGroupOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#OutletGroup.v1_2_0.OutletGroup"
    )
    actions: Actions | None = None
    configuration_locked: bool | None = None
    created_by: str | None = None
    description: str | None = None
    energyk_wh: SensorEnergykWhExcerpt | None = None
    id: str | None = None
    links: Links | None = None
    name: str | None = None
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


class OutletGroupOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    configuration_locked: bool | None = None
    created_by: str | None = None
    energyk_wh: SensorEnergykWhExcerpt | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    power_control_locked: bool | None = None
    power_cycle_delay_seconds: float | None = None
    power_off_delay_seconds: float | None = None
    power_on_delay_seconds: float | None = None
    power_restore_delay_seconds: float | None = None
    power_restore_policy: PowerRestorePolicyTypes | None = None
    power_watts: SensorPowerExcerpt | None = None
    status: Status | None = None


class OutletGroupType(StrEnum):
    HARDWARE_DEFINED = "HardwareDefined"
    USER_DEFINED = "UserDefined"


class PowerControl(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class PowerControlRequest(RedfishModel):
    power_state: CircuitPowerState | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)
