from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .action_info import Parameters
from .base import RedfishModel


class ResolutionStep(RedfishModel):
    action_parameters: list[Parameters] | None = None
    action_uri: str | None = Field(alias="ActionURI", default=None)
    oem: dict[str, Any] | None = None
    priority: int | None = None
    resolution_type: ResolutionType | None = None
    retry_count: int | None = None
    retry_interval_seconds: int | None = None
    target_component_uri: str | None = Field(alias="TargetComponentURI", default=None)


class ResolutionType(StrEnum):
    CONTACT_VENDOR = "ContactVendor"
    REPLACE_COMPONENT = "ReplaceComponent"
    FIRMWARE_UPDATE = "FirmwareUpdate"
    RESET = "Reset"
    POWER_CYCLE = "PowerCycle"
    RESET_TO_DEFAULTS = "ResetToDefaults"
    COLLECT_DIAGNOSTIC_DATA = "CollectDiagnosticData"
    OEM = "OEM"
