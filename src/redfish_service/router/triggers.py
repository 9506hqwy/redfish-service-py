from typing import Any, cast

from fastapi import APIRouter

from ..model.triggers import Triggers
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/TelemetryService/Triggers/{triggers_id}", response_model_exclude_none=True
)
@authenticate
async def get1(triggers_id: str) -> Triggers:
    s: Service = find_service(Triggers)
    b: dict[str, Any] = {"triggers_id": triggers_id}
    return cast(Triggers, s.get(**b))
