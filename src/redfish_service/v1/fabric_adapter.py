from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .pcie_device import PcieInterface
from .protocol import Protocol
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class FabricAdapter(RedfishResource):
    asicmanufacturer: str | None = Field(alias="ASICManufacturer", default=None)
    asicpart_number: str | None = Field(alias="ASICPartNumber", default=None)
    asicrevision_identifier: str | None = Field(alias="ASICRevisionIdentifier", default=None)
    actions: Actions | None = None
    description: str | None = None
    fabric_type: Protocol | None = None
    fabric_type_capabilities: list[Protocol] | None = None
    firmware_version: str | None = None
    gen_z: GenZ | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    pcie_interface: PcieInterface | None = Field(alias="PCIeInterface", default=None)
    part_number: str | None = None
    ports: IdRef | None = None
    sku: str | None = Field(alias="SKU", default=None)
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    uuid: str | None = Field(alias="UUID", default=None)


class GenZ(RedfishModel):
    msdt: IdRef | None = Field(alias="MSDT", default=None)
    pidt: list[str] | None = Field(alias="PIDT", default=None)
    ritable: list[str] | None = Field(alias="RITable", default=None)
    requestor_vcat: IdRef | None = Field(alias="RequestorVCAT", default=None)
    responder_vcat: IdRef | None = Field(alias="ResponderVCAT", default=None)
    ssdt: IdRef | None = Field(alias="SSDT", default=None)


class Links(RedfishModel):
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    memory_domains: list[IdRef] | None = None
    memory_domains_odata_count: int | None = Field(alias="MemoryDomains@odata.count", default=None)
    oem: dict[str, Any] | None = None
    pcie_devices: list[IdRef] | None = Field(alias="PCIeDevices", default=None)
    pcie_devices_odata_count: int | None = Field(alias="PCIeDevices@odata.count", default=None)
    processors: list[IdRef] | None = None
    processors_odata_count: int | None = Field(alias="Processors@odata.count", default=None)
