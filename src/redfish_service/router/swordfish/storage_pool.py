from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...model.swordfish.storage_pool import StoragePool
from ...service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, storage_pool_id: str, request: Request, response: Response
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
async def get3(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get4(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get5(
    storage_service_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get6(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get7(
    storage_id: str, storage_pool_id: str, request: Request, response: Response
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
async def get8(
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
async def get9(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get10(
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get11(
    storage_id: str, volume_id: str, storage_pool_id: str, request: Request, response: Response
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get12(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get13(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedPools/{allocated_pool_id}",
    response_model_exclude_none=True,
)
async def get14(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    allocated_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "allocated_pool_id": allocated_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{providing_pool_id}",
    response_model_exclude_none=True,
)
async def get15(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    providing_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "providing_pool_id": providing_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get16(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/AllocatedPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get17(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}/ProvidingPools/{storage_pool_id}",
    response_model_exclude_none=True,
)
async def get18(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    storage_pool_id: str,
    request: Request,
    response: Response,
) -> StoragePool:
    s: Service = find_service(StoragePool)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "storage_pool_id": storage_pool_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(StoragePool, s.get(**b))
