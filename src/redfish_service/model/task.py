from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .message import Message
from .odata_v4 import IdRef
from .resource import Health


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    created_resources: list[IdRef] | None = None
    created_resources_odata_count: int | None = Field(
        serialization_alias="CreatedResources@odata.count", default=None
    )
    oem: dict[str, Any] | None = None


class Payload(RedfishModel):
    http_headers: list[str] | None = None
    http_operation: str | None = None
    json_body: str | None = None
    target_uri: str | None = None


class Task(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Task.v1_7_4.Task")
    actions: Actions | None = None
    description: str | None = None
    end_time: str | None = None
    estimated_duration: str | None = None
    hide_payload: bool | None = None
    id: str
    links: Links | None = None
    messages: list[Message] | None = None
    name: str
    oem: dict[str, Any] | None = None
    payload: Payload | None = None
    percent_complete: int | None = None
    start_time: str | None = None
    sub_tasks: IdRef | None = None
    task_monitor: str | None = None
    task_state: TaskState | None = None
    task_status: Health | None = None


class TaskState(StrEnum):
    NEW = "New"
    STARTING = "Starting"
    RUNNING = "Running"
    SUSPENDED = "Suspended"
    INTERRUPTED = "Interrupted"
    PENDING = "Pending"
    STOPPING = "Stopping"
    COMPLETED = "Completed"
    KILLED = "Killed"
    EXCEPTION = "Exception"
    SERVICE = "Service"
    CANCELLING = "Cancelling"
    CANCELLED = "Cancelled"
