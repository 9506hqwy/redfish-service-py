from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.power_equipment import PowerEquipment
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/PowerEquipment", response_model_exclude_none=True)
@router.head("/redfish/v1/PowerEquipment", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> PowerEquipment:
    s: Service = get_service(PowerEquipment, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(PowerEquipment, s.get(**b))
    set_link_header(m, response)
    return m
