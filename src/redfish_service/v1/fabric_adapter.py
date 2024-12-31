from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .pcie_device import PcieInterface
from .protocol import Protocol
from .resource import Location, Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class FabricAdapter(RedfishResource):
    asicmanufacturer: str | None = None
    asicpart_number: str | None = None
    asicrevision_identifier: str | None = None
    actions: Actions | None = None
    description: str | None = None
    fabric_type: Protocol | None = None
    fabric_type_capabilities: list[Protocol] | None = None
    firmware_version: str | None = None
    gen_z: GenZ | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    pcie_interface: PcieInterface | None = None
    part_number: str | None = None
    ports: IdRef | None = None
    sku: str | None = None
    serial_number: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    uuid: str | None = None


class GenZ(RedfishResource):
    msdt: IdRef | None = None
    pidt: list[str] | None = None
    ritable: list[str] | None = None
    requestor_vcat: IdRef | None = None
    responder_vcat: IdRef | None = None
    ssdt: IdRef | None = None


class Links(RedfishResource):
    endpoints: list[IdRef] | None = None
    memory_domains: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    pcie_devices: list[IdRef] | None = None
    processors: list[IdRef] | None = None


class OemActions(RedfishResource):
    pass
