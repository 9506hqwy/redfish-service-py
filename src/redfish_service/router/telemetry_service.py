from typing import Any, cast

from fastapi import APIRouter

from ..model.telemetry_service import TelemetryService
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/TelemetryService", response_model_exclude_none=True)
@authenticate
async def get1() -> TelemetryService:
    s: Service = find_service(TelemetryService)
    b: dict[str, Any] = {}
    return cast(TelemetryService, s.get(**b))
