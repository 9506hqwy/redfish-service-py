from typing import Generator

from ..model import RedfishModel


class Instances(object):
    def __init__(self) -> None:
        self.instances: list[RedfishModel] = []

    def add(self, instance: RedfishModel) -> None:
        self.instances.append(instance)

    def enum_by_type[T: RedfishModel](self, ty: type[T]) -> Generator[T, None, None]:
        for i in self.instances:
            if isinstance(i, ty):
                yield i

    def find_by_type[T: RedfishModel](self, ty: type[T]) -> T | None:
        for i in self.enum_by_type(ty):
            return i

        return None

    def remove(self, item: RedfishModel) -> None:
        self.instances.remove(item)


instances = Instances()
