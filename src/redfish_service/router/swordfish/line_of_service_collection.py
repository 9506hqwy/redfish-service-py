from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.line_of_service import LineOfService, LineOfServiceOnCreate
from ...model.swordfish.line_of_service_collection import LineOfServiceCollection
from ...service import Service, ServiceCollection
from ...util import get_service, get_service_collection

router = APIRouter()


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService",
    response_model_exclude_none=True,
)
async def get1(
    storage_service_id: str, request: Request, response: Response
) -> LineOfServiceCollection:
    s: Service = get_service(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    storage_service_id: str, request: Request, response: Response, body: LineOfServiceOnCreate
) -> LineOfService:
    s: ServiceCollection = get_service_collection(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataProtectionLinesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataProtectionLinesOfService",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str, request: Request, response: Response
) -> LineOfServiceCollection:
    s: Service = get_service(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataProtectionLinesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataProtectionLinesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    storage_service_id: str, request: Request, response: Response, body: LineOfServiceOnCreate
) -> LineOfService:
    s: ServiceCollection = get_service_collection(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataSecurityLinesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataSecurityLinesOfService",
    response_model_exclude_none=True,
)
async def get3(
    storage_service_id: str, request: Request, response: Response
) -> LineOfServiceCollection:
    s: Service = get_service(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataSecurityLinesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataSecurityLinesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    storage_service_id: str, request: Request, response: Response, body: LineOfServiceOnCreate
) -> LineOfService:
    s: ServiceCollection = get_service_collection(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataStorageLinesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataStorageLinesOfService",
    response_model_exclude_none=True,
)
async def get4(
    storage_service_id: str, request: Request, response: Response
) -> LineOfServiceCollection:
    s: Service = get_service(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataStorageLinesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/DataStorageLinesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    storage_service_id: str, request: Request, response: Response, body: LineOfServiceOnCreate
) -> LineOfService:
    s: ServiceCollection = get_service_collection(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOConnectivityLinesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOConnectivityLinesOfService",
    response_model_exclude_none=True,
)
async def get5(
    storage_service_id: str, request: Request, response: Response
) -> LineOfServiceCollection:
    s: Service = get_service(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOConnectivityLinesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOConnectivityLinesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post5(
    storage_service_id: str, request: Request, response: Response, body: LineOfServiceOnCreate
) -> LineOfService:
    s: ServiceCollection = get_service_collection(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOPerformanceLinesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOPerformanceLinesOfService",
    response_model_exclude_none=True,
)
async def get6(
    storage_service_id: str, request: Request, response: Response
) -> LineOfServiceCollection:
    s: Service = get_service(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOPerformanceLinesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/LinesOfService/IOPerformanceLinesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post6(
    storage_service_id: str, request: Request, response: Response, body: LineOfServiceOnCreate
) -> LineOfService:
    s: ServiceCollection = get_service_collection(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataProtectionLinesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataProtectionLinesOfService",
    response_model_exclude_none=True,
)
async def get7(
    storage_service_id: str, class_of_service_id: str, request: Request, response: Response
) -> LineOfServiceCollection:
    s: Service = get_service(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataProtectionLinesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataProtectionLinesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post7(
    storage_service_id: str,
    class_of_service_id: str,
    request: Request,
    response: Response,
    body: LineOfServiceOnCreate,
) -> LineOfService:
    s: ServiceCollection = get_service_collection(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataSecurityLinesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataSecurityLinesOfService",
    response_model_exclude_none=True,
)
async def get8(
    storage_service_id: str, class_of_service_id: str, request: Request, response: Response
) -> LineOfServiceCollection:
    s: Service = get_service(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataSecurityLinesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataSecurityLinesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post8(
    storage_service_id: str,
    class_of_service_id: str,
    request: Request,
    response: Response,
    body: LineOfServiceOnCreate,
) -> LineOfService:
    s: ServiceCollection = get_service_collection(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataStorageLinesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataStorageLinesOfService",
    response_model_exclude_none=True,
)
async def get9(
    storage_service_id: str, class_of_service_id: str, request: Request, response: Response
) -> LineOfServiceCollection:
    s: Service = get_service(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataStorageLinesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/DataStorageLinesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post9(
    storage_service_id: str,
    class_of_service_id: str,
    request: Request,
    response: Response,
    body: LineOfServiceOnCreate,
) -> LineOfService:
    s: ServiceCollection = get_service_collection(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOConnectivityLinesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOConnectivityLinesOfService",
    response_model_exclude_none=True,
)
async def get10(
    storage_service_id: str, class_of_service_id: str, request: Request, response: Response
) -> LineOfServiceCollection:
    s: Service = get_service(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOConnectivityLinesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOConnectivityLinesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post10(
    storage_service_id: str,
    class_of_service_id: str,
    request: Request,
    response: Response,
    body: LineOfServiceOnCreate,
) -> LineOfService:
    s: ServiceCollection = get_service_collection(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOPerformanceLinesOfService",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOPerformanceLinesOfService",
    response_model_exclude_none=True,
)
async def get11(
    storage_service_id: str, class_of_service_id: str, request: Request, response: Response
) -> LineOfServiceCollection:
    s: Service = get_service(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
    }
    return cast(LineOfServiceCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOPerformanceLinesOfService",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/ClassesOfService/{class_of_service_id}/IOPerformanceLinesOfService/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post11(
    storage_service_id: str,
    class_of_service_id: str,
    request: Request,
    response: Response,
    body: LineOfServiceOnCreate,
) -> LineOfService:
    s: ServiceCollection = get_service_collection(LineOfServiceCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "class_of_service_id": class_of_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(LineOfService, s.post(**b))
