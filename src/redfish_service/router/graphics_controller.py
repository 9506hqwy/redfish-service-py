from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.graphics_controller import GraphicsController, GraphicsControllerOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    computer_system_id: str, controller_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(GraphicsController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, controller_id: str, request: Request, response: Response
) -> GraphicsController:
    s: Service = get_service(GraphicsController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(GraphicsController, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    computer_system_id: str,
    controller_id: str,
    request: Request,
    response: Response,
    body: GraphicsControllerOnUpdate,
) -> GraphicsController:
    s: Service = get_service(GraphicsController, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(GraphicsController, s.patch(**b))
