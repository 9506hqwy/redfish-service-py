from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.cable import Cable, CableOnCreate
from ..model.cable_collection import CableCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/Cables", response_model_exclude_none=True)
@router.head("/redfish/v1/Cables", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> CableCollection:
    s: Service = get_service(CableCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(CableCollection, s.get(**b))


@router.post("/redfish/v1/Cables", response_model_exclude_none=True)
@router.post("/redfish/v1/Cables/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: CableOnCreate) -> Cable:
    s: ServiceCollection = get_service_collection(CableCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(Cable, s.post(**b))
