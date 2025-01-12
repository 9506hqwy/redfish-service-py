from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.connection import Connection, ConnectionOnUpdate
from ..service import Service
from ..util import get_service

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
    return cast(Connection, s.get(**b))


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
