from typing import Any

from ..exception import ResourceNotFoundError
from ..model.session_collection import SessionCollection
from ..repository import instances
from ..service import Service


class SessionCollectionService(Service[SessionCollection]):
    def respond(self, ty: type) -> bool:
        return ty == SessionCollection

    def get(self, **kwargs: dict[str, Any]) -> SessionCollection:
        i = instances.find_by_type(SessionCollection)
        if i is None:
            raise ResourceNotFoundError("SessionCollection", "SessionCollection")
        return i
