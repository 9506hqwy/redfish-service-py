from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
)
from .odata_v4 import IdRef
from .resource import Health
from .values import EventType


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Cper(RedfishModel):
    notification_type: str | None = None
    oem: dict[str, Any] | None = None
    section_type: str | None = None


class Event(RedfishModel):
    actions: Actions | None = None
    context: str | None = None
    description: str | None = None
    events: list[EventRecord]
    id: str
    name: str
    oem: dict[str, Any] | None = None


class EventRecord(RedfishModel):
    actions: EventRecordActions | None = None
    additional_data_size_bytes: str | None = None
    additional_data_uri: str | None = None
    cper: Cper | None = None
    context: str | None = None
    diagnostic_data: str | None = None
    diagnostic_data_type: str | None = None
    event_group_id: int | None = None
    event_id: str | None = None
    event_timestamp: str | None = None
    event_type: EventType
    log_entry: IdRef | None = None
    member_id: str
    message: str | None = None
    message_args: list[str] | None = None
    message_id: str
    message_severity: Health | None = None
    oemdiagnostic_data_type: str | None = None
    oem: dict[str, Any] | None = None
    origin_of_condition: IdRef | None = None
    resolution: str | None = None
    severity: str | None = None
    specific_event_exists_in_group: bool | None = None


class EventRecordActions(RedfishModel):
    oem: dict[str, Any] | None = None
