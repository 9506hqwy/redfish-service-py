from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

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
    dhcp: Protocol | None = Field(alias="DHCP", default=None)
    dhcpv6: Protocol | None = Field(alias="DHCPv6", default=None)
    description: str | None = None
    fqdn: str | None = Field(alias="FQDN", default=None)
    http: Protocol | None = Field(alias="HTTP", default=None)
    https: Httpsprotocol | None = Field(alias="HTTPS", default=None)
    host_name: str | None = None
    ipmi: Protocol | None = Field(alias="IPMI", default=None)
    kvmip: Protocol | None = Field(alias="KVMIP", default=None)
    ntp: Ntpprotocol | None = Field(alias="NTP", default=None)
    oem: dict[str, Any] | None = None
    proxy: ProxyConfiguration | None = None
    rdp: Protocol | None = Field(alias="RDP", default=None)
    rfb: Protocol | None = Field(alias="RFB", default=None)
    snmp: Snmpprotocol | None = Field(alias="SNMP", default=None)
    ssdp: Ssdprotocol | None = Field(alias="SSDP", default=None)
    ssh: Protocol | None = Field(alias="SSH", default=None)
    status: Status | None = None
    telnet: Protocol | None = None
    virtual_media: Protocol | None = None


class Ntpprotocol(RedfishModel):
    ntpservers: list[str] | None = Field(alias="NTPServers", default=None)
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
    proxy_auto_config_uri: str | None = Field(alias="ProxyAutoConfigURI", default=None)
    proxy_server_uri: str | None = Field(alias="ProxyServerURI", default=None)
    username: str | None = None


class Snmpprotocol(RedfishModel):
    authentication_protocol: str | None = None
    community_access_mode: str | None = None
    community_strings: list[str] | None = None
    enable_snmpv1: str | None = Field(alias="EnableSNMPv1", default=None)
    enable_snmpv2c: str | None = Field(alias="EnableSNMPv2c", default=None)
    enable_snmpv3: str | None = Field(alias="EnableSNMPv3", default=None)
    encryption_protocol: str | None = None
    engine_id: str | None = None
    hide_community_strings: str | None = None
    port: str | None = None
    protocol_enabled: str | None = None


class Ssdprotocol(RedfishModel):
    notify_ipv6_scope: str | None = Field(alias="NotifyIPv6Scope", default=None)
    notify_multicast_interval_seconds: str | None = None
    notify_ttl: str | None = Field(alias="NotifyTTL", default=None)
    port: str | None = None
    protocol_enabled: str | None = None
