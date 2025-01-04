from ..model import RedfishModel


class Instances(object):
    def __init__(self) -> None:
        self.instances: list[RedfishModel] = []

    def add(self, instance: RedfishModel) -> None:
        self.instances.append(instance)

    def find_by_type[T: RedfishModel](self, ty: type[T]) -> T | None:
        for i in self.instances:
            if isinstance(i, ty):
                return i

        return None


instances = Instances()
