from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .message import Message
from .odata_v4 import IdRef
from .resource import Health
from .schedule import Schedule


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Job(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Job.v1_2_4.Job")
    actions: Actions | None = None
    created_by: str | None = None
    description: str | None = None
    end_time: str | None = None
    estimated_duration: str | None = None
    hide_payload: bool | None = None
    id: str
    job_state: JobState | None = None
    job_status: Health | None = None
    links: Links | None = None
    max_execution_time: str | None = None
    messages: list[Message] | None = None
    name: str
    oem: dict[str, Any] | None = None
    payload: Payload | None = None
    percent_complete: int | None = None
    schedule: Schedule | None = None
    start_time: str | None = None
    step_order: list[str] | None = None
    steps: IdRef | None = None


class JobOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(serialization_alias="@odata.type", default="#Job.v1_2_4.Job")
    actions: Actions | None = None
    created_by: str | None = None
    description: str | None = None
    end_time: str | None = None
    estimated_duration: str | None = None
    hide_payload: bool | None = None
    id: str | None = None
    job_state: JobState | None = None
    job_status: Health | None = None
    links: Links | None = None
    max_execution_time: str | None = None
    messages: list[Message] | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    payload: Payload | None = None
    percent_complete: int | None = None
    schedule: Schedule | None = None
    start_time: str | None = None
    step_order: list[str] | None = None
    steps: IdRef | None = None


class JobOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    job_state: JobState | None = None
    links: Links | None = None
    max_execution_time: str | None = None
    messages: list[Message] | None = None
    oem: dict[str, Any] | None = None
    payload: Payload | None = None
    schedule: Schedule | None = None


class JobState(StrEnum):
    NEW = "New"
    STARTING = "Starting"
    RUNNING = "Running"
    SUSPENDED = "Suspended"
    INTERRUPTED = "Interrupted"
    PENDING = "Pending"
    STOPPING = "Stopping"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    EXCEPTION = "Exception"
    SERVICE = "Service"
    USER_INTERVENTION = "UserIntervention"
    CONTINUE = "Continue"


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
