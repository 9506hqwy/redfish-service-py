from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel, RedfishModelOnUpdate
from ..odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Capacity(RedfishModel):
    data: CapacityInfo | None = None
    is_thin_provisioned: bool | None = None
    metadata: CapacityInfo | None = None
    snapshot: CapacityInfo | None = None


class CapacityInfo(RedfishModel):
    allocated_bytes: int | None = None
    consumed_bytes: int | None = None
    guaranteed_bytes: int | None = None
    provisioned_bytes: int | None = None


class CapacitySource(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#CapacitySource.v1_2_1.CapacitySource"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    provided_capacity: Capacity | None = None
    provided_class_of_service: IdRef | None = None
    providing_drives: IdRef | None = None
    providing_memory: IdRef | None = None
    providing_memory_chunks: IdRef | None = None
    providing_pools: IdRef | None = None
    providing_volumes: IdRef | None = None


class CapacitySourceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    oem: dict[str, Any] | None = None
    provided_capacity: Capacity | None = None
    provided_class_of_service: IdRef | None = None
    providing_drives: IdRef | None = None
    providing_memory: IdRef | None = None
    providing_memory_chunks: IdRef | None = None
    providing_pools: IdRef | None = None
    providing_volumes: IdRef | None = None
