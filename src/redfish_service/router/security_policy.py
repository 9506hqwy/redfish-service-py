from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.security_policy import SecurityPolicy, SecurityPolicyOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}/SecurityPolicy", response_model_exclude_none=True)
@router.head("/redfish/v1/Managers/{manager_id}/SecurityPolicy", response_model_exclude_none=True)
async def get1(manager_id: str, request: Request, response: Response) -> SecurityPolicy:
    s: Service = get_service(SecurityPolicy, request)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(SecurityPolicy, s.get(**b))


@router.patch("/redfish/v1/Managers/{manager_id}/SecurityPolicy", response_model_exclude_none=True)
@authenticate
async def patch1(
    manager_id: str, request: Request, response: Response, body: SecurityPolicyOnUpdate
) -> SecurityPolicy:
    s: Service = get_service(SecurityPolicy, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SecurityPolicy, s.patch(**b))
