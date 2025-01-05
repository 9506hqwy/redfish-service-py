from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.manager_collection import ManagerCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Managers", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> ManagerCollection:
    s: Service = find_service(ManagerCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ManagerCollection, s.get(**b))
