from __future__ import annotations  # PEP563 Forward References

import itertools
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Generator, TypeGuard
from urllib.parse import urlparse
from warnings import warn

# TODO
COMMON_VALUES: list[str] = ["EventType"]
# TODO
PLAIN_VALUES: list[str] = ["Oem"]


@dataclass
class ClassInfo:
    domain: str
    schema_path: Path
    definition: dict[str, Any]
    name: str
    properties: list[PropetyInfo]
    reachable: bool = False
    loaded: bool = False
    _module: str | None = None

    @property
    def base_name(self) -> str:
        def get_base_class_name(d: dict[str, Any]) -> str:
            if has_base_resource_collection(d):
                return "RedfishResourceCollection"

            if has_base_resource(d):
                return "RedfishResource"

            if has_base_object_id(d):
                return "RedfishObjectId"

            if has_base_object(d):
                return "RedfishObject"

            return "RedfishModel"

        if (any_of := self.definition.get("anyOf", None)) is not None:
            selected = select_definition(any_of)
            if isinstance(selected, dict):
                return get_base_class_name(selected["properties"])

        if (properties := self.definition.get("properties", None)) is not None:
            return get_base_class_name(properties)

        return "RedfishModel"

    @property
    def cls_name(self) -> str:
        return get_class_name(self.name)

    @property
    def id_ref(self) -> bool:
        if (any_of := self.definition.get("anyOf", None)) is not None:
            ids: list[str] = [d["$ref"] for d in any_of if "$ref" in d]
            return any(filter(lambda r: r.endswith("/idRef"), ids))
        return False

    @property
    def is_primitive(self) -> bool:
        return is_primitive(self.definition)

    @property
    def is_primitive_array(self) -> bool:
        return is_array(self.definition) and is_primitive(self.definition["items"])

    @property
    def module(self) -> str:
        return self._module or get_module_name(self.schema_path)

    @property
    def module_path(self) -> str:
        m = self.module
        if self.domain == "swordfish":
            m = f"swordfish.{m}"
        return m

    @property
    def required(self) -> list[str]:
        v: list[str] = self.definition.get("required", [])
        return v

    @property
    def type_name(self) -> str:
        return get_primitive_type_name(self.definition) or self.cls_name

    @property
    def version(self) -> tuple[int, int, int] | None:
        if not self.versioned:
            return None

        version = get_module_name(self.schema_path).rsplit(".", 1)[-1].split("_", 2)
        return (int(version[0].strip("v")), int(version[1]), int(version[2]))

    @property
    def versioned(self) -> bool:
        return get_module_name(self.schema_path).find(".") > -1

    def is_base_properties(self, name: str) -> bool:
        if self.base_name == "RedfishResourceCollection":
            return is_base_collection_properties(name)
        elif self.base_name == "RedfishResource":
            return is_base_resource_properties(name)
        elif self.base_name == "RedfishObjectId":
            return is_base_id_properties(name)
        elif self.base_name == "RedfishObject":
            return is_base_object_properties(name)
        else:
            return False

    def load_properties(self, classall: list[ClassInfo | EnumInfo]) -> None:
        self.load_properties_from_definition(classall, self.definition)

    def load_properties_from_definition(
        self, classall: list[ClassInfo | EnumInfo], definition: dict[str, Any]
    ) -> None:
        if (properties := definition.get("properties", None)) is not None:
            for prop_name, prop_definition in properties.items():
                self._load_property(classall, prop_name, prop_definition)

    def set_module(self, module: str) -> None:
        self._module = module

    def _load_property(
        self,
        classall: list[ClassInfo | EnumInfo],
        name: str,
        definition: dict[str, Any],
    ) -> None:
        if not self.is_base_properties(name):
            type, array = resolve_property_type(classall, self, definition)
            nonable = name not in self.required
            info = PropetyInfo(name, type, array, nonable)
            self.properties.append(info)

    def __hash__(self) -> int:
        return (self.schema_path, self.name).__hash__()

    def __str__(self) -> str:
        return f"{self.schema_path}#{self.name}"


