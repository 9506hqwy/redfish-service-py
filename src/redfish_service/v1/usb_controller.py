from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    pcie_device: IdRef | None = Field(alias="PCIeDevice", default=None)
    processors: list[IdRef] | None = None
    processors_odata_count: int | None = Field(alias="Processors@odata.count", default=None)


class UsbController(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    description: str | None = None
    id: str
    links: Links | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    ports: IdRef | None = None
    sku: str | None = Field(alias="SKU", default=None)
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
