from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class Application(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    destination_uris: list[str] | None = None
    links: Links | None = None
    metrics_uris: list[str] | None = None
    oem: dict[str, Any] | None = None
    start_time: str | None = None
    status: Status | None = None
    vendor: str | None = None
    version: str | None = None


class Links(RedfishResource):
    oem: dict[str, Any] | None = None
    software_image: IdRef | None = None


class OemActions(RedfishResource):
    pass


class Reset(RedfishResource):
    target: str | None = None
    title: str | None = None
