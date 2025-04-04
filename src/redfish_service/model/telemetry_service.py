from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    clear_metric_reports: ClearMetricReports | None = Field(
        serialization_alias="#TelemetryService.ClearMetricReports", default=None
    )
    reset_metric_report_definitions_to_defaults: ResetMetricReportDefinitionsToDefaults | None = (
        Field(
            serialization_alias="#TelemetryService.ResetMetricReportDefinitionsToDefaults",
            default=None,
        )
    )
    reset_triggers_to_defaults: ResetTriggersToDefaults | None = Field(
        serialization_alias="#TelemetryService.ResetTriggersToDefaults", default=None
    )
    submit_test_metric_report: SubmitTestMetricReport | None = Field(
        serialization_alias="#TelemetryService.SubmitTestMetricReport", default=None
    )
    oem: dict[str, Any] | None = None


class ClearMetricReports(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class CollectionFunction(StrEnum):
    AVERAGE = "Average"
    MAXIMUM = "Maximum"
    MINIMUM = "Minimum"
    SUMMATION = "Summation"


class MetricValue(RedfishModel):
    metric_definition: IdRef | None = None
    metric_id: str | None = None
    metric_property: str | None = None
    metric_value: str | None = None
    timestamp: str | None = None


class ResetMetricReportDefinitionsToDefaults(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetTriggersToDefaults(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SubmitTestMetricReport(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SubmitTestMetricReportRequest(RedfishModel):
    generated_metric_report_values: list[MetricValue]
    metric_report_name: str
    metric_report_values: str | None = None


class TelemetryService(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#TelemetryService.v1_3_4.TelemetryService"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    log_service: IdRef | None = None
    max_reports: int | None = None
    metric_definitions: IdRef | None = None
    metric_report_definitions: IdRef | None = None
    metric_reports: IdRef | None = None
    min_collection_interval: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    service_enabled: bool | None = None
    status: Status | None = None
    supported_collection_functions: list[CollectionFunction] | None = None
    triggers: IdRef | None = None


class TelemetryServiceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    oem: dict[str, Any] | None = None
    service_enabled: bool | None = None
    status: Status | None = None
