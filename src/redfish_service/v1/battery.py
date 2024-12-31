from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Location, Status
from .sensor import SensorExcerpt


class Actions(RedfishModel):
    oem: OemActions | None = None


class Battery(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    capacity_actual_amp_hours: str | None = None
    capacity_actual_watt_hours: str | None = None
    capacity_rated_amp_hours: str | None = None
    capacity_rated_watt_hours: str | None = None
    charge_state: str | None = None
    description: str | None = None
    firmware_version: str | None = None
    hot_pluggable: str | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    manufacturer: str | None = None
    max_charge_rate_amps: str | None = None
    max_charge_voltage: str | None = None
    max_discharge_rate_amps: str | None = None
    metrics: IdRef | None = None
    model: str | None = None
    nominal_output_voltage: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    production_date: str | None = None
    replaceable: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    state_of_health_percent: SensorExcerpt | None = None
    status: Status | None = None
    version: str | None = None


class Calibrate(RedfishModel):
    target: str | None = None
    title: str | None = None


class Links(RedfishModel):
    memory: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    storage_controllers: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass


class Reset(RedfishModel):
    target: str | None = None
    title: str | None = None


class SelfTest(RedfishModel):
    target: str | None = None
    title: str | None = None
