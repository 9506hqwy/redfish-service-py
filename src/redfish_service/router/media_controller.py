from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.media_controller import MediaController
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    chassis_id: str, media_controller_id: str, request: Request, response: Response
) -> MediaController:
    s: Service = find_service(MediaController)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "media_controller_id": media_controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(MediaController, s.get(**b))
