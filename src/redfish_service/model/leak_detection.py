from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .leak_detector import LeakDetectorArrayExcerpt
from .odata_v4 import IdRef
from .resource import Status
from .sensor import SensorExcerpt


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class LeakDetection(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#LeakDetection.v1_2_0.LeakDetection"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    leak_detector_groups: list[LeakDetectorGroup] | None = None
    leak_detectors: IdRef | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None


class LeakDetectorGroup(RedfishModel):
    detectors: list[LeakDetectorArrayExcerpt] | None = None
    detectors_odata_count: int | None = Field(
        serialization_alias="Detectors@odata.count", default=None
    )
    group_name: str | None = None
    humidity_percent: SensorExcerpt | None = None
    status: Status
