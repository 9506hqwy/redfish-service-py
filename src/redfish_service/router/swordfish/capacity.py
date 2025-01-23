from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.capacity import CapacitySource, CapacitySourceOnUpdate
from ...service import Service
from ...util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySource, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_service_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: CapacitySourceOnUpdate,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CapacitySource, s.patch(**b))


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySource, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    storage_service_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: CapacitySourceOnUpdate,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CapacitySource, s.patch(**b))


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
async def get3(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySource, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    storage_service_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: CapacitySourceOnUpdate,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CapacitySource, s.patch(**b))


@router.delete(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
async def get4(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySource, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: CapacitySourceOnUpdate,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CapacitySource, s.patch(**b))


@router.delete(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete5(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
async def get5(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySource, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Storage/{storage_id}/StoragePools/{storage_pool_id}/AllocatedVolumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    storage_id: str,
    storage_pool_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: CapacitySourceOnUpdate,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CapacitySource, s.patch(**b))


@router.delete(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete6(
    storage_id: str, volume_id: str, capacity_source_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
async def get6(
    storage_id: str, volume_id: str, capacity_source_id: str, request: Request, response: Response
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySource, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: CapacitySourceOnUpdate,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CapacitySource, s.patch(**b))


@router.delete(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete7(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
async def get7(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySource, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: CapacitySourceOnUpdate,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CapacitySource, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete8(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
async def get8(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySource, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StoragePools/{storage_pool_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    computer_system_id: str,
    storage_id: str,
    storage_pool_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: CapacitySourceOnUpdate,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_pool_id": storage_pool_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CapacitySource, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete9(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
async def get9(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySource, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Volumes/{volume_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    computer_system_id: str,
    storage_id: str,
    volume_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: CapacitySourceOnUpdate,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "volume_id": volume_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CapacitySource, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete10(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
async def get10(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
    }
    m = cast(CapacitySource, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/FileSystems/{file_system_id}/CapacitySources/{capacity_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    computer_system_id: str,
    storage_id: str,
    file_system_id: str,
    capacity_source_id: str,
    request: Request,
    response: Response,
    body: CapacitySourceOnUpdate,
) -> CapacitySource:
    s: Service = get_service(CapacitySource, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "file_system_id": file_system_id,
        "capacity_source_id": capacity_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CapacitySource, s.patch(**b))
