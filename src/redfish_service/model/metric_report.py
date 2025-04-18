from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class MetricReport(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#MetricReport.v1_5_2.MetricReport"
    )
    actions: Actions | None = None
    context: str | None = None
    description: str | None = None
    id: str
    metric_report_definition: IdRef | None = None
    metric_values: list[MetricValue] | None = None
    name: str
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
