from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Filter(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Filter.v1_0_2.Filter")
    actions: Actions | None = None
    assembly: IdRef | None = None
    description: str | None = None
    hot_pluggable: bool | None = None
    id: str
    location: Location | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    rated_service_hours: float | None = None
    replaceable: bool | None = None
    serial_number: str | None = None
    service_hours: float | None = None
    serviced_date: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    user_label: str | None = None


class FilterOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    oem: dict[str, Any] | None = None
    service_hours: float | None = None
    serviced_date: str | None = None
    status: Status | None = None
    user_label: str | None = None
