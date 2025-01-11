from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .physical_context import PhysicalContext, PhysicalSubContext
from .redundancy import RedundantGroup
from .resource import Location, Status


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(alias="#Sensor.ResetMetrics", default=None)
    reset_to_defaults: ResetToDefaults | None = Field(
        alias="#Sensor.ResetToDefaults", default=None
    )
    oem: dict[str, Any] | None = None


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
    LINE1_TO_NEUTRAL_AND_L1L2 = "Line1ToNeutralAndL1L2"
    LINE2_TO_NEUTRAL_AND_L1L2 = "Line2ToNeutralAndL1L2"
    LINE2_TO_NEUTRAL_AND_L2L3 = "Line2ToNeutralAndL2L3"
    LINE3_TO_NEUTRAL_AND_L3L1 = "Line3ToNeutralAndL3L1"
    TOTAL = "Total"


class ImplementationType(StrEnum):
    PHYSICAL_SENSOR = "PhysicalSensor"
    SYNTHESIZED = "Synthesized"
    REPORTED = "Reported"


class Links(RedfishModel):
    associated_controls: list[IdRef] | None = None
    associated_controls_odata_count: int | None = Field(
        alias="AssociatedControls@odata.count", default=None
    )
    oem: dict[str, Any] | None = None


class ReadingBasisType(StrEnum):
    ZERO = "Zero"
    DELTA = "Delta"
    HEADROOM = "Headroom"


