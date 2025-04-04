from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.route_set_entry import RouteSetEntry, RouteSetEntryOnCreate
from ..model.route_set_entry_collection import RouteSetEntryCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet",
    response_model_exclude_none=True,
)
async def get1(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntryCollection:
    s: Service = get_service(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }
    m = cast(RouteSetEntryCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteSetEntryOnCreate,
) -> RouteSetEntry:
    s: ServiceCollection = get_service_collection(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(RouteSetEntry, s.post(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet",
    response_model_exclude_none=True,
)
async def get2(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntryCollection:
    s: Service = get_service(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }
    m = cast(RouteSetEntryCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteSetEntryOnCreate,
) -> RouteSetEntry:
    s: ServiceCollection = get_service_collection(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(RouteSetEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet",
    response_model_exclude_none=True,
)
async def get3(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntryCollection:
    s: Service = get_service(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }
    m = cast(RouteSetEntryCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteSetEntryOnCreate,
) -> RouteSetEntry:
    s: ServiceCollection = get_service_collection(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(RouteSetEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet",
    response_model_exclude_none=True,
)
async def get4(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntryCollection:
    s: Service = get_service(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }
    m = cast(RouteSetEntryCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteSetEntryOnCreate,
) -> RouteSetEntry:
    s: ServiceCollection = get_service_collection(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(RouteSetEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}/RouteSet",
    response_model_exclude_none=True,
)
async def get5(
    chassis_id: str, fabric_adapter_id: str, ssdt_id: str, request: Request, response: Response
) -> RouteSetEntryCollection:
    s: Service = get_service(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }
    m = cast(RouteSetEntryCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}/RouteSet/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post5(
    chassis_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
    body: RouteSetEntryOnCreate,
) -> RouteSetEntry:
    s: ServiceCollection = get_service_collection(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(RouteSetEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}/RouteSet",
    response_model_exclude_none=True,
)
async def get6(
    chassis_id: str, fabric_adapter_id: str, msdt_id: str, request: Request, response: Response
) -> RouteSetEntryCollection:
    s: Service = get_service(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }
    m = cast(RouteSetEntryCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}/RouteSet/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post6(
    chassis_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
    body: RouteSetEntryOnCreate,
) -> RouteSetEntry:
    s: ServiceCollection = get_service_collection(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(RouteSetEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}/RouteSet",
    response_model_exclude_none=True,
)
async def get7(
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntryCollection:
    s: Service = get_service(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
    }
    m = cast(RouteSetEntryCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/MSDT/{msdt_id}/RouteSet/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post7(
    computer_system_id: str,
    fabric_adapter_id: str,
    msdt_id: str,
    request: Request,
    response: Response,
    body: RouteSetEntryOnCreate,
) -> RouteSetEntry:
    s: ServiceCollection = get_service_collection(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "msdt_id": msdt_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(RouteSetEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}/RouteSet",
    response_model_exclude_none=True,
)
async def get8(
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntryCollection:
    s: Service = get_service(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
    }
    m = cast(RouteSetEntryCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/SSDT/{ssdt_id}/RouteSet/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post8(
    computer_system_id: str,
    fabric_adapter_id: str,
    ssdt_id: str,
    request: Request,
    response: Response,
    body: RouteSetEntryOnCreate,
) -> RouteSetEntry:
    s: ServiceCollection = get_service_collection(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "ssdt_id": ssdt_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(RouteSetEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet",
    response_model_exclude_none=True,
)
async def get9(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntryCollection:
    s: Service = get_service(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
    }
    m = cast(RouteSetEntryCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/LPRT/{lprt_id}/RouteSet/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post9(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    lprt_id: str,
    request: Request,
    response: Response,
    body: RouteSetEntryOnCreate,
) -> RouteSetEntry:
    s: ServiceCollection = get_service_collection(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "lprt_id": lprt_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(RouteSetEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet",
    response_model_exclude_none=True,
)
async def get10(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
) -> RouteSetEntryCollection:
    s: Service = get_service(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
    }
    m = cast(RouteSetEntryCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/MPRT/{mprt_id}/RouteSet/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post10(
    computer_system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    mprt_id: str,
    request: Request,
    response: Response,
    body: RouteSetEntryOnCreate,
) -> RouteSetEntry:
    s: ServiceCollection = get_service_collection(RouteSetEntryCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "mprt_id": mprt_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(RouteSetEntry, s.post(**b))
