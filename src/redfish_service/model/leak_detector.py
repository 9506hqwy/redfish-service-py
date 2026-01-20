from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .physical_context import PhysicalContext, PhysicalSubContext
from .resource import Location, Status
from .sensor import SensorCurrentExcerpt, SensorVoltageExcerpt


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DetectorState(StrEnum):
    OK = "OK"
    WARNING = "Warning"
    CRITICAL = "Critical"
    UNAVAILABLE = "Unavailable"
    ABSENT = "Absent"


class LeakDetector(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#LeakDetector.v1_6_0.LeakDetector"
    )
    actions: Actions | None = None
    critical_reaction_type: ReactionType | None = None
    current_amps: SensorCurrentExcerpt | None = None
    description: str | None = None
    detector_state: DetectorState | None = None
    enabled: bool | None = None
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
    reaction_delay_seconds: int | None = None
    sku: str | None = Field(serialization_alias="SKU", default=None)
    sensing_frequency: float | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    user_label: str | None = None
    voltage: SensorVoltageExcerpt | None = None
    warning_reaction_type: ReactionType | None = None


class LeakDetectorOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    critical_reaction_type: ReactionType | None = None
    current_amps: SensorCurrentExcerpt | None = None
    enabled: bool | None = None
    location: Location | None = None
    oem: dict[str, Any] | None = None
    reaction_delay_seconds: int | None = None
    status: Status | None = None
    user_label: str | None = None
    voltage: SensorVoltageExcerpt | None = None
    warning_reaction_type: ReactionType | None = None


class LeakDetectorArrayExcerpt(RedfishModel):
    data_source_uri: str | None = None
    detector_state: DetectorState | None = None
    device_name: str | None = None
    physical_context: PhysicalContext | None = None
    physical_sub_context: PhysicalSubContext | None = None


class LeakDetectorExcerpt(RedfishModel):
    data_source_uri: str | None = None
    detector_state: DetectorState | None = None


class LeakDetectorType(StrEnum):
    MOISTURE = "Moisture"
    FLOAT_SWITCH = "FloatSwitch"


class ReactionType(StrEnum):
    NONE = "None"
    FORCE_OFF = "ForceOff"
    GRACEFUL_SHUTDOWN = "GracefulShutdown"
