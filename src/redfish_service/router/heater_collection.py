from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.heater_collection import HeaterCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/Heaters", response_model_exclude_none=True
)
async def get1(chassis_id: str, request: Request, response: Response) -> HeaterCollection:
    s: Service = get_service(HeaterCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(HeaterCollection, s.get(**b))
