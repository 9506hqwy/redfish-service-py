from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Location, Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class Control(RedfishResource):
    accuracy: str | None = None
    actions: Actions | None = None
    allowable_max: str | None = None
    allowable_min: str | None = None
    allowable_numeric_values: list[str] | None = None
    associated_sensors: list[IdRef] | None = None
    control_delay_seconds: str | None = None
    control_loop: ControlLoop | None = None
    control_mode: str | None = None
    control_type: str | None = None
    dead_band: str | None = None
    default_set_point: str | None = None
    description: str | None = None
    implementation: str | None = None
    increment: str | None = None
    location: Location | None = None
    oem: dict[str, Any] | None = None
    physical_context: str | None = None
    physical_sub_context: str | None = None
    related_item: list[IdRef] | None = None
    sensor: str | None = None
    set_point: str | None = None
    set_point_accuracy: str | None = None
    set_point_type: str | None = None
    set_point_units: str | None = None
    set_point_update_time: str | None = None
    setting_max: str | None = None
    setting_min: str | None = None
    status: Status | None = None


class ControlExcerpt(RedfishResource):
    allowable_max: str | None = None
    allowable_min: str | None = None
    control_mode: str | None = None
    data_source_uri: str | None = None
    reading: str | None = None
    reading_units: str | None = None


class ControlLoop(RedfishResource):
    coefficient_update_time: str | None = None
    differential: str | None = None
    integral: str | None = None
    proportional: str | None = None


class ControlRangeExcerpt(RedfishResource):
    allowable_max: str | None = None
    allowable_min: str | None = None
    allowable_numeric_values: list[str] | None = None
    control_mode: str | None = None
    data_source_uri: str | None = None
    reading: str | None = None
    reading_units: str | None = None
    setting_max: str | None = None
    setting_min: str | None = None


class ControlSingleExcerpt(RedfishResource):
    allowable_max: str | None = None
    allowable_min: str | None = None
    control_mode: str | None = None
    data_source_uri: str | None = None
    default_set_point: str | None = None
    reading: str | None = None
    reading_units: str | None = None
    set_point: str | None = None


class ControlSingleLoopExcerpt(RedfishResource):
    allowable_max: str | None = None
    allowable_min: str | None = None
    control_loop: ControlLoop | None = None
    control_mode: str | None = None
    data_source_uri: str | None = None
    reading: str | None = None
    reading_units: str | None = None
    set_point: str | None = None


class OemActions(RedfishResource):
    pass


class ResetToDefaults(RedfishResource):
    target: str | None = None
    title: str | None = None
