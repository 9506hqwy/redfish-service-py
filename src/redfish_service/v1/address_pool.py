from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class AsnumberRange(RedfishModel):
    lower: int | None = None
    upper: int | None = None


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AddressPool(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    ethernet: Ethernet | None = None
    gen_z: GenZ | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class BfdsingleHopOnly(RedfishModel):
    demand_mode_enabled: bool | None = None
    desired_min_tx_interval_milliseconds: int | None = None
    key_chain: str | None = None
    local_multiplier: int | None = None
    meticulous_mode_enabled: bool | None = None
    required_min_rx_interval_milliseconds: int | None = None
    source_port: int | None = None


class Bgpevpn(RedfishModel):
    arpproxy_enabled: bool | None = Field(alias="ARPProxyEnabled", default=None)
    arpsuppression_enabled: bool | None = Field(alias="ARPSuppressionEnabled", default=None)
    arpsupression_enabled: bool | None = Field(alias="ARPSupressionEnabled", default=None)
    anycast_gateway_ipaddress: str | None = Field(alias="AnycastGatewayIPAddress", default=None)
    anycast_gateway_macaddress: str | None = Field(alias="AnycastGatewayMACAddress", default=None)
    esinumber_range: EsinumberRange | None = Field(alias="ESINumberRange", default=None)
    evinumber_range: EvinumberRange | None = Field(alias="EVINumberRange", default=None)
    gateway_ipaddress: str | None = Field(alias="GatewayIPAddress", default=None)
    gateway_ipaddress_range: GatewayIpaddressRange | None = Field(
        alias="GatewayIPAddressRange", default=None
    )
    ndpproxy_enabled: bool | None = Field(alias="NDPProxyEnabled", default=None)
    ndpsuppression_enabled: bool | None = Field(alias="NDPSuppressionEnabled", default=None)
    ndpsupression_enabled: bool | None = Field(alias="NDPSupressionEnabled", default=None)
    route_distinguisher_administrator_subfield: str | None = None
    route_distinguisher_range: RouteDistinguisherRange | None = None
    route_target_administrator_subfield: str | None = None
    route_target_range: RouteTargetRange | None = None
    underlay_multicast_enabled: bool | None = None
    unknown_unicast_suppression_enabled: bool | None = None
    vlanidentifier_address_range: VlanidentifierAddressRange | None = Field(
        alias="VLANIdentifierAddressRange", default=None
    )


class Bgpneighbor(RedfishModel):
    address: str | None = None
    allow_own_asenabled: bool | None = Field(alias="AllowOwnASEnabled", default=None)
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
    path_mtudiscovery_enabled: bool | None = Field(alias="PathMTUDiscoveryEnabled", default=None)
    peer_as: int | None = Field(alias="PeerAS", default=None)
    replace_peer_asenabled: bool | None = Field(alias="ReplacePeerASEnabled", default=None)
    tcpmax_segment_size_bytes: int | None = Field(alias="TCPMaxSegmentSizeBytes", default=None)
    treat_as_withdraw_enabled: bool | None = None


class Bgproute(RedfishModel):
    advertise_inactive_routes_enabled: bool | None = None
    distance_external: int | None = None
    distance_internal: int | None = None
    distance_local: int | None = None
    external_compare_router_id_enabled: bool | None = None
    flap_damping_enabled: bool | None = None
    send_default_route_enabled: bool | None = None


class CommonBgpproperties(RedfishModel):
    asnumber_range: AsnumberRange | None = Field(alias="ASNumberRange", default=None)
    bgpneighbor: Bgpneighbor | None = Field(alias="BGPNeighbor", default=None)
    bgproute: Bgproute | None = Field(alias="BGPRoute", default=None)
    graceful_restart: GracefulRestart | None = None
    multiple_paths: MultiplePaths | None = None
    send_community_enabled: bool | None = None


class Dhcp(RedfishModel):
    dhcpinterface_mtubytes: int | None = Field(alias="DHCPInterfaceMTUBytes", default=None)
    dhcprelay_enabled: bool | None = Field(alias="DHCPRelayEnabled", default=None)
    dhcpserver: list[str] | None = Field(alias="DHCPServer", default=None)


class Ebgp(RedfishModel):
    asnumber_range: AsnumberRange | None = Field(alias="ASNumberRange", default=None)
    allow_duplicate_asenabled: bool | None = Field(alias="AllowDuplicateASEnabled", default=None)
    allow_override_asenabled: bool | None = Field(alias="AllowOverrideASEnabled", default=None)
    always_compare_medenabled: bool | None = Field(alias="AlwaysCompareMEDEnabled", default=None)
    bgplocal_preference: int | None = Field(alias="BGPLocalPreference", default=None)
    bgpneighbor: Bgpneighbor | None = Field(alias="BGPNeighbor", default=None)
    bgproute: Bgproute | None = Field(alias="BGPRoute", default=None)
    bgpweight: int | None = Field(alias="BGPWeight", default=None)
    graceful_restart: GracefulRestart | None = None
    med: int | None = Field(alias="MED", default=None)
    multihop_enabled: bool | None = None
    multihop_ttl: int | None = Field(alias="MultihopTTL", default=None)
    multiple_paths: MultiplePaths | None = None
    send_community_enabled: bool | None = None


class EsinumberRange(RedfishModel):
    lower: int | None = None
    upper: int | None = None


class EvinumberRange(RedfishModel):
    lower: int | None = None
    upper: int | None = None


class Ethernet(RedfishModel):
    bfdsingle_hop_only: BfdsingleHopOnly | None = Field(alias="BFDSingleHopOnly", default=None)
    bgpevpn: Bgpevpn | None = Field(alias="BGPEvpn", default=None)
    ebgp: Ebgp | None = Field(alias="EBGP", default=None)
    ipv4: Ipv4 | None = Field(alias="IPv4", default=None)
    multi_protocol_ebgp: Ebgp | None = Field(alias="MultiProtocolEBGP", default=None)
    multi_protocol_ibgp: CommonBgpproperties | None = Field(
        alias="MultiProtocolIBGP", default=None
    )


class GatewayIpaddressRange(RedfishModel):
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
    anycast_gateway_ipaddress: str | None = Field(alias="AnycastGatewayIPAddress", default=None)
    anycast_gateway_macaddress: str | None = Field(alias="AnycastGatewayMACAddress", default=None)
    dhcp: Dhcp | None = Field(alias="DHCP", default=None)
    dnsdomain_name: str | None = Field(alias="DNSDomainName", default=None)
    dnsserver: list[str] | None = Field(alias="DNSServer", default=None)
    distribute_into_underlay_enabled: bool | None = None
    ebgpaddress_range: Ipv4AddressRange | None = Field(alias="EBGPAddressRange", default=None)
    fabric_link_address_range: Ipv4AddressRange | None = None
    gateway_ipaddress: str | None = Field(alias="GatewayIPAddress", default=None)
    host_address_range: Ipv4AddressRange | None = None
    ibgpaddress_range: Ipv4AddressRange | None = Field(alias="IBGPAddressRange", default=None)
    loopback_address_range: Ipv4AddressRange | None = None
    management_address_range: Ipv4AddressRange | None = None
    ntpoffset_hours_minutes: int | None = Field(alias="NTPOffsetHoursMinutes", default=None)
    ntpserver: list[str] | None = Field(alias="NTPServer", default=None)
    ntptimezone: str | None = Field(alias="NTPTimezone", default=None)
    native_vlan: int | None = Field(alias="NativeVLAN", default=None)
    system_macrange: SystemMacrange | None = Field(alias="SystemMACRange", default=None)
    vlanidentifier_address_range: VlanidentifierAddressRange | None = Field(
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


class SystemMacrange(RedfishModel):
    lower: str | None = None
    upper: str | None = None


class VlanidentifierAddressRange(RedfishModel):
    lower: int | None = None
    upper: int | None = None
