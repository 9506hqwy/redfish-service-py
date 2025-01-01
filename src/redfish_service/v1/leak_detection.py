from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .leak_detector import LeakDetectorArrayExcerpt
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class LeakDetection(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    leak_detector_groups: list[LeakDetectorGroup] | None = None
    leak_detectors: IdRef | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class LeakDetectorGroup(RedfishModel):
    detectors: list[LeakDetectorArrayExcerpt] | None = None
    detectors_odata_count: int | None = Field(alias="Detectors@odata.count", default=None)
    group_name: str | None = None
    humidity_percent: str | None = None
    status: Status
