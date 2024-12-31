from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class DeviceType(StrEnum):
    SINGLE_FUNCTION = "SingleFunction"
    MULTI_FUNCTION = "MultiFunction"
    SIMULATED = "Simulated"


class Links(RedfishModel):
    chassis: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass


class PcieDevice(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    description: str | None = None
    device_type: DeviceType | None = None
    environment_metrics: IdRef | None = None
    firmware_version: str | None = None
    links: Links | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    pcie_functions: IdRef | None = None
    pcie_interface: PcieInterface | None = None
    part_number: str | None = None
    ready_to_remove: str | None = None
    sku: str | None = None
    serial_number: str | None = None
    slot: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    uuid: str | None = None


class PcieErrors(RedfishModel):
    correctable_error_count: str | None = None
    fatal_error_count: str | None = None
    l0_to_recovery_count: str | None = None
    nakreceived_count: str | None = None
    naksent_count: str | None = None
    non_fatal_error_count: str | None = None
    replay_count: str | None = None
    replay_rollover_count: str | None = None


class PcieInterface(RedfishModel):
    lanes_in_use: str | None = None
    max_lanes: str | None = None
    max_pcie_type: str | None = None
    oem: dict[str, Any] | None = None
    pcie_type: str | None = None


class PcieTypes(StrEnum):
    GEN1 = "Gen1"
    GEN2 = "Gen2"
    GEN3 = "Gen3"
    GEN4 = "Gen4"
    GEN5 = "Gen5"
    GEN6 = "Gen6"
