from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.chassis import Chassis, ChassisOnCreate
from ..model.chassis_collection import ChassisCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Chassis", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> ChassisCollection:
    s: Service = get_service(ChassisCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(ChassisCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/Chassis", response_model_exclude_none=True)
@router.post("/redfish/v1/Chassis/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: ChassisOnCreate) -> Chassis:
    s: ServiceCollection = get_service_collection(ChassisCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(Chassis, s.post(**b))
