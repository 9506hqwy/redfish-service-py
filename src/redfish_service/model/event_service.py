from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .event import EventType
from .event_destination import EventFormatType
from .odata_v4 import IdRef
from .resource import Health, Status


class Actions(RedfishModel):
    submit_test_event: SubmitTestEvent | None = Field(
        alias="#EventService.SubmitTestEvent", default=None
    )
    test_event_subscription: TestEventSubscription | None = Field(
        alias="#EventService.TestEventSubscription", default=None
    )
    oem: dict[str, Any] | None = None


class EventService(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#EventService.v1_10_2.EventService")
    actions: Actions | None = None
    delivery_retry_attempts: int | None = None
    delivery_retry_interval_seconds: int | None = None
    description: str | None = None
    event_format_types: list[EventFormatType] | None = None
    event_types_for_subscription: list[EventType] | None = None
    exclude_message_id: bool | None = None
    exclude_registry_prefix: bool | None = None
    id: str
    include_origin_of_condition_supported: bool | None = None
    name: str
    oem: dict[str, Any] | None = None
    registry_prefixes: list[str] | None = None
    resource_types: list[str] | None = None
    smtp: Smtp | None = Field(alias="SMTP", default=None)
    sse_filter_properties_supported: SseFilterPropertiesSupported | None = Field(
        alias="SSEFilterPropertiesSupported", default=None
    )
    server_sent_event_uri: str | None = None
    service_enabled: bool | None = None
    severities: list[Health] | None = None
    status: Status | None = None
    subordinate_resources_supported: bool | None = None
    subscriptions: IdRef | None = None


class Smtp(RedfishModel):
    authentication: SmtpAuthenticationMethods | None = None
    connection_protocol: SmtpConnectionProtocol | None = None
    from_address: str | None = None
    password: str | None = None
    password_set: bool | None = None
    port: int | None = None
    server_address: str | None = None
    service_enabled: bool | None = None
    username: str | None = None


class SmtpAuthenticationMethods(StrEnum):
    NONE = "None"
    AUTO_DETECT = "AutoDetect"
    PLAIN = "Plain"
    LOGIN = "Login"
    CRA_M_MD5 = "CRAM_MD5"


class SmtpConnectionProtocol(StrEnum):
    NONE = "None"
    AUTO_DETECT = "AutoDetect"
    START_TLS = "StartTLS"
    TL_S_SSL = "TLS_SSL"


class SseFilterPropertiesSupported(RedfishModel):
    event_format_type: bool | None = None
    event_type: bool | None = None
    message_id: bool | None = None
    metric_report_definition: bool | None = None
    origin_resource: bool | None = None
    registry_prefix: bool | None = None
    resource_type: bool | None = None
    subordinate_resources: bool | None = None


class SubmitTestEvent(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class TestEventSubscription(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
