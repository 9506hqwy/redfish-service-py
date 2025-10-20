from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .pcie_device import PcieInterface
from .resource import Identifier, Location, ResetType, Status
from .software_inventory import MeasurementBlock


class Actions(RedfishModel):
    reset: Reset | None = Field(serialization_alias="#NetworkAdapter.Reset", default=None)
    reset_settings_to_default: ResetSettingsToDefault | None = Field(
        serialization_alias="#NetworkAdapter.ResetSettingsToDefault", default=None
    )
    oem: dict[str, Any] | None = None


class ControllerCapabilities(RedfishModel):
    data_center_bridging: DataCenterBridging | None = None
    npar: NicPartitioning | None = Field(serialization_alias="NPAR", default=None)
    npiv: Npiv | None = Field(serialization_alias="NPIV", default=None)
    network_device_function_count: int | None = None
    network_port_count: int | None = None
    virtualization_offload: VirtualizationOffload | None = None


class ControllerLinks(RedfishModel):
    active_software_image: IdRef | None = None
    network_device_functions: list[IdRef] | None = None
    network_device_functions_odata_count: int | None = Field(
        serialization_alias="NetworkDeviceFunctions@odata.count", default=None
    )
    network_ports: list[IdRef] | None = None
    network_ports_odata_count: int | None = Field(
        serialization_alias="NetworkPorts@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_devices: list[IdRef] | None = Field(serialization_alias="PCIeDevices", default=None)
    pcie_devices_odata_count: int | None = Field(
        serialization_alias="PCIeDevices@odata.count", default=None
    )
    ports: list[IdRef] | None = None
    ports_odata_count: int | None = Field(serialization_alias="Ports@odata.count", default=None)
    software_images: list[IdRef] | None = None
    software_images_odata_count: int | None = Field(
        serialization_alias="SoftwareImages@odata.count", default=None
    )


class Controllers(RedfishModel):
    controller_capabilities: ControllerCapabilities | None = None
    firmware_package_version: str | None = None
    identifiers: list[Identifier] | None = None
    links: ControllerLinks | None = None
    location: Location | None = None
    pcie_interface: PcieInterface | None = Field(serialization_alias="PCIeInterface", default=None)


class DataCenterBridging(RedfishModel):
    capable: bool | None = None


class Npiv(RedfishModel):
    max_device_logins: int | None = None
    max_port_logins: int | None = None


class NetworkAdapter(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#NetworkAdapter.v1_13_0.NetworkAdapter"
    )
    actions: Actions | None = None
    assembly: IdRef | None = None
    certificates: IdRef | None = None
    controllers: list[Controllers] | None = None
    description: str | None = None
    environment_metrics: IdRef | None = None
    id: str
    identifiers: list[Identifier] | None = None
    lldp_enabled: bool | None = Field(serialization_alias="LLDPEnabled", default=None)
    location: Location | None = None
    manufacturer: str | None = None
    measurements: list[MeasurementBlock] | None = None
    metrics: IdRef | None = None
    model: str | None = None
    name: str
    network_device_functions: IdRef | None = None
    network_ports: IdRef | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    port_splitting: PortSplitting | None = None
    ports: IdRef | None = None
    processors: IdRef | None = None
    sku: str | None = Field(serialization_alias="SKU", default=None)
    serial_number: str | None = None
    status: Status | None = None


class NetworkAdapterOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    controllers: list[Controllers] | None = None
    identifiers: list[Identifier] | None = None
    lldp_enabled: bool | None = Field(serialization_alias="LLDPEnabled", default=None)
    location: Location | None = None
    measurements: list[MeasurementBlock] | None = None
    oem: dict[str, Any] | None = None
    port_splitting: PortSplitting | None = None
    status: Status | None = None


class NicPartitioning(RedfishModel):
    npar_capable: bool | None = None
    npar_enabled: bool | None = None


class PortSplitting(RedfishModel):
    current_configuration: list[PortSplittingSubconfiguration] | None = None
    maximum_subports: int | None = None
    maximum_subports_per_port: int | None = None
    supported_configurations: list[PortSplittingSubconfigurationList] | None = None


class PortSplittingSubconfiguration(RedfishModel):
    ending_physical_port: int | None = None
    first_subport_id: int | None = None
    lanes: list[int] | None = None
    link_speed_gbps: list[int] | None = None
    starting_physical_port: int | None = None
    subports_per_port: int | None = None


class PortSplittingSubconfigurationList(RedfishModel):
    subconfigurations: list[PortSplittingSubconfiguration] | None = None


class Reset(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetRequest(RedfishModel):
    reset_type: ResetType | None = None


class ResetSettingsToDefault(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class Sriov(RedfishModel):
    sriov_enabled: bool | None = Field(serialization_alias="SRIOVEnabled", default=None)
    sriovvepa_capable: bool | None = Field(serialization_alias="SRIOVVEPACapable", default=None)


class VirtualFunction(RedfishModel):
    device_max_count: int | None = None
    min_assignment_group_size: int | None = None
    network_port_max_count: int | None = None


class VirtualizationOffload(RedfishModel):
    sriov: Sriov | None = Field(serialization_alias="SRIOV", default=None)
    virtual_function: VirtualFunction | None = None
