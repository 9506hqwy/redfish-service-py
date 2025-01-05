from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.endpoint import Endpoint
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Endpoints/{endpoint_id}", response_model_exclude_none=True
)
@authenticate
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


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/Endpoints/{endpoint_id}",
    response_model_exclude_none=True,
)
@authenticate
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


@router.get(
    "/redfish/v1/Storage/{storage_id}/Endpoints/{endpoint_id}", response_model_exclude_none=True
)
@authenticate
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
