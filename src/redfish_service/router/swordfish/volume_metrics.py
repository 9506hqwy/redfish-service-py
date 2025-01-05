from typing import Any, cast

from fastapi import APIRouter

from ...model.swordfish.volume_metrics import VolumeMetrics
from ...service import Service, find_service
from .. import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get1(resource_block_id: str, storage_id: str, volume_id: str) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    resource_block_id: str, computer_system_id: str, storage_id: str, volume_id: str
) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get3(resource_block_id: str, storage_id: str, volume_id: str) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    resource_block_id: str, computer_system_id: str, storage_id: str, volume_id: str
) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get5(storage_id: str, consistency_group_id: str, volume_id: str) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    storage_id: str, file_system_id: str, capacity_source_id: str, volume_id: str
) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get7(storage_id: str, storage_pool_id: str, volume_id: str) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get8(
    storage_id: str, storage_pool_id: str, capacity_source_id: str, volume_id: str
) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get9(storage_id: str, volume_id: str) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {"storage_id": storage_id, "volume_id": volume_id}
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get10(
    computer_system_id: str, storage_id: str, consistency_group_id: str, volume_id: str
) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    volume_id: str,
) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get12(
    computer_system_id: str, storage_id: str, storage_pool_id: str, volume_id: str
) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    volume_id: str,
) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get14(computer_system_id: str, storage_id: str, volume_id: str) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get15(
    storage_service_id: str, consistency_group_id: str, volume_id: str
) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get16(
    storage_service_id: str, file_system_id: str, capacity_source_id: str, volume_id: str
) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get17(storage_service_id: str, storage_pool_id: str, volume_id: str) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get18(
    storage_service_id: str, storage_pool_id: str, capacity_source_id: str, volume_id: str
) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "volume_id": volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get19(storage_service_id: str, volume_id: str) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {"storage_service_id": storage_service_id, "volume_id": volume_id}
    return cast(VolumeMetrics, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/{providing_volume_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get20(
    storage_service_id: str, volume_id: str, capacity_source_id: str, providing_volume_id: str
) -> VolumeMetrics:
    s: Service = find_service(VolumeMetrics)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "providing_volume_id": providing_volume_id,
    }
    return cast(VolumeMetrics, s.get(**b))
