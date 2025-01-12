from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.power_subsystem import PowerSubsystem, PowerSubsystemOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/PowerSubsystem", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/PowerSubsystem", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> PowerSubsystem:
    s: Service = get_service(PowerSubsystem, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(PowerSubsystem, s.get(**b))


@router.patch("/redfish/v1/Chassis/{chassis_id}/PowerSubsystem", response_model_exclude_none=True)
@authenticate
async def patch1(
    chassis_id: str, request: Request, response: Response, body: PowerSubsystemOnUpdate
) -> PowerSubsystem:
    s: Service = get_service(PowerSubsystem, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PowerSubsystem, s.patch(**b))
