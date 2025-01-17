from fastapi import FastAPI

from ...model.swordfish.capacity import CapacitySource
from ...model.swordfish.capacity_source_collection import CapacitySourceCollection
from ...model.swordfish.class_of_service import ClassOfService
from ...model.swordfish.class_of_service_collection import ClassOfServiceCollection
from ...model.swordfish.consistency_group import ConsistencyGroup
from ...model.swordfish.consistency_group_collection import ConsistencyGroupCollection
from ...model.swordfish.data_protection_line_of_service import DataProtectionLineOfService
from ...model.swordfish.data_protection_los_capabilities import DataProtectionLosCapabilities
from ...model.swordfish.data_security_line_of_service import DataSecurityLineOfService
from ...model.swordfish.data_security_los_capabilities import DataSecurityLosCapabilities
from ...model.swordfish.data_storage_line_of_service import DataStorageLineOfService
from ...model.swordfish.data_storage_los_capabilities import DataStorageLosCapabilities
from ...model.swordfish.file_share import FileShare
from ...model.swordfish.file_share_collection import FileShareCollection
from ...model.swordfish.file_system import FileSystem
from ...model.swordfish.file_system_collection import FileSystemCollection
from ...model.swordfish.file_system_metrics import FileSystemMetrics
from ...model.swordfish.hosted_storage_services import HostedStorageServices
from ...model.swordfish.io_connectivity_line_of_service import IoConnectivityLineOfService
from ...model.swordfish.io_connectivity_los_capabilities import IoConnectivityLosCapabilities
from ...model.swordfish.io_performance_line_of_service import IoPerformanceLineOfService
from ...model.swordfish.io_performance_los_capabilities import IoPerformanceLosCapabilities
from ...model.swordfish.line_of_service_collection import LineOfServiceCollection
from ...model.swordfish.nvme_domain import NvmeDomain
from ...model.swordfish.nvme_domain_collection import NvmeDomainCollection
from ...model.swordfish.nvme_firmware_image import NvmeFirmwareImage
from ...model.swordfish.storage_group import StorageGroup
from ...model.swordfish.storage_group_collection import StorageGroupCollection
from ...model.swordfish.storage_pool import StoragePool
from ...model.swordfish.storage_pool_collection import StoragePoolCollection
from ...model.swordfish.storage_pool_metrics import StoragePoolMetrics
from ...model.swordfish.storage_service import StorageService
from ...model.swordfish.storage_service_collection import StorageServiceCollection
from ...model.swordfish.storage_service_metrics import StorageServiceMetrics
from ...model.swordfish.storage_system_collection import StorageSystemCollection
from ...model.swordfish.volume import Volume
from ...model.swordfish.volume_collection import VolumeCollection
from ...model.swordfish.volume_metrics import VolumeMetrics
from ...service import find_service
from . import (
    capacity,
    capacity_source_collection,
    class_of_service,
    class_of_service_collection,
    consistency_group,
    consistency_group_collection,
    data_protection_line_of_service,
    data_protection_los_capabilities,
    data_security_line_of_service,
    data_security_los_capabilities,
    data_storage_line_of_service,
    data_storage_los_capabilities,
    file_share,
    file_share_collection,
    file_system,
    file_system_collection,
    file_system_metrics,
    hosted_storage_services,
    io_connectivity_line_of_service,
    io_connectivity_los_capabilities,
    io_performance_line_of_service,
    io_performance_los_capabilities,
    line_of_service_collection,
    nvme_domain,
    nvme_domain_collection,
    nvme_firmware_image,
    storage_group,
    storage_group_collection,
    storage_pool,
    storage_pool_collection,
    storage_pool_metrics,
    storage_service,
    storage_service_collection,
    storage_service_metrics,
    storage_system_collection,
    volume,
    volume_collection,
    volume_metrics,
)


def include_router(app: FastAPI) -> None:
    if find_service(CapacitySource):
        app.include_router(capacity.router)

    if find_service(CapacitySourceCollection):
        app.include_router(capacity_source_collection.router)

    if find_service(ClassOfService):
        app.include_router(class_of_service.router)

    if find_service(ClassOfServiceCollection):
        app.include_router(class_of_service_collection.router)

    if find_service(ConsistencyGroup):
        app.include_router(consistency_group.router)

    if find_service(ConsistencyGroupCollection):
        app.include_router(consistency_group_collection.router)

    if find_service(DataProtectionLineOfService):
        app.include_router(data_protection_line_of_service.router)

    if find_service(DataProtectionLosCapabilities):
        app.include_router(data_protection_los_capabilities.router)

    if find_service(DataSecurityLineOfService):
        app.include_router(data_security_line_of_service.router)

    if find_service(DataSecurityLosCapabilities):
        app.include_router(data_security_los_capabilities.router)

    if find_service(DataStorageLineOfService):
        app.include_router(data_storage_line_of_service.router)

    if find_service(DataStorageLosCapabilities):
        app.include_router(data_storage_los_capabilities.router)

    if find_service(FileShare):
        app.include_router(file_share.router)

    if find_service(FileShareCollection):
        app.include_router(file_share_collection.router)

    if find_service(FileSystem):
        app.include_router(file_system.router)

    if find_service(FileSystemCollection):
        app.include_router(file_system_collection.router)

    if find_service(FileSystemMetrics):
        app.include_router(file_system_metrics.router)

    if find_service(HostedStorageServices):
        app.include_router(hosted_storage_services.router)

    if find_service(IoConnectivityLineOfService):
        app.include_router(io_connectivity_line_of_service.router)

    if find_service(IoConnectivityLosCapabilities):
        app.include_router(io_connectivity_los_capabilities.router)

    if find_service(IoPerformanceLineOfService):
        app.include_router(io_performance_line_of_service.router)

    if find_service(IoPerformanceLosCapabilities):
        app.include_router(io_performance_los_capabilities.router)

    if find_service(LineOfServiceCollection):
        app.include_router(line_of_service_collection.router)

    if find_service(NvmeDomain):
        app.include_router(nvme_domain.router)

    if find_service(NvmeDomainCollection):
        app.include_router(nvme_domain_collection.router)

    if find_service(NvmeFirmwareImage):
        app.include_router(nvme_firmware_image.router)

    if find_service(StorageGroup):
        app.include_router(storage_group.router)

    if find_service(StorageGroupCollection):
        app.include_router(storage_group_collection.router)

    if find_service(StoragePool):
        app.include_router(storage_pool.router)

    if find_service(StoragePoolCollection):
        app.include_router(storage_pool_collection.router)

    if find_service(StoragePoolMetrics):
        app.include_router(storage_pool_metrics.router)

    if find_service(StorageService):
        app.include_router(storage_service.router)

    if find_service(StorageServiceCollection):
        app.include_router(storage_service_collection.router)

    if find_service(StorageServiceMetrics):
        app.include_router(storage_service_metrics.router)

    if find_service(StorageSystemCollection):
        app.include_router(storage_system_collection.router)

    if find_service(Volume):
        app.include_router(volume.router)

    if find_service(VolumeCollection):
        app.include_router(volume_collection.router)

    if find_service(VolumeMetrics):
        app.include_router(volume_metrics.router)
