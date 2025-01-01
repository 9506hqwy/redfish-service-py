from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class FileShare(RedfishResource):
    actions: Actions | None = None
    casupported: str | None = Field(alias="CASupported", default=None)
    default_access_capabilities: list[str] | None = None
    description: str | None = None
    ethernet_interfaces: IdRef | None = None
    execute_support: str | None = None
    file_share_path: str | None = None
    file_share_quota_type: str | None = None
    file_share_remaining_quota_bytes: str | None = None
    file_share_total_quota_bytes: str | None = None
    file_sharing_protocols: list[str] | None = None
    links: Links | None = None
    low_space_warning_threshold_percents: list[str] | None = None
    oem: dict[str, Any] | None = None
    remaining_capacity_percent: str | None = None
    replication_enabled: str | None = None
    root_access: str | None = None
    status: Status | None = None
    write_policy: str | None = None


class Links(RedfishModel):
    class_of_service: IdRef | None = None
    file_system: IdRef | None = None
    oem: dict[str, Any] | None = None
