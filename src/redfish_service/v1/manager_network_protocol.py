from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Httpsprotocol(RedfishModel):
    certificates: IdRef | None = None
    port: str | None = None
    protocol_enabled: str | None = None


class ManagerNetworkProtocol(RedfishResource):
    actions: Actions | None = None
    dhcp: Protocol | None = None
    dhcpv6: Protocol | None = None
    description: str | None = None
    fqdn: str | None = None
    http: Protocol | None = None
    https: Httpsprotocol | None = None
    host_name: str | None = None
    ipmi: Protocol | None = None
    kvmip: Protocol | None = None
    ntp: Ntpprotocol | None = None
    oem: dict[str, Any] | None = None
    proxy: ProxyConfiguration | None = None
    rdp: Protocol | None = None
    rfb: Protocol | None = None
    snmp: Snmpprotocol | None = None
    ssdp: Ssdprotocol | None = None
    ssh: Protocol | None = None
    status: Status | None = None
    telnet: Protocol | None = None
    virtual_media: Protocol | None = None


class Ntpprotocol(RedfishModel):
    ntpservers: list[str] | None = None
    network_supplied_servers: list[str] | None = None
    port: str | None = None
    protocol_enabled: str | None = None


class Protocol(RedfishModel):
    port: str | None = None
    protocol_enabled: str | None = None


class ProxyConfiguration(RedfishModel):
    enabled: bool | None = None
    exclude_addresses: list[str] | None = None
    password: str | None = None
    password_set: bool | None = None
    proxy_auto_config_uri: str | None = None
    proxy_server_uri: str | None = None
    username: str | None = None


class Snmpprotocol(RedfishModel):
    authentication_protocol: str | None = None
    community_access_mode: str | None = None
    community_strings: list[str] | None = None
    enable_snmpv1: str | None = None
    enable_snmpv2c: str | None = None
    enable_snmpv3: str | None = None
    encryption_protocol: str | None = None
    engine_id: str | None = None
    hide_community_strings: str | None = None
    port: str | None = None
    protocol_enabled: str | None = None


class Ssdprotocol(RedfishModel):
    notify_ipv6_scope: str | None = None
    notify_multicast_interval_seconds: str | None = None
    notify_ttl: str | None = None
    port: str | None = None
    protocol_enabled: str | None = None
