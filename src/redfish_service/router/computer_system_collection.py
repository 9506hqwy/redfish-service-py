from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.computer_system_collection import ComputerSystemCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Systems", response_model_exclude_none=True)
@authenticate
async def get1() -> ComputerSystemCollection:
    s: Service = find_service(ComputerSystemCollection)
    b: dict[str, Any] = {}
    return cast(ComputerSystemCollection, s.get(**b))
