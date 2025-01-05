from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.key_policy_collection import KeyPolicyCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/KeyService/NVMeoFKeyPolicies", response_model_exclude_none=True)
@authenticate
async def get1() -> KeyPolicyCollection:
    s: Service = find_service(KeyPolicyCollection)
    b: dict[str, Any] = {}
    return cast(KeyPolicyCollection, s.get(**b))
