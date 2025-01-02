from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import RedfishModel
from .odata_v4 import IdRef
from .protocol import Protocol
from .resource import IndicatorLed, Location, PowerState, Status
from .software_inventory import MeasurementBlock


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#Switch.Reset", default=None)
    oem: dict[str, Any] | None = None


class Cxl(RedfishModel):
    max_vc_ss_supported: int | None = Field(alias="MaxVCSsSupported", default=None)
    total_numberv_pp_bs: int | None = Field(alias="TotalNumbervPPBs", default=None)
    vcs: VcsSwitch | None = Field(alias="VCS", default=None)


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


class Switch(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    asset_tag: str | None = None
    cxl: Cxl | None = Field(alias="CXL", default=None)
    certificates: IdRef | None = None
    current_bandwidth_gbps: float | None = None
    description: str | None = None
    domain_id: int | None = Field(alias="DomainID", default=None)
    enabled: bool | None = None
    environment_metrics: IdRef | None = None
    firmware_version: str | None = None
    id: str
    indicator_led: IndicatorLed | None = Field(alias="IndicatorLED", default=None)
    is_managed: bool | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    log_services: IdRef | None = None
    manufacturer: str | None = None
    max_bandwidth_gbps: float | None = None
    measurements: list[MeasurementBlock] | None = None
    metrics: IdRef | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    ports: IdRef | None = None
    power_state: PowerState | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(alias="Redundancy@odata.count", default=None)
    sku: str | None = Field(alias="SKU", default=None)
    serial_number: str | None = None
    status: Status | None = None
    supported_protocols: list[Protocol] | None = None
    switch_type: Protocol | None = None
    total_switch_width: int | None = None
    uuid: str | None = Field(alias="UUID", default=None)


class VcsSwitch(RedfishModel):
    hdm_decoders: int | None = Field(alias="HDMDecoders", default=None)
