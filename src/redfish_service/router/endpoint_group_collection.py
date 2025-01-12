from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.endpoint_group import EndpointGroup, EndpointGroupOnCreate
from ..model.endpoint_group_collection import EndpointGroupCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/Storage/{storage_id}/EndpointGroups", response_model_exclude_none=True)
@router.head("/redfish/v1/Storage/{storage_id}/EndpointGroups", response_model_exclude_none=True)
async def get1(storage_id: str, request: Request, response: Response) -> EndpointGroupCollection:
    s: Service = get_service(EndpointGroupCollection, request)
    b: dict[str, Any] = {"storage_id": storage_id, "request": request, "response": response}
    return cast(EndpointGroupCollection, s.get(**b))


@router.post("/redfish/v1/Storage/{storage_id}/EndpointGroups", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Storage/{storage_id}/EndpointGroups/Members", response_model_exclude_none=True
)
@authenticate
async def post1(
    storage_id: str, request: Request, response: Response, body: EndpointGroupOnCreate
) -> EndpointGroup:
    s: ServiceCollection = get_service_collection(EndpointGroupCollection, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(EndpointGroup, s.post(**b))


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/EndpointGroups",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/EndpointGroups",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str, storage_id: str, request: Request, response: Response
) -> EndpointGroupCollection:
    s: Service = get_service(EndpointGroupCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
    }
    return cast(EndpointGroupCollection, s.get(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/EndpointGroups",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/EndpointGroups/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    computer_system_id: str,
    storage_id: str,
    request: Request,
    response: Response,
    body: EndpointGroupOnCreate,
) -> EndpointGroup:
    s: ServiceCollection = get_service_collection(EndpointGroupCollection, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(EndpointGroup, s.post(**b))


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/EndpointGroups",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/EndpointGroups",
    response_model_exclude_none=True,
)
async def get3(
    storage_service_id: str, request: Request, response: Response
) -> EndpointGroupCollection:
    s: Service = get_service(EndpointGroupCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
    }
    return cast(EndpointGroupCollection, s.get(**b))


@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/EndpointGroups",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/StorageServices/{storage_service_id}/EndpointGroups/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    storage_service_id: str, request: Request, response: Response, body: EndpointGroupOnCreate
) -> EndpointGroup:
    s: ServiceCollection = get_service_collection(EndpointGroupCollection, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(EndpointGroup, s.post(**b))


@router.get("/redfish/v1/Fabrics/{fabric_id}/EndpointGroups", response_model_exclude_none=True)
@router.head("/redfish/v1/Fabrics/{fabric_id}/EndpointGroups", response_model_exclude_none=True)
async def get4(fabric_id: str, request: Request, response: Response) -> EndpointGroupCollection:
    s: Service = get_service(EndpointGroupCollection, request)
    b: dict[str, Any] = {"fabric_id": fabric_id, "request": request, "response": response}
    return cast(EndpointGroupCollection, s.get(**b))


@router.post("/redfish/v1/Fabrics/{fabric_id}/EndpointGroups", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/EndpointGroups/Members", response_model_exclude_none=True
)
@authenticate
async def post4(
    fabric_id: str, request: Request, response: Response, body: EndpointGroupOnCreate
) -> EndpointGroup:
    s: ServiceCollection = get_service_collection(EndpointGroupCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(EndpointGroup, s.post(**b))
