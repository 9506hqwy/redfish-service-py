from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class Links(RedfishResource):
    electrical_buses: list[IdRef] | None = None
    floor_pdus: list[IdRef] | None = None
    managed_by: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    power_shelves: list[IdRef] | None = None
    rack_pdus: list[IdRef] | None = None
    switchgear: list[IdRef] | None = None
    transfer_switches: list[IdRef] | None = None


class OemActions(RedfishResource):
    pass


class PowerDomain(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
