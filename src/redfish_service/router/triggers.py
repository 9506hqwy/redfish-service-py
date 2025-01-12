from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.triggers import Triggers, TriggersOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/TelemetryService/Triggers/{triggers_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(triggers_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Triggers, request)
    b: dict[str, Any] = {"triggers_id": triggers_id, "request": request, "response": response}
    return s.delete(**b)


@router.get(
    "/redfish/v1/TelemetryService/Triggers/{triggers_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/TelemetryService/Triggers/{triggers_id}", response_model_exclude_none=True
)
async def get1(triggers_id: str, request: Request, response: Response) -> Triggers:
    s: Service = get_service(Triggers, request)
    b: dict[str, Any] = {"triggers_id": triggers_id, "request": request, "response": response}
    return cast(Triggers, s.get(**b))


@router.patch(
    "/redfish/v1/TelemetryService/Triggers/{triggers_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    triggers_id: str, request: Request, response: Response, body: TriggersOnUpdate
) -> Triggers:
    s: Service = get_service(Triggers, request)
    b: dict[str, Any] = {
        "triggers_id": triggers_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Triggers, s.patch(**b))
