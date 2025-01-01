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
from .values import EventType


class Actions(RedfishModel):
    resume_subscription: ResumeSubscription | None = Field(
        alias="#EventDestination.ResumeSubscription", default=None
    )
    oem: dict[str, Any] | None = None


class EventDestination(RedfishResource):
    actions: Actions | None = None
    certificates: IdRef | None = None
    context: str
    delivery_retry_policy: str | None = None
    description: str | None = None
    destination: str | None = None
    event_format_type: str | None = None
    event_types: list[EventType] | None = None
    http_headers: list[dict[str, Any]] | None = None
    include_origin_of_condition: str | None = None
    message_ids: list[str] | None = None
    metric_report_definitions: list[IdRef] | None = None
    metric_report_definitions_odata_count: int | None = Field(
        alias="MetricReportDefinitions@odata.count", default=None
    )
    oemprotocol: str | None = Field(alias="OEMProtocol", default=None)
    oemsubscription_type: str | None = Field(alias="OEMSubscriptionType", default=None)
    oem: dict[str, Any] | None = None
    origin_resources: list[IdRef] | None = None
    origin_resources_odata_count: int | None = Field(
        alias="OriginResources@odata.count", default=None
    )
    protocol: EventDestinationProtocol | None = None
    registry_prefixes: list[str] | None = None
    resource_types: list[str] | None = None
    snmp: Snmpsettings | None = Field(alias="SNMP", default=None)
    status: Status | None = None
    subordinate_resources: str | None = None
    subscription_type: str
    syslog_filters: list[str] | None = None
    verify_certificate: str | None = None


class EventDestinationProtocol(StrEnum):
    REDFISH = "Redfish"
    SNMPV1 = "SNMPv1"
    SNMPV2C = "SNMPv2c"
    SNMPV3 = "SNMPv3"
    SMTP = "SMTP"
    SYSLOG_TLS = "SyslogTLS"
    SYSLOG_TCP = "SyslogTCP"
    SYSLOG_UDP = "SyslogUDP"
    SYSLOG_RELP = "SyslogRELP"
    OEM = "OEM"


class EventFormatType(StrEnum):
    EVENT = "Event"
    METRIC_REPORT = "MetricReport"


class ResumeSubscription(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Snmpsettings(RedfishModel):
    authentication_key: str | None = None
    authentication_protocol: str | None = None
    encryption_key: str | None = None
    encryption_protocol: str | None = None
    trap_community: str | None = None