class ReadingType(StrEnum):
    TEMPERATURE = "Temperature"
    HUMIDITY = "Humidity"
    POWER = "Power"
    ENERGYK_WH = "EnergykWh"
    ENERGY_JOULES = "EnergyJoules"
    ENERGY_WH = "EnergyWh"
    CHARGE_AH = "ChargeAh"
    VOLTAGE = "Voltage"
    CURRENT = "Current"
    FREQUENCY = "Frequency"
    PRESSURE = "Pressure"
    PRESSUREK_PA = "PressurekPa"
    PRESSURE_PA = "PressurePa"
    LIQUID_LEVEL = "LiquidLevel"
    ROTATIONAL = "Rotational"
    AIR_FLOW = "AirFlow"
    AIR_FLOW_CMM = "AirFlowCMM"
    LIQUID_FLOW = "LiquidFlow"
    LIQUID_FLOW_LPM = "LiquidFlowLPM"
    BAROMETRIC = "Barometric"
    ALTITUDE = "Altitude"
    PERCENT = "Percent"
    ABSOLUTE_HUMIDITY = "AbsoluteHumidity"
    HEAT = "Heat"


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ResetToDefaults(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Sensor(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#Sensor.v1_10_1.Sensor")
    accuracy: float | None = None
    actions: Actions | None = None
    adjusted_max_allowable_operating_value: float | None = None
    adjusted_min_allowable_operating_value: float | None = None
    apparent_va: float | None = Field(alias="ApparentVA", default=None)
    apparent_kvah: float | None = Field(alias="ApparentkVAh", default=None)
    average_reading: float | None = None
    averaging_interval: str | None = None
    averaging_interval_achieved: bool | None = None
    calibration: float | None = None
    calibration_time: str | None = None
    crest_factor: float | None = None
    description: str | None = None
    electrical_context: ElectricalContext | None = None
    enabled: bool | None = None
    id: str
    implementation: ImplementationType | None = None
    lifetime_reading: float | None = None
    lifetime_start_date_time: str | None = None
    links: Links | None = None
    load_percent: float | None = None
    location: Location | None = None
    lowest_reading: float | None = None
    lowest_reading_time: str | None = None
    manufacturer: str | None = None
    max_allowable_operating_value: float | None = None
    min_allowable_operating_value: float | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    peak_reading: float | None = None
    peak_reading_time: str | None = None
    phase_angle_degrees: float | None = None
    physical_context: PhysicalContext | None = None
    physical_sub_context: PhysicalSubContext | None = None
    power_factor: float | None = None
    precision: float | None = None
    reactive_var: float | None = Field(alias="ReactiveVAR", default=None)
    reactive_kvarh: float | None = Field(alias="ReactivekVARh", default=None)
    reading: float | None = None
    reading_accuracy: float | None = None
    reading_basis: ReadingBasisType | None = None
    reading_range_max: float | None = None
    reading_range_min: float | None = None
    reading_time: str | None = None
    reading_type: ReadingType | None = None
    reading_units: str | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(alias="RelatedItem@odata.count", default=None)
    sku: str | None = Field(alias="SKU", default=None)
    sensing_frequency: float | None = None
    sensing_interval: str | None = None
    sensor_group: RedundantGroup | None = None
    sensor_reset_time: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    speed_rpm: float | None = Field(alias="SpeedRPM", default=None)
    status: Status | None = None
    thd_percent: float | None = Field(alias="THDPercent", default=None)
    thresholds: Thresholds | None = None
    user_label: str | None = None
    voltage_type: VoltageType | None = None


class SensorOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#Sensor.v1_10_1.Sensor")
    accuracy: float | None = None
    actions: Actions | None = None
    adjusted_max_allowable_operating_value: float | None = None
    adjusted_min_allowable_operating_value: float | None = None
    apparent_va: float | None = Field(alias="ApparentVA", default=None)
    apparent_kvah: float | None = Field(alias="ApparentkVAh", default=None)
    average_reading: float | None = None
    averaging_interval: str | None = None
    averaging_interval_achieved: bool | None = None
    calibration: float | None = None
    calibration_time: str | None = None
    crest_factor: float | None = None
    description: str | None = None
    electrical_context: ElectricalContext | None = None
    enabled: bool | None = None
    id: str | None = None
    implementation: ImplementationType | None = None
    lifetime_reading: float | None = None
    lifetime_start_date_time: str | None = None
    links: Links | None = None
    load_percent: float | None = None
    location: Location | None = None
    lowest_reading: float | None = None
    lowest_reading_time: str | None = None
    manufacturer: str | None = None
    max_allowable_operating_value: float | None = None
    min_allowable_operating_value: float | None = None
    model: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    peak_reading: float | None = None
    peak_reading_time: str | None = None
    phase_angle_degrees: float | None = None
    physical_context: PhysicalContext | None = None
    physical_sub_context: PhysicalSubContext | None = None
    power_factor: float | None = None
    precision: float | None = None
    reactive_var: float | None = Field(alias="ReactiveVAR", default=None)
    reactive_kvarh: float | None = Field(alias="ReactivekVARh", default=None)
    reading: float | None = None
    reading_accuracy: float | None = None
    reading_basis: ReadingBasisType | None = None
    reading_range_max: float | None = None
    reading_range_min: float | None = None
    reading_time: str | None = None
    reading_type: ReadingType | None = None
    reading_units: str | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(alias="RelatedItem@odata.count", default=None)
    sku: str | None = Field(alias="SKU", default=None)
    sensing_frequency: float | None = None
    sensing_interval: str | None = None
    sensor_group: RedundantGroup | None = None
    sensor_reset_time: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    speed_rpm: float | None = Field(alias="SpeedRPM", default=None)
    status: Status | None = None
    thd_percent: float | None = Field(alias="THDPercent", default=None)
    thresholds: Thresholds | None = None
    user_label: str | None = None
    voltage_type: VoltageType | None = None


class SensorArrayExcerpt(RedfishModel):
    data_source_uri: str | None = None
    device_name: str | None = None
    physical_context: PhysicalContext | None = None
    physical_sub_context: PhysicalSubContext | None = None
    reading: float | None = None


class SensorCurrentExcerpt(RedfishModel):
    crest_factor: float | None = None
    data_source_uri: str | None = None
    reading: float | None = None
    thd_percent: float | None = Field(alias="THDPercent", default=None)


class SensorEnergykWhExcerpt(RedfishModel):
    apparent_kvah: float | None = Field(alias="ApparentkVAh", default=None)
    data_source_uri: str | None = None
    lifetime_reading: float | None = None
    reactive_kvarh: float | None = Field(alias="ReactivekVARh", default=None)
    reading: float | None = None
    sensor_reset_time: str | None = None


class SensorExcerpt(RedfishModel):
    data_source_uri: str | None = None
    reading: float | None = None


class SensorFanArrayExcerpt(RedfishModel):
    data_source_uri: str | None = None
    device_name: str | None = None
    physical_context: PhysicalContext | None = None
    physical_sub_context: PhysicalSubContext | None = None
    reading: float | None = None
    speed_rpm: float | None = Field(alias="SpeedRPM", default=None)


class SensorFanExcerpt(RedfishModel):
    data_source_uri: str | None = None
    reading: float | None = None
    speed_rpm: float | None = Field(alias="SpeedRPM", default=None)


class SensorPowerArrayExcerpt(RedfishModel):
    apparent_va: float | None = Field(alias="ApparentVA", default=None)
    data_source_uri: str | None = None
    phase_angle_degrees: float | None = None
    physical_context: PhysicalContext | None = None
    physical_sub_context: PhysicalSubContext | None = None
    power_factor: float | None = None
    reactive_var: float | None = Field(alias="ReactiveVAR", default=None)
    reading: float | None = None


class SensorPowerExcerpt(RedfishModel):
    apparent_va: float | None = Field(alias="ApparentVA", default=None)
    data_source_uri: str | None = None
    phase_angle_degrees: float | None = None
    power_factor: float | None = None
    reactive_var: float | None = Field(alias="ReactiveVAR", default=None)
    reading: float | None = None


class SensorPumpExcerpt(RedfishModel):
    data_source_uri: str | None = None
    reading: float | None = None
    speed_rpm: float | None = Field(alias="SpeedRPM", default=None)


class SensorVoltageExcerpt(RedfishModel):
    crest_factor: float | None = None
    data_source_uri: str | None = None
    reading: float | None = None
    thd_percent: float | None = Field(alias="THDPercent", default=None)


class Threshold(RedfishModel):
    activation: ThresholdActivation | None = None
    dwell_time: str | None = None
    hysteresis_duration: str | None = None
    hysteresis_reading: float | None = None
    reading: float | None = None


class ThresholdActivation(StrEnum):
    INCREASING = "Increasing"
    DECREASING = "Decreasing"
    EITHER = "Either"
    DISABLED = "Disabled"


class Thresholds(RedfishModel):
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
