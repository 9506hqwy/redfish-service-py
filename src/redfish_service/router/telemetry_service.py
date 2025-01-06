from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.telemetry_service import TelemetryService
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/TelemetryService", response_model_exclude_none=True)
@router.head("/redfish/v1/TelemetryService", response_model_exclude_none=True)
@authenticate
async def get1(request: Request, response: Response) -> TelemetryService:
    s: Service = find_service(TelemetryService)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(TelemetryService, s.get(**b))
