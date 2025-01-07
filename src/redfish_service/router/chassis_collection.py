from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.chassis import Chassis, ChassisOnCreate
from ..model.chassis_collection import ChassisCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/Chassis", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> ChassisCollection:
    s: Service = find_service(ChassisCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ChassisCollection, s.get(**b))


@router.post("/redfish/v1/Chassis", response_model_exclude_none=True)
@router.post("/redfish/v1/Chassis/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: ChassisOnCreate) -> Chassis:
    s: ServiceCollection = find_service_collection(ChassisCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(Chassis, s.post(**b))
