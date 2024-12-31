from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CompositionStatus(RedfishModel):
    composition_state: str
    max_compositions: str | None = None
    number_of_compositions: str | None = None
    reserved: str | None = None
    sharing_capable: str | None = None
    sharing_enabled: str | None = None


class Links(RedfishModel):
    chassis: list[IdRef] | None = None
    computer_systems: list[IdRef] | None = None
    consuming_resource_blocks: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    supplying_resource_blocks: list[IdRef] | None = None
    zones: list[IdRef] | None = None


class ResourceBlock(RedfishResource):
    actions: Actions | None = None
    client: str | None = None
    composition_status: CompositionStatus
    computer_systems: list[IdRef] | None = None
    description: str | None = None
    drives: list[IdRef] | None = None
    ethernet_interfaces: list[IdRef] | None = None
    links: Links | None = None
    memory: list[IdRef] | None = None
    network_interfaces: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    pool: str | None = None
    processors: list[IdRef] | None = None
    resource_block_type: list[ResourceBlockType]
    simple_storage: list[IdRef] | None = None
    status: Status | None = None
    storage: list[IdRef] | None = None


class ResourceBlockLimits(RedfishModel):
    max_compute: str | None = None
    max_computer_system: str | None = None
    max_expansion: str | None = None
    max_memory: str | None = None
    max_network: str | None = None
    max_processor: str | None = None
    max_storage: str | None = None
    min_compute: str | None = None
    min_computer_system: str | None = None
    min_expansion: str | None = None
    min_memory: str | None = None
    min_network: str | None = None
    min_processor: str | None = None
    min_storage: str | None = None


class ResourceBlockType(StrEnum):
    COMPUTE = "Compute"
    PROCESSOR = "Processor"
    MEMORY = "Memory"
    NETWORK = "Network"
    STORAGE = "Storage"
    COMPUTER_SYSTEM = "ComputerSystem"
    EXPANSION = "Expansion"
    INDEPENDENT_RESOURCE = "IndependentResource"
