from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class OemActions(RedfishResource):
    pass


class Redundancy(RedfishResource):
    actions: Actions | None = None
    max_num_supported: str | None = None
    member_id: str
    min_num_needed: str
    mode: str
    oem: dict[str, Any] | None = None
    redundancy_enabled: str | None = None
    redundancy_set: list[IdRef]
    status: Status


class RedundantGroup(RedfishResource):
    max_supported_in_group: str | None = None
    min_needed_in_group: str
    redundancy_group: list[IdRef]
    redundancy_type: str
    status: Status
