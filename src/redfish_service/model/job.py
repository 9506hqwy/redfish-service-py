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
    cancel: Cancel | None = Field(serialization_alias="#Job.Cancel", default=None)
    force_start: ForceStart | None = Field(serialization_alias="#Job.ForceStart", default=None)
    invalidate: Invalidate | None = Field(serialization_alias="#Job.Invalidate", default=None)
    resubmit: Resubmit | None = Field(serialization_alias="#Job.Resubmit", default=None)
    resume: Resume | None = Field(serialization_alias="#Job.Resume", default=None)
    suspend: Suspend | None = Field(serialization_alias="#Job.Suspend", default=None)
    validate_value: Validate | None = Field(serialization_alias="#Job.Validate", default=None)
    oem: dict[str, Any] | None = None


class Cancel(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ForceStart(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class Invalidate(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class Job(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Job.v1_3_0.Job")
    actions: Actions | None = None
    created_by: str | None = None
    creation_time: str | None = None
    description: str | None = None
    end_time: str | None = None
    estimated_completion_time: str | None = None
    estimated_duration: str | None = None
    hide_payload: bool | None = None
    id: str
    job_priority: int | None = None
    job_state: JobState | None = None
    job_status: Health | None = None
    job_type: JobType | None = None
    links: Links | None = None
    max_execution_time: str | None = None
    messages: list[Message] | None = None
    name: str
    oem: dict[str, Any] | None = None
    parameters: dict[str, Any] | None = None
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
    odata_type: str | None = Field(serialization_alias="@odata.type", default="#Job.v1_3_0.Job")
    actions: Actions | None = None
    created_by: str | None = None
    creation_time: str | None = None
    description: str | None = None
    end_time: str | None = None
    estimated_completion_time: str | None = None
    estimated_duration: str | None = None
    hide_payload: bool | None = None
    id: str | None = None
    job_priority: int | None = None
    job_state: JobState | None = None
    job_status: Health | None = None
    job_type: JobType | None = None
    links: Links | None = None
    max_execution_time: str | None = None
    messages: list[Message] | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    parameters: dict[str, Any] | None = None
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
    parameters: dict[str, Any] | None = None
    payload: Payload | None = None
    schedule: Schedule | None = None


class JobExcerpt(RedfishModel):
    estimated_completion_time: str | None = None
    job_state: JobState | None = None
    percent_complete: int | None = None


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
    VALIDATING = "Validating"
    INVALID = "Invalid"


class JobType(StrEnum):
    DOCUMENT_BASED = "DocumentBased"
    USER_SPECIFIED = "UserSpecified"
    SERVICE_GENERATED = "ServiceGenerated"


class Links(RedfishModel):
    created_resources: list[IdRef] | None = None
    created_resources_odata_count: int | None = Field(
        serialization_alias="CreatedResources@odata.count", default=None
    )
    executor: IdRef | None = None
    job_document: IdRef | None = None
    oem: dict[str, Any] | None = None
    parent_job: IdRef | None = None
    preferred_executors: list[IdRef] | None = None
    preferred_executors_odata_count: int | None = Field(
        serialization_alias="PreferredExecutors@odata.count", default=None
    )
    subsidiary_jobs: list[IdRef] | None = None
    subsidiary_jobs_odata_count: int | None = Field(
        serialization_alias="SubsidiaryJobs@odata.count", default=None
    )
    validated_executors: list[IdRef] | None = None
    validated_executors_odata_count: int | None = Field(
        serialization_alias="ValidatedExecutors@odata.count", default=None
    )


class Payload(RedfishModel):
    http_headers: list[str] | None = None
    http_operation: str | None = None
    json_body: str | None = None
    target_uri: str | None = None


class Resubmit(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResubmitRequest(RedfishModel):
    start_time: str | None = None


class Resume(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class Suspend(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class Validate(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)
