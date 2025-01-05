from typing import Any, cast

from fastapi import APIRouter

from ..model.leak_detector import LeakDetector
from ..service import Service, find_service
from . import authenticate

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, leak_detector_id: str) -> LeakDetector:
    s: Service = find_service(LeakDetector)
    b: dict[str, Any] = {"chassis_id": chassis_id, "leak_detector_id": leak_detector_id}
    return cast(LeakDetector, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(cooling_unit_id: str, leak_detector_id: str) -> LeakDetector:
    s: Service = find_service(LeakDetector)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "leak_detector_id": leak_detector_id}
    return cast(LeakDetector, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(cooling_unit_id: str, leak_detector_id: str) -> LeakDetector:
    s: Service = find_service(LeakDetector)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "leak_detector_id": leak_detector_id}
    return cast(LeakDetector, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(cooling_unit_id: str, leak_detector_id: str) -> LeakDetector:
    s: Service = find_service(LeakDetector)
    b: dict[str, Any] = {"cooling_unit_id": cooling_unit_id, "leak_detector_id": leak_detector_id}
    return cast(LeakDetector, s.get(**b))
