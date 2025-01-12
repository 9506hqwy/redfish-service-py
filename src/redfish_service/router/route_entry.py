from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.route_entry import RouteEntry, RouteEntryOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
async def get2(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    chassis_id: str, fabric_adapter_id: str, ssdt_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
async def get3(
    chassis_id: str, fabric_adapter_id: str, ssdt_id: str, request: Request, response: Response
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    chassis_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    chassis_id: str, fabric_adapter_id: str, msdt_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
async def get4(
    chassis_id: str, fabric_adapter_id: str, msdt_id: str, request: Request, response: Response
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    chassis_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete5(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
async def get5(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete6(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
async def get6(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete7(
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
async def get7(
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete8(
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
async def get8(
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete9(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
async def get9(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete10(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
async def get10(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete11(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
async def get11(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch11(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete12(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
async def get12(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch12(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete13(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
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

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
async def get13(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch13(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete14(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
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

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
async def get14(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch14(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete15(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
async def get15(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch15(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete16(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
async def get16(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch16(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete17(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
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

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
async def get17(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch17(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete18(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
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

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
async def get18(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch18(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete19(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
async def get19(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch19(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete20(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
async def get20(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch20(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete21(
    chassis_id: str, fabric_adapter_id: str, ssdt_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
async def get21(
    chassis_id: str, fabric_adapter_id: str, ssdt_id: str, request: Request, response: Response
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch21(
    chassis_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete22(
    chassis_id: str, fabric_adapter_id: str, msdt_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
async def get22(
    chassis_id: str, fabric_adapter_id: str, msdt_id: str, request: Request, response: Response
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch22(
    chassis_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete23(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
async def get23(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch23(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete24(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
async def get24(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch24(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete25(
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
async def get25(
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch25(
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete26(
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
async def get26(
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch26(
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete27(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
async def get27(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch27(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete28(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
async def get28(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch28(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete29(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
async def get29(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch29(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete30(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
async def get30(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch30(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete31(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
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

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
async def get31(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch31(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete32(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
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

    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
async def get32(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch32(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete33(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
async def get33(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/MSDT/{msdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch33(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete34(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
async def get34(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/SSDT/{ssdt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch34(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete35(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
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

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
async def get35(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/LPRT/{lprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch35(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete36(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(RouteEntry, request)
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

    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
async def get36(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
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


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/MPRT/{mprt_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch36(
    resource_block_id: str,
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteEntryOnUpdate,
) -> RouteEntry:
    s: Service = get_service(RouteEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(RouteEntry, s.patch(**b))
