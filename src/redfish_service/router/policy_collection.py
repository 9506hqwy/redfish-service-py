from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.policy import Policy, PolicyOnCreate
from ..model.policy_collection import PolicyCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/PolicyService/Policies", response_model_exclude_none=True)
@router.head("/redfish/v1/PolicyService/Policies", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> PolicyCollection:
    s: Service = get_service(PolicyCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(PolicyCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/PolicyService/Policies", response_model_exclude_none=True)
@router.post("/redfish/v1/PolicyService/Policies/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: PolicyOnCreate) -> Policy:
    s: ServiceCollection = get_service_collection(PolicyCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(Policy, s.post(**b))
