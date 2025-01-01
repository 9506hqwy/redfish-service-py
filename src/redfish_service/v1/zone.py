from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Identifier, Status


class Actions(RedfishModel):
    add_endpoint: AddEndpoint | None = Field(alias="#Zone.AddEndpoint", default=None)
    remove_endpoint: RemoveEndpoint | None = Field(alias="#Zone.RemoveEndpoint", default=None)
    oem: dict[str, Any] | None = None


class AddEndpoint(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Links(RedfishModel):
    address_pools: list[IdRef] | None = None
    address_pools_odata_count: int | None = Field(alias="AddressPools@odata.count", default=None)
    contained_by_zones: list[IdRef] | None = None
    contained_by_zones_odata_count: int | None = Field(
        alias="ContainedByZones@odata.count", default=None
    )
    contains_zones: list[IdRef] | None = None
    contains_zones_odata_count: int | None = Field(alias="ContainsZones@odata.count", default=None)
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    involved_switches: list[IdRef] | None = None
    involved_switches_odata_count: int | None = Field(
        alias="InvolvedSwitches@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    resource_blocks: list[IdRef] | None = None
    resource_blocks_odata_count: int | None = Field(
        alias="ResourceBlocks@odata.count", default=None
    )


class RemoveEndpoint(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


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
