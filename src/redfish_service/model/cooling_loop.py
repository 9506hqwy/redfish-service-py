from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Health, Status
from .sensor import SensorExcerpt


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Coolant(RedfishModel):
    additive_name: str | None = None
    additive_percent: float | None = None
    coolant_type: CoolantType | None = None
    density_kg_per_cubic_meter: float | None = None
    rated_service_hours: float | None = None
    service_hours: float | None = None
    serviced_date: str | None = None
    specific_heatk_joules_per_kg_k: float | None = None


class CoolantType(StrEnum):
    WATER = "Water"
    HYDROCARBON = "Hydrocarbon"
    FLUOROCARBON = "Fluorocarbon"
    DIELECTRIC = "Dielectric"


class CoolingLoop(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#CoolingLoop.v1_0_3.CoolingLoop")
    actions: Actions | None = None
    consuming_equipment_names: list[str] | None = None
    coolant: Coolant | None = None
    coolant_level_percent: SensorExcerpt | None = None
    coolant_level_status: Health | None = None
    coolant_quality: Health | None = None
    cooling_manager_uri: str | None = Field(alias="CoolingManagerURI", default=None)
    description: str | None = None
    id: str
    links: Links | None = None
    location_indicator_active: bool | None = None
    name: str
    oem: dict[str, Any] | None = None
    primary_coolant_connectors: IdRef | None = None
    rated_flow_liters_per_minute: float | None = None
    rated_pressurek_pa: float | None = None
    secondary_coolant_connectors: IdRef | None = None
    status: Status | None = None
    supply_equipment_names: list[str] | None = None
    user_label: str | None = None


class CoolingLoopOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    consuming_equipment_names: list[str] | None = None
    coolant: Coolant | None = None
    cooling_manager_uri: str | None = Field(alias="CoolingManagerURI", default=None)
    links: Links | None = None
    location_indicator_active: bool | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    supply_equipment_names: list[str] | None = None
    user_label: str | None = None


class Links(RedfishModel):
    chassis: IdRef | None = None
    facility: IdRef | None = None
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(alias="ManagedBy@odata.count", default=None)
    oem: dict[str, Any] | None = None
