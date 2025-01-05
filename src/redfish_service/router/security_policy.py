from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.security_policy import SecurityPolicy
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Managers/{manager_id}/SecurityPolicy", response_model_exclude_none=True)
@authenticate
async def get1(manager_id: str, request: Request, response: Response) -> SecurityPolicy:
    s: Service = find_service(SecurityPolicy)
    b: dict[str, Any] = {"manager_id": manager_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(SecurityPolicy, s.get(**b))
