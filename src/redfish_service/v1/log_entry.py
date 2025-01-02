from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .event import EventType
from .odata_v4 import IdRef
from .resolution_step import ResolutionStep


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Cper(RedfishModel):
    notification_type: str | None = None
    oem: dict[str, Any] | None = None
    section_type: str | None = None


class CxlEntryType(StrEnum):
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
    CPER_SECTION = "CPERSection"


class LogEntry(RedfishResource):
    actions: Actions | None = None
    additional_data_size_bytes: int | None = None
    additional_data_uri: str | None = Field(alias="AdditionalDataURI", default=None)
    cper: Cper | None = Field(alias="CPER", default=None)
    cxl_entry_type: CxlEntryType | None = Field(alias="CXLEntryType", default=None)
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
    oem_diagnostic_data_type: str | None = Field(alias="OEMDiagnosticDataType", default=None)
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
    LOWER_NON_CRITICAL_GOING_LOW = "Lower Non-critical - going low"
    LOWER_NON_CRITICAL_GOING_HIGH = "Lower Non-critical - going high"
    LOWER_CRITICAL_GOING_LOW = "Lower Critical - going low"
    LOWER_CRITICAL_GOING_HIGH = "Lower Critical - going high"
    LOWER_NON_RECOVERABLE_GOING_LOW = "Lower Non-recoverable - going low"
    LOWER_NON_RECOVERABLE_GOING_HIGH = "Lower Non-recoverable - going high"
    UPPER_NON_CRITICAL_GOING_LOW = "Upper Non-critical - going low"
    UPPER_NON_CRITICAL_GOING_HIGH = "Upper Non-critical - going high"
    UPPER_CRITICAL_GOING_LOW = "Upper Critical - going low"
    UPPER_CRITICAL_GOING_HIGH = "Upper Critical - going high"
    UPPER_NON_RECOVERABLE_GOING_LOW = "Upper Non-recoverable - going low"
    UPPER_NON_RECOVERABLE_GOING_HIGH = "Upper Non-recoverable - going high"
    TRANSITION_TO_IDLE = "Transition to Idle"
    TRANSITION_TO_ACTIVE = "Transition to Active"
    TRANSITION_TO_BUSY = "Transition to Busy"
    STATE_DEASSERTED = "State Deasserted"
    STATE_ASSERTED = "State Asserted"
    PREDICTIVE_FAILURE_DEASSERTED = "Predictive Failure deasserted"
    PREDICTIVE_FAILURE_ASSERTED = "Predictive Failure asserted"
    LIMIT_NOT_EXCEEDED = "Limit Not Exceeded"
    LIMIT_EXCEEDED = "Limit Exceeded"
    PERFORMANCE_MET = "Performance Met"
    PERFORMANCE_LAGS = "Performance Lags"
    TRANSITION_TO_OK = "Transition to OK"
    TRANSITION_TO_NON_CRITICAL_FROM_OK = "Transition to Non-Critical from OK"
    TRANSITION_TO_CRITICAL_FROM_LESS_SEVERE = "Transition to Critical from less severe"
    TRANSITION_TO_NON_RECOVERABLE_FROM_LESS_SEVERE = (
        "Transition to Non-recoverable from less severe"
    )
    TRANSITION_TO_NON_CRITICAL_FROM_MORE_SEVERE = "Transition to Non-Critical from more severe"
    TRANSITION_TO_CRITICAL_FROM_NON_RECOVERABLE = "Transition to Critical from Non-recoverable"
    TRANSITION_TO_NON_RECOVERABLE = "Transition to Non-recoverable"
    MONITOR = "Monitor"
    INFORMATIONAL = "Informational"
    DEVICE_REMOVED_DEVICE_ABSENT = "Device Removed / Device Absent"
    DEVICE_INSERTED_DEVICE_PRESENT = "Device Inserted / Device Present"
    DEVICE_DISABLED = "Device Disabled"
    DEVICE_ENABLED = "Device Enabled"
    TRANSITION_TO_RUNNING = "Transition to Running"
    TRANSITION_TO_IN_TEST = "Transition to In Test"
    TRANSITION_TO_POWER_OFF = "Transition to Power Off"
    TRANSITION_TO_ON_LINE = "Transition to On Line"
    TRANSITION_TO_OFF_LINE = "Transition to Off Line"
    TRANSITION_TO_OFF_DUTY = "Transition to Off Duty"
    TRANSITION_TO_DEGRADED = "Transition to Degraded"
    TRANSITION_TO_POWER_SAVE = "Transition to Power Save"
    INSTALL_ERROR = "Install Error"
    FULLY_REDUNDANT = "Fully Redundant"
    REDUNDANCY_LOST = "Redundancy Lost"
    REDUNDANCY_DEGRADED = "Redundancy Degraded"
    NON_REDUNDANT_SUFFICIENT_RESOURCES_FROM_REDUNDANT = (
        "Non-redundant:Sufficient Resources from Redundant"
    )
    NON_REDUNDANT_SUFFICIENT_RESOURCES_FROM_INSUFFICIENT_RESOURCES = (
        "Non-redundant:Sufficient Resources from Insufficient Resources"
    )
    NON_REDUNDANT_INSUFFICIENT_RESOURCES = "Non-redundant:Insufficient Resources"
    REDUNDANCY_DEGRADED_FROM_FULLY_REDUNDANT = "Redundancy Degraded from Fully Redundant"
    REDUNDANCY_DEGRADED_FROM_NON_REDUNDANT = "Redundancy Degraded from Non-redundant"
    D0_POWER_STATE = "D0 Power State"
    D1_POWER_STATE = "D1 Power State"
    D2_POWER_STATE = "D2 Power State"
    D3_POWER_STATE = "D3 Power State"
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
    PLATFORM_SECURITY_VIOLATION_ATTEMPT = "Platform Security Violation Attempt"
    TEMPERATURE = "Temperature"
    VOLTAGE = "Voltage"
    CURRENT = "Current"
    FAN = "Fan"
    PHYSICAL_CHASSIS_SECURITY = "Physical Chassis Security"
    PROCESSOR = "Processor"
    POWER_SUPPLY_CONVERTER = "Power Supply / Converter"
    POWER_UNIT = "PowerUnit"
    COOLING_DEVICE = "CoolingDevice"
    OTHER_UNITS_BASED_SENSOR = "Other Units-based Sensor"
    MEMORY = "Memory"
    DRIVE_SLOT_BAY = "Drive Slot/Bay"
    POS_T_MEMORY_RESIZE = "POST Memory Resize"
    SYSTEM_FIRMWARE_PROGRESS = "System Firmware Progress"
    EVENT_LOGGING_DISABLED = "Event Logging Disabled"
    SYSTEM_EVENT = "System Event"
    CRITICAL_INTERRUPT = "Critical Interrupt"
    BUTTON_SWITCH = "Button/Switch"
    MODULE_BOARD = "Module/Board"
    MICROCONTROLLER_COPROCESSOR = "Microcontroller/Coprocessor"
    ADD_IN_CARD = "Add-in Card"
    CHASSIS = "Chassis"
    CHIP_SET = "ChipSet"
    OTHER_FRU = "Other FRU"
    CABLE_INTERCONNECT = "Cable/Interconnect"
    TERMINATOR = "Terminator"
    SYSTEM_BOOT_RESTART = "SystemBoot/Restart"
    BOOT_ERROR = "Boot Error"
    BASE_OS_BOOT_INSTALLATION_STATUS = "BaseOSBoot/InstallationStatus"
    O_S_STOP_SHUTDOWN = "OS Stop/Shutdown"
    SLOT_CONNECTOR = "Slot/Connector"
    SYSTEM_ACP_I_POWER_STATE = "System ACPI PowerState"
    WATCHDOG = "Watchdog"
    PLATFORM_ALERT = "Platform Alert"
    ENTITY_PRESENCE = "Entity Presence"
    MONITOR_ASI_C_IC = "Monitor ASIC/IC"
    LAN = "LAN"
    MANAGEMENT_SUBSYSTEM_HEALTH = "Management Subsystem Health"
    BATTERY = "Battery"
    SESSION_AUDIT = "Session Audit"
    VERSION_CHANGE = "Version Change"
    FRU_STATE = "FRUState"
    OEM = "OEM"
