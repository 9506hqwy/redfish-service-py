from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.key_policy import KeyPolicy, KeyPolicyOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/KeyService/NVMeoFKeyPolicies/{key_policy_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(key_policy_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(KeyPolicy, request)
    b: dict[str, Any] = {"key_policy_id": key_policy_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/KeyService/NVMeoFKeyPolicies/{key_policy_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/KeyService/NVMeoFKeyPolicies/{key_policy_id}", response_model_exclude_none=True
)
async def get1(key_policy_id: str, request: Request, response: Response) -> KeyPolicy:
    s: Service = get_service(KeyPolicy, request)
    b: dict[str, Any] = {"key_policy_id": key_policy_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(KeyPolicy, s.get(**b))


@router.patch(
    "/redfish/v1/KeyService/NVMeoFKeyPolicies/{key_policy_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    key_policy_id: str, request: Request, response: Response, body: KeyPolicyOnUpdate
) -> KeyPolicy:
    s: Service = get_service(KeyPolicy, request)
    b: dict[str, Any] = {
        "key_policy_id": key_policy_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(KeyPolicy, s.patch(**b))
