from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.route_entry import RouteEntry, RouteEntryOnCreate
from ..model.route_entry_collection import RouteEntryCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, fabric_adapter_id: str, port_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
async def get2(
    chassis_id: str, fabric_adapter_id: str, port_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT",
    response_model_exclude_none=True,
)
async def get3(
    chassis_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    chassis_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT",
    response_model_exclude_none=True,
)
async def get4(
    chassis_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    chassis_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
async def get5(
    fabric_id: str, switch_id: str, port_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post5(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
async def get6(
    fabric_id: str, switch_id: str, port_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post6(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT",
    response_model_exclude_none=True,
)
async def get7(
    computer_system_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post7(
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT",
    response_model_exclude_none=True,
)
async def get8(
    computer_system_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post8(
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
async def get9(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post9(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
async def get10(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post10(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT",
    response_model_exclude_none=True,
)
async def get11(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post11(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT",
    response_model_exclude_none=True,
)
async def get12(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post12(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
async def get13(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post13(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
async def get14(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post14(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT",
    response_model_exclude_none=True,
)
async def get15(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post15(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT",
    response_model_exclude_none=True,
)
async def get16(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post16(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
async def get17(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post17(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
async def get18(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post18(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
async def get19(
    chassis_id: str, fabric_adapter_id: str, port_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post19(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
async def get20(
    chassis_id: str, fabric_adapter_id: str, port_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post20(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT",
    response_model_exclude_none=True,
)
async def get21(
    chassis_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post21(
    chassis_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT",
    response_model_exclude_none=True,
)
async def get22(
    chassis_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post22(
    chassis_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
async def get23(
    fabric_id: str, switch_id: str, port_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/LPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post23(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
async def get24(
    fabric_id: str, switch_id: str, port_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/MPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post24(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT",
    response_model_exclude_none=True,
)
async def get25(
    computer_system_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post25(
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT",
    response_model_exclude_none=True,
)
async def get26(
    computer_system_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post26(
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
async def get27(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post27(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
async def get28(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post28(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT",
    response_model_exclude_none=True,
)
async def get29(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post29(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT",
    response_model_exclude_none=True,
)
async def get30(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post30(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
async def get31(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post31(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
async def get32(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post32(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT",
    response_model_exclude_none=True,
)
async def get33(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post33(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT",
    response_model_exclude_none=True,
)
async def get34(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post34(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
async def get35(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post35(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
async def get36(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> RouteEntryCollection:
    s: Service = get_service(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post36(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnCreate,
) -> RouteEntry:
    s: ServiceCollection = get_service_collection(RouteEntryCollection, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.post(**b))
