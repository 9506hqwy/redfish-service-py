from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import RedfishModel
from .odata_v4 import IdRef


class DeepOperations(RedfishModel):
    deep_patch: bool | None = Field(alias="DeepPATCH", default=None)
    deep_post: bool | None = Field(alias="DeepPOST", default=None)
    max_levels: int | None = None


class Expand(RedfishModel):
    expand_all: bool | None = None
    levels: bool | None = None
    links: bool | None = None
    max_levels: int | None = None
    no_links: bool | None = None


class Links(RedfishModel):
    manager_providing_service: IdRef | None = None
    oem: dict[str, Any] | None = None
    sessions: IdRef


class ProtocolFeaturesSupported(RedfishModel):
    deep_operations: DeepOperations | None = None
    excerpt_query: bool | None = None
    expand_query: Expand | None = None
    filter_query: bool | None = None
    filter_query_comparison_operations: bool | None = None
    filter_query_compound_operations: bool | None = None
    multiple_http_requests: bool | None = Field(alias="MultipleHTTPRequests", default=None)
    only_member_query: bool | None = None
    select_query: bool | None = None
    top_skip_query: bool | None = None


class ServiceRoot(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    account_service: IdRef | None = None
    aggregation_service: IdRef | None = None
    cables: IdRef | None = None
    certificate_service: IdRef | None = None
    chassis: IdRef | None = None
    component_integrity: IdRef | None = None
    composition_service: IdRef | None = None
    description: str | None = None
    event_service: IdRef | None = None
    fabrics: IdRef | None = None
    facilities: IdRef | None = None
    id: str
    job_service: IdRef | None = None
    json_schemas: IdRef | None = None
    key_service: IdRef | None = None
    license_service: IdRef | None = None
    links: Links
    managers: IdRef | None = None
    nvme_domains: IdRef | None = Field(alias="NVMeDomains", default=None)
    name: str
    oem: dict[str, Any] | None = None
    power_equipment: IdRef | None = None
    product: str | None = None
    protocol_features_supported: ProtocolFeaturesSupported | None = None
    redfish_version: str | None = None
    registered_clients: IdRef | None = None
    registries: IdRef | None = None
    resource_blocks: IdRef | None = None
    service_conditions: IdRef | None = None
    service_identification: str | None = None
    session_service: IdRef | None = None
    storage: IdRef | None = None
    storage_services: IdRef | None = None
    storage_systems: IdRef | None = None
    systems: IdRef | None = None
    tasks: IdRef | None = None
    telemetry_service: IdRef | None = None
    thermal_equipment: IdRef | None = None
    uuid: str | None = Field(alias="UUID", default=None)
    update_service: IdRef | None = None
    vendor: str | None = None
