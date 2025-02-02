from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.vcat_entry import VcatEntry, VcatEntryOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get1(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get2(
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get3(
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get4(
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete5(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete6(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete7(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get7(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete8(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get8(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete9(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get9(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete10(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get10(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete11(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get11(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch11(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete12(
    chassis_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get12(
    chassis_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch12(
    chassis_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete13(
    chassis_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get13(
    chassis_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch13(
    chassis_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete14(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get14(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch14(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete15(
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get15(
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch15(
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete16(
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get16(
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch16(
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete17(
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get17(
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch17(
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete18(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get18(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch18(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete19(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get19(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch19(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete20(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get20(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch20(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete21(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get21(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch21(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete22(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get22(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch22(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete23(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get23(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch23(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete24(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get24(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch24(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete25(
    chassis_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get25(
    chassis_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch25(
    chassis_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))


@router.delete(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete26(
    chassis_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
async def get26(
    chassis_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
    }
    m = cast(VcatEntry, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/{vcat_entry_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch26(
    chassis_id: str,
    fabric_adapter_id: str,
    vcat_entry_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnUpdate,
) -> VcatEntry:
    s: Service = get_service(VcatEntry, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "vcat_entry_id": vcat_entry_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(VcatEntry, s.patch(**b))
