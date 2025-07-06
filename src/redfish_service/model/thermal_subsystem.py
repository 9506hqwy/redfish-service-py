from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .redundancy import RedundantGroup
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ThermalSubsystem(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#ThermalSubsystem.v1_4_0.ThermalSubsystem"
    )
    actions: Actions | None = None
    coolant_connector_redundancy: list[RedundantGroup] | None = None
    coolant_connectors: IdRef | None = None
    description: str | None = None
    fan_redundancy: list[RedundantGroup] | None = None
    fans: IdRef | None = None
    filters: IdRef | None = None
    heaters: IdRef | None = None
    id: str
    leak_detection: IdRef | None = None
    name: str
    oem: dict[str, Any] | None = None
    pumps: IdRef | None = None
    status: Status | None = None
    thermal_metrics: IdRef | None = None
