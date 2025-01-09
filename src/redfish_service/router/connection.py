from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.connection import Connection
from ..service import Service, find_service

router = APIRouter()


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/Connections/{connection_id}", response_model_exclude_none=True
)
@authenticate
async def delete1(
    fabric_id: str, connection_id: str, request: Request, response: Response
) -> None:
    s: Service = find_service(Connection)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "connection_id": connection_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

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
    s: Service = find_service(Connection)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "connection_id": connection_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(Connection, s.get(**b))
