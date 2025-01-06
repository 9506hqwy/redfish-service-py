from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.route_entry import RouteEntry
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    chassis_id: str, fabric_adapter_id: str, ssdt_id: str, request: Request, response: Response
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    chassis_id: str, fabric_adapter_id: str, msdt_id: str, request: Request, response: Response
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get7(
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get8(
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get9(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get10(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get11(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get12(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get13(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get14(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get15(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get16(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get17(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get18(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get19(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get20(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get21(
    chassis_id: str, fabric_adapter_id: str, ssdt_id: str, request: Request, response: Response
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get22(
    chassis_id: str, fabric_adapter_id: str, msdt_id: str, request: Request, response: Response
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get23(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get24(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get25(
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get26(
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get27(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get28(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get29(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get30(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get31(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get32(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get33(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get34(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get35(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get36(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = find_service(RouteEntry)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))
