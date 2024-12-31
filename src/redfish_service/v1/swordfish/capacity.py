from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import RedfishResource
from ..odata_v4 import IdRef


class Actions(RedfishResource):
    oem: OemActions | None = None


class Capacity(RedfishResource):
    data: CapacityInfo | None = None
    is_thin_provisioned: str | None = None
    metadata: CapacityInfo | None = None
    snapshot: CapacityInfo | None = None


class CapacityInfo(RedfishResource):
    allocated_bytes: str | None = None
    consumed_bytes: str | None = None
    guaranteed_bytes: str | None = None
    provisioned_bytes: str | None = None


class CapacitySource(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    provided_capacity: Capacity | None = None
    provided_class_of_service: IdRef | None = None
    providing_drives: IdRef | None = None
    providing_memory: IdRef | None = None
    providing_memory_chunks: IdRef | None = None
    providing_pools: IdRef | None = None
    providing_volumes: IdRef | None = None


class OemActions(RedfishResource):
    pass
