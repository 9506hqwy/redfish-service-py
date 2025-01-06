from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.key_policy import KeyPolicy
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/KeyService/NVMeoFKeyPolicies/{key_policy_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/KeyService/NVMeoFKeyPolicies/{key_policy_id}", response_model_exclude_none=True
)
@authenticate
async def get1(key_policy_id: str, request: Request, response: Response) -> KeyPolicy:
    s: Service = find_service(KeyPolicy)
    b: dict[str, Any] = {"key_policy_id": key_policy_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(KeyPolicy, s.get(**b))
