from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .redundancy import RedundantGroup
from .resource import Location, Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class ElectricalContext(StrEnum):
    LINE1 = "Line1"
    LINE2 = "Line2"
    LINE3 = "Line3"
    NEUTRAL = "Neutral"
    LINE_TO_LINE = "LineToLine"
    LINE1_TO_LINE2 = "Line1ToLine2"
    LINE2_TO_LINE3 = "Line2ToLine3"
    LINE3_TO_LINE1 = "Line3ToLine1"
    LINE_TO_NEUTRAL = "LineToNeutral"
    LINE1_TO_NEUTRAL = "Line1ToNeutral"
    LINE2_TO_NEUTRAL = "Line2ToNeutral"
    LINE3_TO_NEUTRAL = "Line3ToNeutral"
    LINE1_TO_NEUTRAL_AND_L1_L2 = "Line1ToNeutralAndL1L2"
    LINE2_TO_NEUTRAL_AND_L1_L2 = "Line2ToNeutralAndL1L2"
    LINE2_TO_NEUTRAL_AND_L2_L3 = "Line2ToNeutralAndL2L3"
    LINE3_TO_NEUTRAL_AND_L3_L1 = "Line3ToNeutralAndL3L1"
    TOTAL = "Total"


class Links(RedfishResource):
    associated_controls: list[IdRef] | None = None
    oem: dict[str, Any] | None = None


class OemActions(RedfishResource):
    pass


class ResetMetrics(RedfishResource):
    target: str | None = None
    title: str | None = None


class ResetToDefaults(RedfishResource):
    target: str | None = None
    title: str | None = None


class Sensor(RedfishResource):
    accuracy: str | None = None
    actions: Actions | None = None
    adjusted_max_allowable_operating_value: str | None = None
    adjusted_min_allowable_operating_value: str | None = None
    apparent_va: str | None = None
    apparentk_vah: str | None = None
    average_reading: str | None = None
    averaging_interval: str | None = None
    averaging_interval_achieved: str | None = None
    calibration: str | None = None
    calibration_time: str | None = None
    crest_factor: str | None = None
    description: str | None = None
    electrical_context: str | None = None
    implementation: str | None = None
    lifetime_reading: str | None = None
    lifetime_start_date_time: str | None = None
    links: Links | None = None
    load_percent: str | None = None
    location: Location | None = None
    lowest_reading: str | None = None
    lowest_reading_time: str | None = None
    manufacturer: str | None = None
    max_allowable_operating_value: str | None = None
    min_allowable_operating_value: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    peak_reading: str | None = None
    peak_reading_time: str | None = None
    phase_angle_degrees: str | None = None
    physical_context: str | None = None
    physical_sub_context: str | None = None
    power_factor: str | None = None
    precision: str | None = None
    reactive_var: str | None = None
    reactivek_varh: str | None = None
    reading: str | None = None
    reading_accuracy: str | None = None
    reading_basis: str | None = None
    reading_range_max: str | None = None
    reading_range_min: str | None = None
    reading_time: str | None = None
    reading_type: str | None = None
    reading_units: str | None = None
    related_item: list[IdRef] | None = None
    sku: str | None = None
    sensing_frequency: str | None = None
    sensing_interval: str | None = None
    sensor_group: RedundantGroup | None = None
    sensor_reset_time: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    speed_rpm: str | None = None
    status: Status | None = None
    thdpercent: str | None = None
    thresholds: Thresholds | None = None
    user_label: str | None = None
    voltage_type: str | None = None


class SensorArrayExcerpt(RedfishResource):
    data_source_uri: str | None = None
    device_name: str | None = None
    physical_context: str | None = None
    physical_sub_context: str | None = None
    reading: str | None = None


class SensorCurrentExcerpt(RedfishResource):
    crest_factor: str | None = None
    data_source_uri: str | None = None
    reading: str | None = None
    thdpercent: str | None = None


class SensorEnergykWhExcerpt(RedfishResource):
    apparentk_vah: str | None = None
    data_source_uri: str | None = None
    lifetime_reading: str | None = None
    reactivek_varh: str | None = None
    reading: str | None = None
    sensor_reset_time: str | None = None


class SensorExcerpt(RedfishResource):
    data_source_uri: str | None = None
    reading: str | None = None


class SensorFanArrayExcerpt(RedfishResource):
    data_source_uri: str | None = None
    device_name: str | None = None
    physical_context: str | None = None
    physical_sub_context: str | None = None
    reading: str | None = None
    speed_rpm: str | None = None


class SensorFanExcerpt(RedfishResource):
    data_source_uri: str | None = None
    reading: str | None = None
    speed_rpm: str | None = None


class SensorPowerArrayExcerpt(RedfishResource):
    apparent_va: str | None = None
    data_source_uri: str | None = None
    phase_angle_degrees: str | None = None
    physical_context: str | None = None
    physical_sub_context: str | None = None
    power_factor: str | None = None
    reactive_var: str | None = None
    reading: str | None = None


class SensorPowerExcerpt(RedfishResource):
    apparent_va: str | None = None
    data_source_uri: str | None = None
    phase_angle_degrees: str | None = None
    power_factor: str | None = None
    reactive_var: str | None = None
    reading: str | None = None


class SensorPumpExcerpt(RedfishResource):
    data_source_uri: str | None = None
    reading: str | None = None
    speed_rpm: str | None = None


class SensorVoltageExcerpt(RedfishResource):
    crest_factor: str | None = None
    data_source_uri: str | None = None
    reading: str | None = None
    thdpercent: str | None = None


class Threshold(RedfishResource):
    activation: str | None = None
    dwell_time: str | None = None
    hysteresis_duration: str | None = None
    hysteresis_reading: str | None = None
    reading: str | None = None


class Thresholds(RedfishResource):
    lower_caution: Threshold | None = None
    lower_caution_user: Threshold | None = None
    lower_critical: Threshold | None = None
    lower_critical_user: Threshold | None = None
    lower_fatal: Threshold | None = None
    upper_caution: Threshold | None = None
    upper_caution_user: Threshold | None = None
    upper_critical: Threshold | None = None
    upper_critical_user: Threshold | None = None
    upper_fatal: Threshold | None = None


class VoltageType(StrEnum):
    AC = "AC"
    DC = "DC"
