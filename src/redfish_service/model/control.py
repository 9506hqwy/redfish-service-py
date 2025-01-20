from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .physical_context import PhysicalContext, PhysicalSubContext
from .resource import Location, Status
from .sensor import SensorExcerpt


class Actions(RedfishModel):
    reset_to_defaults: ResetToDefaults | None = Field(
        serialization_alias="#Control.ResetToDefaults", default=None
    )
    oem: dict[str, Any] | None = None


class Control(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Control.v1_6_0.Control")
    accuracy: float | None = None
    actions: Actions | None = None
    allowable_max: float | None = None
    allowable_min: float | None = None
    allowable_numeric_values: list[float] | None = None
    associated_sensors: list[IdRef] | None = None
    associated_sensors_odata_count: int | None = Field(
        serialization_alias="AssociatedSensors@odata.count", default=None
    )
    control_delay_seconds: float | None = None
    control_loop: ControlLoop | None = None
    control_mode: ControlMode | None = None
    control_type: ControlType | None = None
    dead_band: float | None = None
    default_set_point: float | None = None
    description: str | None = None
    id: str
    implementation: ImplementationType | None = None
    increment: float | None = None
    location: Location | None = None
    name: str
    oem: dict[str, Any] | None = None
    physical_context: PhysicalContext | None = None
    physical_sub_context: PhysicalSubContext | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(
        serialization_alias="RelatedItem@odata.count", default=None
    )
    sensor: SensorExcerpt | None = None
    set_point: float | None = None
    set_point_accuracy: float | None = None
    set_point_type: SetPointType | None = None
    set_point_units: str | None = None
    set_point_update_time: str | None = None
    setting_max: float | None = None
    setting_min: float | None = None
    status: Status | None = None


class ControlOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    control_delay_seconds: float | None = None
    control_loop: ControlLoop | None = None
    control_mode: ControlMode | None = None
    dead_band: float | None = None
    location: Location | None = None
    oem: dict[str, Any] | None = None
    sensor: SensorExcerpt | None = None
    set_point: float | None = None
    setting_max: float | None = None
    setting_min: float | None = None
    status: Status | None = None


class ControlExcerpt(RedfishModel):
    allowable_max: float | None = None
    allowable_min: float | None = None
    control_mode: ControlMode | None = None
    data_source_uri: str | None = None
    reading: float | None = None
    reading_units: str | None = None


class ControlLoop(RedfishModel):
    coefficient_update_time: str | None = None
    differential: float | None = None
    integral: float | None = None
    proportional: float | None = None


class ControlMode(StrEnum):
    AUTOMATIC = "Automatic"
    OVERRIDE = "Override"
    MANUAL = "Manual"
    DISABLED = "Disabled"


class ControlRangeExcerpt(RedfishModel):
    allowable_max: float | None = None
    allowable_min: float | None = None
    allowable_numeric_values: list[float] | None = None
    control_mode: ControlMode | None = None
    data_source_uri: str | None = None
    reading: float | None = None
    reading_units: str | None = None
    setting_max: float | None = None
    setting_min: float | None = None


class ControlSingleExcerpt(RedfishModel):
    allowable_max: float | None = None
    allowable_min: float | None = None
    control_mode: ControlMode | None = None
    data_source_uri: str | None = None
    default_set_point: float | None = None
    reading: float | None = None
    reading_units: str | None = None
    set_point: float | None = None


class ControlSingleLoopExcerpt(RedfishModel):
    allowable_max: float | None = None
    allowable_min: float | None = None
    control_loop: ControlLoop | None = None
    control_mode: ControlMode | None = None
    data_source_uri: str | None = None
    reading: float | None = None
    reading_units: str | None = None
    set_point: float | None = None


class ControlType(StrEnum):
    TEMPERATURE = "Temperature"
    POWER = "Power"
    FREQUENCY = "Frequency"
    FREQUENCY_MHZ = "FrequencyMHz"
    PRESSURE = "Pressure"
    PRESSUREK_PA = "PressurekPa"
    VALVE = "Valve"
    PERCENT = "Percent"
    DUTY_CYCLE = "DutyCycle"
    LIQUID_FLOW_LPM = "LiquidFlowLPM"


class ImplementationType(StrEnum):
    PROGRAMMABLE = "Programmable"
    DIRECT = "Direct"
    MONITORED = "Monitored"


class ResetToDefaults(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SetPointType(StrEnum):
    SINGLE = "Single"
    RANGE = "Range"
