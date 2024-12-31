from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishModel, RedfishResource
from .odata_v4 import IdRef


class DeepOperations(RedfishResource):
    deep_patch: bool | None = None
    deep_post: bool | None = None
    max_levels: int | None = None


class Expand(RedfishResource):
    expand_all: bool | None = None
    levels: bool | None = None
    links: bool | None = None
    max_levels: int | None = None
    no_links: bool | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    sessions: IdRef


class ProtocolFeaturesSupported(RedfishResource):
    deep_operations: DeepOperations | None = None
    excerpt_query: bool | None = None
    expand_query: Expand | None = None
    filter_query: bool | None = None
    only_member_query: bool | None = None
    select_query: bool | None = None


class ServiceRoot(RedfishResource):
    account_service: IdRef | None = None
    aggregation_service: IdRef | None = None
    certificate_service: IdRef | None = None
    chassis: IdRef | None = None
    composition_service: IdRef | None = None
    description: str | None = None
    event_service: IdRef | None = None
    fabrics: IdRef | None = None
    facilities: IdRef | None = None
    job_service: IdRef | None = None
    json_schemas: IdRef | None = None
    links: Links
    managers: IdRef | None = None
    oem: dict[str, Any] | None = None
    power_equipment: IdRef | None = None
    product: str | None = None
    protocol_features_supported: ProtocolFeaturesSupported | None = None
    redfish_version: str | None = None
    registries: IdRef | None = None
    resource_blocks: IdRef | None = None
    session_service: IdRef | None = None
    storage: IdRef | None = None
    storage_services: IdRef | None = None
    storage_systems: IdRef | None = None
    systems: IdRef | None = None
    tasks: IdRef | None = None
    telemetry_service: IdRef | None = None
    uuid: str | None = None
    update_service: IdRef | None = None
    vendor: str | None = None
