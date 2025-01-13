from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.media_controller import MediaController, ResetRequest
from ..model.redfish_error import RedfishError
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


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}/Actions/MediaController.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    chassis_id: str,
    media_controller_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(MediaController, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "media_controller_id": media_controller_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)
