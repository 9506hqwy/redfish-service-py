from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.outlet_group_collection import OutletGroupCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
@authenticate
async def get1(power_distribution_id: str) -> OutletGroupCollection:
    s: Service = find_service(OutletGroupCollection)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id}
    return cast(OutletGroupCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
@authenticate
async def get2(power_distribution_id: str) -> OutletGroupCollection:
    s: Service = find_service(OutletGroupCollection)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id}
    return cast(OutletGroupCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
@authenticate
async def get3(power_distribution_id: str) -> OutletGroupCollection:
    s: Service = find_service(OutletGroupCollection)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id}
    return cast(OutletGroupCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
@authenticate
async def get4(power_distribution_id: str) -> OutletGroupCollection:
    s: Service = find_service(OutletGroupCollection)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id}
    return cast(OutletGroupCollection, s.get(**b))
