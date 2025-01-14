from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DeviceClass(StrEnum):
    UNCLASSIFIED_DEVICE = "UnclassifiedDevice"
    MASS_STORAGE_CONTROLLER = "MassStorageController"
    NETWORK_CONTROLLER = "NetworkController"
    DISPLAY_CONTROLLER = "DisplayController"
    MULTIMEDIA_CONTROLLER = "MultimediaController"
    MEMORY_CONTROLLER = "MemoryController"
    BRIDGE = "Bridge"
    COMMUNICATION_CONTROLLER = "CommunicationController"
    GENERIC_SYSTEM_PERIPHERAL = "GenericSystemPeripheral"
    INPUT_DEVICE_CONTROLLER = "InputDeviceController"
    DOCKING_STATION = "DockingStation"
    PROCESSOR = "Processor"
    SERIAL_BUS_CONTROLLER = "SerialBusController"
    WIRELESS_CONTROLLER = "WirelessController"
    INTELLIGENT_CONTROLLER = "IntelligentController"
    SATELLITE_COMMUNICATIONS_CONTROLLER = "SatelliteCommunicationsController"
    ENCRYPTION_CONTROLLER = "EncryptionController"
    SIGNAL_PROCESSING_CONTROLLER = "SignalProcessingController"
    PROCESSING_ACCELERATORS = "ProcessingAccelerators"
    NON_ESSENTIAL_INSTRUMENTATION = "NonEssentialInstrumentation"
    COPROCESSOR = "Coprocessor"
    UNASSIGNED_CLASS = "UnassignedClass"
    OTHER = "Other"


class FunctionProtocol(StrEnum):
    PCIE = "PCIe"
    CXL = "CXL"


class FunctionType(StrEnum):
    PHYSICAL = "Physical"
    VIRTUAL = "Virtual"


class Links(RedfishModel):
    cxl_logical_device: IdRef | None = Field(alias="CXLLogicalDevice", default=None)
    drives: list[IdRef] | None = None
    drives_odata_count: int | None = Field(alias="Drives@odata.count", default=None)
    ethernet_interfaces: list[IdRef] | None = None
    ethernet_interfaces_odata_count: int | None = Field(
        alias="EthernetInterfaces@odata.count", default=None
    )
    memory_domains: list[IdRef] | None = None
    memory_domains_odata_count: int | None = Field(alias="MemoryDomains@odata.count", default=None)
    network_device_functions: list[IdRef] | None = None
    network_device_functions_odata_count: int | None = Field(
        alias="NetworkDeviceFunctions@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_device: IdRef | None = Field(alias="PCIeDevice", default=None)
    processor: IdRef | None = None
    storage_controllers: list[IdRef] | None = None
    storage_controllers_odata_count: int | None = Field(
        alias="StorageControllers@odata.count", default=None
    )


class PcieFunction(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#PCIeFunction.v1_6_0.PCIeFunction")
    actions: Actions | None = None
    bus_number: str | None = None
    class_code: str | None = None
    description: str | None = None
    device_class: DeviceClass | None = None
    device_id: str | None = None
    device_number: str | None = None
    enabled: bool | None = None
    function_id: int | None = None
    function_number: str | None = None
    function_protocol: FunctionProtocol | None = None
    function_type: FunctionType | None = None
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    revision_id: str | None = None
    segment_number: str | None = None
    status: Status | None = None
    subsystem_id: str | None = None
    subsystem_vendor_id: str | None = None
    vendor_id: str | None = None


class PcieFunctionOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    enabled: bool | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
