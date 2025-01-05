from typing import Any, cast

from fastapi import APIRouter

from ..authenticate import authenticate
from ..model.power_distribution_metrics import PowerDistributionMetrics
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get1(power_distribution_id: str) -> PowerDistributionMetrics:
    s: Service = find_service(PowerDistributionMetrics)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id}
    return cast(PowerDistributionMetrics, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get2(power_distribution_id: str) -> PowerDistributionMetrics:
    s: Service = find_service(PowerDistributionMetrics)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id}
    return cast(PowerDistributionMetrics, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get3(power_distribution_id: str) -> PowerDistributionMetrics:
    s: Service = find_service(PowerDistributionMetrics)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id}
    return cast(PowerDistributionMetrics, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get4(power_distribution_id: str) -> PowerDistributionMetrics:
    s: Service = find_service(PowerDistributionMetrics)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id}
    return cast(PowerDistributionMetrics, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get5(power_distribution_id: str) -> PowerDistributionMetrics:
    s: Service = find_service(PowerDistributionMetrics)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id}
    return cast(PowerDistributionMetrics, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Metrics",
    response_model_exclude_none=True,
)
@authenticate
async def get6(power_distribution_id: str) -> PowerDistributionMetrics:
    s: Service = find_service(PowerDistributionMetrics)
    b: dict[str, Any] = {"power_distribution_id": power_distribution_id}
    return cast(PowerDistributionMetrics, s.get(**b))
