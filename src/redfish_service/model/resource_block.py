from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CompositionState(StrEnum):
    COMPOSING = "Composing"
    COMPOSED_AND_AVAILABLE = "ComposedAndAvailable"
    COMPOSED = "Composed"
    UNUSED = "Unused"
    FAILED = "Failed"
    UNAVAILABLE = "Unavailable"


class CompositionStatus(RedfishModel):
    composition_state: CompositionState | None = None
    max_compositions: int | None = None
    number_of_compositions: int | None = None
    reserved: bool | None = None
    sharing_capable: bool | None = None
    sharing_enabled: bool | None = None


class Links(RedfishModel):
    chassis: list[IdRef] | None = None
    chassis_odata_count: int | None = Field(
        serialization_alias="Chassis@odata.count", default=None
    )
    computer_systems: list[IdRef] | None = None
    computer_systems_odata_count: int | None = Field(
        serialization_alias="ComputerSystems@odata.count", default=None
    )
    consuming_resource_blocks: list[IdRef] | None = None
    consuming_resource_blocks_odata_count: int | None = Field(
        serialization_alias="ConsumingResourceBlocks@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    supplying_resource_blocks: list[IdRef] | None = None
    supplying_resource_blocks_odata_count: int | None = Field(
        serialization_alias="SupplyingResourceBlocks@odata.count", default=None
    )
    zones: list[IdRef] | None = None
    zones_odata_count: int | None = Field(serialization_alias="Zones@odata.count", default=None)


class PoolType(StrEnum):
    FREE = "Free"
    ACTIVE = "Active"
    UNASSIGNED = "Unassigned"


class ResourceBlock(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#ResourceBlock.v1_4_3.ResourceBlock"
    )
    actions: Actions | None = None
    client: str | None = None
    composition_status: CompositionStatus
    computer_systems: list[IdRef] | None = None
    computer_systems_odata_count: int | None = Field(
        serialization_alias="ComputerSystems@odata.count", default=None
    )
    description: str | None = None
    drives: list[IdRef] | None = None
    drives_odata_count: int | None = Field(serialization_alias="Drives@odata.count", default=None)
    ethernet_interfaces: list[IdRef] | None = None
    ethernet_interfaces_odata_count: int | None = Field(
        serialization_alias="EthernetInterfaces@odata.count", default=None
    )
    id: str
    links: Links | None = None
    memory: list[IdRef] | None = None
    memory_odata_count: int | None = Field(serialization_alias="Memory@odata.count", default=None)
    name: str
    network_interfaces: list[IdRef] | None = None
    network_interfaces_odata_count: int | None = Field(
        serialization_alias="NetworkInterfaces@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pool: PoolType | None = None
    processors: list[IdRef] | None = None
    processors_odata_count: int | None = Field(
        serialization_alias="Processors@odata.count", default=None
    )
    resource_block_type: list[ResourceBlockType]
    simple_storage: list[IdRef] | None = None
    simple_storage_odata_count: int | None = Field(
        serialization_alias="SimpleStorage@odata.count", default=None
    )
    status: Status | None = None
    storage: list[IdRef] | None = None
    storage_odata_count: int | None = Field(
        serialization_alias="Storage@odata.count", default=None
    )


class ResourceBlockOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#ResourceBlock.v1_4_3.ResourceBlock"
    )
    actions: Actions | None = None
    client: str | None = None
    composition_status: CompositionStatus | None = None
    computer_systems: list[IdRef] | None = None
    computer_systems_odata_count: int | None = Field(
        serialization_alias="ComputerSystems@odata.count", default=None
    )
    description: str | None = None
    drives: list[IdRef] | None = None
    drives_odata_count: int | None = Field(serialization_alias="Drives@odata.count", default=None)
    ethernet_interfaces: list[IdRef] | None = None
    ethernet_interfaces_odata_count: int | None = Field(
        serialization_alias="EthernetInterfaces@odata.count", default=None
    )
    id: str | None = None
    links: Links | None = None
    memory: list[IdRef] | None = None
    memory_odata_count: int | None = Field(serialization_alias="Memory@odata.count", default=None)
    name: str | None = None
    network_interfaces: list[IdRef] | None = None
    network_interfaces_odata_count: int | None = Field(
        serialization_alias="NetworkInterfaces@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pool: PoolType | None = None
    processors: list[IdRef] | None = None
    processors_odata_count: int | None = Field(
        serialization_alias="Processors@odata.count", default=None
    )
    resource_block_type: list[ResourceBlockType] | None = None
    simple_storage: list[IdRef] | None = None
    simple_storage_odata_count: int | None = Field(
        serialization_alias="SimpleStorage@odata.count", default=None
    )
    status: Status | None = None
    storage: list[IdRef] | None = None
    storage_odata_count: int | None = Field(
        serialization_alias="Storage@odata.count", default=None
    )


class ResourceBlockOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    client: str | None = None
    composition_status: CompositionStatus | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    pool: PoolType | None = None
    status: Status | None = None


class ResourceBlockLimits(RedfishModel):
    max_compute: int | None = None
    max_computer_system: int | None = None
    max_expansion: int | None = None
    max_memory: int | None = None
    max_network: int | None = None
    max_processor: int | None = None
    max_storage: int | None = None
    min_compute: int | None = None
    min_computer_system: int | None = None
    min_expansion: int | None = None
    min_memory: int | None = None
    min_network: int | None = None
    min_processor: int | None = None
    min_storage: int | None = None


class ResourceBlockType(StrEnum):
    COMPUTE = "Compute"
    PROCESSOR = "Processor"
    MEMORY = "Memory"
    NETWORK = "Network"
    STORAGE = "Storage"
    COMPUTER_SYSTEM = "ComputerSystem"
    EXPANSION = "Expansion"
    INDEPENDENT_RESOURCE = "IndependentResource"
