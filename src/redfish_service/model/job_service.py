from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class JobService(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#JobService.v1_0_6.JobService")
    actions: Actions | None = None
    date_time: str | None = None
    description: str | None = None
    id: str
    jobs: IdRef | None = None
    log: IdRef | None = None
    name: str
    oem: dict[str, Any] | None = None
    service_capabilities: JobServiceCapabilities | None = None
    service_enabled: bool | None = None
    status: Status | None = None


class JobServiceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    oem: dict[str, Any] | None = None
    service_capabilities: JobServiceCapabilities | None = None
    service_enabled: bool | None = None
    status: Status | None = None


class JobServiceCapabilities(RedfishModel):
    max_jobs: int | None = None
    max_steps: int | None = None
    scheduling: bool | None = None
