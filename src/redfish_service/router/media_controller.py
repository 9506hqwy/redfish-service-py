from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.media_controller import MediaController
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, media_controller_id: str, request: Request, response: Response
) -> MediaController:
    s: Service = get_service(MediaController, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "media_controller_id": media_controller_id,
        "request": request,
        "response": response,
    }
    return cast(MediaController, s.get(**b))
