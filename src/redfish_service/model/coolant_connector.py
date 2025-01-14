from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .cooling_loop import Coolant
from .odata_v4 import IdRef
from .resource import Status
from .sensor import SensorExcerpt


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CoolantConnector(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#CoolantConnector.v1_0_2.CoolantConnector"
    )
    actions: Actions | None = None
    coolant: Coolant | None = None
    coolant_connector_type: CoolantConnectorType | None = None
    cooling_loop_name: str | None = None
    cooling_manager_uri: str | None = Field(serialization_alias="CoolingManagerURI", default=None)
    delta_pressurek_pa: SensorExcerpt | None = None
    delta_temperature_celsius: SensorExcerpt | None = None
    description: str | None = None
    flow_liters_per_minute: SensorExcerpt | None = None
    heat_removedk_w: SensorExcerpt | None = None
    id: str
    links: Links | None = None
    location_indicator_active: bool | None = None
    name: str
    oem: dict[str, Any] | None = None
    rated_flow_liters_per_minute: float | None = None
    rated_flow_pressurek_pa: float | None = None
    rated_pressurek_pa: float | None = None
    return_pressurek_pa: SensorExcerpt | None = None
    return_temperature_celsius: SensorExcerpt | None = None
    status: Status | None = None
    supply_pressurek_pa: SensorExcerpt | None = None
    supply_temperature_celsius: SensorExcerpt | None = None


class CoolantConnectorOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    coolant: Coolant | None = None
    cooling_loop_name: str | None = None
    cooling_manager_uri: str | None = Field(serialization_alias="CoolingManagerURI", default=None)
    links: Links | None = None
    location_indicator_active: bool | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class CoolantConnectorType(StrEnum):
    PAIR = "Pair"
    SUPPLY = "Supply"
    RETURN = "Return"
    INLINE = "Inline"
    CLOSED = "Closed"


class Links(RedfishModel):
    connected_chassis: list[IdRef] | None = None
    connected_chassis_odata_count: int | None = Field(
        serialization_alias="ConnectedChassis@odata.count", default=None
    )
    connected_cooling_loop: IdRef | None = None
    connected_cooling_unit: IdRef | None = None
    oem: dict[str, Any] | None = None
