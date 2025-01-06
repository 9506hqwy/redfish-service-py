from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.component_integrity import ComponentIntegrity
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/ComponentIntegrity/{component_integrity_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ComponentIntegrity/{component_integrity_id}", response_model_exclude_none=True
)
@authenticate
async def get1(
    component_integrity_id: str, request: Request, response: Response
) -> ComponentIntegrity:
    s: Service = find_service(ComponentIntegrity)
    b: dict[str, Any] = {
        "component_integrity_id": component_integrity_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(ComponentIntegrity, s.get(**b))
