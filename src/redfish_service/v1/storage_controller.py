from __future__ import annotations  # PEP563 Forward References

from typing import Any

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
    oem: OemActions | None = None


class AttachNamespaces(RedfishModel):
    target: str | None = None
    title: str | None = None


class CacheSummary(RedfishModel):
    persistent_cache_size_mi_b: str | None = None
    status: Status | None = None
    total_cache_size_mi_b: str


class DetachNamespaces(RedfishModel):
    target: str | None = None
    title: str | None = None


class Links(RedfishModel):
    attached_volumes: list[IdRef] | None = None
    batteries: list[IdRef] | None = None
    endpoints: list[IdRef] | None = None
    nvme_discovered_subsystems: list[IdRef] | None = None
    network_device_functions: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = None


class NvmeControllerProperties(RedfishModel):
    anacharacteristics: list[str] | None = None
    allocated_completion_queues: str | None = None
    allocated_submission_queues: str | None = None
    controller_type: str | None = None
    max_attached_namespaces: str | None = None
    max_queue_size: str | None = None
    nvme_controller_attributes: str | None = None
    nvme_smartcritical_warnings: str | None = None
    nvme_version: str | None = None


class NvmeSmartcriticalWarnings(RedfishModel):
    media_in_read_only: str | None = None
    overall_subsystem_degraded: str | None = None
    pmrunreliable: str | None = None
    power_backup_failed: str | None = None
    spare_capacity_worn_out: str | None = None


class OemActions(RedfishModel):
    pass


class Rates(RedfishModel):
    consistency_check_rate_percent: str | None = None
    rebuild_rate_percent: str | None = None
    transformation_rate_percent: str | None = None


class SecurityReceive(RedfishModel):
    target: str | None = None
    title: str | None = None


class SecuritySend(RedfishModel):
    target: str | None = None
    title: str | None = None


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
    nvme_controller_properties: NvmeControllerProperties | None = None
    oem: dict[str, Any] | None = None
    pcie_interface: PcieInterface | None = None
    part_number: str | None = None
    ports: IdRef | None = None
    sku: str | None = None
    serial_number: str | None = None
    speed_gbps: str | None = None
    status: Status | None = None
    supported_controller_protocols: list[Protocol] | None = None
    supported_device_protocols: list[Protocol] | None = None
    supported_raidtypes: list[str] | None = None
