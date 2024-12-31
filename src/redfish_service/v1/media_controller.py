from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    endpoints: list[IdRef] | None = None
    memory_domains: list[IdRef] | None = None
    oem: dict[str, Any] | None = None


class MediaController(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    environment_metrics: IdRef | None = None
    links: Links | None = None
    manufacturer: str | None = None
    media_controller_type: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    ports: IdRef | None = None
    serial_number: str | None = None
    status: Status | None = None
    uuid: str | None = None


class Reset(RedfishModel):
    target: str | None = None
    title: str | None = None
