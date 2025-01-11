from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.endpoint import Endpoint, EndpointOnUpdate
from ..service import Service, find_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/Endpoints/{endpoint_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(fabric_id: str, endpoint_id: str, request: Request, response: Response) -> None:
    s: Service = find_service(Endpoint)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "endpoint_id": endpoint_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Endpoints/{endpoint_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Endpoints/{endpoint_id}", response_model_exclude_none=True
)
async def get1(fabric_id: str, endpoint_id: str, request: Request, response: Response) -> Endpoint:
    s: Service = find_service(Endpoint)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "endpoint_id": endpoint_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Endpoint, s.get(**b))


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Endpoints/{endpoint_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    fabric_id: str, endpoint_id: str, request: Request, response: Response, body: EndpointOnUpdate
) -> Endpoint:
    s: Service = find_service(Endpoint)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "endpoint_id": endpoint_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Endpoint, s.patch(**b))


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/Endpoints/{endpoint_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    storage_service_id: str, endpoint_id: str, request: Request, response: Response
) -> None:
    s: Service = find_service(Endpoint)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "endpoint_id": endpoint_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Endpoints/{endpoint_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/Endpoints/{endpoint_id}",
    response_model_exclude_none=True,
)
async def get2(
    storage_service_id: str, endpoint_id: str, request: Request, response: Response
) -> Endpoint:
    s: Service = find_service(Endpoint)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "endpoint_id": endpoint_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Endpoint, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/Endpoints/{endpoint_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    storage_service_id: str,
    endpoint_id: str,
    request: Request,
    response: Response,
    body: EndpointOnUpdate,
) -> Endpoint:
    s: Service = find_service(Endpoint)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "endpoint_id": endpoint_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Endpoint, s.patch(**b))


@router.delete(
    "/redfish/v1/Storage/{storage_id}/Endpoints/{endpoint_id}", response_model_exclude_none=True
)
@authenticate
async def delete3(storage_id: str, endpoint_id: str, request: Request, response: Response) -> None:
    s: Service = find_service(Endpoint)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "endpoint_id": endpoint_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/Endpoints/{endpoint_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Endpoints/{endpoint_id}", response_model_exclude_none=True
)
async def get3(
    storage_id: str, endpoint_id: str, request: Request, response: Response
) -> Endpoint:
    s: Service = find_service(Endpoint)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "endpoint_id": endpoint_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Endpoint, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Endpoints/{endpoint_id}", response_model_exclude_none=True
)
@authenticate
async def patch3(
    storage_id: str, endpoint_id: str, request: Request, response: Response, body: EndpointOnUpdate
) -> Endpoint:
    s: Service = find_service(Endpoint)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "endpoint_id": endpoint_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Endpoint, s.patch(**b))
