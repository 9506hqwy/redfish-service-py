from typing import Any, cast

from fastapi import APIRouter

from ..model.graphics_controller import GraphicsController
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(computer_system_id: str, controller_id: str) -> GraphicsController:
    s: Service = find_service(GraphicsController)
    b: dict[str, Any] = {"computer_system_id": computer_system_id, "controller_id": controller_id}
    return cast(GraphicsController, s.get(**b))
