from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class ClearLog(RedfishResource):
    target: str | None = None
    title: str | None = None


class CollectDiagnosticData(RedfishResource):
    target: str | None = None
    title: str | None = None


class LogService(RedfishResource):
    actions: Actions | None = None
    auto_clear_resolved_entries: str | None = None
    auto_dstenabled: bool | None = None
    date_time: str | None = None
    date_time_local_offset: str | None = None
    description: str | None = None
    diagnostic_data_details: list[str] | None = None
    entries: IdRef | None = None
    log_entry_type: str | None = None
    log_purposes: list[str] | None = None
    max_number_of_records: int | None = None
    oemlog_purpose: str | None = None
    oem: dict[str, Any] | None = None
    over_write_policy: OverWritePolicy | None = None
    overflow: bool | None = None
    persistency: bool | None = None
    service_enabled: str | None = None
    status: Status | None = None
    syslog_filters: list[str] | None = None


class OemActions(RedfishResource):
    pass


class OverWritePolicy(StrEnum):
    UNKNOWN = "Unknown"
    WRAPS_WHEN_FULL = "WrapsWhenFull"
    NEVER_OVER_WRITES = "NeverOverWrites"


class PushDiagnosticData(RedfishResource):
    target: str | None = None
    title: str | None = None
