from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Cable(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#Cable.v1_2_3.Cable")
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    cable_class: CableClass | None = None
    cable_status: CableStatus | None = None
    cable_type: str | None = None
    description: str | None = None
    downstream_connector_types: list[ConnectorType] | None = None
    downstream_name: str | None = None
    id: str
    length_meters: float | None = None
    links: Links | None = None
    location: Location | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    sku: str | None = Field(alias="SKU", default=None)
    serial_number: str | None = None
    status: Status | None = None
    upstream_connector_types: list[ConnectorType] | None = None
    upstream_name: str | None = None
    user_description: str | None = None
    user_label: str | None = None
    vendor: str | None = None


class CableOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#Cable.v1_2_3.Cable")
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    cable_class: CableClass | None = None
    cable_status: CableStatus | None = None
    cable_type: str | None = None
    description: str | None = None
    downstream_connector_types: list[ConnectorType] | None = None
    downstream_name: str | None = None
    id: str | None = None
    length_meters: float | None = None
    links: Links | None = None
    location: Location | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    sku: str | None = Field(alias="SKU", default=None)
    serial_number: str | None = None
    status: Status | None = None
    upstream_connector_types: list[ConnectorType] | None = None
    upstream_name: str | None = None
    user_description: str | None = None
    user_label: str | None = None
    vendor: str | None = None


class CableOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#Cable.v1_2_3.Cable")
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    cable_class: CableClass | None = None
    cable_status: CableStatus | None = None
    cable_type: str | None = None
    description: str | None = None
    downstream_connector_types: list[ConnectorType] | None = None
    downstream_name: str | None = None
    id: str | None = None
    length_meters: float | None = None
    links: Links | None = None
    location: Location | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    sku: str | None = Field(alias="SKU", default=None)
    serial_number: str | None = None
    status: Status | None = None
    upstream_connector_types: list[ConnectorType] | None = None
    upstream_name: str | None = None
    user_description: str | None = None
    user_label: str | None = None
    vendor: str | None = None


class CableClass(StrEnum):
    POWER = "Power"
    NETWORK = "Network"
    STORAGE = "Storage"
    FAN = "Fan"
    PCIE = "PCIe"
    USB = "USB"
    VIDEO = "Video"
    FABRIC = "Fabric"
    SERIAL = "Serial"
    GENERAL = "General"


class CableStatus(StrEnum):
    NORMAL = "Normal"
    DEGRADED = "Degraded"
    FAILED = "Failed"
    TESTING = "Testing"
    DISABLED = "Disabled"
    SET_BY_SERVICE = "SetByService"


class ConnectorType(StrEnum):
    AC_POWER = "ACPower"
    DB9 = "DB9"
    DC_POWER = "DCPower"
    DISPLAY_PORT = "DisplayPort"
    HDMI = "HDMI"
    ICI = "ICI"
    IPASS = "IPASS"
    PCIE = "PCIe"
    PROPRIETARY = "Proprietary"
    RJ45 = "RJ45"
    SATA = "SATA"
    SCSI = "SCSI"
    SLIM_SAS = "SlimSAS"
    SFP = "SFP"
    SFP_PLUS = "SFPPlus"
    USBA = "USBA"
    USBC = "USBC"
    QSFP = "QSFP"
    CDFP = "CDFP"
    OSFP = "OSFP"


class Links(RedfishModel):
    downstream_chassis: list[IdRef] | None = None
    downstream_chassis_odata_count: int | None = Field(
        alias="DownstreamChassis@odata.count", default=None
    )
    downstream_ports: list[IdRef] | None = None
    downstream_ports_odata_count: int | None = Field(
        alias="DownstreamPorts@odata.count", default=None
    )
    downstream_resources: list[IdRef] | None = None
    downstream_resources_odata_count: int | None = Field(
        alias="DownstreamResources@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    upstream_chassis: list[IdRef] | None = None
    upstream_chassis_odata_count: int | None = Field(
        alias="UpstreamChassis@odata.count", default=None
    )
    upstream_ports: list[IdRef] | None = None
    upstream_ports_odata_count: int | None = Field(alias="UpstreamPorts@odata.count", default=None)
    upstream_resources: list[IdRef] | None = None
    upstream_resources_odata_count: int | None = Field(
        alias="UpstreamResources@odata.count", default=None
    )
