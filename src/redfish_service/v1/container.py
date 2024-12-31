from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class Container(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    ethernet_interfaces: IdRef | None = None
    limits: Limits | None = None
    links: Links | None = None
    mount_points: list[str] | None = None
    oem: dict[str, Any] | None = None
    programmatic_id: str | None = None
    start_time: str | None = None
    status: Status | None = None


class Limits(RedfishModel):
    cpucount: str | None = None
    memory_bytes: str | None = None


class Links(RedfishModel):
    container_image: IdRef | None = None
    oem: dict[str, Any] | None = None


class OemActions(RedfishModel):
    pass


class Reset(RedfishModel):
    target: str | None = None
    title: str | None = None
