from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .physical_context import PhysicalContext, PhysicalSubContext
from .resource import Health, Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class LeakDetector(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    description: str | None = None
    detector_state: Health | None = None
    id: str
    leak_detector_type: LeakDetectorType | None = None
    location: Location | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    physical_sub_context: PhysicalSubContext | None = None
    sku: str | None = Field(alias="SKU", default=None)
    sensing_frequency: float | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    user_label: str | None = None


class LeakDetectorArrayExcerpt(RedfishModel):
    data_source_uri: str | None = None
    detector_state: Health | None = None
    device_name: str | None = None
    physical_context: PhysicalContext | None = None
    physical_sub_context: PhysicalSubContext | None = None


class LeakDetectorExcerpt(RedfishModel):
    data_source_uri: str | None = None
    detector_state: Health | None = None


class LeakDetectorType(StrEnum):
    MOISTURE = "Moisture"
    FLOAT_SWITCH = "FloatSwitch"
