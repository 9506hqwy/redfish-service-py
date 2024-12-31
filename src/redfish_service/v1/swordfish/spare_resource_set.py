from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import RedfishResource
from ..odata_v4 import IdRef
from ..resource import Location


class Actions(RedfishResource):
    oem: OemActions | None = None


class Links(RedfishResource):
    oem: dict[str, Any] | None = None
    on_hand_spares: list[IdRef] | None = None
    replacement_spare_sets: list[SpareResourceSet] | None = None


class OemActions(RedfishResource):
    pass


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