@dataclass
class EnumInfo:
    domain: str
    schema_path: Path
    definition: dict[str, Any]
    name: str
    properties: list[str]
    reachable: bool = False
    loaded: bool = False
    _module: str | None = None

    @property
    def cls_name(self) -> str:
        return get_class_name(self.name)

    @property
    def id_ref(self) -> bool:
        return False

    @property
    def module(self) -> str:
        return self._module or get_module_name(self.schema_path)

    @property
    def module_path(self) -> str:
        m = self.module
        if self.domain == "swordfish":
            m = f"swordfish.{m}"
        return m

    @property
    def type_name(self) -> str:
        return self.cls_name

    @property
    def version(self) -> tuple[int, int, int] | None:
        if not self.versioned:
            return None

        version = get_module_name(self.schema_path).rsplit(".", 1)[-1].split("_", 2)
        return (int(version[0].strip("v")), int(version[1]), int(version[2]))

    @property
    def versioned(self) -> bool:
        return get_module_name(self.schema_path).find(".") > -1

    def set_module(self, module: str) -> None:
        self._module = module

    def write_to(self, w: Any) -> None:
        w.write(f"class {self.cls_name}(StrEnum):\n")
        for v in self.properties:
            w.write(f'    {get_variant_name(v)} = "{v}"')
            if v.lower().find("password") > -1:
                w.write("  # noqa: S105")
            w.write("\n")
        return None

    def __hash__(self) -> int:
        return (self.schema_path, self.name).__hash__()

    def __str__(self) -> str:
        return f"{self.schema_path}#{self.name}"


@dataclass
class PropetyInfo:
    name: str
    type: str | ClassInfo | EnumInfo
    array: bool
    nonable: bool


def get_class_name(name: str) -> str:
    words = get_snake_case(name).split("_")
    return "".join(map(lambda w: w.capitalize(), words))


def get_module_name(path: Path) -> str:
    name = path.name.rsplit(".", 1)[0]
    name = name.replace("-", "_")
    return get_snake_case(name)


def get_snake_case(name: str) -> str:
    words = [w.lower() for w in re.split(r"([A-Z]+[^A-Z]+)", name) if w]
    return "_".join(words).replace(" ", "_")


def get_primitive_type_name(definition: dict[str, Any]) -> str | None:
    if type := definition.get("type", None):
        match type:
            case "boolean":
                return "bool"
            case "integer":
                return "int"
            case "number":
                return "float"
            case "string":
                return "str"
            case _:
                pass

    return None


def get_variant_name(name: str) -> str:
    v = get_snake_case(name).upper()
    if re.match(r"^\d", v):
        v = f"N{v}"
    return v


def has_base_object(definition: dict[str, Any]) -> bool:
    return (
        "@odata.context" in definition
        and "@odata.etag" in definition
        and "@odata.id" in definition
        and "@odata.type" in definition
    )


def has_base_object_id(definition: dict[str, Any]) -> bool:
    return "@odata.id" in definition and "@odata.type" not in definition


def has_base_resource(definition: dict[str, Any]) -> bool:
    return has_base_object(definition) and "Id" in definition and "Name" in definition


def has_base_resource_collection(definition: dict[str, Any]) -> bool:
    return (
        has_base_object(definition)
        and "Description" in definition
        and "Members" in definition
        and "Members@odata.count" in definition
        and "Members@odata.nextLink" in definition
        and "Name" in definition
        and "Oem" in definition
    )


def is_array(defenition: dict[str, str]) -> bool:
    return defenition.get("type", "") in [
        "array",
    ]


def is_base_collection_properties(name: str) -> bool:
    return is_base_object_properties(name) or name in [
        "Description",
        "Members",
        "Members@odata.count",
        "Members@odata.nextLink",
        "Name",
        "Oem",
    ]


def is_base_id_properties(name: str) -> bool:
    return name in [
        "@odata.id",
    ]


def is_base_object_properties(name: str) -> bool:
    return name in [
        "@odata.context",
        "@odata.etag",
        "@odata.id",
        "@odata.type",
    ]


def is_base_resource_properties(name: str) -> bool:
    return is_base_object_properties(name) or name in [
        "Id",
        "Name",
    ]


def is_object(defenition: dict[str, str]) -> bool:
    return defenition.get("type", "") in [
        "object",
    ]


def is_primitive(defenition: dict[str, str]) -> bool:
    return defenition.get("type", "") in [
        "boolean",
        "integer",
        "number",
        "string",
    ]


def iter_definitions(
    schema_path: Path,
) -> Generator[tuple[str, dict[str, Any]], None, None]:
    schema = json.loads(schema_path.read_text())
    if "definitions" in schema:
        for name, defenition in schema["definitions"].items():
            yield (name, defenition)


def iter_schemas(base_path: Path) -> Generator[Path, None, None]:
    for f in base_path.glob("*.json"):
        yield f


def load_classes(redfish_path: Path, swordfish_path: Path) -> list[ClassInfo | EnumInfo]:
    classes: list[ClassInfo | EnumInfo] = []

    for domain, path in (("redfish", redfish_path), ("swordfish", swordfish_path)):
        for schema_path in iter_schemas(path):
            for cls_name, definition in iter_definitions(schema_path):
                info: ClassInfo | EnumInfo

                if (values := definition.get("enum", None)) is not None:
                    info = EnumInfo(domain, schema_path, definition, cls_name, values)
                else:
                    info = ClassInfo(
                        domain,
                        schema_path,
                        definition,
                        cls_name,
                        [],
                    )

                classes.append(info)

    return classes


