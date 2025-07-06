from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    cancel_all_jobs: CancelAllJobs | None = Field(
        serialization_alias="#JobService.CancelAllJobs", default=None
    )
    oem: dict[str, Any] | None = None


class CancelAllJobs(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class JobService(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#JobService.v1_1_0.JobService"
    )
    actions: Actions | None = None
    date_time: str | None = None
    description: str | None = None
    id: str
    job_documents: IdRef | None = None
    job_executors: IdRef | None = None
    jobs: IdRef | None = None
    log: IdRef | None = None
    name: str
    oem: dict[str, Any] | None = None
    service_capabilities: JobServiceCapabilities | None = None
    service_enabled: bool | None = None
    status: Status | None = None
    validation_policy: ValidationPolicy | None = None


class JobServiceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    oem: dict[str, Any] | None = None
    service_capabilities: JobServiceCapabilities | None = None
    service_enabled: bool | None = None
    status: Status | None = None


class JobServiceCapabilities(RedfishModel):
    document_based_jobs: bool | None = None
    max_jobs: int | None = None
    max_steps: int | None = None
    scheduling: bool | None = None
    user_specified_jobs: bool | None = None


class ValidationPolicy(StrEnum):
    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    BYPASS = "Bypass"
