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


class EventSeverity(StrEnum):
    OK = "OK"
    WARNING = "Warning"
    CRITICAL = "Critical"


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    origin_of_condition: IdRef | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(alias="RelatedItem@odata.count", default=None)
    related_log_entries: list[IdRef] | None = None
    related_log_entries_odata_count: int | None = Field(
        alias="RelatedLogEntries@odata.count", default=None
    )


class LogDiagnosticDataTypes(StrEnum):
    MANAGER = "Manager"
    PRE_OS = "PreOS"
    OS = "OS"
    OEM = "OEM"
    CPER = "CPER"
    CPERSECTION = "CPERSection"


class LogEntry(RedfishResource):
    actions: Actions | None = None
    additional_data_size_bytes: int | None = None
    additional_data_uri: str | None = Field(alias="AdditionalDataURI", default=None)
    cper: Cper | None = Field(alias="CPER", default=None)
    cxlentry_type: CxlentryType | None = Field(alias="CXLEntryType", default=None)
    created: str | None = None
    description: str | None = None
    diagnostic_data: str | None = None
    diagnostic_data_type: LogDiagnosticDataTypes | None = None
    entry_code: LogEntryCode | None = None
    entry_type: LogEntryType
    event_group_id: int | None = None
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
    resolved: bool | None = None
    sensor_number: int | None = None
    sensor_type: SensorType | None = None
    service_provider_notified: bool | None = None
    severity: EventSeverity | None = None
    specific_event_exists_in_group: bool | None = None
    user_authentication_source: str | None = None
    username: str | None = None


class LogEntryCode(StrEnum):
    ASSERT = "Assert"
    DEASSERT = "Deassert"
    LOWER__NON_CRITICAL_GOING_LOW = "Lower Non-critical - going low"
    LOWER__NON_CRITICAL_GOING_HIGH = "Lower Non-critical - going high"
    LOWER__CRITICAL_GOING_LOW = "Lower Critical - going low"
    LOWER__CRITICAL_GOING_HIGH = "Lower Critical - going high"
    LOWER__NON_RECOVERABLE_GOING_LOW = "Lower Non-recoverable - going low"
    LOWER__NON_RECOVERABLE_GOING_HIGH = "Lower Non-recoverable - going high"
    UPPER__NON_CRITICAL_GOING_LOW = "Upper Non-critical - going low"
    UPPER__NON_CRITICAL_GOING_HIGH = "Upper Non-critical - going high"
    UPPER__CRITICAL_GOING_LOW = "Upper Critical - going low"
    UPPER__CRITICAL_GOING_HIGH = "Upper Critical - going high"
    UPPER__NON_RECOVERABLE_GOING_LOW = "Upper Non-recoverable - going low"
    UPPER__NON_RECOVERABLE_GOING_HIGH = "Upper Non-recoverable - going high"
    TRANSITION_TO__IDLE = "Transition to Idle"
    TRANSITION_TO__ACTIVE = "Transition to Active"
    TRANSITION_TO__BUSY = "Transition to Busy"
    STATE__DEASSERTED = "State Deasserted"
    STATE__ASSERTED = "State Asserted"
    PREDICTIVE__FAILURE_DEASSERTED = "Predictive Failure deasserted"
    PREDICTIVE__FAILURE_ASSERTED = "Predictive Failure asserted"
    LIMIT__NOT__EXCEEDED = "Limit Not Exceeded"
    LIMIT__EXCEEDED = "Limit Exceeded"
    PERFORMANCE__MET = "Performance Met"
    PERFORMANCE__LAGS = "Performance Lags"
    TRANSITION_TO__OK = "Transition to OK"
    TRANSITION_TO__NON__CRITICAL_FROM__OK = "Transition to Non-Critical from OK"
    TRANSITION_TO__CRITICAL_FROM_LESS_SEVERE = "Transition to Critical from less severe"
    TRANSITION_TO__NON_RECOVERABLE_FROM_LESS_SEVERE = (
        "Transition to Non-recoverable from less severe"
    )
    TRANSITION_TO__NON__CRITICAL_FROM_MORE_SEVERE = "Transition to Non-Critical from more severe"
    TRANSITION_TO__CRITICAL_FROM__NON_RECOVERABLE = "Transition to Critical from Non-recoverable"
    TRANSITION_TO__NON_RECOVERABLE = "Transition to Non-recoverable"
    MONITOR = "Monitor"
    INFORMATIONAL = "Informational"
    DEVICE__REMOVED__DEVICE__ABSENT = "Device Removed / Device Absent"
    DEVICE__INSERTED__DEVICE__PRESENT = "Device Inserted / Device Present"
    DEVICE__DISABLED = "Device Disabled"
    DEVICE__ENABLED = "Device Enabled"
    TRANSITION_TO__RUNNING = "Transition to Running"
    TRANSITION_TO__IN__TEST = "Transition to In Test"
    TRANSITION_TO__POWER__OFF = "Transition to Power Off"
    TRANSITION_TO__ON__LINE = "Transition to On Line"
    TRANSITION_TO__OFF__LINE = "Transition to Off Line"
    TRANSITION_TO__OFF__DUTY = "Transition to Off Duty"
    TRANSITION_TO__DEGRADED = "Transition to Degraded"
    TRANSITION_TO__POWER__SAVE = "Transition to Power Save"
    INSTALL__ERROR = "Install Error"
    FULLY__REDUNDANT = "Fully Redundant"
    REDUNDANCY__LOST = "Redundancy Lost"
    REDUNDANCY__DEGRADED = "Redundancy Degraded"
    NON_REDUNDANT__SUFFICIENT__RESOURCES_FROM__REDUNDANT = (
        "Non-redundant:Sufficient Resources from Redundant"
    )
    NON_REDUNDANT__SUFFICIENT__RESOURCES_FROM__INSUFFICIENT__RESOURCES = (
        "Non-redundant:Sufficient Resources from Insufficient Resources"
    )
    NON_REDUNDANT__INSUFFICIENT__RESOURCES = "Non-redundant:Insufficient Resources"
    REDUNDANCY__DEGRADED_FROM__FULLY__REDUNDANT = "Redundancy Degraded from Fully Redundant"
    REDUNDANCY__DEGRADED_FROM__NON_REDUNDANT = "Redundancy Degraded from Non-redundant"
    D0__POWER__STATE = "D0 Power State"
    D1__POWER__STATE = "D1 Power State"
    D2__POWER__STATE = "D2 Power State"
    D3__POWER__STATE = "D3 Power State"
    OEM = "OEM"


