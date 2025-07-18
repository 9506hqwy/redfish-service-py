from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class EngineId(RedfishModel):
    architecture_id: str | None = None
    enterprise_specific_method: str | None = None
    private_enterprise_id: str | None = None


class HttpsProtocol(RedfishModel):
    certificates: IdRef | None = None
    port: int | None = None
    protocol_enabled: bool | None = None


class ManagerNetworkProtocol(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#ManagerNetworkProtocol.v1_12_0.ManagerNetworkProtocol",
    )
    actions: Actions | None = None
    dhcp: Protocol | None = Field(serialization_alias="DHCP", default=None)
    dhcpv6: Protocol | None = Field(serialization_alias="DHCPv6", default=None)
    description: str | None = None
    fqdn: str | None = Field(serialization_alias="FQDN", default=None)
    ftp: Protocol | None = Field(serialization_alias="FTP", default=None)
    ftps: Protocol | None = Field(serialization_alias="FTPS", default=None)
    http: Protocol | None = Field(serialization_alias="HTTP", default=None)
    https: HttpsProtocol | None = Field(serialization_alias="HTTPS", default=None)
    host_name: str | None = None
    ipmi: Protocol | None = Field(serialization_alias="IPMI", default=None)
    id: str
    kvmip: Protocol | None = Field(serialization_alias="KVMIP", default=None)
    modbus: ModbusProtocol | None = None
    ntp: NtpProtocol | None = Field(serialization_alias="NTP", default=None)
    name: str
    oem: dict[str, Any] | None = None
    proxy: ProxyConfiguration | None = None
    rdp: Protocol | None = Field(serialization_alias="RDP", default=None)
    rfb: Protocol | None = Field(serialization_alias="RFB", default=None)
    sftp: Protocol | None = Field(serialization_alias="SFTP", default=None)
    snmp: SnmpProtocol | None = Field(serialization_alias="SNMP", default=None)
    ssdp: SsdProtocol | None = Field(serialization_alias="SSDP", default=None)
    ssh: Protocol | None = Field(serialization_alias="SSH", default=None)
    status: Status | None = None
    telnet: Protocol | None = None
    virtual_media: Protocol | None = None
    mdns: Protocol | None = Field(serialization_alias="mDNS", default=None)


class ManagerNetworkProtocolOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    dhcp: Protocol | None = Field(serialization_alias="DHCP", default=None)
    dhcpv6: Protocol | None = Field(serialization_alias="DHCPv6", default=None)
    ftp: Protocol | None = Field(serialization_alias="FTP", default=None)
    ftps: Protocol | None = Field(serialization_alias="FTPS", default=None)
    http: Protocol | None = Field(serialization_alias="HTTP", default=None)
    https: HttpsProtocol | None = Field(serialization_alias="HTTPS", default=None)
    ipmi: Protocol | None = Field(serialization_alias="IPMI", default=None)
    kvmip: Protocol | None = Field(serialization_alias="KVMIP", default=None)
    modbus: ModbusProtocol | None = None
    ntp: NtpProtocol | None = Field(serialization_alias="NTP", default=None)
    oem: dict[str, Any] | None = None
    proxy: ProxyConfiguration | None = None
    rdp: Protocol | None = Field(serialization_alias="RDP", default=None)
    rfb: Protocol | None = Field(serialization_alias="RFB", default=None)
    sftp: Protocol | None = Field(serialization_alias="SFTP", default=None)
    snmp: SnmpProtocol | None = Field(serialization_alias="SNMP", default=None)
    ssdp: SsdProtocol | None = Field(serialization_alias="SSDP", default=None)
    ssh: Protocol | None = Field(serialization_alias="SSH", default=None)
    status: Status | None = None
    telnet: Protocol | None = None
    virtual_media: Protocol | None = None
    mdns: Protocol | None = Field(serialization_alias="mDNS", default=None)


class ModbusProtocol(RedfishModel):
    allowed_clients: list[str] | None = None
    maximum_connected_clients: int | None = None
    number_of_connected_clients: int | None = None
    port: int | None = None
    protocol_enabled: bool | None = None
    read_only: bool | None = None
    restrict_access_to_allowed_clients: bool | None = None
    server_id: int | None = None


class NtpProtocol(RedfishModel):
    ntp_servers: list[str] | None = Field(serialization_alias="NTPServers", default=None)
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
    proxy_auto_config_uri: str | None = Field(
        serialization_alias="ProxyAutoConfigURI", default=None
    )
    proxy_server_uri: str | None = Field(serialization_alias="ProxyServerURI", default=None)
    username: str | None = None


class SnmpAuthenticationProtocols(StrEnum):
    ACCOUNT = "Account"
    COMMUNITY_STRING = "CommunityString"
    HMA_C_MD5 = "HMAC_MD5"
    HMA_C_SHA96 = "HMAC_SHA96"
    HMA_C128_SHA224 = "HMAC128_SHA224"
    HMA_C192_SHA256 = "HMAC192_SHA256"
    HMA_C256_SHA384 = "HMAC256_SHA384"
    HMA_C384_SHA512 = "HMAC384_SHA512"


class SnmpCommunity(RedfishModel):
    access_mode: SnmpCommunityAccessMode | None = None
    community_string: str | None = None
    ipv4_address_range_lower: str | None = Field(
        serialization_alias="IPv4AddressRangeLower", default=None
    )
    ipv4_address_range_upper: str | None = Field(
        serialization_alias="IPv4AddressRangeUpper", default=None
    )
    name: str | None = None
    restrict_community_to_ipv4_address_range: bool | None = Field(
        serialization_alias="RestrictCommunityToIPv4AddressRange", default=None
    )


class SnmpCommunityAccessMode(StrEnum):
    FULL = "Full"
    LIMITED = "Limited"


class SnmpEncryptionProtocols(StrEnum):
    NONE = "None"
    ACCOUNT = "Account"
    CB_C_DES = "CBC_DES"
    CF_B128_AES128 = "CFB128_AES128"
    CF_B128_AES192 = "CFB128_AES192"
    CF_B128_AES256 = "CFB128_AES256"


class SnmpProtocol(RedfishModel):
    authentication_protocol: SnmpAuthenticationProtocols | None = None
    community_access_mode: SnmpCommunityAccessMode | None = None
    community_strings: list[SnmpCommunity] | None = None
    enable_snmpv1: bool | None = Field(serialization_alias="EnableSNMPv1", default=None)
    enable_snmpv2c: bool | None = Field(serialization_alias="EnableSNMPv2c", default=None)
    enable_snmpv3: bool | None = Field(serialization_alias="EnableSNMPv3", default=None)
    encryption_protocol: SnmpEncryptionProtocols | None = None
    engine_id: EngineId | None = None
    hide_community_strings: bool | None = None
    port: int | None = None
    protocol_enabled: bool | None = None
    trap_port: int | None = None


class SsdProtocol(RedfishModel):
    notify_ipv6_scope: NotifyIpv6Scope | None = Field(
        serialization_alias="NotifyIPv6Scope", default=None
    )
    notify_multicast_interval_seconds: int | None = None
    notify_ttl: int | None = Field(serialization_alias="NotifyTTL", default=None)
    port: int | None = None
    protocol_enabled: bool | None = None
