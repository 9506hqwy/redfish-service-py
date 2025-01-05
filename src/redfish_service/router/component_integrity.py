from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.component_integrity import ComponentIntegrity
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/ComponentIntegrity/{component_integrity_id}", response_model_exclude_none=True
)
@authenticate
async def get1(component_integrity_id: str) -> ComponentIntegrity:
    s: Service = find_service(ComponentIntegrity)
    b: dict[str, Any] = {"component_integrity_id": component_integrity_id}
    return cast(ComponentIntegrity, s.get(**b))