class LogEntryType(StrEnum):
    EVENT = "Event"
    SEL = "SEL"
    OEM = "Oem"
    CXL = "CXL"


class OriginatorTypes(StrEnum):
    CLIENT = "Client"
    INTERNAL = "Internal"
    SUPPORTING_SERVICE = "SupportingService"


class SensorType(StrEnum):
    PLATFORM__SECURITY__VIOLATION__ATTEMPT = "Platform Security Violation Attempt"
    TEMPERATURE = "Temperature"
    VOLTAGE = "Voltage"
    CURRENT = "Current"
    FAN = "Fan"
    PHYSICAL__CHASSIS__SECURITY = "Physical Chassis Security"
    PROCESSOR = "Processor"
    POWER__SUPPLY__CONVERTER = "Power Supply / Converter"
    POWER_UNIT = "PowerUnit"
    COOLING_DEVICE = "CoolingDevice"
    OTHER__UNITS_BASED__SENSOR = "Other Units-based Sensor"
    MEMORY = "Memory"
    DRIVE__SLOT__BAY = "Drive Slot/Bay"
    POST__MEMORY__RESIZE = "POST Memory Resize"
    SYSTEM__FIRMWARE__PROGRESS = "System Firmware Progress"
    EVENT__LOGGING__DISABLED = "Event Logging Disabled"
    SYSTEM__EVENT = "System Event"
    CRITICAL__INTERRUPT = "Critical Interrupt"
    BUTTON__SWITCH = "Button/Switch"
    MODULE__BOARD = "Module/Board"
    MICROCONTROLLER__COPROCESSOR = "Microcontroller/Coprocessor"
    ADD_IN__CARD = "Add-in Card"
    CHASSIS = "Chassis"
    CHIP_SET = "ChipSet"
    OTHER__FRU = "Other FRU"
    CABLE__INTERCONNECT = "Cable/Interconnect"
    TERMINATOR = "Terminator"
    SYSTEM_BOOT__RESTART = "SystemBoot/Restart"
    BOOT__ERROR = "Boot Error"
    BASE_OSBOOT__INSTALLATION_STATUS = "BaseOSBoot/InstallationStatus"
    OS__STOP__SHUTDOWN = "OS Stop/Shutdown"
    SLOT__CONNECTOR = "Slot/Connector"
    SYSTEM__ACPI__POWER_STATE = "System ACPI PowerState"
    WATCHDOG = "Watchdog"
    PLATFORM__ALERT = "Platform Alert"
    ENTITY__PRESENCE = "Entity Presence"
    MONITOR__ASIC__IC = "Monitor ASIC/IC"
    LAN = "LAN"
    MANAGEMENT__SUBSYSTEM__HEALTH = "Management Subsystem Health"
    BATTERY = "Battery"
    SESSION__AUDIT = "Session Audit"
    VERSION__CHANGE = "Version Change"
    FRUSTATE = "FRUState"
    OEM = "OEM"
