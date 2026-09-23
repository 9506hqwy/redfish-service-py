from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.policy import Policy, PolicyOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete("/redfish/v1/PolicyService/Policies/{policy_id}", response_model_exclude_none=True)
@authenticate
async def delete1(policy_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Policy, request)
    b: dict[str, Any] = {"policy_id": policy_id, "request": request, "response": response}
    return s.delete(**b)


@router.get("/redfish/v1/PolicyService/Policies/{policy_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/PolicyService/Policies/{policy_id}", response_model_exclude_none=True)
async def get1(policy_id: str, request: Request, response: Response) -> Policy:
    s: Service = get_service(Policy, request)
    b: dict[str, Any] = {"policy_id": policy_id, "request": request, "response": response}
    m = cast(Policy, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/PolicyService/Policies/{policy_id}", response_model_exclude_none=True)
@authenticate
async def patch1(
    policy_id: str, request: Request, response: Response, body: PolicyOnUpdate
) -> Policy:
    s: Service = get_service(Policy, request)
    b: dict[str, Any] = {
        "policy_id": policy_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Policy, s.patch(**b))
