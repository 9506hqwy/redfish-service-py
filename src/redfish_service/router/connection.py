from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.connection import (
    AddVolumeInfoRequest,
    Connection,
    ConnectionOnUpdate,
    RemoveVolumeInfoRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/Connections/{connection_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(
    fabric_id: str, connection_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Connection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "connection_id": connection_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Connections/{connection_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/Connections/{connection_id}", response_model_exclude_none=True
)
async def get1(
    fabric_id: str, connection_id: str, request: Request, response: Response
) -> Connection:
    s: Service = get_service(Connection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "connection_id": connection_id,
        "request": request,
        "response": response,
    }
    m = cast(Connection, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/Connections/{connection_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    fabric_id: str,
    connection_id: str,
    request: Request,
    response: Response,
    body: ConnectionOnUpdate,
) -> Connection:
    s: Service = get_service(Connection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "connection_id": connection_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Connection, s.patch(**b))


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Connections/{connection_id}/Actions/Connection.AddVolumeInfo",
    response_model_exclude_none=True,
)
@authenticate
async def add_volume_info1(
    fabric_id: str,
    connection_id: str,
    request: Request,
    response: Response,
    body: AddVolumeInfoRequest,
) -> RedfishError:
    s: Service = get_service(Connection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "connection_id": connection_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddVolumeInfo",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Connections/{connection_id}/Actions/Connection.RemoveVolumeInfo",
    response_model_exclude_none=True,
)
@authenticate
async def remove_volume_info1(
    fabric_id: str,
    connection_id: str,
    request: Request,
    response: Response,
    body: RemoveVolumeInfoRequest,
) -> RedfishError:
    s: Service = get_service(Connection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "connection_id": connection_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveVolumeInfo",
    }
    return s.action(**b)
