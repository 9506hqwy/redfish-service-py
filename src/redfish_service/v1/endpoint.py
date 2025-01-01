from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .ipaddresses import Ipv4Address, Ipv6Address
from .odata_v4 import IdRef
from .protocol import Protocol
from .resource import Identifier, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


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
    iptransport_details: list[IptransportDetails] | None = Field(
        alias="IPTransportDetails", default=None
    )
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    pci_id: PciId | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(alias="Redundancy@odata.count", default=None)
    status: Status | None = None


class GenZ(RedfishModel):
    access_key: str | None = None
    gcid: str | None = Field(alias="GCID", default=None)
    region_key: str | None = None


class IptransportDetails(RedfishModel):
    ipv4_address: Ipv4Address | None = Field(alias="IPv4Address", default=None)
    ipv6_address: Ipv6Address | None = Field(alias="IPv6Address", default=None)
    port: int | None = None
    transport_protocol: Protocol | None = None


class Links(RedfishModel):
    address_pools: list[IdRef] | None = None
    address_pools_odata_count: int | None = Field(alias="AddressPools@odata.count", default=None)
    connected_ports: list[IdRef] | None = None
    connected_ports_odata_count: int | None = Field(
        alias="ConnectedPorts@odata.count", default=None
    )
    connections: list[IdRef] | None = None
    connections_odata_count: int | None = Field(alias="Connections@odata.count", default=None)
    local_ports: list[IdRef] | None = None
    local_ports_odata_count: int | None = Field(alias="LocalPorts@odata.count", default=None)
    mutually_exclusive_endpoints: list[IdRef] | None = None
    mutually_exclusive_endpoints_odata_count: int | None = Field(
        alias="MutuallyExclusiveEndpoints@odata.count", default=None
    )
    network_device_function: list[IdRef] | None = None
    network_device_function_odata_count: int | None = Field(
        alias="NetworkDeviceFunction@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    ports: list[IdRef] | None = None
    ports_odata_count: int | None = Field(alias="Ports@odata.count", default=None)
    zones: list[IdRef] | None = None
    zones_odata_count: int | None = Field(alias="Zones@odata.count", default=None)


class PciId(RedfishModel):
    class_code: str | None = None
    device_id: str | None = None
    function_number: str | None = None
    subsystem_id: str | None = None
    subsystem_vendor_id: str | None = None
    vendor_id: str | None = None
