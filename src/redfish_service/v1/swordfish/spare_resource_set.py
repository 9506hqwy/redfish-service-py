from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Location


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    on_hand_spares: list[IdRef] | None = None
    on_hand_spares_odata_count: int | None = Field(alias="OnHandSpares@odata.count", default=None)
    replacement_spare_sets: list[SpareResourceSet] | None = None
    replacement_spare_sets_odata_count: int | None = Field(
        alias="ReplacementSpareSets@odata.count", default=None
    )


class SpareResourceSet(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    on_hand_location: Location | None = None
    on_line: str | None = None
    resource_type: str | None = None
    time_to_provision: str | None = None
    time_to_replenish: str | None = None
