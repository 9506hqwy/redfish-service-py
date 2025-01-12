from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.trusted_component_collection import TrustedComponentCollection
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/TrustedComponents", response_model_exclude_none=True)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/TrustedComponents", response_model_exclude_none=True
)
async def get1(
    chassis_id: str, request: Request, response: Response
) -> TrustedComponentCollection:
    s: Service = get_service(TrustedComponentCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    return cast(TrustedComponentCollection, s.get(**b))
