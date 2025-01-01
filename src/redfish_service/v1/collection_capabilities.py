from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
)
from .odata_v4 import IdRef


class Capability(RedfishModel):
    capabilities_object: IdRef
    links: Links
    use_case: UseCase


class CollectionCapabilities(RedfishModel):
    capabilities: list[Capability] | None = None
    max_members: int | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(alias="RelatedItem@odata.count", default=None)
    target_collection: IdRef


class UseCase(StrEnum):
    COMPUTER_SYSTEM_COMPOSITION = "ComputerSystemComposition"
    COMPUTER_SYSTEM_CONSTRAINED_COMPOSITION = "ComputerSystemConstrainedComposition"
    VOLUME_CREATION = "VolumeCreation"
    RESOURCE_BLOCK_COMPOSITION = "ResourceBlockComposition"
    RESOURCE_BLOCK_CONSTRAINED_COMPOSITION = "ResourceBlockConstrainedComposition"
    REGISTER_RESOURCE_BLOCK = "RegisterResourceBlock"
