from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Identifier, Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class AddEndpoint(RedfishResource):
    target: str | None = None
    title: str | None = None


class Links(RedfishResource):
    address_pools: list[IdRef] | None = None
    contained_by_zones: list[IdRef] | None = None
    contains_zones: list[IdRef] | None = None
    endpoints: list[IdRef] | None = None
    involved_switches: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    resource_blocks: list[IdRef] | None = None


class OemActions(RedfishResource):
    pass


class RemoveEndpoint(RedfishResource):
    target: str | None = None
    title: str | None = None


class Zone(RedfishResource):
    actions: Actions | None = None
    default_routing_enabled: str | None = None
    description: str | None = None
    external_accessibility: str | None = None
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    zone_type: str | None = None
