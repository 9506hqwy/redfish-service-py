from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.zone import Zone
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/Zones/{zone_id}", response_model_exclude_none=True)
@authenticate
async def get1(fabric_id: str, zone_id: str, request: Request, response: Response) -> Zone:
    s: Service = find_service(Zone)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "zone_id": zone_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Zone, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceZones/{zone_id}", response_model_exclude_none=True
)
@authenticate
async def get2(zone_id: str, request: Request, response: Response) -> Zone:
    s: Service = find_service(Zone)
    b: dict[str, Any] = {"zone_id": zone_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Zone, s.get(**b))
