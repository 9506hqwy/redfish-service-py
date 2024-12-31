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
    oem: dict[str, Any] | None = None
    pcie_device: IdRef | None = None
    processors: list[IdRef] | None = None


class Usbcontroller(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    links: Links | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    ports: IdRef | None = None
    sku: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
