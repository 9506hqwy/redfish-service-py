from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...model.swordfish.storage_system_collection import StorageSystemCollection
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.get("/redfish/v1/StorageSystems", response_model_exclude_none=True)
@router.head("/redfish/v1/StorageSystems", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> StorageSystemCollection:
    s: Service = get_service(StorageSystemCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(StorageSystemCollection, s.get(**b))
