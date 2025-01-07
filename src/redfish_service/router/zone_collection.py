from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.zone import Zone, ZoneOnCreate
from ..model.zone_collection import ZoneCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/Zones", response_model_exclude_none=True)
@router.head("/redfish/v1/Fabrics/{fabric_id}/Zones", response_model_exclude_none=True)
@authenticate
async def get1(fabric_id: str, request: Request, response: Response) -> ZoneCollection:
    s: Service = find_service(ZoneCollection)
    b: dict[str, Any] = {"fabric_id": fabric_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ZoneCollection, s.get(**b))


@router.post("/redfish/v1/Fabrics/{fabric_id}/Zones", response_model_exclude_none=True)
@router.post("/redfish/v1/Fabrics/{fabric_id}/Zones/Members", response_model_exclude_none=True)
@authenticate
async def post1(fabric_id: str, request: Request, response: Response, body: ZoneOnCreate) -> Zone:
    s: ServiceCollection = find_service_collection(ZoneCollection)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Zone, s.post(**b))


@router.get("/redfish/v1/CompositionService/ResourceZones", response_model_exclude_none=True)
@router.head("/redfish/v1/CompositionService/ResourceZones", response_model_exclude_none=True)
@authenticate
async def get2(request: Request, response: Response) -> ZoneCollection:
    s: Service = find_service(ZoneCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ZoneCollection, s.get(**b))


@router.post("/redfish/v1/CompositionService/ResourceZones", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/CompositionService/ResourceZones/Members", response_model_exclude_none=True
)
@authenticate
async def post2(request: Request, response: Response, body: ZoneOnCreate) -> Zone:
    s: ServiceCollection = find_service_collection(ZoneCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(Zone, s.post(**b))
