from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .pcie_device import PcieInterface
from .protocol import Protocol
from .resource import Identifier, Location, Status
from .software_inventory import MeasurementBlock
from .swordfish.volume import RaidType


class AnaAccessState(StrEnum):
    OPTIMIZED = "Optimized"
    NON_OPTIMIZED = "NonOptimized"
    INACCESSIBLE = "Inaccessible"
    PERSISTENT_LOSS = "PersistentLoss"


class AnaCharacteristics(RedfishModel):
    access_state: AnaAccessState | None = None
    volume: IdRef | None = None


class Actions(RedfishModel):
    attach_namespaces: AttachNamespaces | None = Field(
        serialization_alias="#StorageController.AttachNamespaces", default=None
    )
    detach_namespaces: DetachNamespaces | None = Field(
        serialization_alias="#StorageController.DetachNamespaces", default=None
    )
    security_receive: SecurityReceive | None = Field(
        serialization_alias="#StorageController.SecurityReceive", default=None
    )
    security_send: SecuritySend | None = Field(
        serialization_alias="#StorageController.SecuritySend", default=None
    )
    oem: dict[str, Any] | None = None


class AttachNamespaces(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class AttachNamespacesRequest(RedfishModel):
    namespaces: list[IdRef]


class CacheSummary(RedfishModel):
    persistent_cache_size_mib: int | None = Field(
        serialization_alias="PersistentCacheSizeMiB", default=None
    )
    status: Status | None = None
    total_cache_size_mib: int | None = Field(serialization_alias="TotalCacheSizeMiB", default=None)


class DetachNamespaces(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class DetachNamespacesRequest(RedfishModel):
    namespaces: list[IdRef]


class Links(RedfishModel):
    attached_volumes: list[IdRef] | None = None
    attached_volumes_odata_count: int | None = Field(
        serialization_alias="AttachedVolumes@odata.count", default=None
    )
    batteries: list[IdRef] | None = None
    batteries_odata_count: int | None = Field(
        serialization_alias="Batteries@odata.count", default=None
    )
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(
        serialization_alias="Endpoints@odata.count", default=None
    )
    nvme_discovered_subsystems: list[IdRef] | None = Field(
        serialization_alias="NVMeDiscoveredSubsystems", default=None
    )
    nvme_discovered_subsystems_odata_count: int | None = Field(
        serialization_alias="NVMeDiscoveredSubsystems@odata.count", default=None
    )
    network_device_functions: list[IdRef] | None = None
    network_device_functions_odata_count: int | None = Field(
        serialization_alias="NetworkDeviceFunctions@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = Field(serialization_alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(
        serialization_alias="PCIeFunctions@odata.count", default=None
    )


class NvmeControllerAttributes(RedfishModel):
    reports_namespace_granularity: bool | None = None
    reports_uuid_list: bool | None = Field(serialization_alias="ReportsUUIDList", default=None)
    supports128_bit_host_id: bool | None = None
    supports_endurance_groups: bool | None = None
    supports_exceeding_power_of_non_operational_state: bool | None = None
    supports_nvm_sets: bool | None = Field(serialization_alias="SupportsNVMSets", default=None)
    supports_predictable_latency_mode: bool | None = None
    supports_read_recovery_levels: bool | None = None
    supports_reservations: bool | None = None
    supports_sq_associations: bool | None = Field(
        serialization_alias="SupportsSQAssociations", default=None
    )
    supports_traffic_based_keep_alive: bool | None = None


class NvmeControllerProperties(RedfishModel):
    ana_characteristics: list[AnaCharacteristics] | None = Field(
        serialization_alias="ANACharacteristics", default=None
    )
    allocated_completion_queues: int | None = None
    allocated_submission_queues: int | None = None
    controller_type: NvmeControllerType | None = None
    max_attached_namespaces: int | None = None
    max_queue_size: int | None = None
    nvme_controller_attributes: NvmeControllerAttributes | None = Field(
        serialization_alias="NVMeControllerAttributes", default=None
    )
    nvme_smart_critical_warnings: NvmeSmartCriticalWarnings | None = Field(
        serialization_alias="NVMeSMARTCriticalWarnings", default=None
    )
    nvme_version: str | None = Field(serialization_alias="NVMeVersion", default=None)


class NvmeControllerType(StrEnum):
    ADMIN = "Admin"
    DISCOVERY = "Discovery"
    IO = "IO"


class NvmeSmartCriticalWarnings(RedfishModel):
    media_in_read_only: bool | None = None
    overall_subsystem_degraded: bool | None = None
    pmr_unreliable: bool | None = Field(serialization_alias="PMRUnreliable", default=None)
    power_backup_failed: bool | None = None
    spare_capacity_worn_out: bool | None = None


class Rates(RedfishModel):
    consistency_check_rate_percent: int | None = None
    rebuild_rate_percent: int | None = None
    transformation_rate_percent: int | None = None


class SecurityReceive(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SecurityReceiveRequest(RedfishModel):
    allocation_length: int
    security_protocol: int
    security_protocol_specific: int


class SecuritySend(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SecuritySendRequest(RedfishModel):
    data: str
    security_protocol: int
    security_protocol_specific: int


class StorageController(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#StorageController.v1_8_0.StorageController"
    )
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    cache_summary: CacheSummary | None = None
    certificates: IdRef | None = None
    controller_rates: Rates | None = None
    description: str | None = None
    environment_metrics: IdRef | None = None
    firmware_version: str | None = None
    id: str
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    location: Location | None = None
    manufacturer: str | None = None
    measurements: list[MeasurementBlock] | None = None
    metrics: IdRef | None = None
    model: str | None = None
    nvme_controller_properties: NvmeControllerProperties | None = Field(
        serialization_alias="NVMeControllerProperties", default=None
    )
    name: str
    oem: dict[str, Any] | None = None
    pcie_interface: PcieInterface | None = Field(serialization_alias="PCIeInterface", default=None)
    part_number: str | None = None
    ports: IdRef | None = None
    sku: str | None = Field(serialization_alias="SKU", default=None)
    serial_number: str | None = None
    speed_gbps: float | None = None
    status: Status | None = None
    supported_controller_protocols: list[Protocol] | None = None
    supported_device_protocols: list[Protocol] | None = None
    supported_raid_types: list[RaidType] | None = Field(
        serialization_alias="SupportedRAIDTypes", default=None
    )


class StorageControllerOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    asset_tag: str | None = None
    cache_summary: CacheSummary | None = None
    controller_rates: Rates | None = None
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    location: Location | None = None
    measurements: list[MeasurementBlock] | None = None
    nvme_controller_properties: NvmeControllerProperties | None = Field(
        serialization_alias="NVMeControllerProperties", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_interface: PcieInterface | None = Field(serialization_alias="PCIeInterface", default=None)
    status: Status | None = None
