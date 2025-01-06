from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.graphics_controller import GraphicsController
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    computer_system_id: str, controller_id: str, request: Request, response: Response
) -> GraphicsController:
    s: Service = find_service(GraphicsController)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(GraphicsController, s.get(**b))
