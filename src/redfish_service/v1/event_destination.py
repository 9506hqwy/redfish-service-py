from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Health, Status
from .values import EventType


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


class EventDestination(RedfishResource):
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
    include_origin_of_condition: bool | None = None
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


class SnmpauthenticationProtocols(StrEnum):
    NONE = "None"
    COMMUNITY_STRING = "CommunityString"
    HMAC__MD5 = "HMAC_MD5"
    HMAC__SHA96 = "HMAC_SHA96"
    HMAC128__SHA224 = "HMAC128_SHA224"
    HMAC192__SHA256 = "HMAC192_SHA256"
    HMAC256__SHA384 = "HMAC256_SHA384"
    HMAC384__SHA512 = "HMAC384_SHA512"


class SnmpencryptionProtocols(StrEnum):
    NONE = "None"
    CBC__DES = "CBC_DES"
    CFB128__AES128 = "CFB128_AES128"
    CFB128__AES192 = "CFB128_AES192"
    CFB128__AES256 = "CFB128_AES256"


class Snmpsettings(RedfishModel):
    authentication_key: str | None = None
    authentication_key_set: bool | None = None
    authentication_protocol: SnmpauthenticationProtocols | None = None
    encryption_key: str | None = None
    encryption_key_set: bool | None = None
    encryption_protocol: SnmpencryptionProtocols | None = None
    trap_community: str | None = None


class SubscriptionType(StrEnum):
    REDFISH_EVENT = "RedfishEvent"
    SSE = "SSE"
    SNMPTRAP = "SNMPTrap"
    SNMPINFORM = "SNMPInform"
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
