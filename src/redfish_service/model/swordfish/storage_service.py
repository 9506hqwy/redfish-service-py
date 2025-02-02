from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel, RedfishModelOnUpdate
from ..odata_v4 import IdRef
from ..resource import Identifier, Status
from ..swordfish.io_statistics import IoStatistics


class Actions(RedfishModel):
    set_encryption_key: SetEncryptionKey | None = Field(
        serialization_alias="#StorageService.SetEncryptionKey", default=None
    )
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    data_protection_los_capabilities: IdRef | None = Field(
        serialization_alias="DataProtectionLoSCapabilities", default=None
    )
    data_security_los_capabilities: IdRef | None = Field(
        serialization_alias="DataSecurityLoSCapabilities", default=None
    )
    data_storage_los_capabilities: IdRef | None = Field(
        serialization_alias="DataStorageLoSCapabilities", default=None
    )
    default_class_of_service: IdRef | None = None
    hosting_system: IdRef | None = None
    io_connectivity_los_capabilities: IdRef | None = Field(
        serialization_alias="IOConnectivityLoSCapabilities", default=None
    )
    io_performance_los_capabilities: IdRef | None = Field(
        serialization_alias="IOPerformanceLoSCapabilities", default=None
    )
    oem: dict[str, Any] | None = None


class SetEncryptionKey(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SetEncryptionKeyRequest(RedfishModel):
    encryption_key: str | None = None


class StorageService(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#StorageService.v1_7_0.StorageService"
    )
    actions: Actions | None = None
    classes_of_service: IdRef | None = None
    client_endpoint_groups: IdRef | None = None
    connections: IdRef | None = None
    consistency_groups: IdRef | None = None
    data_protection_los_capabilities: IdRef | None = Field(
        serialization_alias="DataProtectionLoSCapabilities", default=None
    )
    data_security_los_capabilities: IdRef | None = Field(
        serialization_alias="DataSecurityLoSCapabilities", default=None
    )
    data_storage_los_capabilities: IdRef | None = Field(
        serialization_alias="DataStorageLoSCapabilities", default=None
    )
    default_class_of_service: IdRef | None = None
    description: str | None = None
    drives: IdRef | None = None
    endpoint_groups: IdRef | None = None
    endpoints: IdRef | None = None
    file_systems: IdRef | None = None
    io_connectivity_los_capabilities: IdRef | None = Field(
        serialization_alias="IOConnectivityLoSCapabilities", default=None
    )
    io_performance_los_capabilities: IdRef | None = Field(
        serialization_alias="IOPerformanceLoSCapabilities", default=None
    )
    io_statistics: IoStatistics | None = Field(serialization_alias="IOStatistics", default=None)
    id: str
    identifier: Identifier | None = None
    lines_of_service: list[IdRef] | None = None
    lines_of_service_odata_count: int | None = Field(
        serialization_alias="LinesOfService@odata.count", default=None
    )
    links: Links | None = None
    metrics: IdRef | None = None
    name: str
    oem: dict[str, Any] | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(
        serialization_alias="Redundancy@odata.count", default=None
    )
    server_endpoint_groups: IdRef | None = None
    spare_resource_sets: list[IdRef] | None = None
    spare_resource_sets_odata_count: int | None = Field(
        serialization_alias="SpareResourceSets@odata.count", default=None
    )
    status: Status | None = None
    storage_groups: IdRef | None = None
    storage_pools: IdRef | None = None
    storage_subsystems: list[IdRef] | None = None
    storage_subsystems_odata_count: int | None = Field(
        serialization_alias="StorageSubsystems@odata.count", default=None
    )
    volumes: IdRef | None = None


class StorageServiceOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#StorageService.v1_7_0.StorageService"
    )
    actions: Actions | None = None
    classes_of_service: IdRef | None = None
    client_endpoint_groups: IdRef | None = None
    connections: IdRef | None = None
    consistency_groups: IdRef | None = None
    data_protection_los_capabilities: IdRef | None = Field(
        serialization_alias="DataProtectionLoSCapabilities", default=None
    )
    data_security_los_capabilities: IdRef | None = Field(
        serialization_alias="DataSecurityLoSCapabilities", default=None
    )
    data_storage_los_capabilities: IdRef | None = Field(
        serialization_alias="DataStorageLoSCapabilities", default=None
    )
    default_class_of_service: IdRef | None = None
    description: str | None = None
    drives: IdRef | None = None
    endpoint_groups: IdRef | None = None
    endpoints: IdRef | None = None
    file_systems: IdRef | None = None
    io_connectivity_los_capabilities: IdRef | None = Field(
        serialization_alias="IOConnectivityLoSCapabilities", default=None
    )
    io_performance_los_capabilities: IdRef | None = Field(
        serialization_alias="IOPerformanceLoSCapabilities", default=None
    )
    io_statistics: IoStatistics | None = Field(serialization_alias="IOStatistics", default=None)
    id: str | None = None
    identifier: Identifier | None = None
    lines_of_service: list[IdRef] | None = None
    lines_of_service_odata_count: int | None = Field(
        serialization_alias="LinesOfService@odata.count", default=None
    )
    links: Links | None = None
    metrics: IdRef | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(
        serialization_alias="Redundancy@odata.count", default=None
    )
    server_endpoint_groups: IdRef | None = None
    spare_resource_sets: list[IdRef] | None = None
    spare_resource_sets_odata_count: int | None = Field(
        serialization_alias="SpareResourceSets@odata.count", default=None
    )
    status: Status | None = None
    storage_groups: IdRef | None = None
    storage_pools: IdRef | None = None
    storage_subsystems: list[IdRef] | None = None
    storage_subsystems_odata_count: int | None = Field(
        serialization_alias="StorageSubsystems@odata.count", default=None
    )
    volumes: IdRef | None = None


class StorageServiceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    classes_of_service: IdRef | None = None
    client_endpoint_groups: IdRef | None = None
    consistency_groups: IdRef | None = None
    data_protection_los_capabilities: IdRef | None = Field(
        serialization_alias="DataProtectionLoSCapabilities", default=None
    )
    data_security_los_capabilities: IdRef | None = Field(
        serialization_alias="DataSecurityLoSCapabilities", default=None
    )
    data_storage_los_capabilities: IdRef | None = Field(
        serialization_alias="DataStorageLoSCapabilities", default=None
    )
    default_class_of_service: IdRef | None = None
    endpoint_groups: IdRef | None = None
    file_systems: IdRef | None = None
    io_connectivity_los_capabilities: IdRef | None = Field(
        serialization_alias="IOConnectivityLoSCapabilities", default=None
    )
    io_performance_los_capabilities: IdRef | None = Field(
        serialization_alias="IOPerformanceLoSCapabilities", default=None
    )
    io_statistics: IoStatistics | None = Field(serialization_alias="IOStatistics", default=None)
    identifier: Identifier | None = None
    lines_of_service: list[IdRef] | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    server_endpoint_groups: IdRef | None = None
    spare_resource_sets: list[IdRef] | None = None
    status: Status | None = None
    volumes: IdRef | None = None
