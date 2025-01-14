from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class BaseSpeedPrioritySettings(RedfishModel):
    base_speed_mhz: int | None = Field(serialization_alias="BaseSpeedMHz", default=None)
    core_count: int | None = None
    core_ids: list[int] | None = Field(serialization_alias="CoreIDs", default=None)


class OperatingConfig(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#OperatingConfig.v1_0_4.OperatingConfig"
    )
    actions: Actions | None = None
    base_speed_mhz: int | None = Field(serialization_alias="BaseSpeedMHz", default=None)
    base_speed_priority_settings: list[BaseSpeedPrioritySettings] | None = None
    description: str | None = None
    id: str
    max_junction_temperature_celsius: int | None = None
    max_speed_mhz: int | None = Field(serialization_alias="MaxSpeedMHz", default=None)
    name: str
    oem: dict[str, Any] | None = None
    tdp_watts: int | None = Field(serialization_alias="TDPWatts", default=None)
    total_available_core_count: int | None = None
    turbo_profile: list[TurboProfileDatapoint] | None = None


class TurboProfileDatapoint(RedfishModel):
    active_core_count: int | None = None
    max_speed_mhz: int | None = Field(serialization_alias="MaxSpeedMHz", default=None)
