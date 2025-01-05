from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Heater(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#Heater.v1_0_2.Heater")
    actions: Actions | None = None
    assembly: IdRef | None = None
    description: str | None = None
    hot_pluggable: bool | None = None
    id: str
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    metrics: IdRef | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None


class Links(RedfishModel):
    managers: list[IdRef] | None = None
    managers_odata_count: int | None = Field(alias="Managers@odata.count", default=None)
    memory: list[IdRef] | None = None
    memory_odata_count: int | None = Field(alias="Memory@odata.count", default=None)
    network_adapters: list[IdRef] | None = None
    network_adapters_odata_count: int | None = Field(
        alias="NetworkAdapters@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    processors: list[IdRef] | None = None
    processors_odata_count: int | None = Field(alias="Processors@odata.count", default=None)
    storage_controllers: list[IdRef] | None = None
    storage_controllers_odata_count: int | None = Field(
        alias="StorageControllers@odata.count", default=None
    )
