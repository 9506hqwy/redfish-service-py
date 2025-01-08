from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.vcat_entry import VcatEntry, VcatEntryOnCreate
from ..model.vcat_entry_collection import VcatEntryCollection
from ..service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
async def get1(
    fabric_id: str, switch_id: str, port_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
async def get2(
    system_id: str, fabric_adapter_id: str, port_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT",
    response_model_exclude_none=True,
)
async def get3(
    system_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT",
    response_model_exclude_none=True,
)
async def get4(
    system_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post5(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post6(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT",
    response_model_exclude_none=True,
)
async def get7(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post7(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
async def get8(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post8(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT",
    response_model_exclude_none=True,
)
async def get9(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post9(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT",
    response_model_exclude_none=True,
)
async def get10(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post10(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
async def get11(
    chassis_id: str, fabric_adapter_id: str, port_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post11(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT",
    response_model_exclude_none=True,
)
async def get12(
    chassis_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/REQ-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post12(
    chassis_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT",
    response_model_exclude_none=True,
)
async def get13(
    chassis_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/RSP-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post13(
    chassis_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
async def get14(
    fabric_id: str, switch_id: str, port_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Switches/{switch_id}/Ports/{port_id}/GenZ/VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post14(
    fabric_id: str,
    switch_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "switch_id": switch_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
async def get15(
    system_id: str, fabric_adapter_id: str, port_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post15(
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT",
    response_model_exclude_none=True,
)
async def get16(
    system_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post16(
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT",
    response_model_exclude_none=True,
)
async def get17(
    system_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post17(
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
async def get18(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post18(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT",
    response_model_exclude_none=True,
)
async def get19(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post19(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT",
    response_model_exclude_none=True,
)
async def get20(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post20(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
async def get21(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post21(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT",
    response_model_exclude_none=True,
)
async def get22(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post22(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT",
    response_model_exclude_none=True,
)
async def get23(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{system_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post23(
    resource_block_id: str,
    system_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "system_id": system_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
async def get24(
    chassis_id: str, fabric_adapter_id: str, port_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/Ports/{port_id}/GenZ/VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post24(
    chassis_id: str,
    fabric_adapter_id: str,
    port_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "port_id": port_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT",
    response_model_exclude_none=True,
)
async def get25(
    chassis_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/REQ-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post25(
    chassis_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT",
    response_model_exclude_none=True,
)
async def get26(
    chassis_id: str, fabric_adapter_id: str, request: Request, response: Response
) -> VcatEntryCollection:
    s: Service = find_service(VcatEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntryCollection, s.get(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Chassis/{chassis_id}/FabricAdapters/{fabric_adapter_id}/GenZ/RSP-VCAT/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post26(
    chassis_id: str,
    fabric_adapter_id: str,
    request: Request,
    response: Response,
    body: VcatEntryOnCreate,
) -> VcatEntry:
    s: ServiceCollection = find_service_collection(VcatEntryCollection)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "fabric_adapter_id": fabric_adapter_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(VcatEntry, s.post(**b))
