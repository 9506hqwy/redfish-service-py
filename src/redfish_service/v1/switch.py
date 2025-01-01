from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .protocol import Protocol
from .resource import Location, Status
from .software_inventory import MeasurementBlock


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#Switch.Reset", default=None)
    oem: dict[str, Any] | None = None


class Cxl(RedfishModel):
    max_vcss_supported: int | None = Field(alias="MaxVCSsSupported", default=None)
    total_numberv_ppbs: int | None = Field(alias="TotalNumbervPPBs", default=None)
    vcs: Vcsswitch | None = Field(alias="VCS", default=None)


class Links(RedfishModel):
    chassis: IdRef | None = None
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(alias="ManagedBy@odata.count", default=None)
    oem: dict[str, Any] | None = None
    pcie_device: IdRef | None = Field(alias="PCIeDevice", default=None)


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Switch(RedfishResource):
    actions: Actions | None = None
    asset_tag: str | None = None
    cxl: Cxl | None = Field(alias="CXL", default=None)
    certificates: IdRef | None = None
    current_bandwidth_gbps: str | None = None
    description: str | None = None
    domain_id: str | None = Field(alias="DomainID", default=None)
    enabled: bool | None = None
    environment_metrics: IdRef | None = None
    firmware_version: str | None = None
    indicator_led: str | None = Field(alias="IndicatorLED", default=None)
    is_managed: str | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    log_services: IdRef | None = None
    manufacturer: str | None = None
    max_bandwidth_gbps: str | None = None
    measurements: list[MeasurementBlock] | None = None
    metrics: IdRef | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    ports: IdRef | None = None
    power_state: str | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(alias="Redundancy@odata.count", default=None)
    sku: str | None = Field(alias="SKU", default=None)
    serial_number: str | None = None
    status: Status | None = None
    supported_protocols: list[Protocol] | None = None
    switch_type: str | None = None
    total_switch_width: str | None = None
    uuid: str | None = Field(alias="UUID", default=None)


class Vcsswitch(RedfishModel):
    hdmdecoders: int | None = Field(alias="HDMDecoders", default=None)
