from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.trusted_component import TrustedComponent, TrustedComponentOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, trusted_component_id: str, request: Request, response: Response
) -> TrustedComponent:
    s: Service = get_service(TrustedComponent, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "trusted_component_id": trusted_component_id,
        "request": request,
        "response": response,
    }
    m = cast(TrustedComponent, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents/{trusted_component_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    trusted_component_id: str,
    request: Request,
    response: Response,
    body: TrustedComponentOnUpdate,
) -> TrustedComponent:
    s: Service = get_service(TrustedComponent, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "trusted_component_id": trusted_component_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(TrustedComponent, s.patch(**b))
