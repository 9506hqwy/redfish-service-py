from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.manager_collection import ManagerCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Managers", response_model_exclude_none=True)
@router.head("/redfish/v1/Managers", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> ManagerCollection:
    s: Service = get_service(ManagerCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(ManagerCollection, s.get(**b))
