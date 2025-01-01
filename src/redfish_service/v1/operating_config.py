from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class BaseSpeedPrioritySettings(RedfishModel):
    base_speed_mhz: int | None = Field(alias="BaseSpeedMHz", default=None)
    core_count: int | None = None
    core_ids: list[int] | None = Field(alias="CoreIDs", default=None)


class OperatingConfig(RedfishResource):
    actions: Actions | None = None
    base_speed_mhz: int | None = Field(alias="BaseSpeedMHz", default=None)
    base_speed_priority_settings: list[BaseSpeedPrioritySettings] | None = None
    description: str | None = None
    max_junction_temperature_celsius: int | None = None
    max_speed_mhz: int | None = Field(alias="MaxSpeedMHz", default=None)
    oem: dict[str, Any] | None = None
    tdpwatts: int | None = Field(alias="TDPWatts", default=None)
    total_available_core_count: int | None = None
    turbo_profile: list[TurboProfileDatapoint] | None = None


class TurboProfileDatapoint(RedfishModel):
    active_core_count: int | None = None
    max_speed_mhz: int | None = Field(alias="MaxSpeedMHz", default=None)
