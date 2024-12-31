from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class MetricReport(RedfishResource):
    actions: Actions | None = None
    context: str | None = None
    description: str | None = None
    metric_report_definition: IdRef | None = None
    metric_values: list[MetricValue] | None = None
    oem: dict[str, Any] | None = None
    report_sequence: str | None = None
    timestamp: str | None = None


class MetricValue(RedfishModel):
    metric_definition: IdRef | None = None
    metric_id: str | None = None
    metric_property: str | None = None
    metric_value: str | None = None
    oem: dict[str, Any] | None = None
    timestamp: str | None = None
