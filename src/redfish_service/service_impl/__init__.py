from __future__ import annotations  # PEP563 Forward References

from ..service import registry_service
from .service_root import ServiceRootService
from .session import SessionService
from .session_collection import SessionCollectionService

registry_service(ServiceRootService())
registry_service(SessionService())
registry_service(SessionCollectionService())
