from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .redundancy import RedundantGroup
from .resource import Location, Status


class Actions(RedfishModel):
    transfer_control: TransferControl | None = Field(
        alias="#PowerDistribution.TransferControl", default=None
    )
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    chassis: list[IdRef] | None = None
    chassis_odata_count: int | None = Field(alias="Chassis@odata.count", default=None)
    facility: IdRef | None = None
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(alias="ManagedBy@odata.count", default=None)
    oem: dict[str, Any] | None = None


class PowerDistribution(RedfishResource):
    actions: Actions | None = None
    asset_tag: str | None = None
    branches: IdRef | None = None
    description: str | None = None
    equipment_type: PowerEquipmentType
    feeders: IdRef | None = None
    firmware_version: str | None = None
    links: Links | None = None
    location: Location | None = None
    mains: IdRef | None = None
    mains_redundancy: RedundantGroup | None = None
    manufacturer: str | None = None
    metrics: IdRef | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    outlet_groups: IdRef | None = None
    outlets: IdRef | None = None
    part_number: str | None = None
    power_capacity_va: int | None = Field(alias="PowerCapacityVA", default=None)
    power_supplies: IdRef | None = None
    power_supply_redundancy: list[RedundantGroup] | None = None
    production_date: str | None = None
    sensors: IdRef | None = None
    serial_number: str | None = None
    status: Status | None = None
    subfeeds: IdRef | None = None
    transfer_configuration: TransferConfiguration | None = None
    transfer_criteria: TransferCriteria | None = None
    uuid: str | None = Field(alias="UUID", default=None)
    user_label: str | None = None
    version: str | None = None


class PowerEquipmentType(StrEnum):
    RACK_PDU = "RackPDU"
    FLOOR_PDU = "FloorPDU"
    MANUAL_TRANSFER_SWITCH = "ManualTransferSwitch"
    AUTOMATIC_TRANSFER_SWITCH = "AutomaticTransferSwitch"
    SWITCHGEAR = "Switchgear"
    POWER_SHELF = "PowerShelf"
    BUS = "Bus"
    BATTERY_SHELF = "BatteryShelf"


class TransferConfiguration(RedfishModel):
    active_mains_id: str | None = None
    auto_transfer_enabled: bool | None = None
    closed_transition_allowed: bool | None = None
    closed_transition_timeout_seconds: int | None = None
    preferred_mains_id: str | None = None
    retransfer_delay_seconds: int | None = None
    retransfer_enabled: bool | None = None
    transfer_delay_seconds: int | None = None
    transfer_inhibit: bool | None = None


class TransferControl(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class TransferCriteria(RedfishModel):
    over_nominal_frequency_hz: float | None = None
    over_voltage_rmspercentage: float | None = Field(
        alias="OverVoltageRMSPercentage", default=None
    )
    transfer_sensitivity: TransferSensitivityType | None = None
    under_nominal_frequency_hz: float | None = None
    under_voltage_rmspercentage: float | None = Field(
        alias="UnderVoltageRMSPercentage", default=None
    )


class TransferSensitivityType(StrEnum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
