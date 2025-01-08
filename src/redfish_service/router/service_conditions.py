from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.service_conditions import ServiceConditions
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/ServiceConditions", response_model_exclude_none=True)
@router.head("/redfish/v1/ServiceConditions", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> ServiceConditions:
    s: Service = find_service(ServiceConditions)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ServiceConditions, s.get(**b))
