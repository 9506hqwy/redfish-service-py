from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Location, ResetType, Status
from .sensor import SensorExcerpt


class Actions(RedfishModel):
    calibrate: Calibrate | None = Field(alias="#Battery.Calibrate", default=None)
    reset: Reset | None = Field(alias="#Battery.Reset", default=None)
    self_test: SelfTest | None = Field(alias="#Battery.SelfTest", default=None)
    oem: dict[str, Any] | None = None


class Battery(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#Battery.v1_3_0.Battery")
    actions: Actions | None = None
    assembly: IdRef | None = None
    capacity_actual_amp_hours: float | None = None
    capacity_actual_watt_hours: float | None = None
    capacity_rated_amp_hours: float | None = None
    capacity_rated_watt_hours: float | None = None
    charge_state: ChargeState | None = None
    description: str | None = None
    firmware_version: str | None = None
    hot_pluggable: bool | None = None
    id: str
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    max_charge_rate_amps: float | None = None
    max_charge_voltage: float | None = None
    max_discharge_rate_amps: float | None = None
    metrics: IdRef | None = None
    model: str | None = None
    name: str
    nominal_output_voltage: float | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    production_date: str | None = None
    replaceable: bool | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    state_of_health_percent: SensorExcerpt | None = None
    status: Status | None = None
    version: str | None = None


class BatteryOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#Battery.v1_3_0.Battery")
    actions: Actions | None = None
    assembly: IdRef | None = None
    capacity_actual_amp_hours: float | None = None
    capacity_actual_watt_hours: float | None = None
    capacity_rated_amp_hours: float | None = None
    capacity_rated_watt_hours: float | None = None
    charge_state: ChargeState | None = None
    description: str | None = None
    firmware_version: str | None = None
    hot_pluggable: bool | None = None
    id: str | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    max_charge_rate_amps: float | None = None
    max_charge_voltage: float | None = None
    max_discharge_rate_amps: float | None = None
    metrics: IdRef | None = None
    model: str | None = None
    name: str | None = None
    nominal_output_voltage: float | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    production_date: str | None = None
    replaceable: bool | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    state_of_health_percent: SensorExcerpt | None = None
    status: Status | None = None
    version: str | None = None


class Calibrate(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ChargeState(StrEnum):
    IDLE = "Idle"
    CHARGING = "Charging"
    DISCHARGING = "Discharging"


class Links(RedfishModel):
    memory: list[IdRef] | None = None
    memory_odata_count: int | None = Field(alias="Memory@odata.count", default=None)
    oem: dict[str, Any] | None = None
    storage_controllers: list[IdRef] | None = None
    storage_controllers_odata_count: int | None = Field(
        alias="StorageControllers@odata.count", default=None
    )


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ResetRequest(RedfishModel):
    reset_type: ResetType | None = None


class SelfTest(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
