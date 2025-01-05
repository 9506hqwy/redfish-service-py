from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.thermal import Thermal
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/Thermal", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str, request: Request, response: Response) -> Thermal:
    s: Service = find_service(Thermal)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Thermal, s.get(**b))
