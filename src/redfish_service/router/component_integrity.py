from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.component_integrity import ComponentIntegrity, ComponentIntegrityOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/ComponentIntegrity/{component_integrity_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ComponentIntegrity/{component_integrity_id}", response_model_exclude_none=True
)
async def get1(
    component_integrity_id: str, request: Request, response: Response
) -> ComponentIntegrity:
    s: Service = get_service(ComponentIntegrity, request)
    b: dict[str, Any] = {
        "component_integrity_id": component_integrity_id,
        "request": request,
        "response": response,
    }
    return cast(ComponentIntegrity, s.get(**b))


@router.patch(
    "/redfish/v1/ComponentIntegrity/{component_integrity_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    component_integrity_id: str,
    request: Request,
    response: Response,
    body: ComponentIntegrityOnUpdate,
) -> ComponentIntegrity:
    s: Service = get_service(ComponentIntegrity, request)
    b: dict[str, Any] = {
        "component_integrity_id": component_integrity_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ComponentIntegrity, s.patch(**b))
