from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.composition_service import CompositionService, CompositionServiceOnUpdate
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/CompositionService", response_model_exclude_none=True)
@router.head("/redfish/v1/CompositionService", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> CompositionService:
    s: Service = find_service(CompositionService)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(CompositionService, s.get(**b))


@router.patch("/redfish/v1/CompositionService", response_model_exclude_none=True)
@authenticate
async def patch1(
    request: Request, response: Response, body: CompositionServiceOnUpdate
) -> CompositionService:
    s: Service = find_service(CompositionService)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(CompositionService, s.patch(**b))
