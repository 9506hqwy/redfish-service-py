from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.chassis import Chassis, ChassisOnUpdate, ResetRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete("/redfish/v1/Chassis/{chassis_id}", response_model_exclude_none=True)
@authenticate
async def delete1(chassis_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Chassis, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    return s.delete(**b)


@router.get("/redfish/v1/Chassis/{chassis_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> Chassis:
    s: Service = get_service(Chassis, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    return cast(Chassis, s.get(**b))


@router.patch("/redfish/v1/Chassis/{chassis_id}", response_model_exclude_none=True)
@authenticate
async def patch1(
    chassis_id: str, request: Request, response: Response, body: ChassisOnUpdate
) -> Chassis:
    s: Service = get_service(Chassis, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Chassis, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Actions/Chassis.Reset", response_model_exclude_none=True
)
@authenticate
async def reset1(
    chassis_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(Chassis, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)
