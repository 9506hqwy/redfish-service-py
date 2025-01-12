from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.boot_option import BootOption, BootOptionOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/BootOptions/{boot_option_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    computer_system_id: str, boot_option_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(BootOption, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "boot_option_id": boot_option_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


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
    s: Service = get_service(BootOption, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "boot_option_id": boot_option_id,
        "request": request,
        "response": response,
    }
    return cast(BootOption, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/BootOptions/{boot_option_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    computer_system_id: str,
    boot_option_id: str,
    request: Request,
    response: Response,
    body: BootOptionOnUpdate,
) -> BootOption:
    s: Service = get_service(BootOption, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "boot_option_id": boot_option_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(BootOption, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions/{boot_option_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    resource_block_id: str,
    computer_system_id: str,
    boot_option_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(BootOption, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "boot_option_id": boot_option_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


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
    s: Service = get_service(BootOption, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "boot_option_id": boot_option_id,
        "request": request,
        "response": response,
    }
    return cast(BootOption, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions/{boot_option_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    resource_block_id: str,
    computer_system_id: str,
    boot_option_id: str,
    request: Request,
    response: Response,
    body: BootOptionOnUpdate,
) -> BootOption:
    s: Service = get_service(BootOption, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "boot_option_id": boot_option_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(BootOption, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions/{boot_option_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    resource_block_id: str,
    computer_system_id: str,
    boot_option_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(BootOption, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "boot_option_id": boot_option_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


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
    s: Service = get_service(BootOption, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "boot_option_id": boot_option_id,
        "request": request,
        "response": response,
    }
    return cast(BootOption, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/BootOptions/{boot_option_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    computer_system_id: str,
    boot_option_id: str,
    request: Request,
    response: Response,
    body: BootOptionOnUpdate,
) -> BootOption:
    s: Service = get_service(BootOption, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "boot_option_id": boot_option_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(BootOption, s.patch(**b))
