from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.cable import Cable
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Cables/{cable_id}", response_model_exclude_none=True)
@authenticate
async def get1(cable_id: str, request: Request, response: Response) -> Cable:
    s: Service = find_service(Cable)
    b: dict[str, Any] = {"cable_id": cable_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Cable, s.get(**b))
