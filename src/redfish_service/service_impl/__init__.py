from __future__ import annotations  # PEP563 Forward References

from ..service import registry_service
from .account_service import AccountServiceService
from .manager_account import ManagerAccountService
from .manager_account_collection import ManagerAccountCollectionService
from .role import RoleService
from .role_collection import RoleCollectionService
from .service_root import ServiceRootService
from .session import SessionService
from .session_collection import SessionCollectionService

registry_service(AccountServiceService())
registry_service(ManagerAccountService())
registry_service(ManagerAccountCollectionService())
registry_service(RoleService())
registry_service(RoleCollectionService())
registry_service(ServiceRootService())
registry_service(SessionService())
registry_service(SessionCollectionService())
