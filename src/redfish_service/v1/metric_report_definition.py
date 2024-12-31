from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status
from .schedule import Schedule


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    triggers: list[IdRef] | None = None


class Metric(RedfishModel):
    collection_duration: str | None = None
    collection_function: str | None = None
    collection_time_scope: str | None = None
    metric_id: str | None = None
    metric_properties: list[str] | None = None
    oem: dict[str, Any] | None = None


class MetricReportDefinition(RedfishResource):
    actions: Actions | None = None
    append_limit: int | None = None
    description: str | None = None
    links: Links | None = None
    metric_properties: list[str] | None = None
    metric_report: IdRef | None = None
    metric_report_definition_enabled: str | None = None
    metric_report_definition_type: str | None = None
    metric_report_heartbeat_interval: str | None = None
    metrics: list[Metric] | None = None
    oem: dict[str, Any] | None = None
    report_actions: list[ReportActionsEnum] | None = None
    report_timespan: str | None = None
    report_updates: ReportUpdatesEnum | None = None
    schedule: Schedule | None = None
    status: Status | None = None
    suppress_repeated_metric_value: str | None = None
    wildcards: list[Wildcard] | None = None


class ReportActionsEnum(StrEnum):
    LOG_TO_METRIC_REPORTS_COLLECTION = "LogToMetricReportsCollection"
    REDFISH_EVENT = "RedfishEvent"


class ReportUpdatesEnum(StrEnum):
    OVERWRITE = "Overwrite"
    APPEND_WRAPS_WHEN_FULL = "AppendWrapsWhenFull"
    APPEND_STOPS_WHEN_FULL = "AppendStopsWhenFull"
    NEW_REPORT = "NewReport"


class Wildcard(RedfishModel):
    keys: list[str] | None = None
    name: str | None = None
    values: list[str] | None = None
