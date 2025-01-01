from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resolution_step import ResolutionStep
from .values import EventType


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Cper(RedfishModel):
    notification_type: str | None = None
    oem: dict[str, Any] | None = None
    section_type: str | None = None


class CxlentryType(StrEnum):
    DYNAMIC_CAPACITY = "DynamicCapacity"
    INFORMATIONAL = "Informational"
    WARNING = "Warning"
    FAILURE = "Failure"
    FATAL = "Fatal"


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    origin_of_condition: IdRef | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(alias="RelatedItem@odata.count", default=None)
    related_log_entries: list[IdRef] | None = None
    related_log_entries_odata_count: int | None = Field(
        alias="RelatedLogEntries@odata.count", default=None
    )


class LogEntry(RedfishResource):
    actions: Actions | None = None
    additional_data_size_bytes: str | None = None
    additional_data_uri: str | None = Field(alias="AdditionalDataURI", default=None)
    cper: Cper | None = Field(alias="CPER", default=None)
    cxlentry_type: CxlentryType | None = Field(alias="CXLEntryType", default=None)
    created: str | None = None
    description: str | None = None
    diagnostic_data: str | None = None
    diagnostic_data_type: str | None = None
    entry_code: str | None = None
    entry_type: LogEntryType
    event_group_id: str | None = None
    event_id: str | None = None
    event_timestamp: str | None = None
    event_type: EventType | None = None
    first_overflow_timestamp: str | None = None
    generator_id: str | None = None
    last_overflow_timestamp: str | None = None
    links: Links | None = None
    message: str | None = None
    message_args: list[str] | None = None
    message_id: str | None = None
    modified: str | None = None
    oemdiagnostic_data_type: str | None = Field(alias="OEMDiagnosticDataType", default=None)
    oem: dict[str, Any] | None = None
    oem_log_entry_code: str | None = None
    oem_record_format: str | None = None
    oem_sensor_type: str | None = None
    originator: str | None = None
    originator_type: OriginatorTypes | None = None
    overflow_error_count: int | None = None
    persistency: bool | None = None
    resolution: str | None = None
    resolution_steps: list[ResolutionStep] | None = None
    resolved: str | None = None
    sensor_number: str | None = None
    sensor_type: str | None = None
    service_provider_notified: str | None = None
    severity: str | None = None
    specific_event_exists_in_group: bool | None = None
    user_authentication_source: str | None = None
    username: str | None = None


class LogEntryType(StrEnum):
    EVENT = "Event"
    SEL = "SEL"
    OEM = "Oem"
    CXL = "CXL"


class OriginatorTypes(StrEnum):
    CLIENT = "Client"
    INTERNAL = "Internal"
    SUPPORTING_SERVICE = "SupportingService"
