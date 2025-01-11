from typing import Any

from ..exception import ResourceNotFoundError
from ..model.account_service import AccountService
from ..repository import instances
from ..service import Service


class AccountServiceService(Service[AccountService]):
    def respond(self, ty: type) -> bool:
        return ty == AccountService

    def get(self, **kwargs: dict[str, Any]) -> AccountService:
        i = instances.find_by_type(AccountService)
        if i is None:
            raise ResourceNotFoundError("ServiceRoot", "ServiceRoot")

        return i
