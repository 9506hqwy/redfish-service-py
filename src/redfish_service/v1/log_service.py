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


class AutoClearResolvedEntries(StrEnum):
    CLEAR_EVENT_GROUP = "ClearEventGroup"
    RETAIN_CAUSE_RESOLUTION_ENTRIES = "RetainCauseResolutionEntries"
    UPDATE_CAUSE_ENTRY = "UpdateCauseEntry"
    NONE = "None"


class ClearLog(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class CollectDiagnosticData(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class DiagnosticDataDetails(RedfishModel):
    diagnostic_data_type: LogDiagnosticDataTypes | None = None
    estimated_duration: str | None = None
    estimated_size_bytes: int | None = None
    oem_diagnostic_data_type: str | None = Field(alias="OEMDiagnosticDataType", default=None)


class LogDiagnosticDataTypes(StrEnum):
    MANAGER = "Manager"
    PRE_OS = "PreOS"
    OS = "OS"
    OEM = "OEM"


class LogEntryTypes(StrEnum):
    EVENT = "Event"
    SEL = "SEL"
    MULTIPLE = "Multiple"
    OEM = "OEM"
    CXL = "CXL"


class LogPurpose(StrEnum):
    DIAGNOSTIC = "Diagnostic"
    OPERATIONS = "Operations"
    SECURITY = "Security"
    TELEMETRY = "Telemetry"
    EXTERNAL_ENTITY = "ExternalEntity"
    OEM = "OEM"


class LogService(RedfishResource):
    actions: Actions | None = None
    auto_clear_resolved_entries: AutoClearResolvedEntries | None = None
    auto_dst_enabled: bool | None = Field(alias="AutoDSTEnabled", default=None)
    date_time: str | None = None
    date_time_local_offset: str | None = None
    description: str | None = None
    diagnostic_data_details: list[DiagnosticDataDetails] | None = None
    entries: IdRef | None = None
    log_entry_type: LogEntryTypes | None = None
    log_purposes: list[LogPurpose] | None = None
    max_number_of_records: int | None = None
    oem_log_purpose: str | None = Field(alias="OEMLogPurpose", default=None)
    oem: dict[str, Any] | None = None
    over_write_policy: OverWritePolicy | None = None
    overflow: bool | None = None
    persistency: bool | None = None
    service_enabled: bool | None = None
    status: Status | None = None
    syslog_filters: list[SyslogFilter] | None = None


class OverWritePolicy(StrEnum):
    UNKNOWN = "Unknown"
    WRAPS_WHEN_FULL = "WrapsWhenFull"
    NEVER_OVER_WRITES = "NeverOverWrites"


class PushDiagnosticData(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SyslogFacility(StrEnum):
    KERN = "Kern"
    USER = "User"
    MAIL = "Mail"
    DAEMON = "Daemon"
    AUTH = "Auth"
    SYSLOG = "Syslog"
    LPR = "LPR"
    NEWS = "News"
    UUCP = "UUCP"
    CRON = "Cron"
    AUTHPRIV = "Authpriv"
    FTP = "FTP"
    NTP = "NTP"
    SECURITY = "Security"
    CONSOLE = "Console"
    SOLARIS_CRON = "SolarisCron"
    LOCAL0 = "Local0"
    LOCAL1 = "Local1"
    LOCAL2 = "Local2"
    LOCAL3 = "Local3"
    LOCAL4 = "Local4"
    LOCAL5 = "Local5"
    LOCAL6 = "Local6"
    LOCAL7 = "Local7"


class SyslogFilter(RedfishModel):
    log_facilities: list[SyslogFacility] | None = None
    lowest_severity: SyslogSeverity | None = None


class SyslogSeverity(StrEnum):
    EMERGENCY = "Emergency"
    ALERT = "Alert"
    CRITICAL = "Critical"
    ERROR = "Error"
    WARNING = "Warning"
    NOTICE = "Notice"
    INFORMATIONAL = "Informational"
    DEBUG = "Debug"
    ALL = "All"
