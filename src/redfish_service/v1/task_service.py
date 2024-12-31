from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class OemActions(RedfishResource):
    pass


class OverWritePolicy(StrEnum):
    MANUAL = "Manual"
    OLDEST = "Oldest"


class TaskService(RedfishResource):
    actions: Actions | None = None
    completed_task_over_write_policy: OverWritePolicy | None = None
    date_time: str | None = None
    description: str | None = None
    life_cycle_event_on_task_state_change: bool | None = None
    oem: dict[str, Any] | None = None
    service_enabled: str | None = None
    status: Status | None = None
    task_auto_delete_timeout_minutes: int | None = None
    tasks: IdRef | None = None
