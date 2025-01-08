from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.boot_option import BootOption
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/BootOptions/{boot_option_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/BootOptions/{boot_option_id}",
    response_model_exclude_none=True,
)
async def get1(
    computer_system_id: str, boot_option_id: str, request: Request, response: Response
) -> BootOption:
    s: Service = find_service(BootOption)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "boot_option_id": boot_option_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(BootOption, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions/{boot_option_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions/{boot_option_id}",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str,
    computer_system_id: str,
    boot_option_id: str,
    request: Request,
    response: Response,
) -> BootOption:
    s: Service = find_service(BootOption)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "boot_option_id": boot_option_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(BootOption, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions/{boot_option_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions/{boot_option_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str,
    computer_system_id: str,
    boot_option_id: str,
    request: Request,
    response: Response,
) -> BootOption:
    s: Service = find_service(BootOption)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "boot_option_id": boot_option_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(BootOption, s.get(**b))
