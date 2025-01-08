from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.route_set_entry import RouteSetEntry
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
async def get1(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    lprt_id: str,
    route_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntry:
    s: Service = find_service(RouteSetEntry)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "route_id": route_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteSetEntry, s.get(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
async def get2(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    mprt_id: str,
    route_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntry:
    s: Service = find_service(RouteSetEntry)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "route_id": route_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteSetEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
async def get3(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    route_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntry:
    s: Service = find_service(RouteSetEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "route_id": route_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteSetEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
async def get4(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    route_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntry:
    s: Service = find_service(RouteSetEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "route_id": route_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteSetEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
async def get5(
    chassis_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    route_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntry:
    s: Service = find_service(RouteSetEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "route_id": route_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteSetEntry, s.get(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
async def get6(
    chassis_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    route_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntry:
    s: Service = find_service(RouteSetEntry)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "route_id": route_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteSetEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
async def get7(
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    route_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntry:
    s: Service = find_service(RouteSetEntry)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "route_id": route_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteSetEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
async def get8(
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    route_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntry:
    s: Service = find_service(RouteSetEntry)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "route_id": route_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteSetEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
async def get9(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    route_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntry:
    s: Service = find_service(RouteSetEntry)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "route_id": route_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteSetEntry, s.get(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet/{route_id}",
    response_model_exclude_none=True,
)
async def get10(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    route_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntry:
    s: Service = find_service(RouteSetEntry)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "route_id": route_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteSetEntry, s.get(**b))
