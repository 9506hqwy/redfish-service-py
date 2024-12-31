from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .pcie_device import PcieInterface
from .resource import Identifier, Location, Status
from .software_inventory import MeasurementBlock


class Actions(RedfishResource):
    oem: OemActions | None = None


class ControllerCapabilities(RedfishResource):
    data_center_bridging: DataCenterBridging | None = None
    npar: NicPartitioning | None = None
    npiv: Npiv | None = None
    network_device_function_count: str | None = None
    network_port_count: str | None = None
    virtualization_offload: VirtualizationOffload | None = None


class ControllerLinks(RedfishResource):
    network_device_functions: list[IdRef] | None = None
    network_ports: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    pcie_devices: list[IdRef] | None = None
    ports: list[IdRef] | None = None


class Controllers(RedfishResource):
    controller_capabilities: ControllerCapabilities | None = None
    firmware_package_version: str | None = None
    identifiers: list[Identifier] | None = None
    links: ControllerLinks | None = None
    location: Location | None = None
    pcie_interface: PcieInterface | None = None


class DataCenterBridging(RedfishResource):
    capable: str | None = None


class Npiv(RedfishResource):
    max_device_logins: str | None = None
    max_port_logins: str | None = None


class NetworkAdapter(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    certificates: IdRef | None = None
    controllers: list[Controllers] | None = None
    description: str | None = None
    environment_metrics: IdRef | None = None
    identifiers: list[Identifier] | None = None
    lldpenabled: bool | None = None
    location: Location | None = None
    manufacturer: str | None = None
    measurements: list[MeasurementBlock] | None = None
    metrics: str | None = None
    model: str | None = None
    network_device_functions: IdRef | None = None
    network_ports: IdRef | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    ports: IdRef | None = None
    processors: IdRef | None = None
    sku: str | None = None
    serial_number: str | None = None
    status: Status | None = None


class NicPartitioning(RedfishResource):
    npar_capable: str | None = None
    npar_enabled: str | None = None


class OemActions(RedfishResource):
    pass


class ResetSettingsToDefault(RedfishResource):
    target: str | None = None
    title: str | None = None


class Sriov(RedfishResource):
    sriovvepacapable: str | None = None


class VirtualFunction(RedfishResource):
    device_max_count: str | None = None
    min_assignment_group_size: str | None = None
    network_port_max_count: str | None = None


class VirtualizationOffload(RedfishResource):
    sriov: Sriov | None = None
    virtual_function: VirtualFunction | None = None
