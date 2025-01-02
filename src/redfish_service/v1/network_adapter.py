from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .pcie_device import PcieInterface
from .resource import Identifier, Location, Status
from .software_inventory import MeasurementBlock


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#NetworkAdapter.Reset", default=None)
    reset_settings_to_default: ResetSettingsToDefault | None = Field(
        alias="#NetworkAdapter.ResetSettingsToDefault", default=None
    )
    oem: dict[str, Any] | None = None


class ControllerCapabilities(RedfishModel):
    data_center_bridging: DataCenterBridging | None = None
    npar: NicPartitioning | None = Field(alias="NPAR", default=None)
    npiv: Npiv | None = Field(alias="NPIV", default=None)
    network_device_function_count: int | None = None
    network_port_count: int | None = None
    virtualization_offload: VirtualizationOffload | None = None


class ControllerLinks(RedfishModel):
    active_software_image: IdRef | None = None
    network_device_functions: list[IdRef] | None = None
    network_device_functions_odata_count: int | None = Field(
        alias="NetworkDeviceFunctions@odata.count", default=None
    )
    network_ports: list[IdRef] | None = None
    network_ports_odata_count: int | None = Field(alias="NetworkPorts@odata.count", default=None)
    oem: dict[str, Any] | None = None
    pcie_devices: list[IdRef] | None = Field(alias="PCIeDevices", default=None)
    pcie_devices_odata_count: int | None = Field(alias="PCIeDevices@odata.count", default=None)
    ports: list[IdRef] | None = None
    ports_odata_count: int | None = Field(alias="Ports@odata.count", default=None)
    software_images: list[IdRef] | None = None
    software_images_odata_count: int | None = Field(
        alias="SoftwareImages@odata.count", default=None
    )


class Controllers(RedfishModel):
    controller_capabilities: ControllerCapabilities | None = None
    firmware_package_version: str | None = None
    identifiers: list[Identifier] | None = None
    links: ControllerLinks | None = None
    location: Location | None = None
    pcie_interface: PcieInterface | None = Field(alias="PCIeInterface", default=None)


class DataCenterBridging(RedfishModel):
    capable: bool | None = None


class Npiv(RedfishModel):
    max_device_logins: int | None = None
    max_port_logins: int | None = None


class NetworkAdapter(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    certificates: IdRef | None = None
    controllers: list[Controllers] | None = None
    description: str | None = None
    environment_metrics: IdRef | None = None
    identifiers: list[Identifier] | None = None
    lldp_enabled: bool | None = Field(alias="LLDPEnabled", default=None)
    location: Location | None = None
    manufacturer: str | None = None
    measurements: list[MeasurementBlock] | None = None
    metrics: IdRef | None = None
    model: str | None = None
    network_device_functions: IdRef | None = None
    network_ports: IdRef | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    ports: IdRef | None = None
    processors: IdRef | None = None
    sku: str | None = Field(alias="SKU", default=None)
    serial_number: str | None = None
    status: Status | None = None


class NicPartitioning(RedfishModel):
    npar_capable: bool | None = None
    npar_enabled: bool | None = None


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ResetSettingsToDefault(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Sriov(RedfishModel):
    sriovvepa_capable: bool | None = Field(alias="SRIOVVEPACapable", default=None)


class VirtualFunction(RedfishModel):
    device_max_count: int | None = None
    min_assignment_group_size: int | None = None
    network_port_max_count: int | None = None


class VirtualizationOffload(RedfishModel):
    sriov: Sriov | None = Field(alias="SRIOV", default=None)
    virtual_function: VirtualFunction | None = None
