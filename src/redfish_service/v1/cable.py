from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Location, Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class Cable(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    cable_class: str | None = None
    cable_status: CableStatus | None = None
    cable_type: str | None = None
    description: str | None = None
    downstream_connector_types: list[ConnectorType] | None = None
    downstream_name: str | None = None
    length_meters: str | None = None
    links: Links | None = None
    location: Location | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    sku: str | None = None
    serial_number: str | None = None
    status: Status | None = None
    upstream_connector_types: list[ConnectorType] | None = None
    upstream_name: str | None = None
    user_description: str | None = None
    user_label: str | None = None
    vendor: str | None = None


class CableStatus(StrEnum):
    NORMAL = "Normal"
    DEGRADED = "Degraded"
    FAILED = "Failed"
    TESTING = "Testing"
    DISABLED = "Disabled"
    SET_BY_SERVICE = "SetByService"


class ConnectorType(StrEnum):
    ACPOWER = "ACPower"
    DB9 = "DB9"
    DCPOWER = "DCPower"
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
    SFPPLUS = "SFPPlus"
    USBA = "USBA"
    USBC = "USBC"
    QSFP = "QSFP"
    CDFP = "CDFP"
    OSFP = "OSFP"


class Links(RedfishModel):
    downstream_chassis: list[IdRef] | None = None
    downstream_ports: list[IdRef] | None = None
    downstream_resources: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    upstream_chassis: list[IdRef] | None = None
    upstream_ports: list[IdRef] | None = None
    upstream_resources: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass
