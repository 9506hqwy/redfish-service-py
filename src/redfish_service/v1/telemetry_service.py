from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    clear_metric_reports: ClearMetricReports | None = Field(
        alias="#TelemetryService.ClearMetricReports", default=None
    )
    reset_metric_report_definitions_to_defaults: ResetMetricReportDefinitionsToDefaults | None = (
        Field(alias="#TelemetryService.ResetMetricReportDefinitionsToDefaults", default=None)
    )
    reset_triggers_to_defaults: ResetTriggersToDefaults | None = Field(
        alias="#TelemetryService.ResetTriggersToDefaults", default=None
    )
    submit_test_metric_report: SubmitTestMetricReport | None = Field(
        alias="#TelemetryService.SubmitTestMetricReport", default=None
    )
    oem: dict[str, Any] | None = None


class ClearMetricReports(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ResetMetricReportDefinitionsToDefaults(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ResetTriggersToDefaults(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SubmitTestMetricReport(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class TelemetryService(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    log_service: IdRef | None = None
    max_reports: str | None = None
    metric_definitions: IdRef | None = None
    metric_report_definitions: IdRef | None = None
    metric_reports: IdRef | None = None
    min_collection_interval: str | None = None
    oem: dict[str, Any] | None = None
    service_enabled: str | None = None
    status: Status | None = None
    supported_collection_functions: list[str] | None = None
    triggers: IdRef | None = None
