from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class Links(RedfishResource):
    oem: dict[str, Any] | None = None
    software_image: IdRef | None = None


class OemActions(RedfishResource):
    pass


class OperatingSystem(RedfishResource):
    actions: Actions | None = None
    applications: IdRef | None = None
    container_engines: list[str] | None = None
    container_images: IdRef | None = None
    containers: IdRef | None = None
    description: str | None = None
    kernel: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    type: str | None = None
    uptime_seconds: str | None = None
    virtual_machine_engines: list[str] | None = None
