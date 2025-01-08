from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.component_integrity_collection import ComponentIntegrityCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/ComponentIntegrity", response_model_exclude_none=True)
@router.head("/redfish/v1/ComponentIntegrity", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> ComponentIntegrityCollection:
    s: Service = find_service(ComponentIntegrityCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(ComponentIntegrityCollection, s.get(**b))
