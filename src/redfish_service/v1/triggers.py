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
    oem: dict[str, Any] | None = None


class DiscreteTrigger(RedfishModel):
    dwell_time: str | None = None
    name: str | None = None
    severity: str | None = None
    value: str | None = None


class Links(RedfishModel):
    metric_report_definitions: list[IdRef] | None = None
    metric_report_definitions_odata_count: int | None = Field(
        alias="MetricReportDefinitions@odata.count", default=None
    )
    oem: dict[str, Any] | None = None


class Threshold(RedfishModel):
    activation: str | None = None
    dwell_time: str | None = None
    reading: str | None = None


class Thresholds(RedfishModel):
    lower_critical: Threshold | None = None
    lower_warning: Threshold | None = None
    upper_critical: Threshold | None = None
    upper_warning: Threshold | None = None


class TriggerActionEnum(StrEnum):
    LOG_TO_LOG_SERVICE = "LogToLogService"
    REDFISH_EVENT = "RedfishEvent"
    REDFISH_METRIC_REPORT = "RedfishMetricReport"


class Triggers(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    discrete_trigger_condition: str | None = None
    discrete_triggers: list[DiscreteTrigger] | None = None
    event_triggers: list[str] | None = None
    hysteresis_duration: str | None = None
    hysteresis_reading: str | None = None
    links: Links | None = None
    metric_ids: list[str] | None = None
    metric_properties: list[str] | None = None
    metric_type: str | None = None
    numeric_thresholds: Thresholds | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    trigger_action_message: str | None = None
    trigger_actions: list[TriggerActionEnum] | None = None
    trigger_enabled: str | None = None
    wildcards: list[Wildcard] | None = None


class Wildcard(RedfishModel):
    name: str | None = None
    values: list[str] | None = None
