from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.computer_system import (
    AddResourceBlockRequest,
    ComputerSystem,
    ComputerSystemOnUpdate,
    DecommissionRequest,
    ExportConfigurationRequest,
    RemoveResourceBlockRequest,
    ResetRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete("/redfish/v1/Systems/{computer_system_id}", response_model_exclude_none=True)
@authenticate
async def delete1(computer_system_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get("/redfish/v1/Systems/{computer_system_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Systems/{computer_system_id}", response_model_exclude_none=True)
async def get1(computer_system_id: str, request: Request, response: Response) -> ComputerSystem:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(ComputerSystem, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/Systems/{computer_system_id}", response_model_exclude_none=True)
@authenticate
async def patch1(
    computer_system_id: str, request: Request, response: Response, body: ComputerSystemOnUpdate
) -> ComputerSystem:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ComputerSystem, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Actions/ComputerSystem.AddResourceBlock",
    response_model_exclude_none=True,
)
@authenticate
async def add_resource_block1(
    computer_system_id: str, request: Request, response: Response, body: AddResourceBlockRequest
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddResourceBlock",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Actions/ComputerSystem.Decommission",
    response_model_exclude_none=True,
)
@authenticate
async def decommission1(
    computer_system_id: str, request: Request, response: Response, body: DecommissionRequest
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Decommission",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Actions/ComputerSystem.ExportConfiguration",
    response_model_exclude_none=True,
)
@authenticate
async def export_configuration1(
    computer_system_id: str, request: Request, response: Response, body: ExportConfigurationRequest
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ExportConfiguration",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Actions/ComputerSystem.RemoveResourceBlock",
    response_model_exclude_none=True,
)
@authenticate
async def remove_resource_block1(
    computer_system_id: str, request: Request, response: Response, body: RemoveResourceBlockRequest
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveResourceBlock",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Actions/ComputerSystem.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    computer_system_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
async def get2(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> ComputerSystem:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(ComputerSystem, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: ComputerSystemOnUpdate,
) -> ComputerSystem:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ComputerSystem, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Actions/ComputerSystem.AddResourceBlock",
    response_model_exclude_none=True,
)
@authenticate
async def add_resource_block2(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: AddResourceBlockRequest,
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddResourceBlock",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Actions/ComputerSystem.Decommission",
    response_model_exclude_none=True,
)
@authenticate
async def decommission2(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: DecommissionRequest,
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Decommission",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Actions/ComputerSystem.ExportConfiguration",
    response_model_exclude_none=True,
)
@authenticate
async def export_configuration2(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: ExportConfigurationRequest,
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ExportConfiguration",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Actions/ComputerSystem.RemoveResourceBlock",
    response_model_exclude_none=True,
)
@authenticate
async def remove_resource_block2(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: RemoveResourceBlockRequest,
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveResourceBlock",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Actions/ComputerSystem.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset2(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
async def get3(
    resource_block_id: str, computer_system_id: str, request: Request, response: Response
) -> ComputerSystem:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
    }
    m = cast(ComputerSystem, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: ComputerSystemOnUpdate,
) -> ComputerSystem:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ComputerSystem, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Actions/ComputerSystem.AddResourceBlock",
    response_model_exclude_none=True,
)
@authenticate
async def add_resource_block3(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: AddResourceBlockRequest,
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddResourceBlock",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Actions/ComputerSystem.Decommission",
    response_model_exclude_none=True,
)
@authenticate
async def decommission3(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: DecommissionRequest,
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Decommission",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Actions/ComputerSystem.ExportConfiguration",
    response_model_exclude_none=True,
)
@authenticate
async def export_configuration3(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: ExportConfigurationRequest,
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ExportConfiguration",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Actions/ComputerSystem.RemoveResourceBlock",
    response_model_exclude_none=True,
)
@authenticate
async def remove_resource_block3(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: RemoveResourceBlockRequest,
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveResourceBlock",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Actions/ComputerSystem.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset3(
    resource_block_id: str,
    computer_system_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(ComputerSystem, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)
