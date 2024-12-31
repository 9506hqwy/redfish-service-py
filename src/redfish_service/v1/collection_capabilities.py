from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef


class Capability(RedfishResource):
    capabilities_object: IdRef
    links: Links
    use_case: UseCase


class CollectionCapabilities(RedfishResource):
    capabilities: list[Capability] | None = None
    max_members: int | None = None


class Links(RedfishResource):
    oem: dict[str, Any] | None = None
    related_item: list[IdRef] | None = None
    target_collection: IdRef


class UseCase(StrEnum):
    COMPUTER_SYSTEM_COMPOSITION = "ComputerSystemComposition"
    COMPUTER_SYSTEM_CONSTRAINED_COMPOSITION = "ComputerSystemConstrainedComposition"
    VOLUME_CREATION = "VolumeCreation"
    RESOURCE_BLOCK_COMPOSITION = "ResourceBlockComposition"
    RESOURCE_BLOCK_CONSTRAINED_COMPOSITION = "ResourceBlockConstrainedComposition"
    REGISTER_RESOURCE_BLOCK = "RegisterResourceBlock"
