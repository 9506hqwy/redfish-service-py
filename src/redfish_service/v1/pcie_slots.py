from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Location, Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class OemActions(RedfishResource):
    pass


class PcieLinks(RedfishResource):
    oem: dict[str, Any] | None = None
    pcie_device: list[IdRef] | None = None
    processors: list[IdRef] | None = None


class PcieSlot(RedfishResource):
    hot_pluggable: str | None = None
    lanes: str | None = None
    links: PcieLinks | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    oem: dict[str, Any] | None = None
    pcie_type: str | None = None
    slot_type: str | None = None
    status: Status | None = None


class PcieSlots(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    slots: list[PcieSlot] | None = None
