from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .resource import Location, Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class LeakDetector(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    detector_state: str | None = None
    leak_detector_type: str | None = None
    location: Location | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: str | None = None
    physical_sub_context: str | None = None
    sku: str | None = None
    sensing_frequency: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    user_label: str | None = None


class LeakDetectorArrayExcerpt(RedfishResource):
    data_source_uri: str | None = None
    detector_state: str | None = None
    device_name: str | None = None
    physical_context: str | None = None
    physical_sub_context: str | None = None


class LeakDetectorExcerpt(RedfishResource):
    data_source_uri: str | None = None
    detector_state: str | None = None


class OemActions(RedfishResource):
    pass
