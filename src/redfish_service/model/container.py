from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import ResetType, Status


class Actions(RedfishModel):
    reset: Reset | None = Field(serialization_alias="#Container.Reset", default=None)
    oem: dict[str, Any] | None = None


class Container(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#Container.v1_0_1.Container"
    )
    actions: Actions | None = None
    description: str | None = None
    ethernet_interfaces: IdRef | None = None
    id: str
    limits: Limits | None = None
    links: Links | None = None
    mount_points: list[MountPoint] | None = None
    name: str
    oem: dict[str, Any] | None = None
    programmatic_id: str | None = None
    start_time: str | None = None
    status: Status | None = None


class Limits(RedfishModel):
    cpu_count: float | None = Field(serialization_alias="CPUCount", default=None)
    memory_bytes: int | None = None


class Links(RedfishModel):
    container_image: IdRef | None = None
    oem: dict[str, Any] | None = None


class MountPoint(RedfishModel):
    destination: str | None = None
    source: str | None = None


class Reset(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetRequest(RedfishModel):
    reset_type: ResetType | None = None
