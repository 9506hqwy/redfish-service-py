from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Coolant(RedfishModel):
    additive_name: str | None = None
    additive_percent: str | None = None
    coolant_type: str | None = None
    density_kg_per_cubic_meter: str | None = None
    rated_service_hours: str | None = None
    service_hours: str | None = None
    serviced_date: str | None = None
    specific_heatk_joules_per_kg_k: str | None = None


class CoolingLoop(RedfishResource):
    actions: Actions | None = None
    consuming_equipment_names: list[str] | None = None
    coolant: Coolant | None = None
    coolant_level_percent: str | None = None
    coolant_level_status: str | None = None
    coolant_quality: str | None = None
    cooling_manager_uri: str | None = Field(alias="CoolingManagerURI", default=None)
    description: str | None = None
    links: Links | None = None
    location_indicator_active: str | None = None
    oem: dict[str, Any] | None = None
    primary_coolant_connectors: IdRef | None = None
    rated_flow_liters_per_minute: str | None = None
    rated_pressurek_pa: str | None = None
    secondary_coolant_connectors: IdRef | None = None
    status: Status | None = None
    supply_equipment_names: list[str] | None = None
    user_label: str | None = None


class Links(RedfishModel):
    chassis: str | None = None
    facility: IdRef | None = None
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(alias="ManagedBy@odata.count", default=None)
    oem: dict[str, Any] | None = None
