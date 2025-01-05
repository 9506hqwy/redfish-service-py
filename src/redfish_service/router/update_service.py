from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.update_service import UpdateService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/UpdateService", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> UpdateService:
    s: Service = find_service(UpdateService)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(UpdateService, s.get(**b))
