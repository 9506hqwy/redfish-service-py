from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .pcie_device import PcieInterface
from .protocol import Protocol
from .resource import Identifier, Location, Status
from .software_inventory import MeasurementBlock


class Actions(RedfishModel):
    attach_namespaces: AttachNamespaces | None = Field(
        alias="#StorageController.AttachNamespaces", default=None
    )
    detach_namespaces: DetachNamespaces | None = Field(
        alias="#StorageController.DetachNamespaces", default=None
    )
    security_receive: SecurityReceive | None = Field(
        alias="#StorageController.SecurityReceive", default=None
    )
    security_send: SecuritySend | None = Field(
        alias="#StorageController.SecuritySend", default=None
    )
    oem: dict[str, Any] | None = None


class AttachNamespaces(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class CacheSummary(RedfishModel):
    persistent_cache_size_mi_b: str | None = None
    status: Status | None = None
    total_cache_size_mi_b: str


class DetachNamespaces(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Links(RedfishModel):
    attached_volumes: list[IdRef] | None = None
    attached_volumes_odata_count: int | None = Field(
        alias="AttachedVolumes@odata.count", default=None
    )
    batteries: list[IdRef] | None = None
    batteries_odata_count: int | None = Field(alias="Batteries@odata.count", default=None)
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    nvme_discovered_subsystems: list[IdRef] | None = Field(
        alias="NVMeDiscoveredSubsystems", default=None
    )
    nvme_discovered_subsystems_odata_count: int | None = Field(
        alias="NVMeDiscoveredSubsystems@odata.count", default=None
    )
    network_device_functions: list[IdRef] | None = None
    network_device_functions_odata_count: int | None = Field(
        alias="NetworkDeviceFunctions@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = Field(alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(alias="PCIeFunctions@odata.count", default=None)


class NvmeControllerProperties(RedfishModel):
    anacharacteristics: list[str] | None = Field(alias="ANACharacteristics", default=None)
    allocated_completion_queues: str | None = None
    allocated_submission_queues: str | None = None
    controller_type: str | None = None
    max_attached_namespaces: str | None = None
    max_queue_size: str | None = None
    nvme_controller_attributes: str | None = Field(alias="NVMeControllerAttributes", default=None)
    nvme_smartcritical_warnings: str | None = Field(
        alias="NVMeSMARTCriticalWarnings", default=None
    )
    nvme_version: str | None = Field(alias="NVMeVersion", default=None)


class NvmeSmartcriticalWarnings(RedfishModel):
    media_in_read_only: str | None = None
    overall_subsystem_degraded: str | None = None
    pmrunreliable: str | None = Field(alias="PMRUnreliable", default=None)
    power_backup_failed: str | None = None
    spare_capacity_worn_out: str | None = None


class Rates(RedfishModel):
    consistency_check_rate_percent: str | None = None
    rebuild_rate_percent: str | None = None
    transformation_rate_percent: str | None = None


class SecurityReceive(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SecuritySend(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class StorageController(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    cache_summary: CacheSummary | None = None
    certificates: IdRef | None = None
    controller_rates: Rates | None = None
    description: str | None = None
    environment_metrics: IdRef | None = None
    firmware_version: str | None = None
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    location: Location | None = None
    manufacturer: str | None = None
    measurements: list[MeasurementBlock] | None = None
    metrics: str | None = None
    model: str | None = None
    nvme_controller_properties: NvmeControllerProperties | None = Field(
        alias="NVMeControllerProperties", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_interface: PcieInterface | None = Field(alias="PCIeInterface", default=None)
    part_number: str | None = None
    ports: IdRef | None = None
    sku: str | None = Field(alias="SKU", default=None)
    serial_number: str | None = None
    speed_gbps: str | None = None
    status: Status | None = None
    supported_controller_protocols: list[Protocol] | None = None
    supported_device_protocols: list[Protocol] | None = None
    supported_raidtypes: list[str] | None = Field(alias="SupportedRAIDTypes", default=None)
