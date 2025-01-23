from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.memory import (
    DisableMasterPassphraseRequest,
    DisablePassphraseRequest,
    InjectPersistentPoisonRequest,
    Memory,
    MemoryOnUpdate,
    OverwriteUnitRequest,
    ResetRequest,
    ScanMediaRequest,
    SecureEraseUnitRequest,
    SetMasterPassphraseRequest,
    SetPassphraseRequest,
    UnlockUnitRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}", response_model_exclude_none=True
)
async def get1(
    computer_system_id: str, memory_id: str, request: Request, response: Response
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(Memory, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: MemoryOnUpdate,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.DisableMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_master_passphrase1(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisableMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisableMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.DisablePassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_passphrase1(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisablePassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisablePassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.InjectPersistentPoison",
    response_model_exclude_none=True,
)
@authenticate
async def inject_persistent_poison1(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: InjectPersistentPoisonRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "InjectPersistentPoison",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.OverwriteUnit",
    response_model_exclude_none=True,
)
@authenticate
async def overwrite_unit1(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: OverwriteUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "OverwriteUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.ScanMedia",
    response_model_exclude_none=True,
)
@authenticate
async def scan_media1(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ScanMediaRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ScanMedia",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.SecureEraseUnit",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase_unit1(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SecureEraseUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureEraseUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.SetMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_master_passphrase1(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.SetPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_passphrase1(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.UnlockUnit",
    response_model_exclude_none=True,
)
@authenticate
async def unlock_unit1(
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: UnlockUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "UnlockUnit",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}",
    response_model_exclude_none=True,
)
async def get2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(Memory, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: MemoryOnUpdate,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/Actions/Memory.DisableMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_master_passphrase2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisableMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisableMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/Actions/Memory.DisablePassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_passphrase2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisablePassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisablePassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/Actions/Memory.InjectPersistentPoison",
    response_model_exclude_none=True,
)
@authenticate
async def inject_persistent_poison2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: InjectPersistentPoisonRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "InjectPersistentPoison",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/Actions/Memory.OverwriteUnit",
    response_model_exclude_none=True,
)
@authenticate
async def overwrite_unit2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: OverwriteUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "OverwriteUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/Actions/Memory.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/Actions/Memory.ScanMedia",
    response_model_exclude_none=True,
)
@authenticate
async def scan_media2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ScanMediaRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ScanMedia",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/Actions/Memory.SecureEraseUnit",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase_unit2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SecureEraseUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureEraseUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/Actions/Memory.SetMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_master_passphrase2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/Actions/Memory.SetPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_passphrase2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Systems/{computer_system_id}/Processors/{processor_id}/CacheMemory/{memory_id}/Actions/Memory.UnlockUnit",
    response_model_exclude_none=True,
)
@authenticate
async def unlock_unit2(
    computer_system_id: str,
    processor_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: UnlockUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "computer_system_id": computer_system_id,
        "processor_id": processor_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "UnlockUnit",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}", response_model_exclude_none=True
)
async def get3(chassis_id: str, memory_id: str, request: Request, response: Response) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(Memory, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}", response_model_exclude_none=True
)
@authenticate
async def patch3(
    chassis_id: str, memory_id: str, request: Request, response: Response, body: MemoryOnUpdate
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Actions/Memory.DisableMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_master_passphrase3(
    chassis_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisableMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisableMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Actions/Memory.DisablePassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_passphrase3(
    chassis_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisablePassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisablePassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Actions/Memory.InjectPersistentPoison",
    response_model_exclude_none=True,
)
@authenticate
async def inject_persistent_poison3(
    chassis_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: InjectPersistentPoisonRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "InjectPersistentPoison",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Actions/Memory.OverwriteUnit",
    response_model_exclude_none=True,
)
@authenticate
async def overwrite_unit3(
    chassis_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: OverwriteUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "OverwriteUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Actions/Memory.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset3(
    chassis_id: str, memory_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Actions/Memory.ScanMedia",
    response_model_exclude_none=True,
)
@authenticate
async def scan_media3(
    chassis_id: str, memory_id: str, request: Request, response: Response, body: ScanMediaRequest
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ScanMedia",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Actions/Memory.SecureEraseUnit",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase_unit3(
    chassis_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SecureEraseUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureEraseUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Actions/Memory.SetMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_master_passphrase3(
    chassis_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Actions/Memory.SetPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_passphrase3(
    chassis_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/Memory/{memory_id}/Actions/Memory.UnlockUnit",
    response_model_exclude_none=True,
)
@authenticate
async def unlock_unit3(
    chassis_id: str, memory_id: str, request: Request, response: Response, body: UnlockUnitRequest
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "UnlockUnit",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
async def get4(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(Memory, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: MemoryOnUpdate,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.DisableMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_master_passphrase4(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisableMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisableMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.DisablePassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_passphrase4(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisablePassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisablePassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.InjectPersistentPoison",
    response_model_exclude_none=True,
)
@authenticate
async def inject_persistent_poison4(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: InjectPersistentPoisonRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "InjectPersistentPoison",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.OverwriteUnit",
    response_model_exclude_none=True,
)
@authenticate
async def overwrite_unit4(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: OverwriteUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "OverwriteUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset4(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.ScanMedia",
    response_model_exclude_none=True,
)
@authenticate
async def scan_media4(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ScanMediaRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ScanMedia",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.SecureEraseUnit",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase_unit4(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SecureEraseUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureEraseUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.SetMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_master_passphrase4(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.SetPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_passphrase4(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.UnlockUnit",
    response_model_exclude_none=True,
)
@authenticate
async def unlock_unit4(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: UnlockUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "UnlockUnit",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
async def get5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(Memory, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: MemoryOnUpdate,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.DisableMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_master_passphrase5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisableMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisableMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.DisablePassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_passphrase5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisablePassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisablePassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.InjectPersistentPoison",
    response_model_exclude_none=True,
)
@authenticate
async def inject_persistent_poison5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: InjectPersistentPoisonRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "InjectPersistentPoison",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.OverwriteUnit",
    response_model_exclude_none=True,
)
@authenticate
async def overwrite_unit5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: OverwriteUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "OverwriteUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.ScanMedia",
    response_model_exclude_none=True,
)
@authenticate
async def scan_media5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ScanMediaRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ScanMedia",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.SecureEraseUnit",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase_unit5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SecureEraseUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureEraseUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.SetMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_master_passphrase5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.SetPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_passphrase5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.UnlockUnit",
    response_model_exclude_none=True,
)
@authenticate
async def unlock_unit5(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: UnlockUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "UnlockUnit",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
async def get6(
    resource_block_id: str, memory_id: str, request: Request, response: Response
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(Memory, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: MemoryOnUpdate,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.DisableMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_master_passphrase6(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisableMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisableMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.DisablePassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_passphrase6(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisablePassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisablePassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.InjectPersistentPoison",
    response_model_exclude_none=True,
)
@authenticate
async def inject_persistent_poison6(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: InjectPersistentPoisonRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "InjectPersistentPoison",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.OverwriteUnit",
    response_model_exclude_none=True,
)
@authenticate
async def overwrite_unit6(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: OverwriteUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "OverwriteUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset6(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.ScanMedia",
    response_model_exclude_none=True,
)
@authenticate
async def scan_media6(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ScanMediaRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ScanMedia",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.SecureEraseUnit",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase_unit6(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SecureEraseUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureEraseUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.SetMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_master_passphrase6(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.SetPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_passphrase6(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Memory/{memory_id}/Actions/Memory.UnlockUnit",
    response_model_exclude_none=True,
)
@authenticate
async def unlock_unit6(
    resource_block_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: UnlockUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "UnlockUnit",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
async def get7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
    }
    m = cast(Memory, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: MemoryOnUpdate,
) -> Memory:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Memory, s.patch(**b))


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.DisableMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_master_passphrase7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisableMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisableMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.DisablePassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def disable_passphrase7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: DisablePassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "DisablePassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.InjectPersistentPoison",
    response_model_exclude_none=True,
)
@authenticate
async def inject_persistent_poison7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: InjectPersistentPoisonRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "InjectPersistentPoison",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.OverwriteUnit",
    response_model_exclude_none=True,
)
@authenticate
async def overwrite_unit7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: OverwriteUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "OverwriteUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.ScanMedia",
    response_model_exclude_none=True,
)
@authenticate
async def scan_media7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: ScanMediaRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "ScanMedia",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.SecureEraseUnit",
    response_model_exclude_none=True,
)
@authenticate
async def secure_erase_unit7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SecureEraseUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SecureEraseUnit",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.SetMasterPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_master_passphrase7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetMasterPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetMasterPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.SetPassphrase",
    response_model_exclude_none=True,
)
@authenticate
async def set_passphrase7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: SetPassphraseRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetPassphrase",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ResourceBlocks/{resource_block_id}/Systems/{computer_system_id}/Memory/{memory_id}/Actions/Memory.UnlockUnit",
    response_model_exclude_none=True,
)
@authenticate
async def unlock_unit7(
    resource_block_id: str,
    computer_system_id: str,
    memory_id: str,
    request: Request,
    response: Response,
    body: UnlockUnitRequest,
) -> RedfishError:
    s: Service = get_service(Memory, request)
    b: dict[str, Any] = {
        "resource_block_id": resource_block_id,
        "computer_system_id": computer_system_id,
        "memory_id": memory_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "UnlockUnit",
    }
    return s.action(**b)
