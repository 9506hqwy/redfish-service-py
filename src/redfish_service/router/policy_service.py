from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.policy_service import PolicyService, PolicyServiceOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/PolicyService", response_model_exclude_none=True)
@router.head("/redfish/v1/PolicyService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> PolicyService:
    s: Service = get_service(PolicyService, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(PolicyService, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/PolicyService", response_model_exclude_none=True)
@authenticate
async def patch1(
    request: Request, response: Response, body: PolicyServiceOnUpdate
) -> PolicyService:
    s: Service = get_service(PolicyService, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(PolicyService, s.patch(**b))
