from typing import cast

from fastapi import APIRouter

from ..model.service_root import ServiceRoot
from ..service import find_service
from . import authenticate

router = APIRouter()


@router.get("/", response_model_exclude_none=True)
@authenticate
async def root() -> ServiceRoot:
    s = find_service(ServiceRoot)
    return cast(ServiceRoot, s.get())
