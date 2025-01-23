from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.redfish_error import RedfishError
from ..model.switch import ResetRequest, Switch, SwitchOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

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
    m = cast(Switch, s.get(**b))
    set_link_header(m, response)
    return m


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


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Actions/Switch.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    fabric_id: str, switch_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(Switch, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)
