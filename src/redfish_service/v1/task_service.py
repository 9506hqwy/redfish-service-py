from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class OverWritePolicy(StrEnum):
    MANUAL = "Manual"
    OLDEST = "Oldest"


class TaskService(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    completed_task_over_write_policy: OverWritePolicy | None = None
    date_time: str | None = None
    description: str | None = None
    id: str
    life_cycle_event_on_task_state_change: bool | None = None
    name: str
    oem: dict[str, Any] | None = None
    service_enabled: bool | None = None
    status: Status | None = None
    task_auto_delete_timeout_minutes: int | None = None
    tasks: IdRef | None = None
