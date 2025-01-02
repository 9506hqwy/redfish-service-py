from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier, Status
from ..swordfish.io_statistics import IoStatistics


class Actions(RedfishModel):
    set_encryption_key: SetEncryptionKey | None = Field(
        alias="#StorageService.SetEncryptionKey", default=None
    )
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    data_protection_los_capabilities: IdRef | None = Field(
        alias="DataProtectionLoSCapabilities", default=None
    )
    data_security_los_capabilities: IdRef | None = Field(
        alias="DataSecurityLoSCapabilities", default=None
    )
    data_storage_los_capabilities: IdRef | None = Field(
        alias="DataStorageLoSCapabilities", default=None
    )
    default_class_of_service: IdRef | None = None
    hosting_system: IdRef | None = None
    io_connectivity_los_capabilities: IdRef | None = Field(
        alias="IOConnectivityLoSCapabilities", default=None
    )
    io_performance_los_capabilities: IdRef | None = Field(
        alias="IOPerformanceLoSCapabilities", default=None
    )
    oem: dict[str, Any] | None = None


class SetEncryptionKey(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class StorageService(RedfishResource):
    actions: Actions | None = None
    classes_of_service: IdRef | None = None
    client_endpoint_groups: IdRef | None = None
    connections: IdRef | None = None
    consistency_groups: IdRef | None = None
    data_protection_los_capabilities: IdRef | None = Field(
        alias="DataProtectionLoSCapabilities", default=None
    )
    data_security_los_capabilities: IdRef | None = Field(
        alias="DataSecurityLoSCapabilities", default=None
    )
    data_storage_los_capabilities: IdRef | None = Field(
        alias="DataStorageLoSCapabilities", default=None
    )
    default_class_of_service: IdRef | None = None
    description: str | None = None
    drives: IdRef | None = None
    endpoint_groups: IdRef | None = None
    endpoints: IdRef | None = None
    file_systems: IdRef | None = None
    io_connectivity_los_capabilities: IdRef | None = Field(
        alias="IOConnectivityLoSCapabilities", default=None
    )
    io_performance_los_capabilities: IdRef | None = Field(
        alias="IOPerformanceLoSCapabilities", default=None
    )
    io_statistics: IoStatistics | None = Field(alias="IOStatistics", default=None)
    identifier: Identifier | None = None
    lines_of_service: list[IdRef] | None = None
    lines_of_service_odata_count: int | None = Field(
        alias="LinesOfService@odata.count", default=None
    )
    links: Links | None = None
    metrics: IdRef | None = None
    oem: dict[str, Any] | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(alias="Redundancy@odata.count", default=None)
    server_endpoint_groups: IdRef | None = None
    spare_resource_sets: list[IdRef] | None = None
    spare_resource_sets_odata_count: int | None = Field(
        alias="SpareResourceSets@odata.count", default=None
    )
    status: Status | None = None
    storage_groups: IdRef | None = None
    storage_pools: IdRef | None = None
    storage_subsystems: list[IdRef] | None = None
    storage_subsystems_odata_count: int | None = Field(
        alias="StorageSubsystems@odata.count", default=None
    )
    volumes: IdRef | None = None
