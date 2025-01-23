from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.outlet_collection import OutletCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Outlets",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Outlets",
    response_model_exclude_none=True,
)
async def get1(
    power_distribution_id: str, request: Request, response: Response
) -> OutletCollection:
    s: Service = get_service(OutletCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(OutletCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Outlets",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Outlets",
    response_model_exclude_none=True,
)
async def get2(
    power_distribution_id: str, request: Request, response: Response
) -> OutletCollection:
    s: Service = get_service(OutletCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(OutletCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Outlets",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Outlets",
    response_model_exclude_none=True,
)
async def get3(
    power_distribution_id: str, request: Request, response: Response
) -> OutletCollection:
    s: Service = get_service(OutletCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(OutletCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Outlets",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Outlets",
    response_model_exclude_none=True,
)
async def get4(
    power_distribution_id: str, request: Request, response: Response
) -> OutletCollection:
    s: Service = get_service(OutletCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(OutletCollection, s.get(**b))
    set_link_header(m, response)
    return m
