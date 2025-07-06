from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class JobExecutor(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#JobExecutor.v1_0_0.JobExecutor"
    )
    actions: Actions | None = None
    description: str | None = None
    executor_type: str | None = None
    id: str
    links: Links | None = None
    maximum_concurrent_jobs: int | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None


class JobExecutorOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#JobExecutor.v1_0_0.JobExecutor"
    )
    actions: Actions | None = None
    description: str | None = None
    executor_type: str | None = None
    id: str | None = None
    links: Links | None = None
    maximum_concurrent_jobs: int | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class Links(RedfishModel):
    chassis: list[IdRef] | None = None
    chassis_odata_count: int | None = Field(
        serialization_alias="Chassis@odata.count", default=None
    )
    computer_system: IdRef | None = None
    executing_jobs: list[IdRef] | None = None
    executing_jobs_odata_count: int | None = Field(
        serialization_alias="ExecutingJobs@odata.count", default=None
    )
