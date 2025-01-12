from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.application import Application
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Applications/{application_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/OperatingSystem/Applications/{application_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, application_id: str, request: Request, response: Response
) -> Application:
    s: Service = get_service(Application, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "application_id": application_id,
        "request": request,
        "response": response,
    }
    return cast(Application, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Applications/{application_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Applications/{application_id}",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str,
    computer_system_id: str,
    application_id: str,
    request: Request,
    response: Response,
) -> Application:
    s: Service = get_service(Application, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "application_id": application_id,
        "request": request,
        "response": response,
    }
    return cast(Application, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Applications/{application_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/OperatingSystem/Applications/{application_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    application_id: str,
    request: Request,
    response: Response,
) -> Application:
    s: Service = get_service(Application, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "application_id": application_id,
        "request": request,
        "response": response,
    }
    return cast(Application, s.get(**b))
