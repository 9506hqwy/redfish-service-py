from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class GraphicsController(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#GraphicsController.v1_0_2.GraphicsController"
    )
    actions: Actions | None = None
    asset_tag: str | None = None
    bios_version: str | None = None
    description: str | None = None
    driver_version: str | None = None
    id: str
    links: Links | None = None
    location: Location | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    ports: IdRef | None = None
    sku: str | None = Field(serialization_alias="SKU", default=None)
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None


class GraphicsControllerOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    asset_tag: str | None = None
    links: Links | None = None
    location: Location | None = None
    oem: dict[str, Any] | None = None
    ports: IdRef | None = None
    status: Status | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    pcie_device: IdRef | None = Field(serialization_alias="PCIeDevice", default=None)
    processors: list[IdRef] | None = None
    processors_odata_count: int | None = Field(
        serialization_alias="Processors@odata.count", default=None
    )
