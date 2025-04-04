from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum

from pydantic import Field

from . import RedfishModel
from .message import Message
from .odata_v4 import IdRef


class ApplyTime(StrEnum):
    IMMEDIATE = "Immediate"
    ON_RESET = "OnReset"
    AT_MAINTENANCE_WINDOW_START = "AtMaintenanceWindowStart"
    IN_MAINTENANCE_WINDOW_ON_RESET = "InMaintenanceWindowOnReset"


class MaintenanceWindow(RedfishModel):
    maintenance_window_duration_in_seconds: int
    maintenance_window_start_time: str


class OperationApplyTime(StrEnum):
    IMMEDIATE = "Immediate"
    ON_RESET = "OnReset"
    AT_MAINTENANCE_WINDOW_START = "AtMaintenanceWindowStart"
    IN_MAINTENANCE_WINDOW_ON_RESET = "InMaintenanceWindowOnReset"
    ON_START_UPDATE_REQUEST = "OnStartUpdateRequest"
    ON_TARGET_RESET = "OnTargetReset"


class OperationApplyTimeSupport(RedfishModel):
    maintenance_window_duration_in_seconds: int | None = None
    maintenance_window_resource: IdRef | None = None
    maintenance_window_start_time: str | None = None
    supported_values: list[OperationApplyTime]


class PreferredApplyTime(RedfishModel):
    apply_time: ApplyTime | None = None
    maintenance_window_duration_in_seconds: int | None = None
    maintenance_window_start_time: str | None = None


class Settings(RedfishModel):
    etag: str | None = Field(serialization_alias="ETag", default=None)
    maintenance_window_resource: IdRef | None = None
    messages: list[Message] | None = None
    settings_object: IdRef | None = None
    supported_apply_times: list[ApplyTime] | None = None
    time: str | None = None
