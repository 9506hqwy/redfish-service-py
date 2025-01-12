from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.circuit import Circuit, CircuitOnUpdate
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
async def get1(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
async def get2(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
async def get3(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
async def get4(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Subfeeds/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Subfeeds/{circuit_id}",
    response_model_exclude_none=True,
)
async def get5(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Subfeeds/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
async def get6(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
async def get7(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Feeders/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Feeders/{circuit_id}",
    response_model_exclude_none=True,
)
async def get8(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Feeders/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
async def get9(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch9(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
async def get10(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch10(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
async def get11(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch11(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Subfeeds/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Subfeeds/{circuit_id}",
    response_model_exclude_none=True,
)
async def get12(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Subfeeds/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch12(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Feeders/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Feeders/{circuit_id}",
    response_model_exclude_none=True,
)
async def get13(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Feeders/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch13(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
async def get14(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch14(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
async def get15(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Mains/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch15(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
async def get16(
    power_distribution_id: str, circuit_id: str, request: Request, response: Response
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
    }
    return cast(Circuit, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/Branches/{circuit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch16(
    power_distribution_id: str,
    circuit_id: str,
    request: Request,
    response: Response,
    body: CircuitOnUpdate,
) -> Circuit:
    s: Service = get_service(Circuit, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "circuit_id": circuit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Circuit, s.patch(**b))
