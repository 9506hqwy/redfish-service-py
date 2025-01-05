from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.control import Control
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Controls/{control_id}", response_model_exclude_none=True
)
@authenticate
async def get1(chassis_id: str, control_id: str, request: Request, response: Response) -> Control:
    s: Service = find_service(Control)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "control_id": control_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Control, s.get(**b))
