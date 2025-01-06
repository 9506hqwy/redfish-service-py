from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.triggers_collection import TriggersCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/TelemetryService/Triggers", response_model_exclude_none=True)
@router.head("/redfish/v1/TelemetryService/Triggers", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> TriggersCollection:
    s: Service = find_service(TriggersCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(TriggersCollection, s.get(**b))
