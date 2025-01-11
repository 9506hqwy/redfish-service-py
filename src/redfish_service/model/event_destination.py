from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .event import EventType
from .odata_v4 import IdRef
from .resource import Health, Status


class Actions(RedfishModel):
    resume_subscription: ResumeSubscription | None = Field(
        alias="#EventDestination.ResumeSubscription", default=None
    )
    suspend_subscription: SuspendSubscription | None = Field(
        alias="#EventDestination.SuspendSubscription", default=None
    )
    oem: dict[str, Any] | None = None


class DeliveryRetryPolicy(StrEnum):
    TERMINATE_AFTER_RETRIES = "TerminateAfterRetries"
    SUSPEND_RETRIES = "SuspendRetries"
    RETRY_FOREVER = "RetryForever"
    RETRY_FOREVER_WITH_BACKOFF = "RetryForeverWithBackoff"


class EventDestination(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type", default="#EventDestination.v1_15_0.EventDestination"
    )
    actions: Actions | None = None
    backup_destinations: list[str] | None = None
    certificates: IdRef | None = None
    client_certificates: IdRef | None = None
    context: str | None = None
    delivery_retry_policy: DeliveryRetryPolicy | None = None
    description: str | None = None
    destination: str | None = None
    event_format_type: EventFormatType | None = None
    event_types: list[EventType] | None = None
    exclude_message_ids: list[str] | None = None
    exclude_registry_prefixes: list[str] | None = None
    heartbeat_interval_minutes: int | None = None
    http_headers: list[dict[str, Any]] | None = None
    id: str
    include_origin_of_condition: bool | None = None
    message_ids: list[str] | None = None
    metric_report_definitions: list[IdRef] | None = None
    metric_report_definitions_odata_count: int | None = Field(
        alias="MetricReportDefinitions@odata.count", default=None
    )
    name: str
    oem_protocol: str | None = Field(alias="OEMProtocol", default=None)
    oem_subscription_type: str | None = Field(alias="OEMSubscriptionType", default=None)
    oem: dict[str, Any] | None = None
    origin_resources: list[IdRef] | None = None
    origin_resources_odata_count: int | None = Field(
        alias="OriginResources@odata.count", default=None
    )
    protocol: EventDestinationProtocol | None = None
    registry_prefixes: list[str] | None = None
    resource_types: list[str] | None = None
    snmp: SnmpSettings | None = Field(alias="SNMP", default=None)
    send_heartbeat: bool | None = None
    severities: list[Health] | None = None
    status: Status | None = None
    subordinate_resources: bool | None = None
    subscription_type: SubscriptionType | None = None
    syslog_filters: list[SyslogFilter] | None = None
    verify_certificate: bool | None = None


class EventDestinationOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(
        alias="@odata.type", default="#EventDestination.v1_15_0.EventDestination"
    )
    actions: Actions | None = None
    backup_destinations: list[str] | None = None
    certificates: IdRef | None = None
    client_certificates: IdRef | None = None
    context: str | None = None
    delivery_retry_policy: DeliveryRetryPolicy | None = None
    description: str | None = None
    destination: str
    event_format_type: EventFormatType | None = None
    event_types: list[EventType] | None = None
    exclude_message_ids: list[str] | None = None
    exclude_registry_prefixes: list[str] | None = None
    heartbeat_interval_minutes: int | None = None
    http_headers: list[dict[str, Any]] | None = None
    id: str | None = None
    include_origin_of_condition: bool | None = None
    message_ids: list[str] | None = None
    metric_report_definitions: list[IdRef] | None = None
    metric_report_definitions_odata_count: int | None = Field(
        alias="MetricReportDefinitions@odata.count", default=None
    )
    name: str | None = None
    oem_protocol: str | None = Field(alias="OEMProtocol", default=None)
    oem_subscription_type: str | None = Field(alias="OEMSubscriptionType", default=None)
    oem: dict[str, Any] | None = None
    origin_resources: list[IdRef] | None = None
    origin_resources_odata_count: int | None = Field(
        alias="OriginResources@odata.count", default=None
    )
    protocol: EventDestinationProtocol
    registry_prefixes: list[str] | None = None
    resource_types: list[str] | None = None
    snmp: SnmpSettings | None = Field(alias="SNMP", default=None)
    send_heartbeat: bool | None = None
    severities: list[Health] | None = None
    status: Status | None = None
    subordinate_resources: bool | None = None
    subscription_type: SubscriptionType | None = None
    syslog_filters: list[SyslogFilter] | None = None
    verify_certificate: bool | None = None


class EventDestinationOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(
        alias="@odata.type", default="#EventDestination.v1_15_0.EventDestination"
    )
    actions: Actions | None = None
    backup_destinations: list[str] | None = None
    certificates: IdRef | None = None
    client_certificates: IdRef | None = None
    context: str | None = None
    delivery_retry_policy: DeliveryRetryPolicy | None = None
    description: str | None = None
    destination: str | None = None
    event_format_type: EventFormatType | None = None
    event_types: list[EventType] | None = None
    exclude_message_ids: list[str] | None = None
    exclude_registry_prefixes: list[str] | None = None
    heartbeat_interval_minutes: int | None = None
    http_headers: list[dict[str, Any]] | None = None
    id: str | None = None
    include_origin_of_condition: bool | None = None
    message_ids: list[str] | None = None
    metric_report_definitions: list[IdRef] | None = None
    metric_report_definitions_odata_count: int | None = Field(
        alias="MetricReportDefinitions@odata.count", default=None
    )
    name: str | None = None
    oem_protocol: str | None = Field(alias="OEMProtocol", default=None)
    oem_subscription_type: str | None = Field(alias="OEMSubscriptionType", default=None)
    oem: dict[str, Any] | None = None
    origin_resources: list[IdRef] | None = None
    origin_resources_odata_count: int | None = Field(
        alias="OriginResources@odata.count", default=None
    )
    protocol: EventDestinationProtocol | None = None
    registry_prefixes: list[str] | None = None
    resource_types: list[str] | None = None
    snmp: SnmpSettings | None = Field(alias="SNMP", default=None)
    send_heartbeat: bool | None = None
    severities: list[Health] | None = None
    status: Status | None = None
    subordinate_resources: bool | None = None
    subscription_type: SubscriptionType | None = None
    syslog_filters: list[SyslogFilter] | None = None
    verify_certificate: bool | None = None


class EventDestinationProtocol(StrEnum):
    REDFISH = "Redfish"
    KAFKA = "Kafka"
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


class SnmpAuthenticationProtocols(StrEnum):
    NONE = "None"
    COMMUNITY_STRING = "CommunityString"
    HMA_C_MD5 = "HMAC_MD5"
    HMA_C_SHA96 = "HMAC_SHA96"
    HMA_C128_SHA224 = "HMAC128_SHA224"
    HMA_C192_SHA256 = "HMAC192_SHA256"
    HMA_C256_SHA384 = "HMAC256_SHA384"
    HMA_C384_SHA512 = "HMAC384_SHA512"


class SnmpEncryptionProtocols(StrEnum):
    NONE = "None"
    CB_C_DES = "CBC_DES"
    CF_B128_AES128 = "CFB128_AES128"
    CF_B128_AES192 = "CFB128_AES192"
    CF_B128_AES256 = "CFB128_AES256"


class SnmpSettings(RedfishModel):
    authentication_key: str | None = None
    authentication_key_set: bool | None = None
    authentication_protocol: SnmpAuthenticationProtocols | None = None
    encryption_key: str | None = None
    encryption_key_set: bool | None = None
    encryption_protocol: SnmpEncryptionProtocols | None = None
    trap_community: str | None = None


class SubscriptionType(StrEnum):
    REDFISH_EVENT = "RedfishEvent"
    SSE = "SSE"
    SNMP_TRAP = "SNMPTrap"
    SNMP_INFORM = "SNMPInform"
    SYSLOG = "Syslog"
    OEM = "OEM"


class SuspendSubscription(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SyslogFacility(StrEnum):
    KERN = "Kern"
    USER = "User"
    MAIL = "Mail"
    DAEMON = "Daemon"
    AUTH = "Auth"
    SYSLOG = "Syslog"
    LPR = "LPR"
    NEWS = "News"
    UUCP = "UUCP"
    CRON = "Cron"
    AUTHPRIV = "Authpriv"
    FTP = "FTP"
    NTP = "NTP"
    SECURITY = "Security"
    CONSOLE = "Console"
    SOLARIS_CRON = "SolarisCron"
    LOCAL0 = "Local0"
    LOCAL1 = "Local1"
    LOCAL2 = "Local2"
    LOCAL3 = "Local3"
    LOCAL4 = "Local4"
    LOCAL5 = "Local5"
    LOCAL6 = "Local6"
    LOCAL7 = "Local7"


class SyslogFilter(RedfishModel):
    log_facilities: list[SyslogFacility] | None = None
    lowest_severity: SyslogSeverity | None = None


class SyslogSeverity(StrEnum):
    EMERGENCY = "Emergency"
    ALERT = "Alert"
    CRITICAL = "Critical"
    ERROR = "Error"
    WARNING = "Warning"
    NOTICE = "Notice"
    INFORMATIONAL = "Informational"
    DEBUG = "Debug"
    ALL = "All"
