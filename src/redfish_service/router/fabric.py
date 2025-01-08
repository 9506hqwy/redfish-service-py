from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.fabric import Fabric
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Fabrics/{fabric_id}", response_model_exclude_none=True)
async def get1(fabric_id: str, request: Request, response: Response) -> Fabric:
    s: Service = find_service(Fabric)
    b: dict[str, Any] = {"fabric_id": fabric_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(Fabric, s.get(**b))
