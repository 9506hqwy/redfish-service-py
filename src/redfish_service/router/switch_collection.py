from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.switch_collection import SwitchCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/Switches", response_model_exclude_none=True)
@router.head("/redfish/v1/Fabrics/{fabric_id}/Switches", response_model_exclude_none=True)
async def get1(fabric_id: str, request: Request, response: Response) -> SwitchCollection:
    s: Service = get_service(SwitchCollection, request)
    b: dict[str, Any] = {"fabric_id": fabric_id, "request": request, "response": response}
    m = cast(SwitchCollection, s.get(**b))
    set_link_header(m, response)
    return m