def load_properties(
    targets: list[ClassInfo | EnumInfo], classall: list[ClassInfo | EnumInfo]
) -> None:
    for target in targets:
        if target.loaded:
            continue

        if not target.reachable:
            continue

        if isinstance(target, EnumInfo):
            target.loaded = True
            continue

        if "allOf" in target.definition:
            raise Exception("'allOf' does not supported.")

        if "oneOf" in target.definition:
            raise Exception("'oneOf' does not supported.")

        if target.is_primitive:
            continue

        if target.is_primitive_array:
            continue

        if (any_of := target.definition.get("anyOf", None)) is not None:
            selected = select_definition(any_of)
            if selected is None:
                warn(f"'{target}' is arbitrary object.")
                target.loaded = True
                continue

            if isinstance(selected, str):
                temp = resolve_ref(classall, target, selected)
                if isinstance(temp, EnumInfo):
                    temp.loaded = True
                else:
                    # Disable source definition.
                    target.reachable = False
                    target.loaded = False
                continue

            target.load_properties_from_definition(classall, selected)
        elif "properties" in target.definition:
            target.load_properties(classall)
        elif "type" in target.definition and is_object(target.definition):
            warn(f"'{target}' is arbitrary object.")
        else:
            raise Exception(f"Not found schema. '{target}'")

        target.loaded = True


def func_match_domain(
    domain: str, file_name: str, name: str
) -> Callable[
    [
        ClassInfo | EnumInfo,
    ],
    bool,
]:
    def func(c: ClassInfo | EnumInfo) -> bool:
        return domain == c.domain and file_name == c.schema_path.name and c.name == name

    return func


def func_match_newer(
    info: ClassInfo | EnumInfo,
) -> Callable[
    [
        ClassInfo | EnumInfo,
    ],
    TypeGuard[object],
]:
    def func(c: ClassInfo | EnumInfo) -> TypeGuard[object]:
        if not info.version:
            return False
        if not c.version:
            return False

        return info.name == c.name and info.version < c.version

    return func


def resolve_ref(
    classes: list[ClassInfo | EnumInfo], source: ClassInfo, ref: str
) -> ClassInfo | EnumInfo:
    url = urlparse(ref)

    if url.path:
        domain = "swordfish" if ref.find("swordfish") > -1 else "redfish"
        file_name = url.path.rsplit("/", 1)[-1]
    else:
        domain = source.domain
        file_name = source.schema_path.name

    definition = url.fragment.rsplit("/", 1)[-1]

    r = next(filter(func_match_domain(domain, file_name, definition), classes), None)
    if r is None:
        raise Exception(f"Could not found '{ref}'.")

    r.reachable = True
    return r


def resolve_property_type(
    classes: list[ClassInfo | EnumInfo], source: ClassInfo, definition: dict[str, Any]
) -> tuple[str | ClassInfo | EnumInfo, bool]:
    if "$ref" in definition:
        info = resolve_ref(classes, source, definition["$ref"])
        if info.id_ref:
            info = next(
                filter(
                    lambda c: c.schema_path.name == "odata-v4.json" and c.name == "idRef", classes
                )
            )
            info.reachable = True

        return (info, False)

    if "type" in definition:
        match definition["type"]:
            case "array":
                item_type = resolve_property_type(classes, source, definition["items"])
                return (item_type[0], True)
            case _:
                return (get_primitive_type_name(definition) or "str", False)

    # TODO:
    return ("str", False)


def select_definition(definitions: list[dict[str, Any]]) -> str | dict[str, Any] | None:
    for definition in definitions:
        if "properties" in definition:
            return definition

    for definition in definitions:
        if "$ref" not in definition:
            return None

    refs: list[str] = [d["$ref"] for d in definitions if not d["$ref"].endswith("/idRef")]
    sorted_refs = sorted(refs, reverse=True)
    if len(sorted_refs) == 0:
        return None

    return sorted_refs[0]


