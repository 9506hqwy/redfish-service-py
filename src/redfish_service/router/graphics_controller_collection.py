from typing import Any, cast

from fastapi import APIRouter

from ..model.graphics_controller_collection import GraphicsControllerCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers",
    response_model_exclude_none=True,
)
@authenticate
async def get1(computer_system_id: str) -> GraphicsControllerCollection:
    s: Service = find_service(GraphicsControllerCollection)
    b: dict[str, Any] = {"computer_system_id": computer_system_id}
    return cast(GraphicsControllerCollection, s.get(**b))
