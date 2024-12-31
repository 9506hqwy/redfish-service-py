from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class AsnumberRange(RedfishResource):
    lower: int | None = None
    upper: int | None = None


class Actions(RedfishResource):
    oem: OemActions | None = None


class AddressPool(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    ethernet: Ethernet | None = None
    gen_z: GenZ | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class BfdsingleHopOnly(RedfishResource):
    demand_mode_enabled: str | None = None
    desired_min_tx_interval_milliseconds: str | None = None
    key_chain: str | None = None
    local_multiplier: str | None = None
    meticulous_mode_enabled: str | None = None
    required_min_rx_interval_milliseconds: str | None = None
    source_port: str | None = None


class Bgpevpn(RedfishResource):
    arpproxy_enabled: str | None = None
    arpsuppression_enabled: str | None = None
    arpsupression_enabled: str | None = None
    anycast_gateway_ipaddress: str | None = None
    anycast_gateway_macaddress: str | None = None
    esinumber_range: EsinumberRange | None = None
    evinumber_range: EvinumberRange | None = None
    gateway_ipaddress: str | None = None
    gateway_ipaddress_range: GatewayIpaddressRange | None = None
    ndpproxy_enabled: str | None = None
    ndpsuppression_enabled: str | None = None
    ndpsupression_enabled: str | None = None
    route_distinguisher_administrator_subfield: str | None = None
    route_distinguisher_range: RouteDistinguisherRange | None = None
    route_target_administrator_subfield: str | None = None
    route_target_range: RouteTargetRange | None = None
    underlay_multicast_enabled: str | None = None
    unknown_unicast_suppression_enabled: str | None = None
    vlanidentifier_address_range: VlanidentifierAddressRange | None = None


class Bgpneighbor(RedfishResource):
    address: str | None = None
    allow_own_asenabled: str | None = None
    cidr: int | None = None
    connect_retry_seconds: str | None = None
    enabled: bool | None = None
    hold_time_seconds: str | None = None
    keepalive_interval_seconds: str | None = None
    local_as: str | None = None
    log_state_changes_enabled: str | None = None
    max_prefix: MaxPrefix | None = None
    minimum_advertisement_interval_seconds: str | None = None
    passive_mode_enabled: str | None = None
    path_mtudiscovery_enabled: str | None = None
    peer_as: str | None = None
    replace_peer_asenabled: str | None = None
    tcpmax_segment_size_bytes: str | None = None
    treat_as_withdraw_enabled: str | None = None


class Bgproute(RedfishResource):
    advertise_inactive_routes_enabled: str | None = None
    distance_external: str | None = None
    distance_internal: str | None = None
    distance_local: str | None = None
    external_compare_router_id_enabled: str | None = None
    flap_damping_enabled: str | None = None
    send_default_route_enabled: str | None = None


class CommonBgpproperties(RedfishResource):
    asnumber_range: AsnumberRange | None = None
    bgpneighbor: Bgpneighbor | None = None
    bgproute: Bgproute | None = None
    graceful_restart: GracefulRestart | None = None
    multiple_paths: MultiplePaths | None = None
    send_community_enabled: str | None = None


class Dhcp(RedfishResource):
    dhcpinterface_mtubytes: str | None = None
    dhcprelay_enabled: str | None = None
    dhcpserver: list[str] | None = None


class Ebgp(RedfishResource):
    asnumber_range: AsnumberRange | None = None
    allow_duplicate_asenabled: str | None = None
    allow_override_asenabled: str | None = None
    always_compare_medenabled: str | None = None
    bgplocal_preference: str | None = None
    bgpneighbor: Bgpneighbor | None = None
    bgproute: Bgproute | None = None
    bgpweight: str | None = None
    graceful_restart: GracefulRestart | None = None
    med: str | None = None
    multihop_enabled: str | None = None
    multihop_ttl: str | None = None
    multiple_paths: MultiplePaths | None = None
    send_community_enabled: str | None = None


class EsinumberRange(RedfishResource):
    lower: int | None = None
    upper: int | None = None


class EvinumberRange(RedfishResource):
    lower: int | None = None
    upper: int | None = None


class Ethernet(RedfishResource):
    bfdsingle_hop_only: BfdsingleHopOnly | None = None
    bgpevpn: Bgpevpn | None = None
    ebgp: Ebgp | None = None
    ipv4: Ipv4 | None = None
    multi_protocol_ebgp: Ebgp | None = None
    multi_protocol_ibgp: CommonBgpproperties | None = None


class GatewayIpaddressRange(RedfishResource):
    lower: str | None = None
    upper: str | None = None


class GenZ(RedfishResource):
    access_key: str | None = None
    max_cid: str | None = None
    max_sid: str | None = None
    min_cid: str | None = None
    min_sid: str | None = None


class GracefulRestart(RedfishResource):
    graceful_restart_enabled: str | None = None
    helper_mode_enabled: str | None = None
    stale_routes_time_seconds: str | None = None
    time_seconds: str | None = None


class Ipv4(RedfishResource):
    anycast_gateway_ipaddress: str | None = None
    anycast_gateway_macaddress: str | None = None
    dhcp: Dhcp | None = None
    dnsdomain_name: str | None = None
    dnsserver: list[str] | None = None
    distribute_into_underlay_enabled: str | None = None
    ebgpaddress_range: Ipv4AddressRange | None = None
    fabric_link_address_range: Ipv4AddressRange | None = None
    gateway_ipaddress: str | None = None
    host_address_range: Ipv4AddressRange | None = None
    ibgpaddress_range: Ipv4AddressRange | None = None
    loopback_address_range: Ipv4AddressRange | None = None
    management_address_range: Ipv4AddressRange | None = None
    ntpoffset_hours_minutes: str | None = None
    ntpserver: list[str] | None = None
    ntptimezone: str | None = None
    native_vlan: str | None = None
    system_macrange: SystemMacrange | None = None
    vlanidentifier_address_range: VlanidentifierAddressRange | None = None


class Ipv4AddressRange(RedfishResource):
    lower: str | None = None
    upper: str | None = None


class Links(RedfishResource):
    endpoints: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    zones: list[IdRef] | None = None


class MaxPrefix(RedfishResource):
    max_prefix_number: str | None = None
    restart_timer_seconds: str | None = None
    shutdown_threshold_percentage: str | None = None
    threshold_warning_only_enabled: str | None = None


class MultiplePaths(RedfishResource):
    maximum_paths: str | None = None
    use_multiple_paths_enabled: str | None = None


class OemActions(RedfishResource):
    pass


class RouteDistinguisherRange(RedfishResource):
    lower: int | None = None
    upper: int | None = None


class RouteTargetRange(RedfishResource):
    lower: str | None = None
    upper: str | None = None


class SystemMacrange(RedfishResource):
    lower: str | None = None
    upper: str | None = None


class VlanidentifierAddressRange(RedfishResource):
    lower: str | None = None
    upper: str | None = None
