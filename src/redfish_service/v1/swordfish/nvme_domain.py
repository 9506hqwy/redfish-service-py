from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    associated_domains: list[IdRef] | None = None
    oem: dict[str, Any] | None = None


class NvmeDomain(RedfishResource):
    anagroup_id: str | None = None
    actions: Actions | None = None
    available_firmware_images: list[IdRef] | None = None
    description: str | None = None
    domain_contents: str | None = None
    domain_members: list[IdRef] | None = None
    firmware_images: list[IdRef] | None = None
    links: Links | None = None
    max_namespaces_supported_per_controller: str | None = None
    maximum_capacity_per_endurance_group_bytes: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    total_domain_capacity_bytes: str | None = None
    unallocated_domain_capacity_bytes: str | None = None
