from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.control_collection import ControlCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/Controls", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/Controls", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> ControlCollection:
    s: Service = get_service(ControlCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(ControlCollection, s.get(**b))
    set_link_header(m, response)
    return m
