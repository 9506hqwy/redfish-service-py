from typing import Any, cast

from fastapi import APIRouter

from ..model.security_policy import SecurityPolicy
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}/SecurityPolicy", response_model_exclude_none=True)
@authenticate
async def get1(manager_id: str) -> SecurityPolicy:
    s: Service = find_service(SecurityPolicy)
    b: dict[str, Any] = {"manager_id": manager_id}
    return cast(SecurityPolicy, s.get(**b))
