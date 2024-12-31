from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: OemActions | None = None


class OemActions(RedfishModel):
    pass


class OperatingConfig(RedfishResource):
    actions: Actions | None = None
    base_speed_mhz: str | None = None
    base_speed_priority_settings: list[str] | None = None
    description: str | None = None
    max_junction_temperature_celsius: str | None = None
    max_speed_mhz: str | None = None
    oem: dict[str, Any] | None = None
    tdpwatts: str | None = None
    total_available_core_count: str | None = None
    turbo_profile: list[str] | None = None
