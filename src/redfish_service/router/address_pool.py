from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.address_pool import AddressPool, AddressPoolOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/Fabrics/{fabric_id}/AddressPools/{address_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    fabric_id: str, address_pool_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(AddressPool, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "address_pool_id": address_pool_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Fabrics/{fabric_id}/AddressPools/{address_pool_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Fabrics/{fabric_id}/AddressPools/{address_pool_id}",
    response_model_exclude_none=True,
)
async def get1(
    fabric_id: str, address_pool_id: str, request: Request, response: Response
) -> AddressPool:
    s: Service = get_service(AddressPool, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "address_pool_id": address_pool_id,
        "request": request,
        "response": response,
    }
    m = cast(AddressPool, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Fabrics/{fabric_id}/AddressPools/{address_pool_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    fabric_id: str,
    address_pool_id: str,
    request: Request,
    response: Response,
    body: AddressPoolOnUpdate,
) -> AddressPool:
    s: Service = get_service(AddressPool, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "address_pool_id": address_pool_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(AddressPool, s.patch(**b))
