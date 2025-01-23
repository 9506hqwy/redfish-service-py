from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.power import Power, PowerOnUpdate, PowerSupplyResetRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/Power", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/Power", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> Power:
    s: Service = get_service(Power, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(Power, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/Chassis/{chassis_id}/Power", response_model_exclude_none=True)
@authenticate
async def patch1(
    chassis_id: str, request: Request, response: Response, body: PowerOnUpdate
) -> Power:
    s: Service = get_service(Power, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Power, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Power/Actions/Power.PowerSupplyReset",
    response_model_exclude_none=True,
)
@authenticate
async def power_supply_reset1(
    chassis_id: str, request: Request, response: Response, body: PowerSupplyResetRequest
) -> RedfishError:
    s: Service = get_service(Power, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PowerSupplyReset",
    }
    return s.action(**b)
