from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.address_pool_collection import AddressPoolCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/AddressPools", response_model_exclude_none=True)
@authenticate
async def get1(fabric_id: str) -> AddressPoolCollection:
    s: Service = find_service(AddressPoolCollection)
    b: dict[str, Any] = {"fabric_id": fabric_id}
    return cast(AddressPoolCollection, s.get(**b))
