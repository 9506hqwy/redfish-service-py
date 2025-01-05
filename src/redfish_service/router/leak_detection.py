from typing import Any, cast

from fastapi import APIRouter

from ..model.leak_detection import LeakDetection
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/LeakDetection",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str) -> LeakDetection:
    s: Service = find_service(LeakDetection)
    b: dict[str, Any] = {"chassis_id": chassis_id}
    return cast(LeakDetection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/LeakDetection",
    response_model_exclude_none=True,
)
@authenticate
async def get2(cooling_unit_id: str) -> LeakDetection:
    s: Service = find_service(LeakDetection)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id}
    return cast(LeakDetection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/LeakDetection",
    response_model_exclude_none=True,
)
@authenticate
async def get3(cooling_unit_id: str) -> LeakDetection:
    s: Service = find_service(LeakDetection)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id}
    return cast(LeakDetection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/LeakDetection",
    response_model_exclude_none=True,
)
@authenticate
async def get4(cooling_unit_id: str) -> LeakDetection:
    s: Service = find_service(LeakDetection)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id}
    return cast(LeakDetection, s.get(**b))
