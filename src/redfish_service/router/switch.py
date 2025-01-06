from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.switch import Switch
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}", response_model_exclude_none=True
)
@authenticate
async def get1(fabric_id: str, switch_id: str, request: Request, response: Response) -> Switch:
    s: Service = find_service(Switch)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Switch, s.get(**b))
