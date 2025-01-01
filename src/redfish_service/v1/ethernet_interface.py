from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .ipaddresses import Ipv4Address, Ipv6Address
from .odata_v4 import IdRef
from .resource import Status
from .vlan_network_interface import Vlan


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Dhcpv4Configuration(RedfishModel):
    dhcpenabled: str | None = Field(alias="DHCPEnabled", default=None)
    fallback_address: str | None = None
    use_dnsservers: str | None = Field(alias="UseDNSServers", default=None)
    use_domain_name: str | None = None
    use_gateway: str | None = None
    use_ntpservers: str | None = Field(alias="UseNTPServers", default=None)
    use_static_routes: str | None = None


class Dhcpv6Configuration(RedfishModel):
    operating_mode: str | None = None
    use_dnsservers: str | None = Field(alias="UseDNSServers", default=None)
    use_domain_name: str | None = None
    use_ntpservers: str | None = Field(alias="UseNTPServers", default=None)
    use_rapid_commit: str | None = None


class EthernetInterface(RedfishResource):
    actions: Actions | None = None
    auto_neg: str | None = None
    dhcpv4: Dhcpv4Configuration | None = Field(alias="DHCPv4", default=None)
    dhcpv6: Dhcpv6Configuration | None = Field(alias="DHCPv6", default=None)
    description: str | None = None
    ethernet_interface_type: str | None = None
    fqdn: str | None = Field(alias="FQDN", default=None)
    full_duplex: str | None = None
    host_name: str | None = None
    ipv4_addresses: list[Ipv4Address] | None = Field(alias="IPv4Addresses", default=None)
    ipv4_static_addresses: list[str] | None = Field(alias="IPv4StaticAddresses", default=None)
    ipv6_address_policy_table: list[str] | None = Field(
        alias="IPv6AddressPolicyTable", default=None
    )
    ipv6_addresses: list[Ipv6Address] | None = Field(alias="IPv6Addresses", default=None)
    ipv6_default_gateway: str | None = Field(alias="IPv6DefaultGateway", default=None)
    ipv6_static_addresses: list[str] | None = Field(alias="IPv6StaticAddresses", default=None)
    ipv6_static_default_gateways: list[str] | None = Field(
        alias="IPv6StaticDefaultGateways", default=None
    )
    interface_enabled: str | None = None
    link_status: str | None = None
    links: Links | None = None
    macaddress: str | None = Field(alias="MACAddress", default=None)
    mtusize: str | None = Field(alias="MTUSize", default=None)
    max_ipv6_static_addresses: str | None = Field(alias="MaxIPv6StaticAddresses", default=None)
    name_servers: list[str] | None = None
    oem: dict[str, Any] | None = None
    permanent_macaddress: str | None = Field(alias="PermanentMACAddress", default=None)
    speed_mbps: str | None = None
    stateless_address_auto_config: StatelessAddressAutoConfiguration | None = None
    static_name_servers: list[str] | None = None
    status: Status | None = None
    team_mode: str | None = None
    uefi_device_path: str | None = None
    vlan: Vlan | None = Field(alias="VLAN", default=None)
    vlans: IdRef | None = Field(alias="VLANs", default=None)


class Links(RedfishModel):
    chassis: IdRef | None = None
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    host_interface: IdRef | None = None
    network_device_function: str | None = None
    network_device_functions: list[IdRef] | None = None
    network_device_functions_odata_count: int | None = Field(
        alias="NetworkDeviceFunctions@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    ports: list[IdRef] | None = None
    ports_odata_count: int | None = Field(alias="Ports@odata.count", default=None)
    related_interfaces: list[IdRef] | None = None
    related_interfaces_odata_count: int | None = Field(
        alias="RelatedInterfaces@odata.count", default=None
    )


class StatelessAddressAutoConfiguration(RedfishModel):
    ipv4_auto_config_enabled: str | None = Field(alias="IPv4AutoConfigEnabled", default=None)
    ipv6_auto_config_enabled: str | None = Field(alias="IPv6AutoConfigEnabled", default=None)
