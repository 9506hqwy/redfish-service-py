from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import IndicatorLed, Location, Status


class Actions(RedfishModel):
    power_supply_reset: PowerSupplyReset | None = Field(
        alias="#Power.PowerSupplyReset", default=None
    )
    oem: dict[str, Any] | None = None


class InputRange(RedfishModel):
    input_type: InputType | None = None
    maximum_frequency_hz: float | None = None
    maximum_voltage: float | None = None
    minimum_frequency_hz: float | None = None
    minimum_voltage: float | None = None
    oem: dict[str, Any] | None = None
    output_wattage: float | None = None


class InputType(StrEnum):
    AC = "AC"
    DC = "DC"


class LineInputVoltageType(StrEnum):
    UNKNOWN = "Unknown"
    AC_LOW_LINE = "ACLowLine"
    AC_MID_LINE = "ACMidLine"
    AC_HIGH_LINE = "ACHighLine"
    DC_NEG48_V = "DCNeg48V"
    DC380_V = "DC380V"
    AC120_V = "AC120V"
    AC240_V = "AC240V"
    AC277_V = "AC277V"
    A_CAND_DC_WIDE_RANGE = "ACandDCWideRange"
    AC_WIDE_RANGE = "ACWideRange"
    DC240_V = "DC240V"


class Power(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#Power.v1_7_3.Power")
    actions: Actions | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    power_control: list[PowerControl] | None = None
    power_control_odata_count: int | None = Field(alias="PowerControl@odata.count", default=None)
    power_supplies: list[PowerSupply] | None = None
    power_supplies_odata_count: int | None = Field(alias="PowerSupplies@odata.count", default=None)
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(alias="Redundancy@odata.count", default=None)
    voltages: list[Voltage] | None = None
    voltages_odata_count: int | None = Field(alias="Voltages@odata.count", default=None)


class PowerOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#Power.v1_7_3.Power")
    actions: Actions | None = None
    description: str | None = None
    id: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    power_control: list[PowerControl] | None = None
    power_control_odata_count: int | None = Field(alias="PowerControl@odata.count", default=None)
    power_supplies: list[PowerSupply] | None = None
    power_supplies_odata_count: int | None = Field(alias="PowerSupplies@odata.count", default=None)
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(alias="Redundancy@odata.count", default=None)
    voltages: list[Voltage] | None = None
    voltages_odata_count: int | None = Field(alias="Voltages@odata.count", default=None)


class PowerControl(RedfishModel):
    odata_id: str = Field(alias="@odata.id")
    actions: PowerControlActions | None = None
    member_id: str
    name: str | None = None
    oem: dict[str, Any] | None = None
    physical_context: PhysicalContext | None = None
    power_allocated_watts: float | None = None
    power_available_watts: float | None = None
    power_capacity_watts: float | None = None
    power_consumed_watts: float | None = None
    power_limit: PowerLimit | None = None
    power_metrics: PowerMetric | None = None
    power_requested_watts: float | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(alias="RelatedItem@odata.count", default=None)
    status: Status | None = None


class PowerControlActions(RedfishModel):
    oem: dict[str, Any] | None = None


class PowerLimit(RedfishModel):
    correction_in_ms: int | None = None
    limit_exception: PowerLimitException | None = None
    limit_in_watts: float | None = None


class PowerLimitException(StrEnum):
    NO_ACTION = "NoAction"
    HARD_POWER_OFF = "HardPowerOff"
    LOG_EVENT_ONLY = "LogEventOnly"
    OEM = "Oem"


class PowerMetric(RedfishModel):
    average_consumed_watts: float | None = None
    interval_in_min: int | None = None
    max_consumed_watts: float | None = None
    min_consumed_watts: float | None = None


class PowerSupply(RedfishModel):
    odata_id: str = Field(alias="@odata.id")
    actions: PowerSupplyActions | None = None
    assembly: IdRef | None = None
    efficiency_percent: float | None = None
    firmware_version: str | None = None
    hot_pluggable: bool | None = None
    indicator_led: IndicatorLed | None = Field(alias="IndicatorLED", default=None)
    input_ranges: list[InputRange] | None = None
    last_power_output_watts: float | None = None
    line_input_voltage: float | None = None
    line_input_voltage_type: LineInputVoltageType | None = None
    location: Location | None = None
    manufacturer: str | None = None
    member_id: str
    model: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    power_capacity_watts: float | None = None
    power_input_watts: float | None = None
    power_output_watts: float | None = None
    power_supply_type: PowerSupplyType | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(alias="Redundancy@odata.count", default=None)
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(alias="RelatedItem@odata.count", default=None)
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None


class PowerSupplyActions(RedfishModel):
    oem: dict[str, Any] | None = None


class PowerSupplyReset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class PowerSupplyType(StrEnum):
    UNKNOWN = "Unknown"
    AC = "AC"
    DC = "DC"
    A_COR_DC = "ACorDC"


class Voltage(RedfishModel):
    odata_id: str = Field(alias="@odata.id")
    actions: VoltageActions | None = None
    lower_threshold_critical: float | None = None
    lower_threshold_fatal: float | None = None
    lower_threshold_non_critical: float | None = None
    max_reading_range: float | None = None
    member_id: str
    min_reading_range: float | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    physical_context: PhysicalContext | None = None
    reading_volts: float | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(alias="RelatedItem@odata.count", default=None)
    sensor_number: int | None = None
    status: Status | None = None
    upper_threshold_critical: float | None = None
    upper_threshold_fatal: float | None = None
    upper_threshold_non_critical: float | None = None


class VoltageActions(RedfishModel):
    oem: dict[str, Any] | None = None
