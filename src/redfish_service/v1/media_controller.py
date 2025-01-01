from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#MediaController.Reset", default=None)
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    memory_domains: list[IdRef] | None = None
    memory_domains_odata_count: int | None = Field(alias="MemoryDomains@odata.count", default=None)
    oem: dict[str, Any] | None = None


class MediaController(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    environment_metrics: IdRef | None = None
    links: Links | None = None
    manufacturer: str | None = None
    media_controller_type: MediaControllerType | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    ports: IdRef | None = None
    serial_number: str | None = None
    status: Status | None = None
    uuid: str | None = Field(alias="UUID", default=None)


class MediaControllerType(StrEnum):
    MEMORY = "Memory"


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
