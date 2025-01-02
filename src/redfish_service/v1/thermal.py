from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import RedfishModel
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import IndicatorLed, Location, Status


class Fan(RedfishModel):
    odata_id: str = Field(alias="@odata.id")
    actions: FanActions | None = None
    assembly: IdRef | None = None
    fan_name: str | None = None
    hot_pluggable: bool | None = None
    indicator_led: IndicatorLed | None = Field(alias="IndicatorLED", default=None)
    location: Location | None = None
    lower_threshold_critical: int | None = None
    lower_threshold_fatal: int | None = None
    lower_threshold_non_critical: int | None = None
    manufacturer: str | None = None
    max_reading_range: int | None = None
    member_id: str
    min_reading_range: int | None = None
    model: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    reading: int | None = None
    reading_units: ReadingUnits | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(alias="Redundancy@odata.count", default=None)
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(alias="RelatedItem@odata.count", default=None)
    sensor_number: int | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    upper_threshold_critical: int | None = None
    upper_threshold_fatal: int | None = None
    upper_threshold_non_critical: int | None = None


class FanActions(RedfishModel):
    oem: dict[str, Any] | None = None


class ReadingUnits(StrEnum):
    RPM = "RPM"
    PERCENT = "Percent"


class Temperature(RedfishModel):
    odata_id: str = Field(alias="@odata.id")
    actions: TemperatureActions | None = None
    adjusted_max_allowable_operating_value: int | None = None
    adjusted_min_allowable_operating_value: int | None = None
    delta_physical_context: PhysicalContext | None = None
    delta_reading_celsius: float | None = None
    lower_threshold_critical: float | None = None
    lower_threshold_fatal: float | None = None
    lower_threshold_non_critical: float | None = None
    lower_threshold_user: int | None = None
    max_allowable_operating_value: int | None = None
    max_reading_range_temp: float | None = None
    member_id: str
    min_allowable_operating_value: int | None = None
    min_reading_range_temp: float | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    physical_context: PhysicalContext | None = None
    reading_celsius: float | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(alias="RelatedItem@odata.count", default=None)
    sensor_number: int | None = None
    status: Status | None = None
    upper_threshold_critical: float | None = None
    upper_threshold_fatal: float | None = None
    upper_threshold_non_critical: float | None = None
    upper_threshold_user: int | None = None


class TemperatureActions(RedfishModel):
    oem: dict[str, Any] | None = None


class Thermal(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: ThermalActions | None = None
    description: str | None = None
    fans: list[Fan] | None = None
    fans_odata_count: int | None = Field(alias="Fans@odata.count", default=None)
    id: str
    name: str
    oem: dict[str, Any] | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(alias="Redundancy@odata.count", default=None)
    status: Status | None = None
    temperatures: list[Temperature] | None = None
    temperatures_odata_count: int | None = Field(alias="Temperatures@odata.count", default=None)


class ThermalActions(RedfishModel):
    oem: dict[str, Any] | None = None
