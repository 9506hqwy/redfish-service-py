from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.cable import Cable, CableOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete("/redfish/v1/Cables/{cable_id}", response_model_exclude_none=True)
@authenticate
async def delete1(cable_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Cable, request)
    b: dict[str, Any] = {"cable_id": cable_id, "request": request, "response": response}
    return s.delete(**b)


@router.get("/redfish/v1/Cables/{cable_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Cables/{cable_id}", response_model_exclude_none=True)
async def get1(cable_id: str, request: Request, response: Response) -> Cable:
    s: Service = get_service(Cable, request)
    b: dict[str, Any] = {"cable_id": cable_id, "request": request, "response": response}
    m = cast(Cable, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/Cables/{cable_id}", response_model_exclude_none=True)
@authenticate
async def patch1(
    cable_id: str, request: Request, response: Response, body: CableOnUpdate
) -> Cable:
    s: Service = get_service(Cable, request)
    b: dict[str, Any] = {
        "cable_id": cable_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Cable, s.patch(**b))
