from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.telemetry_data import TelemetryData
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/TelemetryService/TelemetryData/{telemetry_data_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(telemetry_data_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(TelemetryData, request)
    b: dict[str, Any] = {
        "telemetry_data_id": telemetry_data_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/TelemetryService/TelemetryData/{telemetry_data_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/TelemetryService/TelemetryData/{telemetry_data_id}",
    response_model_exclude_none=True,
)
async def get1(telemetry_data_id: str, request: Request, response: Response) -> TelemetryData:
    s: Service = get_service(TelemetryData, request)
    b: dict[str, Any] = {
        "telemetry_data_id": telemetry_data_id,
        "request": request,
        "response": response,
    }
    m = cast(TelemetryData, s.get(**b))
    set_link_header(m, response)
    return m
