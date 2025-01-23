from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.fabric import Fabric, FabricOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Fabrics/{fabric_id}", response_model_exclude_none=True)
async def get1(fabric_id: str, request: Request, response: Response) -> Fabric:
    s: Service = get_service(Fabric, request)
    b: dict[str, Any] = {"fabric_id": fabric_id, "request": request, "response": response}
    m = cast(Fabric, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/Fabrics/{fabric_id}", response_model_exclude_none=True)
@authenticate
async def patch1(
    fabric_id: str, request: Request, response: Response, body: FabricOnUpdate
) -> Fabric:
    s: Service = get_service(Fabric, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Fabric, s.patch(**b))
