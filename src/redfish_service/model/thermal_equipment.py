from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .redundancy import RedundantGroup
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ThermalEquipment(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#ThermalEquipment.v1_1_2.ThermalEquipment"
    )
    actions: Actions | None = None
    cdus: IdRef | None = Field(serialization_alias="CDUs", default=None)
    cooling_loop_redundancy: list[RedundantGroup] | None = None
    cooling_loops: IdRef | None = None
    description: str | None = None
    heat_exchangers: IdRef | None = None
    id: str
    immersion_units: IdRef | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None
