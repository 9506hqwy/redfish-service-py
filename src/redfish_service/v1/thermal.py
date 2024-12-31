from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishObjectId,
    RedfishResource,
)
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Location, Status


class Fan(RedfishObjectId):
    actions: FanActions | None = None
    assembly: IdRef | None = None
    fan_name: str | None = None
    hot_pluggable: str | None = None
    indicator_led: str | None = None
    location: Location | None = None
    lower_threshold_critical: str | None = None
    lower_threshold_fatal: str | None = None
    lower_threshold_non_critical: str | None = None
    manufacturer: str | None = None
    max_reading_range: str | None = None
    member_id: str
    min_reading_range: str | None = None
    model: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    reading: str | None = None
    reading_units: str | None = None
    redundancy: list[IdRef] | None = None
    related_item: list[IdRef] | None = None
    sensor_number: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    upper_threshold_critical: str | None = None
    upper_threshold_fatal: str | None = None
    upper_threshold_non_critical: str | None = None


class FanActions(RedfishModel):
    oem: dict[str, Any] | None = None


class Temperature(RedfishObjectId):
    actions: TemperatureActions | None = None
    adjusted_max_allowable_operating_value: str | None = None
    adjusted_min_allowable_operating_value: str | None = None
    delta_physical_context: PhysicalContext | None = None
    delta_reading_celsius: str | None = None
    lower_threshold_critical: str | None = None
    lower_threshold_fatal: str | None = None
    lower_threshold_non_critical: str | None = None
    lower_threshold_user: str | None = None
    max_allowable_operating_value: str | None = None
    max_reading_range_temp: str | None = None
    member_id: str
    min_allowable_operating_value: str | None = None
    min_reading_range_temp: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    physical_context: PhysicalContext | None = None
    reading_celsius: str | None = None
    related_item: list[IdRef] | None = None
    sensor_number: str | None = None
    status: Status | None = None
    upper_threshold_critical: str | None = None
    upper_threshold_fatal: str | None = None
    upper_threshold_non_critical: str | None = None
    upper_threshold_user: str | None = None


class TemperatureActions(RedfishModel):
    oem: dict[str, Any] | None = None


class Thermal(RedfishResource):
    actions: ThermalActions | None = None
    description: str | None = None
    fans: list[Fan] | None = None
    oem: dict[str, Any] | None = None
    redundancy: list[IdRef] | None = None
    status: Status | None = None
    temperatures: list[Temperature] | None = None


class ThermalActions(RedfishModel):
    oem: dict[str, Any] | None = None
