from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.storage_pool import StoragePool, StoragePoolOnCreate
from ...model.swordfish.storage_pool_collection import StoragePoolCollection
from ...service import Service, ServiceCollection
from ...util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    storage_service_id: str, request: Request, response: Response, body: StoragePoolOnCreate
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str, storage_pool_id: str, request: Request, response: Response
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    storage_service_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
async def get3(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
async def get4(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools",
    response_model_exclude_none=True,
)
async def get5(
    storage_service_id: str, volume_id: str, request: Request, response: Response
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post5(
    storage_service_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
async def get6(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post6(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get("/redfish/v1/Storage/{storage_id}/StoragePools", response_model_exclude_none=True)
@router.head("/redfish/v1/Storage/{storage_id}/StoragePools", response_model_exclude_none=True)
async def get7(storage_id: str, request: Request, response: Response) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {"storage_id": storage_id, "request": request, "response": response}
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/Storage/{storage_id}/StoragePools", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/Members", response_model_exclude_none=True
)
@authenticate
async def post7(
    storage_id: str, request: Request, response: Response, body: StoragePoolOnCreate
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools",
    response_model_exclude_none=True,
)
async def get8(
    storage_id: str, storage_pool_id: str, request: Request, response: Response
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post8(
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
async def get9(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post9(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
async def get10(
    storage_id: str, volume_id: str, capacity_source_id: str, request: Request, response: Response
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post10(
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools",
    response_model_exclude_none=True,
)
async def get11(
    storage_id: str, volume_id: str, request: Request, response: Response
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post11(
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
async def get12(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post12(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools",
    response_model_exclude_none=True,
)
async def get13(
    computer_system_id: str, storage_id: str, request: Request, response: Response
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post13(
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools",
    response_model_exclude_none=True,
)
async def get14(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post14(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
async def get15(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post15(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
async def get16(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post16(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools",
    response_model_exclude_none=True,
)
async def get17(
    computer_system_id: str, storage_id: str, volume_id: str, request: Request, response: Response
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post17(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
async def get18(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> StoragePoolCollection:
    s: Service = get_service(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(StoragePoolCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post18(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: StoragePoolOnCreate,
) -> StoragePool:
    s: ServiceCollection = get_service_collection(StoragePoolCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(StoragePool, s.post(**b))
