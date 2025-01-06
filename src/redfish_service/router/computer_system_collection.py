from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.computer_system_collection import ComputerSystemCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Systems", response_model_exclude_none=True)
@router.head("/redfish/v1/Systems", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> ComputerSystemCollection:
    s: Service = find_service(ComputerSystemCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ComputerSystemCollection, s.get(**b))
