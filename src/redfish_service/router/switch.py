from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.switch import Switch, SwitchOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}", response_model_exclude_none=True
)
async def get1(fabric_id: str, switch_id: str, request: Request, response: Response) -> Switch:
    s: Service = get_service(Switch, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "request": request,
        "response": response,
    }
    return cast(Switch, s.get(**b))


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    fabric_id: str, switch_id: str, request: Request, response: Response, body: SwitchOnUpdate
) -> Switch:
    s: Service = get_service(Switch, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Switch, s.patch(**b))
