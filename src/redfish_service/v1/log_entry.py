from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .values import EventType


class Actions(RedfishModel):
    oem: OemActions | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    origin_of_condition: IdRef | None = None


class LogEntry(RedfishResource):
    actions: Actions | None = None
    additional_data_size_bytes: str | None = None
    additional_data_uri: str | None = None
    created: str | None = None
    description: str | None = None
    diagnostic_data_type: str | None = None
    entry_code: str | None = None
    entry_type: LogEntryType
    event_group_id: str | None = None
    event_id: str | None = None
    event_timestamp: str | None = None
    event_type: EventType | None = None
    generator_id: str | None = None
    links: Links | None = None
    message: str | None = None
    message_args: list[str] | None = None
    message_id: str | None = None
    modified: str | None = None
    oemdiagnostic_data_type: str | None = None
    oem: dict[str, Any] | None = None
    oem_log_entry_code: str | None = None
    oem_record_format: str | None = None
    oem_sensor_type: str | None = None
    resolution: str | None = None
    resolved: str | None = None
    sensor_number: str | None = None
    sensor_type: str | None = None
    service_provider_notified: str | None = None
    severity: str | None = None


class LogEntryType(StrEnum):
    EVENT = "Event"
    SEL = "SEL"
    OEM = "Oem"


class OemActions(RedfishModel):
    pass
