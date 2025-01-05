from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.thermal_subsystem import ThermalSubsystem
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str, request: Request, response: Response) -> ThermalSubsystem:
    s: Service = find_service(ThermalSubsystem)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ThermalSubsystem, s.get(**b))
