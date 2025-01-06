from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status
from .schedule import Schedule


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CalculationAlgorithmEnum(StrEnum):
    AVERAGE = "Average"
    MAXIMUM = "Maximum"
    MINIMUM = "Minimum"
    SUMMATION = "Summation"


class CollectionTimeScope(StrEnum):
    POINT = "Point"
    INTERVAL = "Interval"
    STARTUP_INTERVAL = "StartupInterval"


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    triggers: list[IdRef] | None = None
    triggers_odata_count: int | None = Field(alias="Triggers@odata.count", default=None)


class Metric(RedfishModel):
    collection_duration: str | None = None
    collection_function: CalculationAlgorithmEnum | None = None
    collection_time_scope: CollectionTimeScope | None = None
    metric_id: str | None = None
    metric_properties: list[str] | None = None
    oem: dict[str, Any] | None = None


class MetricReportDefinition(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type", default="#MetricReportDefinition.v1_4_6.MetricReportDefinition"
    )
    actions: Actions | None = None
    append_limit: int | None = None
    description: str | None = None
    id: str
    links: Links | None = None
    metric_properties: list[str] | None = None
    metric_report: IdRef | None = None
    metric_report_definition_enabled: bool | None = None
    metric_report_definition_type: MetricReportDefinitionType | None = None
    metric_report_heartbeat_interval: str | None = None
    metrics: list[Metric] | None = None
    name: str
    oem: dict[str, Any] | None = None
    report_actions: list[ReportActionsEnum] | None = None
    report_timespan: str | None = None
    report_updates: ReportUpdatesEnum | None = None
    schedule: Schedule | None = None
    status: Status | None = None
    suppress_repeated_metric_value: bool | None = None
    wildcards: list[Wildcard] | None = None


class MetricReportDefinitionOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(
        alias="@odata.type", default="#MetricReportDefinition.v1_4_6.MetricReportDefinition"
    )
    actions: Actions | None = None
    append_limit: int | None = None
    description: str | None = None
    id: str | None = None
    links: Links | None = None
    metric_properties: list[str] | None = None
    metric_report: IdRef | None = None
    metric_report_definition_enabled: bool | None = None
    metric_report_definition_type: MetricReportDefinitionType | None = None
    metric_report_heartbeat_interval: str | None = None
    metrics: list[Metric] | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    report_actions: list[ReportActionsEnum] | None = None
    report_timespan: str | None = None
    report_updates: ReportUpdatesEnum | None = None
    schedule: Schedule | None = None
    status: Status | None = None
    suppress_repeated_metric_value: bool | None = None
    wildcards: list[Wildcard] | None = None


class MetricReportDefinitionType(StrEnum):
    PERIODIC = "Periodic"
    ON_CHANGE = "OnChange"
    ON_REQUEST = "OnRequest"


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
