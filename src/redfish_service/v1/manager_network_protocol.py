from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
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


class EngineId(RedfishModel):
    architecture_id: str | None = None
    enterprise_specific_method: str | None = None
    private_enterprise_id: str | None = None


class Httpsprotocol(RedfishModel):
    certificates: IdRef | None = None
    port: int | None = None
    protocol_enabled: bool | None = None


class ManagerNetworkProtocol(RedfishResource):
    actions: Actions | None = None
    dhcp: Protocol | None = Field(alias="DHCP", default=None)
    dhcpv6: Protocol | None = Field(alias="DHCPv6", default=None)
    description: str | None = None
    fqdn: str | None = Field(alias="FQDN", default=None)
    ftp: Protocol | None = Field(alias="FTP", default=None)
    ftps: Protocol | None = Field(alias="FTPS", default=None)
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
    sftp: Protocol | None = Field(alias="SFTP", default=None)
    snmp: Snmpprotocol | None = Field(alias="SNMP", default=None)
    ssdp: Ssdprotocol | None = Field(alias="SSDP", default=None)
    ssh: Protocol | None = Field(alias="SSH", default=None)
    status: Status | None = None
    telnet: Protocol | None = None
    virtual_media: Protocol | None = None


class Ntpprotocol(RedfishModel):
    ntpservers: list[str] | None = Field(alias="NTPServers", default=None)
    network_supplied_servers: list[str] | None = None
    port: int | None = None
    protocol_enabled: bool | None = None


class NotifyIpv6Scope(StrEnum):
    LINK = "Link"
    SITE = "Site"
    ORGANIZATION = "Organization"


class Protocol(RedfishModel):
    port: int | None = None
    protocol_enabled: bool | None = None


class ProxyConfiguration(RedfishModel):
    enabled: bool | None = None
    exclude_addresses: list[str] | None = None
    password: str | None = None
    password_set: bool | None = None
    proxy_auto_config_uri: str | None = Field(alias="ProxyAutoConfigURI", default=None)
    proxy_server_uri: str | None = Field(alias="ProxyServerURI", default=None)
    username: str | None = None


class SnmpauthenticationProtocols(StrEnum):
    ACCOUNT = "Account"
    COMMUNITY_STRING = "CommunityString"
    HMAC__MD5 = "HMAC_MD5"
    HMAC__SHA96 = "HMAC_SHA96"
    HMAC128__SHA224 = "HMAC128_SHA224"
    HMAC192__SHA256 = "HMAC192_SHA256"
    HMAC256__SHA384 = "HMAC256_SHA384"
    HMAC384__SHA512 = "HMAC384_SHA512"


class Snmpcommunity(RedfishModel):
    access_mode: SnmpcommunityAccessMode | None = None
    community_string: str | None = None
    ipv4_address_range_lower: str | None = Field(alias="IPv4AddressRangeLower", default=None)
    ipv4_address_range_upper: str | None = Field(alias="IPv4AddressRangeUpper", default=None)
    name: str | None = None
    restrict_community_to_ipv4_address_range: bool | None = Field(
        alias="RestrictCommunityToIPv4AddressRange", default=None
    )


class SnmpcommunityAccessMode(StrEnum):
    FULL = "Full"
    LIMITED = "Limited"


class SnmpencryptionProtocols(StrEnum):
    NONE = "None"
    ACCOUNT = "Account"
    CBC__DES = "CBC_DES"
    CFB128__AES128 = "CFB128_AES128"
    CFB128__AES192 = "CFB128_AES192"
    CFB128__AES256 = "CFB128_AES256"


class Snmpprotocol(RedfishModel):
    authentication_protocol: SnmpauthenticationProtocols | None = None
    community_access_mode: SnmpcommunityAccessMode | None = None
    community_strings: list[Snmpcommunity] | None = None
    enable_snmpv1: bool | None = Field(alias="EnableSNMPv1", default=None)
    enable_snmpv2c: bool | None = Field(alias="EnableSNMPv2c", default=None)
    enable_snmpv3: bool | None = Field(alias="EnableSNMPv3", default=None)
    encryption_protocol: SnmpencryptionProtocols | None = None
    engine_id: EngineId | None = None
    hide_community_strings: bool | None = None
    port: int | None = None
    protocol_enabled: bool | None = None
    trap_port: int | None = None


class Ssdprotocol(RedfishModel):
    notify_ipv6_scope: NotifyIpv6Scope | None = Field(alias="NotifyIPv6Scope", default=None)
    notify_multicast_interval_seconds: int | None = None
    notify_ttl: int | None = Field(alias="NotifyTTL", default=None)
    port: int | None = None
    protocol_enabled: bool | None = None
