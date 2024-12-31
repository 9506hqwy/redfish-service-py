from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class Links(RedfishResource):
    managed_by: list[IdRef] | None = None
    oem: dict[str, Any] | None = None


class OemActions(RedfishResource):
    pass


class PowerEquipment(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    electrical_buses: IdRef | None = None
    floor_pdus: IdRef | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    power_shelves: IdRef | None = None
    rack_pdus: IdRef | None = None
    status: Status | None = None
    switchgear: IdRef | None = None
    transfer_switches: IdRef | None = None
