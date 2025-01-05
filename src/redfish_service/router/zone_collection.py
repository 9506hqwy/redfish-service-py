from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.zone_collection import ZoneCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/Zones", response_model_exclude_none=True)
@authenticate
async def get1(fabric_id: str, request: Request, response: Response) -> ZoneCollection:
    s: Service = find_service(ZoneCollection)
    b: dict[str, Any] = {"fabric_id": fabric_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ZoneCollection, s.get(**b))


@router.get("/redfish/v1/CompositionService/ResourceZones", response_model_exclude_none=True)
@authenticate
async def get2(request: Request, response: Response) -> ZoneCollection:
    s: Service = find_service(ZoneCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ZoneCollection, s.get(**b))
