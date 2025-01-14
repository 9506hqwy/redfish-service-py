from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    electrical_buses: list[IdRef] | None = None
    electrical_buses_odata_count: int | None = Field(
        alias="ElectricalBuses@odata.count", default=None
    )
    floor_pd_us: list[IdRef] | None = Field(alias="FloorPDUs", default=None)
    floor_pd_us_odata_count: int | None = Field(alias="FloorPDUs@odata.count", default=None)
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(alias="ManagedBy@odata.count", default=None)
    oem: dict[str, Any] | None = None
    power_shelves: list[IdRef] | None = None
    power_shelves_odata_count: int | None = Field(alias="PowerShelves@odata.count", default=None)
    rack_pd_us: list[IdRef] | None = Field(alias="RackPDUs", default=None)
    rack_pd_us_odata_count: int | None = Field(alias="RackPDUs@odata.count", default=None)
    switchgear: list[IdRef] | None = None
    switchgear_odata_count: int | None = Field(alias="Switchgear@odata.count", default=None)
    transfer_switches: list[IdRef] | None = None
    transfer_switches_odata_count: int | None = Field(
        alias="TransferSwitches@odata.count", default=None
    )


class PowerDomain(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#PowerDomain.v1_2_2.PowerDomain")
    actions: Actions | None = None
    description: str | None = None
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None


class PowerDomainOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#PowerDomain.v1_2_2.PowerDomain")
    actions: Actions | None = None
    description: str | None = None
    id: str | None = None
    links: Links | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class PowerDomainOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
