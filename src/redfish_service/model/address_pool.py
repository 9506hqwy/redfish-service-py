from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class AsNumberRange(RedfishModel):
    lower: int | None = None
    upper: int | None = None


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AddressPool(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#AddressPool.v1_3_0.AddressPool")
    actions: Actions | None = None
    description: str | None = None
    ethernet: Ethernet | None = None
    gen_z: GenZ | None = None
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None


class AddressPoolOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#AddressPool.v1_3_0.AddressPool")
    actions: Actions | None = None
    description: str | None = None
    ethernet: Ethernet | None = None
    gen_z: GenZ | None = None
    id: str | None = None
    links: Links | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class AddressPoolOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#AddressPool.v1_3_0.AddressPool")
    actions: Actions | None = None
    description: str | None = None
    ethernet: Ethernet | None = None
    gen_z: GenZ | None = None
    id: str | None = None
    links: Links | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class BfdSingleHopOnly(RedfishModel):
    demand_mode_enabled: bool | None = None
    desired_min_tx_interval_milliseconds: int | None = None
    key_chain: str | None = None
    local_multiplier: int | None = None
    meticulous_mode_enabled: bool | None = None
    required_min_rx_interval_milliseconds: int | None = None
    source_port: int | None = None


class BgpEvpn(RedfishModel):
    arp_proxy_enabled: bool | None = Field(alias="ARPProxyEnabled", default=None)
    arp_suppression_enabled: bool | None = Field(alias="ARPSuppressionEnabled", default=None)
    arp_supression_enabled: bool | None = Field(alias="ARPSupressionEnabled", default=None)
    anycast_gateway_ip_address: str | None = Field(alias="AnycastGatewayIPAddress", default=None)
    anycast_gateway_mac_address: str | None = Field(alias="AnycastGatewayMACAddress", default=None)
    esi_number_range: EsiNumberRange | None = Field(alias="ESINumberRange", default=None)
    evi_number_range: EviNumberRange | None = Field(alias="EVINumberRange", default=None)
    gateway_ip_address: str | None = Field(alias="GatewayIPAddress", default=None)
    gateway_ip_address_range: GatewayIpAddressRange | None = Field(
        alias="GatewayIPAddressRange", default=None
    )
    ndp_proxy_enabled: bool | None = Field(alias="NDPProxyEnabled", default=None)
    ndp_suppression_enabled: bool | None = Field(alias="NDPSuppressionEnabled", default=None)
    ndp_supression_enabled: bool | None = Field(alias="NDPSupressionEnabled", default=None)
    route_distinguisher_administrator_subfield: str | None = None
    route_distinguisher_range: RouteDistinguisherRange | None = None
    route_target_administrator_subfield: str | None = None
    route_target_range: RouteTargetRange | None = None
    underlay_multicast_enabled: bool | None = None
    unknown_unicast_suppression_enabled: bool | None = None
    vlan_identifier_address_range: VlanIdentifierAddressRange | None = Field(
        alias="VLANIdentifierAddressRange", default=None
    )


class BgpNeighbor(RedfishModel):
    address: str | None = None
    allow_own_as_enabled: bool | None = Field(alias="AllowOwnASEnabled", default=None)
    cidr: int | None = Field(alias="CIDR", default=None)
    connect_retry_seconds: int | None = None
    enabled: bool | None = None
    hold_time_seconds: int | None = None
    keepalive_interval_seconds: int | None = None
    local_as: int | None = Field(alias="LocalAS", default=None)
    log_state_changes_enabled: bool | None = None
    max_prefix: MaxPrefix | None = None
    minimum_advertisement_interval_seconds: int | None = None
    passive_mode_enabled: bool | None = None
    path_mtu_discovery_enabled: bool | None = Field(alias="PathMTUDiscoveryEnabled", default=None)
    peer_as: int | None = Field(alias="PeerAS", default=None)
    replace_peer_as_enabled: bool | None = Field(alias="ReplacePeerASEnabled", default=None)
    tcp_max_segment_size_bytes: int | None = Field(alias="TCPMaxSegmentSizeBytes", default=None)
    treat_as_withdraw_enabled: bool | None = None


class BgpRoute(RedfishModel):
    advertise_inactive_routes_enabled: bool | None = None
    distance_external: int | None = None
    distance_internal: int | None = None
    distance_local: int | None = None
    external_compare_router_id_enabled: bool | None = None
    flap_damping_enabled: bool | None = None
    send_default_route_enabled: bool | None = None


class CommonBgpProperties(RedfishModel):
    as_number_range: AsNumberRange | None = Field(alias="ASNumberRange", default=None)
    bgp_neighbor: BgpNeighbor | None = Field(alias="BGPNeighbor", default=None)
    bgp_route: BgpRoute | None = Field(alias="BGPRoute", default=None)
    graceful_restart: GracefulRestart | None = None
    multiple_paths: MultiplePaths | None = None
    send_community_enabled: bool | None = None


class Dhcp(RedfishModel):
    dhcp_interface_mtu_bytes: int | None = Field(alias="DHCPInterfaceMTUBytes", default=None)
    dhcp_relay_enabled: bool | None = Field(alias="DHCPRelayEnabled", default=None)
    dhcp_server: list[str] | None = Field(alias="DHCPServer", default=None)


class Ebgp(RedfishModel):
    as_number_range: AsNumberRange | None = Field(alias="ASNumberRange", default=None)
    allow_duplicate_as_enabled: bool | None = Field(alias="AllowDuplicateASEnabled", default=None)
    allow_override_as_enabled: bool | None = Field(alias="AllowOverrideASEnabled", default=None)
    always_compare_med_enabled: bool | None = Field(alias="AlwaysCompareMEDEnabled", default=None)
    bgp_local_preference: int | None = Field(alias="BGPLocalPreference", default=None)
    bgp_neighbor: BgpNeighbor | None = Field(alias="BGPNeighbor", default=None)
    bgp_route: BgpRoute | None = Field(alias="BGPRoute", default=None)
    bgp_weight: int | None = Field(alias="BGPWeight", default=None)
    graceful_restart: GracefulRestart | None = None
    med: int | None = Field(alias="MED", default=None)
    multihop_enabled: bool | None = None
    multihop_ttl: int | None = Field(alias="MultihopTTL", default=None)
    multiple_paths: MultiplePaths | None = None
    send_community_enabled: bool | None = None


class EsiNumberRange(RedfishModel):
    lower: int | None = None
    upper: int | None = None


class EviNumberRange(RedfishModel):
    lower: int | None = None
    upper: int | None = None


class Ethernet(RedfishModel):
    bfd_single_hop_only: BfdSingleHopOnly | None = Field(alias="BFDSingleHopOnly", default=None)
    bgp_evpn: BgpEvpn | None = Field(alias="BGPEvpn", default=None)
    ebgp: Ebgp | None = Field(alias="EBGP", default=None)
    ipv4: Ipv4 | None = Field(alias="IPv4", default=None)
    multi_protocol_ebgp: Ebgp | None = Field(alias="MultiProtocolEBGP", default=None)
    multi_protocol_ibgp: CommonBgpProperties | None = Field(
        alias="MultiProtocolIBGP", default=None
    )


class GatewayIpAddressRange(RedfishModel):
    lower: str | None = None
    upper: str | None = None


class GenZ(RedfishModel):
    access_key: str | None = None
    max_cid: int | None = Field(alias="MaxCID", default=None)
    max_sid: int | None = Field(alias="MaxSID", default=None)
    min_cid: int | None = Field(alias="MinCID", default=None)
    min_sid: int | None = Field(alias="MinSID", default=None)


class GracefulRestart(RedfishModel):
    graceful_restart_enabled: bool | None = None
    helper_mode_enabled: bool | None = None
    stale_routes_time_seconds: int | None = None
    time_seconds: int | None = None


class Ipv4(RedfishModel):
    anycast_gateway_ip_address: str | None = Field(alias="AnycastGatewayIPAddress", default=None)
    anycast_gateway_mac_address: str | None = Field(alias="AnycastGatewayMACAddress", default=None)
    dhcp: Dhcp | None = Field(alias="DHCP", default=None)
    dns_domain_name: str | None = Field(alias="DNSDomainName", default=None)
    dns_server: list[str] | None = Field(alias="DNSServer", default=None)
    distribute_into_underlay_enabled: bool | None = None
    ebgp_address_range: Ipv4AddressRange | None = Field(alias="EBGPAddressRange", default=None)
    fabric_link_address_range: Ipv4AddressRange | None = None
    gateway_ip_address: str | None = Field(alias="GatewayIPAddress", default=None)
    host_address_range: Ipv4AddressRange | None = None
    ibgp_address_range: Ipv4AddressRange | None = Field(alias="IBGPAddressRange", default=None)
    loopback_address_range: Ipv4AddressRange | None = None
    management_address_range: Ipv4AddressRange | None = None
    ntp_offset_hours_minutes: int | None = Field(alias="NTPOffsetHoursMinutes", default=None)
    ntp_server: list[str] | None = Field(alias="NTPServer", default=None)
    ntp_timezone: str | None = Field(alias="NTPTimezone", default=None)
    native_vlan: int | None = Field(alias="NativeVLAN", default=None)
    system_mac_range: SystemMacRange | None = Field(alias="SystemMACRange", default=None)
    vlan_identifier_address_range: VlanIdentifierAddressRange | None = Field(
        alias="VLANIdentifierAddressRange", default=None
    )


class Ipv4AddressRange(RedfishModel):
    lower: str | None = None
    upper: str | None = None


class Links(RedfishModel):
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    oem: dict[str, Any] | None = None
    zones: list[IdRef] | None = None
    zones_odata_count: int | None = Field(alias="Zones@odata.count", default=None)


class MaxPrefix(RedfishModel):
    max_prefix_number: int | None = None
    restart_timer_seconds: int | None = None
    shutdown_threshold_percentage: float | None = None
    threshold_warning_only_enabled: bool | None = None


class MultiplePaths(RedfishModel):
    maximum_paths: int | None = None
    use_multiple_paths_enabled: bool | None = None


class RouteDistinguisherRange(RedfishModel):
    lower: int | None = None
    upper: int | None = None


class RouteTargetRange(RedfishModel):
    lower: int | None = None
    upper: int | None = None


class SystemMacRange(RedfishModel):
    lower: str | None = None
    upper: str | None = None


class VlanIdentifierAddressRange(RedfishModel):
    lower: int | None = None
    upper: int | None = None
