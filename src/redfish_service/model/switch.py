from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .protocol import Protocol
from .resource import IndicatorLed, Location, PowerState, ResetType, Status
from .software_inventory import MeasurementBlock


class Actions(RedfishModel):
    reset: Reset | None = Field(serialization_alias="#Switch.Reset", default=None)
    oem: dict[str, Any] | None = None


class Cxl(RedfishModel):
    max_vc_ss_supported: int | None = Field(serialization_alias="MaxVCSsSupported", default=None)
    total_numberv_pp_bs: int | None = Field(serialization_alias="TotalNumbervPPBs", default=None)
    vcs: VcsSwitch | None = Field(serialization_alias="VCS", default=None)


class Links(RedfishModel):
    chassis: IdRef | None = None
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(
        serialization_alias="Endpoints@odata.count", default=None
    )
    managed_by: list[IdRef] | None = None
    managed_by_odata_count: int | None = Field(
        serialization_alias="ManagedBy@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_device: IdRef | None = Field(serialization_alias="PCIeDevice", default=None)


class Reset(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetRequest(RedfishModel):
    reset_type: ResetType | None = None


class Switch(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Switch.v1_9_3.Switch")
    actions: Actions | None = None
    asset_tag: str | None = None
    cxl: Cxl | None = Field(serialization_alias="CXL", default=None)
    certificates: IdRef | None = None
    current_bandwidth_gbps: float | None = None
    description: str | None = None
    domain_id: int | None = Field(serialization_alias="DomainID", default=None)
    enabled: bool | None = None
    environment_metrics: IdRef | None = None
    firmware_version: str | None = None
    id: str
    indicator_led: IndicatorLed | None = Field(serialization_alias="IndicatorLED", default=None)
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
    redundancy_odata_count: int | None = Field(
        serialization_alias="Redundancy@odata.count", default=None
    )
    sku: str | None = Field(serialization_alias="SKU", default=None)
    serial_number: str | None = None
    status: Status | None = None
    supported_protocols: list[Protocol] | None = None
    switch_type: Protocol | None = None
    total_switch_width: int | None = None
    uuid: str | None = Field(serialization_alias="UUID", default=None)


class SwitchOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    asset_tag: str | None = None
    cxl: Cxl | None = Field(serialization_alias="CXL", default=None)
    enabled: bool | None = None
    indicator_led: IndicatorLed | None = Field(serialization_alias="IndicatorLED", default=None)
    is_managed: bool | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    measurements: list[MeasurementBlock] | None = None
    oem: dict[str, Any] | None = None
    redundancy: list[IdRef] | None = None
    status: Status | None = None


class VcsSwitch(RedfishModel):
    hdm_decoders: int | None = Field(serialization_alias="HDMDecoders", default=None)
