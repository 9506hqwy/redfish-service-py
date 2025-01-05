from typing import Any, cast

from fastapi import APIRouter

from ..model.media_controller import MediaController
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, media_controller_id: str) -> MediaController:
    s: Service = find_service(MediaController)
    b: dict[str, Any] = {"chassis_id": chassis_id, "media_controller_id": media_controller_id}
    return cast(MediaController, s.get(**b))
