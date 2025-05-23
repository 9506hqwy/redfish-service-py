from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.fabric_collection import FabricCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Fabrics", response_model_exclude_none=True)
@router.head("/redfish/v1/Fabrics", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> FabricCollection:
    s: Service = get_service(FabricCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(FabricCollection, s.get(**b))
    set_link_header(m, response)
    return m
