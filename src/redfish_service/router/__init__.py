from fastapi import FastAPI

from ..model.acceleration_function import AccelerationFunction
from ..model.acceleration_function_collection import AccelerationFunctionCollection
from ..model.account_service import AccountService
from ..model.address_pool import AddressPool
from ..model.address_pool_collection import AddressPoolCollection
from ..model.aggregate import Aggregate
from ..model.aggregate_collection import AggregateCollection
from ..model.aggregation_service import AggregationService
from ..model.aggregation_source import AggregationSource
from ..model.aggregation_source_collection import AggregationSourceCollection
from ..model.allow_deny import AllowDeny
from ..model.allow_deny_collection import AllowDenyCollection
from ..model.application import Application
from ..model.application_collection import ApplicationCollection
from ..model.assembly import Assembly
from ..model.battery import Battery
from ..model.battery_collection import BatteryCollection
from ..model.battery_metrics import BatteryMetrics
from ..model.bios import Bios
from ..model.boot_option import BootOption
from ..model.boot_option_collection import BootOptionCollection
from ..model.cable import Cable
from ..model.cable_collection import CableCollection
from ..model.certificate import Certificate
from ..model.certificate_collection import CertificateCollection
from ..model.certificate_locations import CertificateLocations
from ..model.certificate_service import CertificateService
from ..model.chassis import Chassis
from ..model.chassis_collection import ChassisCollection
from ..model.circuit import Circuit
from ..model.circuit_collection import CircuitCollection
from ..model.component_integrity import ComponentIntegrity
from ..model.component_integrity_collection import ComponentIntegrityCollection
from ..model.composition_reservation import CompositionReservation
from ..model.composition_reservation_collection import CompositionReservationCollection
from ..model.composition_service import CompositionService
from ..model.computer_system import ComputerSystem
from ..model.computer_system_collection import ComputerSystemCollection
from ..model.connection import Connection
from ..model.connection_collection import ConnectionCollection
from ..model.connection_method import ConnectionMethod
from ..model.connection_method_collection import ConnectionMethodCollection
from ..model.container import Container
from ..model.container_collection import ContainerCollection
from ..model.container_image import ContainerImage
from ..model.container_image_collection import ContainerImageCollection
from ..model.control import Control
from ..model.control_collection import ControlCollection
from ..model.coolant_connector import CoolantConnector
from ..model.coolant_connector_collection import CoolantConnectorCollection
from ..model.cooling_loop import CoolingLoop
from ..model.cooling_loop_collection import CoolingLoopCollection
from ..model.cooling_unit import CoolingUnit
from ..model.cooling_unit_collection import CoolingUnitCollection
from ..model.cxl_logical_device import CxlLogicalDevice
from ..model.cxl_logical_device_collection import CxlLogicalDeviceCollection
from ..model.drive import Drive
from ..model.drive_collection import DriveCollection
from ..model.drive_metrics import DriveMetrics
from ..model.endpoint import Endpoint
from ..model.endpoint_collection import EndpointCollection
from ..model.endpoint_group import EndpointGroup
from ..model.endpoint_group_collection import EndpointGroupCollection
from ..model.environment_metrics import EnvironmentMetrics
from ..model.ethernet_interface import EthernetInterface
from ..model.ethernet_interface_collection import EthernetInterfaceCollection
from ..model.event_destination import EventDestination
from ..model.event_destination_collection import EventDestinationCollection
from ..model.event_service import EventService
from ..model.external_account_provider import ExternalAccountProvider
from ..model.external_account_provider_collection import ExternalAccountProviderCollection
from ..model.fabric import Fabric
from ..model.fabric_adapter import FabricAdapter
from ..model.fabric_adapter_collection import FabricAdapterCollection
from ..model.fabric_collection import FabricCollection
from ..model.facility import Facility
from ..model.facility_collection import FacilityCollection
from ..model.fan import Fan
from ..model.fan_collection import FanCollection
from ..model.filter import Filter
from ..model.filter_collection import FilterCollection
from ..model.graphics_controller import GraphicsController
from ..model.graphics_controller_collection import GraphicsControllerCollection
from ..model.heater import Heater
from ..model.heater_collection import HeaterCollection
from ..model.heater_metrics import HeaterMetrics
from ..model.host_interface import HostInterface
from ..model.host_interface_collection import HostInterfaceCollection
from ..model.job import Job
from ..model.job_collection import JobCollection
from ..model.job_service import JobService
from ..model.json_schema_file import JsonSchemaFile
from ..model.json_schema_file_collection import JsonSchemaFileCollection
from ..model.key import Key
from ..model.key_collection import KeyCollection
from ..model.key_policy import KeyPolicy
from ..model.key_policy_collection import KeyPolicyCollection
from ..model.key_service import KeyService
from ..model.leak_detection import LeakDetection
from ..model.leak_detector import LeakDetector
from ..model.leak_detector_collection import LeakDetectorCollection
from ..model.license import License
from ..model.license_collection import LicenseCollection
from ..model.license_service import LicenseService
from ..model.log_entry import LogEntry
from ..model.log_entry_collection import LogEntryCollection
from ..model.log_service import LogService
from ..model.log_service_collection import LogServiceCollection
from ..model.manager import Manager
from ..model.manager_account import ManagerAccount
from ..model.manager_account_collection import ManagerAccountCollection
from ..model.manager_collection import ManagerCollection
from ..model.manager_diagnostic_data import ManagerDiagnosticData
from ..model.manager_network_protocol import ManagerNetworkProtocol
from ..model.media_controller import MediaController
from ..model.media_controller_collection import MediaControllerCollection
from ..model.memory import Memory
from ..model.memory_chunks import MemoryChunks
from ..model.memory_chunks_collection import MemoryChunksCollection
from ..model.memory_collection import MemoryCollection
from ..model.memory_domain import MemoryDomain
from ..model.memory_domain_collection import MemoryDomainCollection
from ..model.memory_metrics import MemoryMetrics
from ..model.memory_region import MemoryRegion
from ..model.memory_region_collection import MemoryRegionCollection
from ..model.message_registry_file import MessageRegistryFile
from ..model.message_registry_file_collection import MessageRegistryFileCollection
from ..model.metric_definition import MetricDefinition
from ..model.metric_definition_collection import MetricDefinitionCollection
from ..model.metric_report import MetricReport
from ..model.metric_report_collection import MetricReportCollection
from ..model.metric_report_definition import MetricReportDefinition
from ..model.metric_report_definition_collection import MetricReportDefinitionCollection
from ..model.network_adapter import NetworkAdapter
from ..model.network_adapter_collection import NetworkAdapterCollection
from ..model.network_adapter_metrics import NetworkAdapterMetrics
from ..model.network_device_function import NetworkDeviceFunction
from ..model.network_device_function_collection import NetworkDeviceFunctionCollection
from ..model.network_device_function_metrics import NetworkDeviceFunctionMetrics
from ..model.network_interface import NetworkInterface
from ..model.network_interface_collection import NetworkInterfaceCollection
from ..model.network_port import NetworkPort
from ..model.network_port_collection import NetworkPortCollection
from ..model.operating_config import OperatingConfig
from ..model.operating_config_collection import OperatingConfigCollection
from ..model.operating_system import OperatingSystem
from ..model.outbound_connection import OutboundConnection
from ..model.outbound_connection_collection import OutboundConnectionCollection
from ..model.outlet import Outlet
from ..model.outlet_collection import OutletCollection
from ..model.outlet_group import OutletGroup
from ..model.outlet_group_collection import OutletGroupCollection
from ..model.pcie_device import PcieDevice
from ..model.pcie_device_collection import PcieDeviceCollection
from ..model.pcie_function import PcieFunction
from ..model.pcie_function_collection import PcieFunctionCollection
from ..model.pcie_slots import PcieSlots
from ..model.port import Port
from ..model.port_collection import PortCollection
from ..model.port_metrics import PortMetrics
from ..model.power import Power
from ..model.power_distribution import PowerDistribution
from ..model.power_distribution_collection import PowerDistributionCollection
from ..model.power_distribution_metrics import PowerDistributionMetrics
from ..model.power_domain import PowerDomain
from ..model.power_domain_collection import PowerDomainCollection
from ..model.power_equipment import PowerEquipment
from ..model.power_subsystem import PowerSubsystem
from ..model.power_supply import PowerSupply
from ..model.power_supply_collection import PowerSupplyCollection
from ..model.power_supply_metrics import PowerSupplyMetrics
from ..model.processor import Processor
from ..model.processor_collection import ProcessorCollection
from ..model.processor_metrics import ProcessorMetrics
from ..model.pump import Pump
from ..model.pump_collection import PumpCollection
from ..model.registered_client import RegisteredClient
from ..model.registered_client_collection import RegisteredClientCollection
from ..model.reservoir import Reservoir
from ..model.reservoir_collection import ReservoirCollection
from ..model.resource_block import ResourceBlock
from ..model.resource_block_collection import ResourceBlockCollection
from ..model.role import Role
from ..model.role_collection import RoleCollection
from ..model.route_entry import RouteEntry
from ..model.route_entry_collection import RouteEntryCollection
from ..model.route_set_entry import RouteSetEntry
from ..model.route_set_entry_collection import RouteSetEntryCollection
from ..model.secure_boot import SecureBoot
from ..model.secure_boot_database import SecureBootDatabase
from ..model.secure_boot_database_collection import SecureBootDatabaseCollection
from ..model.security_policy import SecurityPolicy
from ..model.sensor import Sensor
from ..model.sensor_collection import SensorCollection
from ..model.serial_interface import SerialInterface
from ..model.serial_interface_collection import SerialInterfaceCollection
from ..model.service_conditions import ServiceConditions
from ..model.service_root import ServiceRoot
from ..model.session import Session
from ..model.session_collection import SessionCollection
from ..model.session_service import SessionService
from ..model.signature import Signature
from ..model.signature_collection import SignatureCollection
from ..model.simple_storage import SimpleStorage
from ..model.simple_storage_collection import SimpleStorageCollection
from ..model.software_inventory import SoftwareInventory
from ..model.software_inventory_collection import SoftwareInventoryCollection
from ..model.storage import Storage
from ..model.storage_collection import StorageCollection
from ..model.storage_controller import StorageController
from ..model.storage_controller_collection import StorageControllerCollection
from ..model.storage_controller_metrics import StorageControllerMetrics
from ..model.storage_metrics import StorageMetrics
from ..model.switch import Switch
from ..model.switch_collection import SwitchCollection
from ..model.switch_metrics import SwitchMetrics
from ..model.swordfish.volume import Volume
from ..model.task import Task
from ..model.task_collection import TaskCollection
from ..model.task_service import TaskService
from ..model.telemetry_service import TelemetryService
from ..model.thermal import Thermal
from ..model.thermal_equipment import ThermalEquipment
from ..model.thermal_metrics import ThermalMetrics
from ..model.thermal_subsystem import ThermalSubsystem
from ..model.triggers import Triggers
from ..model.triggers_collection import TriggersCollection
from ..model.trusted_component import TrustedComponent
from ..model.trusted_component_collection import TrustedComponentCollection
from ..model.update_service import UpdateService
from ..model.usb_controller import UsbController
from ..model.usb_controller_collection import UsbControllerCollection
from ..model.vcat_entry import VcatEntry
from ..model.vcat_entry_collection import VcatEntryCollection
from ..model.virtual_media import VirtualMedia
from ..model.virtual_media_collection import VirtualMediaCollection
from ..model.vlan_network_interface import VlanNetworkInterface
from ..model.vlan_network_interface_collection import VlanNetworkInterfaceCollection
from ..model.volume_collection import VolumeCollection
from ..model.zone import Zone
from ..model.zone_collection import ZoneCollection
from ..service import find_service
from . import (
    acceleration_function,
    acceleration_function_collection,
    account_service,
    address_pool,
    address_pool_collection,
    aggregate,
    aggregate_collection,
    aggregation_service,
    aggregation_source,
    aggregation_source_collection,
    allow_deny,
    allow_deny_collection,
    application,
    application_collection,
    assembly,
    battery,
    battery_collection,
    battery_metrics,
    bios,
    boot_option,
    boot_option_collection,
    cable,
    cable_collection,
    certificate,
    certificate_collection,
    certificate_locations,
    certificate_service,
    chassis,
    chassis_collection,
    circuit,
    circuit_collection,
    component_integrity,
    component_integrity_collection,
    composition_reservation,
    composition_reservation_collection,
    composition_service,
    computer_system,
    computer_system_collection,
    connection,
    connection_collection,
    connection_method,
    connection_method_collection,
    container,
    container_collection,
    container_image,
    container_image_collection,
    control,
    control_collection,
    coolant_connector,
    coolant_connector_collection,
    cooling_loop,
    cooling_loop_collection,
    cooling_unit,
    cooling_unit_collection,
    cxl_logical_device,
    cxl_logical_device_collection,
    drive,
    drive_collection,
    drive_metrics,
    endpoint,
    endpoint_collection,
    endpoint_group,
    endpoint_group_collection,
    environment_metrics,
    ethernet_interface,
    ethernet_interface_collection,
    event_destination,
    event_destination_collection,
    event_service,
    external_account_provider,
    external_account_provider_collection,
    fabric,
    fabric_adapter,
    fabric_adapter_collection,
    fabric_collection,
    facility,
    facility_collection,
    fan,
    fan_collection,
    filter,
    filter_collection,
    graphics_controller,
    graphics_controller_collection,
    heater,
    heater_collection,
    heater_metrics,
    host_interface,
    host_interface_collection,
    job,
    job_collection,
    job_service,
    json_schema_file,
    json_schema_file_collection,
    key,
    key_collection,
    key_policy,
    key_policy_collection,
    key_service,
    leak_detection,
    leak_detector,
    leak_detector_collection,
    license,
    license_collection,
    license_service,
    log_entry,
    log_entry_collection,
    log_service,
    log_service_collection,
    manager,
    manager_account,
    manager_account_collection,
    manager_collection,
    manager_diagnostic_data,
    manager_network_protocol,
    media_controller,
    media_controller_collection,
    memory,
    memory_chunks,
    memory_chunks_collection,
    memory_collection,
    memory_domain,
    memory_domain_collection,
    memory_metrics,
    memory_region,
    memory_region_collection,
    message_registry_file,
    message_registry_file_collection,
    metric_definition,
    metric_definition_collection,
    metric_report,
    metric_report_collection,
    metric_report_definition,
    metric_report_definition_collection,
    network_adapter,
    network_adapter_collection,
    network_adapter_metrics,
    network_device_function,
    network_device_function_collection,
    network_device_function_metrics,
    network_interface,
    network_interface_collection,
    network_port,
    network_port_collection,
    operating_config,
    operating_config_collection,
    operating_system,
    outbound_connection,
    outbound_connection_collection,
    outlet,
    outlet_collection,
    outlet_group,
    outlet_group_collection,
    pcie_device,
    pcie_device_collection,
    pcie_function,
    pcie_function_collection,
    pcie_slots,
    port,
    port_collection,
    port_metrics,
    power,
    power_distribution,
    power_distribution_collection,
    power_distribution_metrics,
    power_domain,
    power_domain_collection,
    power_equipment,
    power_subsystem,
    power_supply,
    power_supply_collection,
    power_supply_metrics,
    processor,
    processor_collection,
    processor_metrics,
    pump,
    pump_collection,
    registered_client,
    registered_client_collection,
    reservoir,
    reservoir_collection,
    resource_block,
    resource_block_collection,
    role,
    role_collection,
    route_entry,
    route_entry_collection,
    route_set_entry,
    route_set_entry_collection,
    secure_boot,
    secure_boot_database,
    secure_boot_database_collection,
    security_policy,
    sensor,
    sensor_collection,
    serial_interface,
    serial_interface_collection,
    service_conditions,
    service_root,
    session,
    session_collection,
    session_service,
    signature,
    signature_collection,
    simple_storage,
    simple_storage_collection,
    software_inventory,
    software_inventory_collection,
    storage,
    storage_collection,
    storage_controller,
    storage_controller_collection,
    storage_controller_metrics,
    storage_metrics,
    switch,
    switch_collection,
    switch_metrics,
    task,
    task_collection,
    task_service,
    telemetry_service,
    thermal,
    thermal_equipment,
    thermal_metrics,
    thermal_subsystem,
    triggers,
    triggers_collection,
    trusted_component,
    trusted_component_collection,
    update_service,
    usb_controller,
    usb_controller_collection,
    vcat_entry,
    vcat_entry_collection,
    virtual_media,
    virtual_media_collection,
    vlan_network_interface,
    vlan_network_interface_collection,
    volume,
    volume_collection,
    zone,
    zone_collection,
)


