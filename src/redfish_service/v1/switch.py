from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .protocol import Protocol
from .resource import Location, Status
from .software_inventory import MeasurementBlock


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Cxl(RedfishModel):
    max_vcss_supported: int | None = None
    total_numberv_ppbs: int | None = None
    vcs: Vcsswitch | None = None


class Links(RedfishModel):
    chassis: IdRef | None = None
    endpoints: list[IdRef] | None = None
    managed_by: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    pcie_device: IdRef | None = None


class Reset(RedfishModel):
    target: str | None = None
    title: str | None = None


class Switch(RedfishResource):
    actions: Actions | None = None
    asset_tag: str | None = None
    cxl: Cxl | None = None
    certificates: IdRef | None = None
    current_bandwidth_gbps: str | None = None
    description: str | None = None
    domain_id: str | None = None
    enabled: bool | None = None
    environment_metrics: IdRef | None = None
    firmware_version: str | None = None
    indicator_led: str | None = None
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
    sku: str | None = None
    serial_number: str | None = None
    status: Status | None = None
    supported_protocols: list[Protocol] | None = None
    switch_type: str | None = None
    total_switch_width: str | None = None
    uuid: str | None = None


class Vcsswitch(RedfishModel):
    hdmdecoders: int | None = None
