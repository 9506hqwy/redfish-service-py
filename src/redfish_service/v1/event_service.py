from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status
from .values import EventType


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class EventService(RedfishResource):
    actions: Actions | None = None
    delivery_retry_attempts: int | None = None
    delivery_retry_interval_seconds: int | None = None
    description: str | None = None
    event_format_types: list[str] | None = None
    event_types_for_subscription: list[EventType] | None = None
    exclude_message_id: bool | None = None
    exclude_registry_prefix: bool | None = None
    include_origin_of_condition_supported: str | None = None
    oem: dict[str, Any] | None = None
    registry_prefixes: list[str] | None = None
    resource_types: list[str] | None = None
    smtp: Smtp | None = None
    ssefilter_properties_supported: SsefilterPropertiesSupported | None = None
    server_sent_event_uri: str | None = None
    service_enabled: str | None = None
    severities: list[str] | None = None
    status: Status | None = None
    subordinate_resources_supported: str | None = None
    subscriptions: IdRef | None = None


class Smtp(RedfishModel):
    authentication: str | None = None
    connection_protocol: str | None = None
    from_address: str | None = None
    password: str | None = None
    password_set: bool | None = None
    port: str | None = None
    server_address: str | None = None
    service_enabled: str | None = None
    username: str | None = None


class SsefilterPropertiesSupported(RedfishModel):
    event_format_type: bool | None = None
    event_type: bool | None = None
    message_id: bool | None = None
    metric_report_definition: bool | None = None
    origin_resource: bool | None = None
    registry_prefix: bool | None = None
    resource_type: bool | None = None
    subordinate_resources: bool | None = None


class SubmitTestEvent(RedfishModel):
    target: str | None = None
    title: str | None = None
