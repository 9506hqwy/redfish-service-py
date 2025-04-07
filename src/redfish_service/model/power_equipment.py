from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(
        serialization_alias="ManagedBy@odata.count", default=None
    )
    oem: dict[str, Any] | None = None


class PowerEquipment(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#PowerEquipment.v1_2_3.PowerEquipment"
    )
    actions: Actions | None = None
    description: str | None = None
    electrical_buses: IdRef | None = None
    floor_pd_us: IdRef | None = Field(serialization_alias="FloorPDUs", default=None)
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    power_shelves: IdRef | None = None
    rack_pd_us: IdRef | None = Field(serialization_alias="RackPDUs", default=None)
    status: Status | None = None
    switchgear: IdRef | None = None
    transfer_switches: IdRef | None = None
