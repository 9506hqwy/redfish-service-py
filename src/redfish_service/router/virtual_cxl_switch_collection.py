from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.virtual_cxl_switch_collection import VirtualCxlSwitchCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/VCSs", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/VCSs", response_model_exclude_none=True
)
async def get1(
    fabric_id: str, switch_id: str, request: Request, response: Response
) -> VirtualCxlSwitchCollection:
    s: Service = get_service(VirtualCxlSwitchCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "request": request,
        "response": response,
    }
    m = cast(VirtualCxlSwitchCollection, s.get(**b))
    set_link_header(m, response)
    return m
