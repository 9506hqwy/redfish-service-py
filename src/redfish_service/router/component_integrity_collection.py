from typing import Any, cast

from fastapi import APIRouter

from ..model.component_integrity_collection import ComponentIntegrityCollection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get("/redfish/v1/ComponentIntegrity", response_model_exclude_none=True)
@authenticate
async def get1() -> ComponentIntegrityCollection:
    s: Service = find_service(ComponentIntegrityCollection)
    b: dict[str, Any] = {}
    return cast(ComponentIntegrityCollection, s.get(**b))