def write_classes(out_path: Path, classall: list[ClassInfo | EnumInfo]) -> None:
    count = 0
    for domain_name, modules_iter in itertools.groupby(classall, lambda c: c.domain):
        modules = sorted(list(modules_iter), key=lambda m: m.module)
        values: list[EnumInfo] = []
        for module_name, classes_iter in itertools.groupby(modules, lambda c: c.module):
            classes = list(classes_iter)
            if len(classes) == 0:
                continue

            if module_name.find(".") > -1:
                continue

            out_file = out_path
            if domain_name == "swordfish":
                out_file = out_path / "swordfish"

            module_path = out_file / f"{module_name}.py"

            classes = sorted(classes, key=lambda c: c.name)
            with module_path.open("w") as w:
                w.write("from __future__ import annotations  # PEP563 Forward References\n")
                w.write("\n")

                if any(filter(lambda i: isinstance(i, EnumInfo), classes)):
                    w.write("from enum import StrEnum\n")
                    w.write("\n")

                parent = "."
                if domain_name == "swordfish":
                    parent = ".."

                w.write(f"from {parent}base import RedfishModel\n")
                w.write(f"from {parent}base import RedfishObject\n")
                w.write(f"from {parent}base import RedfishObjectId\n")
                w.write(f"from {parent}base import RedfishResource\n")
                w.write(f"from {parent}base import RedfishResourceCollection\n")

                imports = set([])
                for c in classes:
                    if isinstance(c, EnumInfo):
                        continue

                    for p in c.properties:
                        if isinstance(p.type, (ClassInfo, EnumInfo)):
                            if isinstance(p.type, EnumInfo) or not p.type.is_primitive:
                                imports.add(p.type)

                for i in sorted(imports, key=lambda i: i.module):
                    if i.name in COMMON_VALUES:
                        w.write(f"from {parent}values import {i.cls_name}\n")
                    elif i.name in PLAIN_VALUES:
                        w.write("from typing import Any\n")
                    elif i.module != module_name:
                        w.write(f"from {parent}{i.module_path} import {i.cls_name}\n")

                for c in classes:
                    if not c.loaded:
                        continue

                    if isinstance(c, ClassInfo) and c.is_primitive:
                        continue

                    if c.versioned and any(filter(func_match_newer(c), classes)):
                        warn(f"Exist newer version '{c}'")
                        continue

                    if isinstance(c, EnumInfo) and c.name in COMMON_VALUES:
                        values.append(c)
                        continue

                    count += 1
                    print(f"{count}: {c} to {module_path}")

                    w.write("\n")
                    w.write("\n")
                    if isinstance(c, EnumInfo):
                        c.write_to(w)
                    else:
                        w.write(f"class {c.cls_name}({c.base_name}):\n")
                        for p in c.properties:
                            if "." in p.name or "@" in p.name:
                                # TODO:
                                continue

                            prop_name = get_snake_case(p.name)
                            if prop_name == "schema":
                                # TODO:
                                continue

                            ty = p.type if isinstance(p.type, str) else p.type.type_name
                            ty = f"list[{ty}]" if p.array else ty
                            if ty in PLAIN_VALUES:
                                # TODO:
                                ty = "dict[str, Any]"

                            w.write(f"    {prop_name}: {ty}")
                            if p.nonable:
                                w.write(" | None = None\n")
                            else:
                                w.write("\n")
                        if len(c.properties) == 0:
                            w.write("    pass\n")

        if len(values) > 0:
            out_file = out_path
            if domain_name == "swordfish":
                out_file = out_path / "swordfish"
            module_path = out_file / "values.py"

            with module_path.open("w") as w:
                w.write("from enum import StrEnum\n")
                w.write("\n")
                for v in values:
                    count += 1
                    print(f"{count}: {c} to {module_path}")

                    w.write("\n")
                    w.write("\n")
                    v.write_to(w)


def main() -> int:
    redfish_path = Path(sys.argv[1])
    if not redfish_path.is_dir():
        raise Exception(f"'{redfish_path}' is not directory.")

    swordfish_path = Path(sys.argv[2])
    if not swordfish_path.is_dir():
        raise Exception(f"'{swordfish_path}' is not directory.")

    out_path = Path(sys.argv[3])
    if not out_path.is_dir():
        raise Exception(f"'{out_path}' is not directory.")

    classall = load_classes(redfish_path, swordfish_path)

    for c in filter(lambda c: not c.versioned, classall):
        c.reachable = True

    old_reachable = 0
    new_reachable = len(list(filter(lambda c: c.reachable, classall)))

    while old_reachable != new_reachable:
        print(f"reachable: {new_reachable}")
        old_reachable = new_reachable
        load_properties(classall, classall)
        new_reachable = len(list(filter(lambda c: c.reachable, classall)))

    for c in classall:
        if c.loaded and c.versioned:
            c.set_module(c.module.split(".", 1)[0])

    loaded = len(list(filter(lambda c: c.loaded, classall)))
    print(f"loaded: {loaded}")

    write_classes(out_path, classall)

    return 0


if __name__ == "__main__":
    sys.exit(main())
