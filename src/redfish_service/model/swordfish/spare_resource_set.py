from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel, RedfishModelOnUpdate
from ..odata_v4 import IdRef
from ..resource import Location


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    on_hand_spares: list[IdRef] | None = None
    on_hand_spares_odata_count: int | None = Field(
        serialization_alias="OnHandSpares@odata.count", default=None
    )
    replacement_spare_sets: list[SpareResourceSet] | None = None
    replacement_spare_sets_odata_count: int | None = Field(
        serialization_alias="ReplacementSpareSets@odata.count", default=None
    )


class SpareResourceSet(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#SpareResourceSet.v1_0_2.SpareResourceSet"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    on_hand_location: Location | None = None
    on_line: bool | None = None
    resource_type: str | None = None
    time_to_provision: str | None = None
    time_to_replenish: str | None = None


class SpareResourceSetOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    on_line: bool | None = None
    resource_type: str | None = None
    time_to_provision: str | None = None
    time_to_replenish: str | None = None
