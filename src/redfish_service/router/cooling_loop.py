from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.cooling_loop import CoolingLoop, CoolingLoopOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_loop_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_loop_id}", response_model_exclude_none=True
)
async def get1(cooling_loop_id: str, request: Request, response: Response) -> CoolingLoop:
    s: Service = get_service(CoolingLoop, request)
    b: dict[str, Any] = {
        "cooling_loop_id": cooling_loop_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolingLoop, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/CoolingLoops/{cooling_loop_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    cooling_loop_id: str, request: Request, response: Response, body: CoolingLoopOnUpdate
) -> CoolingLoop:
    s: Service = get_service(CoolingLoop, request)
    b: dict[str, Any] = {
        "cooling_loop_id": cooling_loop_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolingLoop, s.patch(**b))
