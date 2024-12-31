from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class GraphicsController(RedfishResource):
    actions: Actions | None = None
    asset_tag: str | None = None
    bios_version: str | None = None
    description: str | None = None
    driver_version: str | None = None
    links: Links | None = None
    location: Location | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    ports: IdRef | None = None
    sku: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    pcie_device: IdRef | None = None
    processors: list[IdRef] | None = None
