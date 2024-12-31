from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Location, Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class InputRange(RedfishResource):
    input_type: str | None = None
    maximum_frequency_hz: str | None = None
    maximum_voltage: str | None = None
    minimum_frequency_hz: str | None = None
    minimum_voltage: str | None = None
    oem: dict[str, Any] | None = None
    output_wattage: str | None = None


class OemActions(RedfishResource):
    pass


class Power(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    power_control: list[PowerControl] | None = None
    power_supplies: list[PowerSupply] | None = None
    redundancy: list[IdRef] | None = None
    voltages: list[Voltage] | None = None


class PowerControl(RedfishResource):
    actions: PowerControlActions | None = None
    member_id: str
    oem: dict[str, Any] | None = None
    physical_context: PhysicalContext | None = None
    power_allocated_watts: str | None = None
    power_available_watts: str | None = None
    power_capacity_watts: str | None = None
    power_consumed_watts: str | None = None
    power_limit: PowerLimit | None = None
    power_metrics: PowerMetric | None = None
    power_requested_watts: str | None = None
    related_item: list[IdRef] | None = None
    status: Status | None = None


class PowerControlActions(RedfishResource):
    oem: PowerControlOemActions | None = None


class PowerControlOemActions(RedfishResource):
    pass


class PowerLimit(RedfishResource):
    correction_in_ms: str | None = None
    limit_exception: str | None = None
    limit_in_watts: str | None = None


class PowerMetric(RedfishResource):
    average_consumed_watts: str | None = None
    interval_in_min: str | None = None
    max_consumed_watts: str | None = None
    min_consumed_watts: str | None = None


class PowerSupply(RedfishResource):
    actions: PowerSupplyActions | None = None
    assembly: IdRef | None = None
    efficiency_percent: str | None = None
    firmware_version: str | None = None
    hot_pluggable: str | None = None
    indicator_led: str | None = None
    input_ranges: list[InputRange] | None = None
    last_power_output_watts: str | None = None
    line_input_voltage: str | None = None
    line_input_voltage_type: str | None = None
    location: Location | None = None
    manufacturer: str | None = None
    member_id: str
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    power_capacity_watts: str | None = None
    power_input_watts: str | None = None
    power_output_watts: str | None = None
    power_supply_type: str | None = None
    redundancy: list[IdRef] | None = None
    related_item: list[IdRef] | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None


class PowerSupplyActions(RedfishResource):
    oem: PowerSupplyOemActions | None = None


class PowerSupplyOemActions(RedfishResource):
    pass


class PowerSupplyReset(RedfishResource):
    target: str | None = None
    title: str | None = None


class Voltage(RedfishResource):
    actions: VoltageActions | None = None
    lower_threshold_critical: str | None = None
    lower_threshold_fatal: str | None = None
    lower_threshold_non_critical: str | None = None
    max_reading_range: str | None = None
    member_id: str
    min_reading_range: str | None = None
    oem: dict[str, Any] | None = None
    physical_context: PhysicalContext | None = None
    reading_volts: str | None = None
    related_item: list[IdRef] | None = None
    sensor_number: str | None = None
    status: Status | None = None
    upper_threshold_critical: str | None = None
    upper_threshold_fatal: str | None = None
    upper_threshold_non_critical: str | None = None


class VoltageActions(RedfishResource):
    oem: VoltageOemActions | None = None


class VoltageOemActions(RedfishResource):
    pass
