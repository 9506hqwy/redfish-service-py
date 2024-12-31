from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .ipaddresses import Ipv4Address, Ipv6Address
from .odata_v4 import IdRef
from .protocol import Protocol
from .resource import Identifier, Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class ConnectedEntity(RedfishModel):
    entity_link: IdRef | None = None
    entity_pci_id: PciId | None = None
    entity_role: str | None = None
    entity_type: str | None = None
    gen_z: GenZ | None = None
    identifiers: list[Identifier] | None = None
    oem: dict[str, Any] | None = None
    pci_class_code: str | None = None
    pci_function_number: str | None = None


class Endpoint(RedfishResource):
    actions: Actions | None = None
    connected_entities: list[ConnectedEntity] | None = None
    description: str | None = None
    endpoint_protocol: str | None = None
    host_reservation_memory_bytes: str | None = None
    iptransport_details: list[IptransportDetails] | None = None
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    pci_id: PciId | None = None
    redundancy: list[IdRef] | None = None
    status: Status | None = None


class GenZ(RedfishModel):
    access_key: str | None = None
    gcid: str | None = None
    region_key: str | None = None


class IptransportDetails(RedfishModel):
    ipv4_address: Ipv4Address | None = None
    ipv6_address: Ipv6Address | None = None
    port: int | None = None
    transport_protocol: Protocol | None = None


class Links(RedfishModel):
    address_pools: list[IdRef] | None = None
    connected_ports: list[IdRef] | None = None
    connections: list[IdRef] | None = None
    local_ports: list[IdRef] | None = None
    mutually_exclusive_endpoints: list[IdRef] | None = None
    network_device_function: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    ports: list[IdRef] | None = None
    zones: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass


class PciId(RedfishModel):
    class_code: str | None = None
    device_id: str | None = None
    function_number: str | None = None
    subsystem_id: str | None = None
    subsystem_vendor_id: str | None = None
    vendor_id: str | None = None
