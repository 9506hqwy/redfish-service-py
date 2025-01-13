from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.port import Port, PortOnUpdate, ResetRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get1(
    fabric_id: str, switch_id: str, port_id: str, request: Request, response: Response
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset2(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get3(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset3(
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get4(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset4(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get5(
    computer_system_id: str, controller_id: str, port_id: str, request: Request, response: Response
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset5(
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get6(
    computer_system_id: str, controller_id: str, port_id: str, request: Request, response: Response
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset6(
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get7(
    computer_system_id: str, processor_id: str, port_id: str, request: Request, response: Response
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset7(
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get8(
    chassis_id: str, media_controller_id: str, port_id: str, request: Request, response: Response
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "media_controller_id": media_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    chassis_id: str,
    media_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "media_controller_id": media_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/MediaControllers/{media_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset8(
    chassis_id: str,
    media_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "media_controller_id": media_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get9(
    chassis_id: str, fabric_adapter_id: str, port_id: str, request: Request, response: Response
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset9(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get10(
    chassis_id: str, network_adapter_id: str, port_id: str, request: Request, response: Response
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    chassis_id: str,
    network_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/NetworkAdapters/{network_adapter_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset10(
    chassis_id: str,
    network_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "network_adapter_id": network_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get11(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch11(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset11(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get12(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch12(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset12(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get13(
    resource_block_id: str, processor_id: str, port_id: str, request: Request, response: Response
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch13(
    resource_block_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset13(
    resource_block_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get14(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch14(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset14(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get15(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch15(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset15(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get16(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch16(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset16(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get17(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch17(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset17(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get18(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch18(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset18(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get19(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch19(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset19(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get20(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch20(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset20(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get21(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch21(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset21(
    resource_block_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get22(
    resource_block_id: str, processor_id: str, port_id: str, request: Request, response: Response
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch22(
    resource_block_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Processors/{processor_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset22(
    resource_block_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get23(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch23(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset23(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get24(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch24(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset24(
    resource_block_id: str,
    computer_system_id: str,
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get25(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch25(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset25(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get26(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch26(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/GraphicsControllers/{controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset26(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get27(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch27(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/USBControllers/{controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset27(
    resource_block_id: str,
    computer_system_id: str,
    controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "controller_id": controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get28(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch28(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Processors/{processor_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset28(
    resource_block_id: str,
    computer_system_id: str,
    processor_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get29(
    storage_id: str, storage_controller_id: str, port_id: str, request: Request, response: Response
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch29(
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/StorageControllers/{storage_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset29(
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
async def get30(
    storage_id: str, storage_controller_id: str, port_id: str, request: Request, response: Response
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch30(
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: PortOnUpdate,
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Storage/{storage_id}/Controllers/{storage_controller_id}/Ports/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset30(
    storage_id: str,
    storage_controller_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "storage_controller_id": storage_controller_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/USBPorts/{port_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/USBPorts/{port_id}", response_model_exclude_none=True
)
async def get31(manager_id: str, port_id: str, request: Request, response: Response) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Managers/{manager_id}/USBPorts/{port_id}", response_model_exclude_none=True
)
@authenticate
async def patch31(
    manager_id: str, port_id: str, request: Request, response: Response, body: PortOnUpdate
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/USBPorts/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset31(
    manager_id: str, port_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/DedicatedNetworkPorts/{port_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/DedicatedNetworkPorts/{port_id}",
    response_model_exclude_none=True,
)
async def get32(manager_id: str, port_id: str, request: Request, response: Response) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }
    return cast(Port, s.get(**b))


@router.patch(
    "/redfish/v1/Managers/{manager_id}/DedicatedNetworkPorts/{port_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch32(
    manager_id: str, port_id: str, request: Request, response: Response, body: PortOnUpdate
) -> Port:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Port, s.patch(**b))


@router.post(
    "/redfish/v1/Managers/{manager_id}/DedicatedNetworkPorts/{port_id}/Actions/Port.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset32(
    manager_id: str, port_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(Port, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)
