from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Location, Status
from .sensor import SensorFanExcerpt, SensorPowerExcerpt


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Fan(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#Fan.v1_5_2.Fan")
    actions: Actions | None = None
    assembly: IdRef | None = None
    description: str | None = None
    fan_diameter_mm: int | None = None
    hot_pluggable: bool | None = None
    id: str
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    power_watts: SensorPowerExcerpt | None = None
    replaceable: bool | None = None
    secondary_speed_percent: SensorFanExcerpt | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    speed_percent: SensorFanExcerpt | None = None
    status: Status | None = None


class FanOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#Fan.v1_5_2.Fan")
    actions: Actions | None = None
    assembly: IdRef | None = None
    description: str | None = None
    fan_diameter_mm: int | None = None
    hot_pluggable: bool | None = None
    id: str | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    power_watts: SensorPowerExcerpt | None = None
    replaceable: bool | None = None
    secondary_speed_percent: SensorFanExcerpt | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    speed_percent: SensorFanExcerpt | None = None
    status: Status | None = None


class Links(RedfishModel):
    cooling_chassis: list[IdRef] | None = None
    cooling_chassis_odata_count: int | None = Field(
        alias="CoolingChassis@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
