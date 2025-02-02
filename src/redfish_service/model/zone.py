from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Identifier, Status


class Actions(RedfishModel):
    add_endpoint: AddEndpoint | None = Field(serialization_alias="#Zone.AddEndpoint", default=None)
    remove_endpoint: RemoveEndpoint | None = Field(
        serialization_alias="#Zone.RemoveEndpoint", default=None
    )
    oem: dict[str, Any] | None = None


class AddEndpoint(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class AddEndpointRequest(RedfishModel):
    endpoint: IdRef
    endpoint_etag: str | None = Field(serialization_alias="EndpointETag", default=None)
    zone_etag: str | None = Field(serialization_alias="ZoneETag", default=None)


class ExternalAccessibility(StrEnum):
    GLOBALLY_ACCESSIBLE = "GloballyAccessible"
    NON_ZONED_ACCESSIBLE = "NonZonedAccessible"
    ZONE_ONLY = "ZoneOnly"
    NO_INTERNAL_ROUTING = "NoInternalRouting"


class Links(RedfishModel):
    address_pools: list[IdRef] | None = None
    address_pools_odata_count: int | None = Field(
        serialization_alias="AddressPools@odata.count", default=None
    )
    contained_by_zones: list[IdRef] | None = None
    contained_by_zones_odata_count: int | None = Field(
        serialization_alias="ContainedByZones@odata.count", default=None
    )
    contains_zones: list[IdRef] | None = None
    contains_zones_odata_count: int | None = Field(
        serialization_alias="ContainsZones@odata.count", default=None
    )
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(
        serialization_alias="Endpoints@odata.count", default=None
    )
    involved_switches: list[IdRef] | None = None
    involved_switches_odata_count: int | None = Field(
        serialization_alias="InvolvedSwitches@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    resource_blocks: list[IdRef] | None = None
    resource_blocks_odata_count: int | None = Field(
        serialization_alias="ResourceBlocks@odata.count", default=None
    )


class RemoveEndpoint(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class RemoveEndpointRequest(RedfishModel):
    endpoint: IdRef
    endpoint_etag: str | None = Field(serialization_alias="EndpointETag", default=None)
    zone_etag: str | None = Field(serialization_alias="ZoneETag", default=None)


class Zone(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Zone.v1_6_3.Zone")
    actions: Actions | None = None
    default_routing_enabled: bool | None = None
    description: str | None = None
    external_accessibility: ExternalAccessibility | None = None
    id: str
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None
    zone_type: ZoneType | None = None


class ZoneOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(serialization_alias="@odata.type", default="#Zone.v1_6_3.Zone")
    actions: Actions | None = None
    default_routing_enabled: bool | None = None
    description: str | None = None
    external_accessibility: ExternalAccessibility | None = None
    id: str | None = None
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    zone_type: ZoneType | None = None


class ZoneOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    default_routing_enabled: bool | None = None
    external_accessibility: ExternalAccessibility | None = None
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    zone_type: ZoneType | None = None


class ZoneType(StrEnum):
    DEFAULT = "Default"
    ZONE_OF_ENDPOINTS = "ZoneOfEndpoints"
    ZONE_OF_ZONES = "ZoneOfZones"
    ZONE_OF_RESOURCE_BLOCKS = "ZoneOfResourceBlocks"
