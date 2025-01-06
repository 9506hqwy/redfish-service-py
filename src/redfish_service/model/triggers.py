from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Health, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DiscreteTrigger(RedfishModel):
    dwell_time: str | None = None
    name: str | None = None
    severity: Health | None = None
    value: str | None = None


class DiscreteTriggerConditionEnum(StrEnum):
    SPECIFIED = "Specified"
    CHANGED = "Changed"


class Links(RedfishModel):
    metric_report_definitions: list[IdRef] | None = None
    metric_report_definitions_odata_count: int | None = Field(
        alias="MetricReportDefinitions@odata.count", default=None
    )
    oem: dict[str, Any] | None = None


class MetricTypeEnum(StrEnum):
    NUMERIC = "Numeric"
    DISCRETE = "Discrete"


class Threshold(RedfishModel):
    activation: ThresholdActivation | None = None
    dwell_time: str | None = None
    reading: float | None = None


class ThresholdActivation(StrEnum):
    INCREASING = "Increasing"
    DECREASING = "Decreasing"
    EITHER = "Either"
    DISABLED = "Disabled"


class Thresholds(RedfishModel):
    lower_critical: Threshold | None = None
    lower_warning: Threshold | None = None
    upper_critical: Threshold | None = None
    upper_warning: Threshold | None = None


class TriggerActionEnum(StrEnum):
    LOG_TO_LOG_SERVICE = "LogToLogService"
    REDFISH_EVENT = "RedfishEvent"
    REDFISH_METRIC_REPORT = "RedfishMetricReport"


class TriggerActionMessage(StrEnum):
    TELEMETRY = "Telemetry"
    DRIVE_MEDIA_LIFE = "DriveMediaLife"
    CONNECTION_SPEED = "ConnectionSpeed"


class Triggers(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#Triggers.v1_4_0.Triggers")
    actions: Actions | None = None
    description: str | None = None
    discrete_trigger_condition: DiscreteTriggerConditionEnum | None = None
    discrete_triggers: list[DiscreteTrigger] | None = None
    event_triggers: list[str] | None = None
    hysteresis_duration: str | None = None
    hysteresis_reading: float | None = None
    id: str
    links: Links | None = None
    metric_ids: list[str] | None = None
    metric_properties: list[str] | None = None
    metric_type: MetricTypeEnum | None = None
    name: str
    numeric_thresholds: Thresholds | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    trigger_action_message: TriggerActionMessage | None = None
    trigger_actions: list[TriggerActionEnum] | None = None
    trigger_enabled: bool | None = None
    wildcards: list[Wildcard] | None = None


class TriggersOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#Triggers.v1_4_0.Triggers")
    actions: Actions | None = None
    description: str | None = None
    discrete_trigger_condition: DiscreteTriggerConditionEnum | None = None
    discrete_triggers: list[DiscreteTrigger] | None = None
    event_triggers: list[str] | None = None
    hysteresis_duration: str | None = None
    hysteresis_reading: float | None = None
    id: str | None = None
    links: Links | None = None
    metric_ids: list[str] | None = None
    metric_properties: list[str] | None = None
    metric_type: MetricTypeEnum | None = None
    name: str | None = None
    numeric_thresholds: Thresholds | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    trigger_action_message: TriggerActionMessage | None = None
    trigger_actions: list[TriggerActionEnum] | None = None
    trigger_enabled: bool | None = None
    wildcards: list[Wildcard] | None = None


class Wildcard(RedfishModel):
    name: str | None = None
    values: list[str] | None = None
