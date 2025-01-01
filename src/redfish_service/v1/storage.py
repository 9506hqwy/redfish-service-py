from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishObjectId,
    RedfishResource,
)
from .odata_v4 import IdRef
from .pcie_device import PcieInterface
from .protocol import Protocol
from .resource import Identifier, Location, Status


class Actions(RedfishModel):
    set_encryption_key: SetEncryptionKey | None = Field(
        alias="#Storage.SetEncryptionKey", default=None
    )
    oem: dict[str, Any] | None = None


class CacheSummary(RedfishModel):
    persistent_cache_size_mi_b: str | None = None
    status: Status | None = None
    total_cache_size_mi_b: str


class Links(RedfishModel):
    enclosures: list[IdRef] | None = None
    enclosures_odata_count: int | None = Field(alias="Enclosures@odata.count", default=None)
    oem: dict[str, Any] | None = None
    simple_storage: IdRef | None = None
    storage_services: list[IdRef] | None = None
    storage_services_odata_count: int | None = Field(
        alias="StorageServices@odata.count", default=None
    )


class Rates(RedfishModel):
    consistency_check_rate_percent: str | None = None
    rebuild_rate_percent: str | None = None
    transformation_rate_percent: str | None = None


class SetEncryptionKey(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Storage(RedfishResource):
    actions: Actions | None = None
    consistency_groups: IdRef | None = None
    controllers: IdRef | None = None
    description: str | None = None
    drives: list[IdRef] | None = None
    drives_odata_count: int | None = Field(alias="Drives@odata.count", default=None)
    endpoint_groups: IdRef | None = None
    file_systems: IdRef | None = None
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(alias="Redundancy@odata.count", default=None)
    status: Status | None = None
    storage_controllers: list[StorageController] | None = None
    storage_controllers_odata_count: int | None = Field(
        alias="StorageControllers@odata.count", default=None
    )
    storage_groups: IdRef | None = None
    storage_pools: IdRef | None = None
    volumes: IdRef | None = None


class StorageController(RedfishObjectId):
    actions: StorageControllerActions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    cache_summary: CacheSummary | None = None
    controller_rates: Rates | None = None
    firmware_version: str | None = None
    identifiers: list[Identifier] | None = None
    links: StorageControllerLinks | None = None
    location: Location | None = None
    manufacturer: str | None = None
    member_id: str
    model: str | None = None
    name: str | None = None
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


class StorageControllerActions(RedfishModel):
    oem: dict[str, Any] | None = None


class StorageControllerLinks(RedfishModel):
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = Field(alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(alias="PCIeFunctions@odata.count", default=None)
    storage_services: list[IdRef] | None = None
    storage_services_odata_count: int | None = Field(
        alias="StorageServices@odata.count", default=None
    )
