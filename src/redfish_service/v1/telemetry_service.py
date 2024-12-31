from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class ClearMetricReports(RedfishModel):
    target: str | None = None
    title: str | None = None


class OemActions(RedfishModel):
    pass


class ResetMetricReportDefinitionsToDefaults(RedfishModel):
    target: str | None = None
    title: str | None = None


class ResetTriggersToDefaults(RedfishModel):
    target: str | None = None
    title: str | None = None


class SubmitTestMetricReport(RedfishModel):
    target: str | None = None
    title: str | None = None


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
