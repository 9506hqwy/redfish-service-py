from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.cooling_loop import CoolingLoop
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_loop_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_loop_id}", response_model_exclude_none=True
)
@authenticate
async def get1(cooling_loop_id: str, request: Request, response: Response) -> CoolingLoop:
    s: Service = find_service(CoolingLoop)
    b: dict[str, Any] = {
        "cooling_loop_id": cooling_loop_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(CoolingLoop, s.get(**b))
