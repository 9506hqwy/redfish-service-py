from typing import Any, cast

from fastapi import APIRouter

from ..model.connection import Connection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/Connections/{connection_id}", response_model_exclude_none=True
)
@authenticate
async def get1(fabric_id: str, connection_id: str) -> Connection:
    s: Service = find_service(Connection)
    b: dict[str, Any] = {"fabric_id": fabric_id, "connection_id": connection_id}
    return cast(Connection, s.get(**b))
