from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .physical_context import PhysicalContext
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Assembly(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Assembly.v1_6_0.Assembly")
    actions: Actions | None = None
    assemblies: list[AssemblyData] | None = None
    assemblies_odata_count: int | None = Field(
        serialization_alias="Assemblies@odata.count", default=None
    )
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None


class AssemblyOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    assemblies: list[AssemblyData] | None = None
    oem: dict[str, Any] | None = None


class AssemblyData(RedfishModel):
    odata_id: str = Field(serialization_alias="@odata.id")
    actions: AssemblyDataActions | None = None
    binary_data_uri: str | None = Field(serialization_alias="BinaryDataURI", default=None)
    description: str | None = None
    engineering_change_level: str | None = None
    iso_country_code_of_origin: str | None = Field(
        serialization_alias="ISOCountryCodeOfOrigin", default=None
    )
    location: Location | None = None
    location_indicator_active: bool | None = None
    member_id: str
    model: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    physical_context: PhysicalContext | None = None
    producer: str | None = None
    production_date: str | None = None
    ready_to_remove: bool | None = None
    replaceable: bool | None = None
    sku: str | None = Field(serialization_alias="SKU", default=None)
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    vendor: str | None = None
    version: str | None = None


class AssemblyDataActions(RedfishModel):
    oem: dict[str, Any] | None = None
