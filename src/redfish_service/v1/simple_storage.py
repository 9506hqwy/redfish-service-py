from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class Device(RedfishResource):
    capacity_bytes: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class Links(RedfishResource):
    chassis: IdRef | None = None
    oem: dict[str, Any] | None = None
    storage: IdRef | None = None


class OemActions(RedfishResource):
    pass


class SimpleStorage(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    devices: list[Device] | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    uefi_device_path: str | None = None
