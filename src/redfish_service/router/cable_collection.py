from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.cable_collection import CableCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Cables", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> CableCollection:
    s: Service = find_service(CableCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CableCollection, s.get(**b))
