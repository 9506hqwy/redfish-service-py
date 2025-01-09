from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.chassis import Chassis
from ..service import Service, find_service

router = APIRouter()


@router.delete("/redfish/v1/Chassis/{chassis_id}", response_model_exclude_none=True)
@authenticate
async def delete1(chassis_id: str, request: Request, response: Response) -> None:
    s: Service = find_service(Chassis)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get("/redfish/v1/Chassis/{chassis_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> Chassis:
    s: Service = find_service(Chassis)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Chassis, s.get(**b))
