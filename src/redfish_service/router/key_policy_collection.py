from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.key_policy import KeyPolicy, KeyPolicyOnCreate
from ..model.key_policy_collection import KeyPolicyCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/KeyService/NVMeoFKeyPolicies", response_model_exclude_none=True)
@router.head("/redfish/v1/KeyService/NVMeoFKeyPolicies", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> KeyPolicyCollection:
    s: Service = get_service(KeyPolicyCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    return cast(KeyPolicyCollection, s.get(**b))


@router.post("/redfish/v1/KeyService/NVMeoFKeyPolicies", response_model_exclude_none=True)
@router.post("/redfish/v1/KeyService/NVMeoFKeyPolicies/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: KeyPolicyOnCreate) -> KeyPolicy:
    s: ServiceCollection = get_service_collection(KeyPolicyCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(KeyPolicy, s.post(**b))
