from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .cooling_loop import Coolant
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Health, Location, Status
from .sensor import SensorExcerpt


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Reservoir(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    assembly: IdRef | None = None
    capacity_liters: float | None = None
    coolant: Coolant | None = None
    description: str | None = None
    filters: IdRef | None = None
    fluid_level_percent: SensorExcerpt | None = None
    fluid_level_status: Health | None = None
    id: str
    internal_pressurek_pa: SensorExcerpt | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    reservoir_type: ReservoirType | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    user_label: str | None = None


class ReservoirType(StrEnum):
    RESERVE = "Reserve"
    OVERFLOW = "Overflow"
    INLINE = "Inline"
    IMMERSION = "Immersion"
