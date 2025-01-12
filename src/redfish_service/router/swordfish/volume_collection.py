from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.volume import Volume, VolumeOnCreate
from ...model.swordfish.volume_collection import VolumeCollection
from ...service import Service, ServiceCollection
from ...util import get_service, get_service_collection

router = APIRouter()


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
async def get1(
    resource_block_id: str, storage_id: str, request: Request, response: Response
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    resource_block_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, storage_id: str, request: Request, response: Response
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Volumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    resource_block_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes",
    response_model_exclude_none=True,
)
async def get5(
    storage_id: str, consistency_group_id: str, request: Request, response: Response
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post5(
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
async def get6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post6(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes",
    response_model_exclude_none=True,
)
async def get7(
    storage_id: str, storage_pool_id: str, request: Request, response: Response
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post7(
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
async def get8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post8(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get("/redfish/v1/Storage/{storage_id}/Volumes", response_model_exclude_none=True)
@router.head("/redfish/v1/Storage/{storage_id}/Volumes", response_model_exclude_none=True)
async def get9(storage_id: str, request: Request, response: Response) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {"storage_id": storage_id, "request": request, "response": response}
    return cast(VolumeCollection, s.get(**b))


@router.post("/redfish/v1/Storage/{storage_id}/Volumes", response_model_exclude_none=True)
@router.post("/redfish/v1/Storage/{storage_id}/Volumes/Members", response_model_exclude_none=True)
@authenticate
async def post9(
    storage_id: str, request: Request, response: Response, body: VolumeOnCreate
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes",
    response_model_exclude_none=True,
)
async def get10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/ConsistencyGroups/{consistency_group_id}/Volumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post10(
    computer_system_id: str,
    storage_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
async def get11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post11(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes",
    response_model_exclude_none=True,
)
async def get12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post12(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
async def get13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
async def get14(
    computer_system_id: str, storage_id: str, request: Request, response: Response
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post14(
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes",
    response_model_exclude_none=True,
)
async def get15(
    storage_service_id: str, consistency_group_id: str, request: Request, response: Response
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ConsistencyGroups/{consistency_group_id}/Volumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post15(
    storage_service_id: str,
    consistency_group_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "consistency_group_id": consistency_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
async def get16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post16(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes",
    response_model_exclude_none=True,
)
async def get17(
    storage_service_id: str, storage_pool_id: str, request: Request, response: Response
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post17(
    storage_service_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
async def get18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post18(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes", response_model_exclude_none=True
)
async def get19(storage_service_id: str, request: Request, response: Response) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes", response_model_exclude_none=True
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post19(
    storage_service_id: str, request: Request, response: Response, body: VolumeOnCreate
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
async def get20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> VolumeCollection:
    s: Service = get_service(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return cast(VolumeCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingVolumes/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post20(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: VolumeOnCreate,
) -> Volume:
    s: ServiceCollection = get_service_collection(VolumeCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Volume, s.post(**b))
