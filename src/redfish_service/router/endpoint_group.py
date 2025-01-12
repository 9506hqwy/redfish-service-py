from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.endpoint_group import EndpointGroup, EndpointGroupOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Storage/{storage_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    storage_id: str, endpoint_group_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(EndpointGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "endpoint_group_id": endpoint_group_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Storage/{storage_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Storage/{storage_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
async def get1(
    storage_id: str, endpoint_group_id: str, request: Request, response: Response
) -> EndpointGroup:
    s: Service = get_service(EndpointGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "endpoint_group_id": endpoint_group_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EndpointGroup, s.get(**b))


@router.patch(
    "/redfish/v1/Storage/{storage_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    storage_id: str,
    endpoint_group_id: str,
    request: Request,
    response: Response,
    body: EndpointGroupOnUpdate,
) -> EndpointGroup:
    s: Service = get_service(EndpointGroup, request)
    b: dict[str, Any] = {
        "storage_id": storage_id,
        "endpoint_group_id": endpoint_group_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EndpointGroup, s.patch(**b))


@router.delete(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    computer_system_id: str,
    storage_id: str,
    endpoint_group_id: str,
    request: Request,
    response: Response,
) -> None:
    s: Service = get_service(EndpointGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "endpoint_group_id": endpoint_group_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str,
    storage_id: str,
    endpoint_group_id: str,
    request: Request,
    response: Response,
) -> EndpointGroup:
    s: Service = get_service(EndpointGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "endpoint_group_id": endpoint_group_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EndpointGroup, s.get(**b))


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Storage/{storage_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    storage_id: str,
    endpoint_group_id: str,
    request: Request,
    response: Response,
    body: EndpointGroupOnUpdate,
) -> EndpointGroup:
    s: Service = get_service(EndpointGroup, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "storage_id": storage_id,
        "endpoint_group_id": endpoint_group_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EndpointGroup, s.patch(**b))


@router.delete(
    "/redfish/v1/StorageServices/{storage_service_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    storage_service_id: str, endpoint_group_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(EndpointGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "endpoint_group_id": endpoint_group_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/StorageServices/{storage_service_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/StorageServices/{storage_service_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
async def get3(
    storage_service_id: str, endpoint_group_id: str, request: Request, response: Response
) -> EndpointGroup:
    s: Service = get_service(EndpointGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "endpoint_group_id": endpoint_group_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EndpointGroup, s.get(**b))


@router.patch(
    "/redfish/v1/StorageServices/{storage_service_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    storage_service_id: str,
    endpoint_group_id: str,
    request: Request,
    response: Response,
    body: EndpointGroupOnUpdate,
) -> EndpointGroup:
    s: Service = get_service(EndpointGroup, request)
    b: dict[str, Any] = {
        "storage_service_id": storage_service_id,
        "endpoint_group_id": endpoint_group_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EndpointGroup, s.patch(**b))


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    fabric_id: str, endpoint_group_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(EndpointGroup, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "endpoint_group_id": endpoint_group_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return s.delete(**b)


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
async def get4(
    fabric_id: str, endpoint_group_id: str, request: Request, response: Response
) -> EndpointGroup:
    s: Service = get_service(EndpointGroup, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "endpoint_group_id": endpoint_group_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EndpointGroup, s.get(**b))


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/EndpointGroups/{endpoint_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    fabric_id: str,
    endpoint_group_id: str,
    request: Request,
    response: Response,
    body: EndpointGroupOnUpdate,
) -> EndpointGroup:
    s: Service = get_service(EndpointGroup, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "endpoint_group_id": endpoint_group_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(EndpointGroup, s.patch(**b))
