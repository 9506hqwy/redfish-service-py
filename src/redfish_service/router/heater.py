from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.heater import Heater, HeaterOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters/{heater_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters/{heater_id}",
    response_model_exclude_none=True,
)
async def get1(chassis_id: str, heater_id: str, request: Request, response: Response) -> Heater:
    s: Service = get_service(Heater, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "heater_id": heater_id,
        "request": request,
        "response": response,
    }
    m = cast(Heater, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters/{heater_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str, heater_id: str, request: Request, response: Response, body: HeaterOnUpdate
) -> Heater:
    s: Service = get_service(Heater, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "heater_id": heater_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Heater, s.patch(**b))
