from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.control_collection import ControlCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/Controls", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/Controls", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str, request: Request, response: Response) -> ControlCollection:
    s: Service = find_service(ControlCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ControlCollection, s.get(**b))
