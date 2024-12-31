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


class Device(RedfishModel):
    capacity_bytes: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None


class Links(RedfishModel):
    chassis: IdRef | None = None
    oem: dict[str, Any] | None = None
    storage: IdRef | None = None


class OemActions(RedfishModel):
    pass


class SimpleStorage(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    devices: list[Device] | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    uefi_device_path: str | None = None
