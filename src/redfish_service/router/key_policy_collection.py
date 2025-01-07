from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.key_policy import KeyPolicy, KeyPolicyOnCreate
from ..model.key_policy_collection import KeyPolicyCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/KeyService/NVMeoFKeyPolicies", response_model_exclude_none=True)
@router.head("/redfish/v1/KeyService/NVMeoFKeyPolicies", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> KeyPolicyCollection:
    s: Service = find_service(KeyPolicyCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(KeyPolicyCollection, s.get(**b))


@router.post("/redfish/v1/KeyService/NVMeoFKeyPolicies", response_model_exclude_none=True)
@router.post("/redfish/v1/KeyService/NVMeoFKeyPolicies/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: KeyPolicyOnCreate) -> KeyPolicy:
    s: ServiceCollection = find_service_collection(KeyPolicyCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(KeyPolicy, s.post(**b))
