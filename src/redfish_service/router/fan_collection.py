from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.fan_collection import FanCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Fans", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Fans", response_model_exclude_none=True
)
async def get1(chassis_id: str, request: Request, response: Response) -> FanCollection:
    s: Service = get_service(FanCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(FanCollection, s.get(**b))
    set_link_header(m, response)
    return m
