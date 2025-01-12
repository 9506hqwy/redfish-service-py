from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.thermal import Thermal, ThermalOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/Thermal", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/Thermal", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> Thermal:
    s: Service = get_service(Thermal, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    return cast(Thermal, s.get(**b))


@router.patch("/redfish/v1/Chassis/{chassis_id}/Thermal", response_model_exclude_none=True)
@authenticate
async def patch1(
    chassis_id: str, request: Request, response: Response, body: ThermalOnUpdate
) -> Thermal:
    s: Service = get_service(Thermal, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Thermal, s.patch(**b))
