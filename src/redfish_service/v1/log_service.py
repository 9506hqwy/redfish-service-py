from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    clear_log: ClearLog | None = Field(alias="#LogService.ClearLog", default=None)
    collect_diagnostic_data: CollectDiagnosticData | None = Field(
        alias="#LogService.CollectDiagnosticData", default=None
    )
    push_diagnostic_data: PushDiagnosticData | None = Field(
        alias="#LogService.PushDiagnosticData", default=None
    )
    oem: dict[str, Any] | None = None


class ClearLog(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class CollectDiagnosticData(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class LogService(RedfishResource):
    actions: Actions | None = None
    auto_clear_resolved_entries: str | None = None
    auto_dstenabled: bool | None = Field(alias="AutoDSTEnabled", default=None)
    date_time: str | None = None
    date_time_local_offset: str | None = None
    description: str | None = None
    diagnostic_data_details: list[str] | None = None
    entries: IdRef | None = None
    log_entry_type: str | None = None
    log_purposes: list[str] | None = None
    max_number_of_records: int | None = None
    oemlog_purpose: str | None = Field(alias="OEMLogPurpose", default=None)
    oem: dict[str, Any] | None = None
    over_write_policy: OverWritePolicy | None = None
    overflow: bool | None = None
    persistency: bool | None = None
    service_enabled: str | None = None
    status: Status | None = None
    syslog_filters: list[str] | None = None


class OverWritePolicy(StrEnum):
    UNKNOWN = "Unknown"
    WRAPS_WHEN_FULL = "WrapsWhenFull"
    NEVER_OVER_WRITES = "NeverOverWrites"


class PushDiagnosticData(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