def include_router(app: FastAPI) -> None:  # noqa: PLR0912, PLR0915
    if find_service(AccelerationFunction):
        app.include_router(acceleration_function.router)

    if find_service(AccelerationFunctionCollection):
        app.include_router(acceleration_function_collection.router)

    if find_service(AccountService):
        app.include_router(account_service.router)

    if find_service(AddressPool):
        app.include_router(address_pool.router)

    if find_service(AddressPoolCollection):
        app.include_router(address_pool_collection.router)

    if find_service(Aggregate):
        app.include_router(aggregate.router)

    if find_service(AggregateCollection):
        app.include_router(aggregate_collection.router)

    if find_service(AggregationService):
        app.include_router(aggregation_service.router)

    if find_service(AggregationSource):
        app.include_router(aggregation_source.router)

    if find_service(AggregationSourceCollection):
        app.include_router(aggregation_source_collection.router)

    if find_service(AllowDeny):
        app.include_router(allow_deny.router)

    if find_service(AllowDenyCollection):
        app.include_router(allow_deny_collection.router)

    if find_service(Application):
        app.include_router(application.router)

    if find_service(ApplicationCollection):
        app.include_router(application_collection.router)

    if find_service(Assembly):
        app.include_router(assembly.router)

    if find_service(Battery):
        app.include_router(battery.router)

    if find_service(BatteryCollection):
        app.include_router(battery_collection.router)

    if find_service(BatteryMetrics):
        app.include_router(battery_metrics.router)

    if find_service(Bios):
        app.include_router(bios.router)

    if find_service(BootOption):
        app.include_router(boot_option.router)

    if find_service(BootOptionCollection):
        app.include_router(boot_option_collection.router)

    if find_service(Cable):
        app.include_router(cable.router)

    if find_service(CableCollection):
        app.include_router(cable_collection.router)

    if find_service(Certificate):
        app.include_router(certificate.router)

    if find_service(CertificateCollection):
        app.include_router(certificate_collection.router)

    if find_service(CertificateLocations):
        app.include_router(certificate_locations.router)

    if find_service(CertificateService):
        app.include_router(certificate_service.router)

    if find_service(Chassis):
        app.include_router(chassis.router)

    if find_service(ChassisCollection):
        app.include_router(chassis_collection.router)

    if find_service(Circuit):
        app.include_router(circuit.router)

    if find_service(CircuitCollection):
        app.include_router(circuit_collection.router)

    if find_service(ComponentIntegrity):
        app.include_router(component_integrity.router)

    if find_service(ComponentIntegrityCollection):
        app.include_router(component_integrity_collection.router)

    if find_service(CompositionReservation):
        app.include_router(composition_reservation.router)

    if find_service(CompositionReservationCollection):
        app.include_router(composition_reservation_collection.router)

    if find_service(CompositionService):
        app.include_router(composition_service.router)

    if find_service(ComputerSystem):
        app.include_router(computer_system.router)

    if find_service(ComputerSystemCollection):
        app.include_router(computer_system_collection.router)

    if find_service(Connection):
        app.include_router(connection.router)

    if find_service(ConnectionCollection):
        app.include_router(connection_collection.router)

    if find_service(ConnectionMethod):
        app.include_router(connection_method.router)

    if find_service(ConnectionMethodCollection):
        app.include_router(connection_method_collection.router)

    if find_service(Container):
        app.include_router(container.router)

    if find_service(ContainerCollection):
        app.include_router(container_collection.router)

    if find_service(ContainerImage):
        app.include_router(container_image.router)

    if find_service(ContainerImageCollection):
        app.include_router(container_image_collection.router)

    if find_service(Control):
        app.include_router(control.router)

    if find_service(ControlCollection):
        app.include_router(control_collection.router)

    if find_service(CoolantConnector):
        app.include_router(coolant_connector.router)

    if find_service(CoolantConnectorCollection):
        app.include_router(coolant_connector_collection.router)

    if find_service(CoolingLoop):
        app.include_router(cooling_loop.router)

    if find_service(CoolingLoopCollection):
        app.include_router(cooling_loop_collection.router)

    if find_service(CoolingUnit):
        app.include_router(cooling_unit.router)

    if find_service(CoolingUnitCollection):
        app.include_router(cooling_unit_collection.router)

    if find_service(CxlLogicalDevice):
        app.include_router(cxl_logical_device.router)

    if find_service(CxlLogicalDeviceCollection):
        app.include_router(cxl_logical_device_collection.router)

    if find_service(Drive):
        app.include_router(drive.router)

    if find_service(DriveCollection):
        app.include_router(drive_collection.router)

    if find_service(DriveMetrics):
        app.include_router(drive_metrics.router)

    if find_service(Endpoint):
        app.include_router(endpoint.router)

    if find_service(EndpointCollection):
        app.include_router(endpoint_collection.router)

    if find_service(EndpointGroup):
        app.include_router(endpoint_group.router)

    if find_service(EndpointGroupCollection):
        app.include_router(endpoint_group_collection.router)

    if find_service(EnvironmentMetrics):
        app.include_router(environment_metrics.router)

    if find_service(EthernetInterface):
        app.include_router(ethernet_interface.router)

    if find_service(EthernetInterfaceCollection):
        app.include_router(ethernet_interface_collection.router)

    if find_service(EventDestination):
        app.include_router(event_destination.router)

    if find_service(EventDestinationCollection):
        app.include_router(event_destination_collection.router)

    if find_service(EventService):
        app.include_router(event_service.router)

    if find_service(ExternalAccountProvider):
        app.include_router(external_account_provider.router)

    if find_service(ExternalAccountProviderCollection):
        app.include_router(external_account_provider_collection.router)

    if find_service(Fabric):
        app.include_router(fabric.router)

    if find_service(FabricAdapter):
        app.include_router(fabric_adapter.router)

    if find_service(FabricAdapterCollection):
        app.include_router(fabric_adapter_collection.router)

    if find_service(FabricCollection):
        app.include_router(fabric_collection.router)

    if find_service(Facility):
        app.include_router(facility.router)

    if find_service(FacilityCollection):
        app.include_router(facility_collection.router)

    if find_service(Fan):
        app.include_router(fan.router)

    if find_service(FanCollection):
        app.include_router(fan_collection.router)

    if find_service(Filter):
        app.include_router(filter.router)

    if find_service(FilterCollection):
        app.include_router(filter_collection.router)

    if find_service(GraphicsController):
        app.include_router(graphics_controller.router)

    if find_service(GraphicsControllerCollection):
        app.include_router(graphics_controller_collection.router)

    if find_service(Heater):
        app.include_router(heater.router)

    if find_service(HeaterCollection):
        app.include_router(heater_collection.router)

    if find_service(HeaterMetrics):
        app.include_router(heater_metrics.router)

    if find_service(HostInterface):
        app.include_router(host_interface.router)

    if find_service(HostInterfaceCollection):
        app.include_router(host_interface_collection.router)

    if find_service(Job):
        app.include_router(job.router)

    if find_service(JobCollection):
        app.include_router(job_collection.router)

    if find_service(JobService):
        app.include_router(job_service.router)

    if find_service(JsonSchemaFile):
        app.include_router(json_schema_file.router)

    if find_service(JsonSchemaFileCollection):
        app.include_router(json_schema_file_collection.router)

    if find_service(Key):
        app.include_router(key.router)

    if find_service(KeyCollection):
        app.include_router(key_collection.router)

    if find_service(KeyPolicy):
        app.include_router(key_policy.router)

    if find_service(KeyPolicyCollection):
        app.include_router(key_policy_collection.router)

    if find_service(KeyService):
        app.include_router(key_service.router)

    if find_service(LeakDetection):
        app.include_router(leak_detection.router)

    if find_service(LeakDetector):
        app.include_router(leak_detector.router)

    if find_service(LeakDetectorCollection):
        app.include_router(leak_detector_collection.router)

    if find_service(License):
        app.include_router(license.router)

    if find_service(LicenseCollection):
        app.include_router(license_collection.router)

    if find_service(LicenseService):
        app.include_router(license_service.router)

    if find_service(LogEntry):
        app.include_router(log_entry.router)

    if find_service(LogEntryCollection):
        app.include_router(log_entry_collection.router)

    if find_service(LogService):
        app.include_router(log_service.router)

    if find_service(LogServiceCollection):
        app.include_router(log_service_collection.router)

    if find_service(Manager):
        app.include_router(manager.router)

    if find_service(ManagerAccount):
        app.include_router(manager_account.router)

    if find_service(ManagerAccountCollection):
        app.include_router(manager_account_collection.router)

    if find_service(ManagerCollection):
        app.include_router(manager_collection.router)

    if find_service(ManagerDiagnosticData):
        app.include_router(manager_diagnostic_data.router)

    if find_service(ManagerNetworkProtocol):
        app.include_router(manager_network_protocol.router)

    if find_service(MediaController):
        app.include_router(media_controller.router)

    if find_service(MediaControllerCollection):
        app.include_router(media_controller_collection.router)

    if find_service(Memory):
        app.include_router(memory.router)

    if find_service(MemoryChunks):
        app.include_router(memory_chunks.router)

    if find_service(MemoryChunksCollection):
        app.include_router(memory_chunks_collection.router)

    if find_service(MemoryCollection):
        app.include_router(memory_collection.router)

    if find_service(MemoryDomain):
        app.include_router(memory_domain.router)

    if find_service(MemoryDomainCollection):
        app.include_router(memory_domain_collection.router)

    if find_service(MemoryMetrics):
        app.include_router(memory_metrics.router)

    if find_service(MemoryRegion):
        app.include_router(memory_region.router)

    if find_service(MemoryRegionCollection):
        app.include_router(memory_region_collection.router)

    if find_service(MessageRegistryFile):
        app.include_router(message_registry_file.router)

    if find_service(MessageRegistryFileCollection):
        app.include_router(message_registry_file_collection.router)

    if find_service(MetricDefinition):
        app.include_router(metric_definition.router)

    if find_service(MetricDefinitionCollection):
        app.include_router(metric_definition_collection.router)

    if find_service(MetricReport):
        app.include_router(metric_report.router)

    if find_service(MetricReportCollection):
        app.include_router(metric_report_collection.router)

    if find_service(MetricReportDefinition):
        app.include_router(metric_report_definition.router)

    if find_service(MetricReportDefinitionCollection):
        app.include_router(metric_report_definition_collection.router)

    if find_service(NetworkAdapter):
        app.include_router(network_adapter.router)

    if find_service(NetworkAdapterCollection):
        app.include_router(network_adapter_collection.router)

    if find_service(NetworkAdapterMetrics):
        app.include_router(network_adapter_metrics.router)

    if find_service(NetworkDeviceFunction):
        app.include_router(network_device_function.router)

    if find_service(NetworkDeviceFunctionCollection):
        app.include_router(network_device_function_collection.router)

    if find_service(NetworkDeviceFunctionMetrics):
        app.include_router(network_device_function_metrics.router)

    if find_service(NetworkInterface):
        app.include_router(network_interface.router)

    if find_service(NetworkInterfaceCollection):
        app.include_router(network_interface_collection.router)

    if find_service(NetworkPort):
        app.include_router(network_port.router)

    if find_service(NetworkPortCollection):
        app.include_router(network_port_collection.router)

    if find_service(OperatingConfig):
        app.include_router(operating_config.router)

    if find_service(OperatingConfigCollection):
        app.include_router(operating_config_collection.router)

    if find_service(OperatingSystem):
        app.include_router(operating_system.router)

    if find_service(OutboundConnection):
        app.include_router(outbound_connection.router)

    if find_service(OutboundConnectionCollection):
        app.include_router(outbound_connection_collection.router)

    if find_service(Outlet):
        app.include_router(outlet.router)

    if find_service(OutletCollection):
        app.include_router(outlet_collection.router)

    if find_service(OutletGroup):
        app.include_router(outlet_group.router)

    if find_service(OutletGroupCollection):
        app.include_router(outlet_group_collection.router)

    if find_service(PcieDevice):
        app.include_router(pcie_device.router)

    if find_service(PcieDeviceCollection):
        app.include_router(pcie_device_collection.router)

    if find_service(PcieFunction):
        app.include_router(pcie_function.router)

    if find_service(PcieFunctionCollection):
        app.include_router(pcie_function_collection.router)

    if find_service(PcieSlots):
        app.include_router(pcie_slots.router)

    if find_service(Port):
        app.include_router(port.router)

    if find_service(PortCollection):
        app.include_router(port_collection.router)

    if find_service(PortMetrics):
        app.include_router(port_metrics.router)

    if find_service(Power):
        app.include_router(power.router)

    if find_service(PowerDistribution):
        app.include_router(power_distribution.router)

    if find_service(PowerDistributionCollection):
        app.include_router(power_distribution_collection.router)

    if find_service(PowerDistributionMetrics):
        app.include_router(power_distribution_metrics.router)

    if find_service(PowerDomain):
        app.include_router(power_domain.router)

    if find_service(PowerDomainCollection):
        app.include_router(power_domain_collection.router)

    if find_service(PowerEquipment):
        app.include_router(power_equipment.router)

    if find_service(PowerSubsystem):
        app.include_router(power_subsystem.router)

    if find_service(PowerSupply):
        app.include_router(power_supply.router)

    if find_service(PowerSupplyCollection):
        app.include_router(power_supply_collection.router)

    if find_service(PowerSupplyMetrics):
        app.include_router(power_supply_metrics.router)

    if find_service(Processor):
        app.include_router(processor.router)

    if find_service(ProcessorCollection):
        app.include_router(processor_collection.router)

    if find_service(ProcessorMetrics):
        app.include_router(processor_metrics.router)

    if find_service(Pump):
        app.include_router(pump.router)

    if find_service(PumpCollection):
        app.include_router(pump_collection.router)

    if find_service(RegisteredClient):
        app.include_router(registered_client.router)

    if find_service(RegisteredClientCollection):
        app.include_router(registered_client_collection.router)

    if find_service(Reservoir):
        app.include_router(reservoir.router)

    if find_service(ReservoirCollection):
        app.include_router(reservoir_collection.router)

    if find_service(ResourceBlock):
        app.include_router(resource_block.router)

    if find_service(ResourceBlockCollection):
        app.include_router(resource_block_collection.router)

    if find_service(Role):
        app.include_router(role.router)

    if find_service(RoleCollection):
        app.include_router(role_collection.router)

    if find_service(RouteEntry):
        app.include_router(route_entry.router)

    if find_service(RouteEntryCollection):
        app.include_router(route_entry_collection.router)

    if find_service(RouteSetEntry):
        app.include_router(route_set_entry.router)

    if find_service(RouteSetEntryCollection):
        app.include_router(route_set_entry_collection.router)

    if find_service(SecureBoot):
        app.include_router(secure_boot.router)

    if find_service(SecureBootDatabase):
        app.include_router(secure_boot_database.router)

    if find_service(SecureBootDatabaseCollection):
        app.include_router(secure_boot_database_collection.router)

    if find_service(SecurityPolicy):
        app.include_router(security_policy.router)

    if find_service(Sensor):
        app.include_router(sensor.router)

    if find_service(SensorCollection):
        app.include_router(sensor_collection.router)

    if find_service(SerialInterface):
        app.include_router(serial_interface.router)

    if find_service(SerialInterfaceCollection):
        app.include_router(serial_interface_collection.router)

    if find_service(ServiceConditions):
        app.include_router(service_conditions.router)

    if find_service(ServiceRoot):
        app.include_router(service_root.router)

    if find_service(Session):
        app.include_router(session.router)

    if find_service(SessionCollection):
        app.include_router(session_collection.router)

    if find_service(SessionService):
        app.include_router(session_service.router)

    if find_service(Signature):
        app.include_router(signature.router)

    if find_service(SignatureCollection):
        app.include_router(signature_collection.router)

    if find_service(SimpleStorage):
        app.include_router(simple_storage.router)

    if find_service(SimpleStorageCollection):
        app.include_router(simple_storage_collection.router)

    if find_service(SoftwareInventory):
        app.include_router(software_inventory.router)

    if find_service(SoftwareInventoryCollection):
        app.include_router(software_inventory_collection.router)

    if find_service(Storage):
        app.include_router(storage.router)

    if find_service(StorageCollection):
        app.include_router(storage_collection.router)

    if find_service(StorageController):
        app.include_router(storage_controller.router)

    if find_service(StorageControllerCollection):
        app.include_router(storage_controller_collection.router)

    if find_service(StorageControllerMetrics):
        app.include_router(storage_controller_metrics.router)

    if find_service(StorageMetrics):
        app.include_router(storage_metrics.router)

    if find_service(Switch):
        app.include_router(switch.router)

    if find_service(SwitchCollection):
        app.include_router(switch_collection.router)

    if find_service(SwitchMetrics):
        app.include_router(switch_metrics.router)

    if find_service(Task):
        app.include_router(task.router)

    if find_service(TaskCollection):
        app.include_router(task_collection.router)

    if find_service(TaskService):
        app.include_router(task_service.router)

    if find_service(TelemetryService):
        app.include_router(telemetry_service.router)

    if find_service(Thermal):
        app.include_router(thermal.router)

    if find_service(ThermalEquipment):
        app.include_router(thermal_equipment.router)

    if find_service(ThermalMetrics):
        app.include_router(thermal_metrics.router)

    if find_service(ThermalSubsystem):
        app.include_router(thermal_subsystem.router)

    if find_service(Triggers):
        app.include_router(triggers.router)

    if find_service(TriggersCollection):
        app.include_router(triggers_collection.router)

    if find_service(TrustedComponent):
        app.include_router(trusted_component.router)

    if find_service(TrustedComponentCollection):
        app.include_router(trusted_component_collection.router)

    if find_service(UpdateService):
        app.include_router(update_service.router)

    if find_service(UsbController):
        app.include_router(usb_controller.router)

    if find_service(UsbControllerCollection):
        app.include_router(usb_controller_collection.router)

    if find_service(VcatEntry):
        app.include_router(vcat_entry.router)

    if find_service(VcatEntryCollection):
        app.include_router(vcat_entry_collection.router)

    if find_service(VirtualMedia):
        app.include_router(virtual_media.router)

    if find_service(VirtualMediaCollection):
        app.include_router(virtual_media_collection.router)

    if find_service(VlanNetworkInterface):
        app.include_router(vlan_network_interface.router)

    if find_service(VlanNetworkInterfaceCollection):
        app.include_router(vlan_network_interface_collection.router)

    if find_service(Volume):
        app.include_router(volume.router)

    if find_service(VolumeCollection):
        app.include_router(volume_collection.router)

    if find_service(Zone):
        app.include_router(zone.router)

    if find_service(ZoneCollection):
        app.include_router(zone_collection.router)
