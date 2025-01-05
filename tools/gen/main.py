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

# pydantic.BaseModel properties.
BASE_MODEL_PROPERTIES: list[str] = ["schema"]

# define common values because of avoiding circular reference.
CIRCULAR_REFERENCE_VALUES: list[str] = ["AccountTypes"]

# enable versioned only schema.
VERSIONED_ONLY: list[str] = ["redfish-error.v1_0_2.json"]


@dataclass
class ClassInfo:
    domain: str
    schema_path: Path
    definition: dict[str, Any]
    name: str
    properties: list[PropetyInfo]
    reachable: bool = False
    loaded: bool = False
    raw: bool = False
    impl_info: ClassInfo | None = None
    _module: str | None = None

    @property
    def base_name(self) -> str:
        return "RedfishModel"

    @property
    def cls_name(self) -> str:
        return get_class_name(self.name)

    @property
    def id_ref(self) -> bool:
        if (any_of := self.definition.get("anyOf", None)) is not None:
            ids: list[str] = [d["$ref"] for d in any_of if "$ref" in d]
            return any((i for i in ids if i.endswith("/idRef")))
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
        if ty := get_primitive_type_name(self.definition):
            return ty

        return "dict[str, Any]" if self.raw else self.cls_name

    @property
    def version(self) -> tuple[int, int, int] | None:
        if not self.versioned:
            return None

        version = get_module_name(self.schema_path).rsplit(".", 1)[-1].split("_", 2)
        return (int(version[0].strip("v")), int(version[1]), int(version[2]))

    @property
    def versioned(self) -> bool:
        return get_module_name(self.schema_path).find(".") > -1

    def load_properties(self, classall: list[ClassInfo | EnumInfo]) -> None:
        self.load_properties_from_definition(classall, self.definition)

    def load_properties_from_definition(
        self, classall: list[ClassInfo | EnumInfo], definition: dict[str, Any]
    ) -> None:
        if (properties := definition.get("properties", None)) is not None:
            required = definition.get("required", [])
            for prop_name, prop_definition in properties.items():
                self._load_property(classall, prop_name, prop_definition, required)

    def set_module(self, module: str) -> None:
        self._module = module

    def write_to(self, w: Any) -> None:
        w.write(f"class {self.cls_name}({self.base_name}):\n")
        for p in self.properties:
            p.write_to(w, self)
        if len(self.properties) == 0:
            w.write("    pass\n")

    def _load_property(
        self,
        classall: list[ClassInfo | EnumInfo],
        name: str,
        definition: dict[str, Any],
        required: list[str],
    ) -> None:
        type, array, nonable = resolve_property_type(classall, self, definition)
        nonable = nonable or (name not in required)
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
            if any(re.finditer(r"(password|token)", v.lower())):
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

    @property
    def property_name(self) -> str:
        return get_property_name(self.name)

    @property
    def type_name(self) -> str:
        ty = self.type if isinstance(self.type, str) else self.type.type_name
        return f"list[{ty}]" if self.array else ty

    def write_to(self, w: Any, owner: ClassInfo) -> None:
        w.write(f"    {self.property_name}: {self.type_name}")
        if self.nonable:
            w.write(" | None")

        if self.name != get_class_name(self.property_name):
            w.write(" \\\n")
            if self.property_name == "odata_type":
                if version := owner.version:
                    (x, y, z) = version
                    ty = f"#{owner.name}.v{x}_{y}_{z}.{owner.name}"
                else:
                    ty = f"#{owner.name}.{owner.name}"
                w.write(f'        = Field(alias="{self.name}", default="{ty}")')
            elif self.nonable:
                w.write(f'        = Field(alias="{self.name}", default=None)')
            else:
                w.write(f'        = Field(alias="{self.name}")')
        elif self.nonable:
            w.write(" = None")

        w.write("\n")


def escape_name(name: str) -> str:
    if name.startswith("#"):
        # Actions property is omit schema name.
        name = name.split(".", 1)[-1]
    words = [w for w in re.split("[^A-Za-z0-9]", name) if w]
    return "_".join(words)


def get_class_name(name: str) -> str:
    name = escape_name(name)
    words = [w for w in get_snake_case(name).split("_") if w]
    return "".join([w.capitalize() for w in words])


def get_module_name(path: Path) -> str:
    name = path.name.rsplit(".", 1)[0]
    name = name.replace("-", "_")
    return get_snake_case(name)


def get_snake_case(name: str) -> str:
    name = (
        name.replace("CDUs", "Cdus")
        .replace("CRCs", "Crcs")
        .replace("DHCPv4", "Dhcpv4")
        .replace("DHCPv6", "Dhcpv6")
        .replace("ETag", "Etag")
        .replace("FCoE", "FcOe")
        .replace("GiB", "Gib")
        .replace("GUIDs", "Guids")
        .replace("I2C", "I2c")
        .replace("IDs", "Ids")
        .replace("IPv4", "Ipv4")
        .replace("IPv6", "Ipv6")
        .replace("KiB", "Kib")
        .replace("kVAh", "Kvah")
        .replace("kVARh", "Kvarh")
        .replace("LoS", "Los")
        .replace("MiB", "Mib")
        .replace("MHz", "Mhz")
        .replace("NVMe", "Nvme")
        .replace("NvmeoF", "Nvme_Of")
        .replace("OAuth", "Oauth")
        .replace("PCIe", "Pcie")
        .replace("PLDMv", "PldmV")
        .replace("QoS", "Qos")
        .replace("SNMPv", "Snmpv")
        .replace("TACACS", "Tacacs_")
        .replace("VLAN", "Vlan")
        .replace("VLan", "Vlan")
    )
    words = []
    for w in [w for w in re.split(r"([A-Z][A-Z0-9]*[^A-Z]+)", name) if w]:
        if re.match(r"^[A-Z0-9]+$", w):
            words.append(w.lower())
        elif m := re.match(r"([A-Z][A-Z0-9]*)([A-Z][^A-Z]+)", w):
            words.append(m.group(1).lower())
            words.append(m.group(2).lower())
        else:
            words.append(w.lower())
    return "_".join(words)


def get_property_name(name: str) -> str:
    name = escape_name(name)
    name = get_snake_case(name)
    name = name.replace("__", "_")
    if name in BASE_MODEL_PROPERTIES:
        name = f"{name}_value"
    return name


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
    name = escape_name(name)
    name = get_snake_case(name).upper()
    name = name.replace("__", "_")
    if re.match(r"^\d", name):
        name = f"N{name}"
    return name


def is_array(defenition: dict[str, str]) -> bool:
    return defenition.get("type", "") in [
        "array",
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
                target.raw = True
                target.loaded = True
                continue

            if isinstance(selected, str):
                temp = resolve_ref(classall, target, selected)
                if isinstance(temp, EnumInfo):
                    temp.loaded = True
                else:
                    target.impl_info = temp
                    # Disable source definition.
                    target.reachable = False
                    target.loaded = False
                continue

            target.load_properties_from_definition(classall, selected)
        elif target.definition.get("properties", []):
            target.load_properties(classall)
        elif "type" in target.definition and is_object(target.definition):
            target.raw = True
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

    r = next((c for c in classes if func_match_domain(domain, file_name, definition)(c)), None)
    if r is None:
        raise Exception(f"Could not found '{ref}'.")

    r.reachable = True
    return r


def resolve_property_type(
    classes: list[ClassInfo | EnumInfo], source: ClassInfo, definition: dict[str, Any]
) -> tuple[str | ClassInfo | EnumInfo, bool, bool]:
    def has_null(d: dict[str, Any]) -> bool:
        if t := d.get("type", ""):
            return isinstance(t, str) and t == "null"
        return False

    def get_from_ref(ref: str, noneable: bool) -> tuple[ClassInfo | EnumInfo, bool, bool]:
        info = resolve_ref(classes, source, ref)
        if info.id_ref:
            info = next(
                (c for c in classes if c.schema_path.name == "odata-v4.json" and c.name == "idRef")
            )
            info.reachable = True

        return (info, False, noneable)

    if (any_of := definition.get("anyOf", None)) is not None:
        nonable = any((a for a in any_of if has_null(a)))
        if nonable and len(any_of) == 2:
            ref = next((a["$ref"] for a in any_of if "$ref" in a))
            return get_from_ref(ref, nonable)

    if (ref := definition.get("$ref", None)) is not None:
        return get_from_ref(ref, False)

    if (type := definition.get("type", None)) is not None:
        match type:
            case list():
                types: list[str] = type
                try:
                    index = types.index("null")
                    types.pop(index)
                    nonable = True
                except IndexError:
                    nonable = False

                if len(types) == 1:
                    if name := get_primitive_type_name({"type": types[0]}):
                        return (name, False, nonable)

                warn(f"{source} {definition} is primitive")
                return ("str", False, False)

            case "array":
                item_type = resolve_property_type(classes, source, definition["items"])
                return (item_type[0], True, False)
            case _:
                if name := get_primitive_type_name(definition):
                    return (name, False, False)

    raise Exception(f"{source} has unsuported type property.")


def select_definition(definitions: list[dict[str, Any]]) -> str | dict[str, Any] | None:
    for definition in definitions:
        if "properties" in definition:
            return definition

    for definition in definitions:
        if "$ref" not in definition:
            return None

    refs: list[str] = [d["$ref"] for d in definitions if not d["$ref"].endswith("/idRef")]

    versions: list[tuple[tuple[int, int, int], str]] = []
    for ref in refs:
        if m := re.match(r".+\.v(\d+)_(\d+)_(\d+)\..+", ref):
            v = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
            versions.append((v, ref))

    sorted_refs = sorted(versions, key=lambda v: v[0], reverse=True)
    if len(sorted_refs) == 0:
        return None

    return sorted_refs[0][1]


def write_base_classes(out_path: Path) -> None:
    out_path = out_path / "model"

    if not out_path.exists():
        out_path.mkdir()

    out_file = out_path / "__init__.py"
    with out_file.open("w") as w:
        w.writelines(
            [
                "from pydantic import BaseModel, ConfigDict\n",
                "from pydantic.alias_generators import to_pascal\n",
                "\n",
                "\n",
                "class RedfishModel(BaseModel):\n",
                "    model_config = ConfigDict(alias_generator=to_pascal, populate_by_name=True)\n",  # noqa: E501
            ]
        )

    out_dir = out_path / "swordfish"
    if not out_dir.exists():
        out_dir.mkdir()

    out_file = out_dir / "__init__.py"
    with out_file.open("w") as w:
        pass


def write_classes(out_path: Path, classall: list[ClassInfo | EnumInfo]) -> None:
    out_path = out_path / "model"

    count = 0
    for domain_name, modules_iter in itertools.groupby(classall, lambda c: c.domain):
        out_file = out_path
        if domain_name == "swordfish":
            out_file = out_path / "swordfish"

        values: list[EnumInfo] = []
        modules = sorted(list(modules_iter), key=lambda m: m.module)
        for module_name, classes_iter in itertools.groupby(modules, lambda c: c.module):
            if module_name.find(".") > -1:
                continue

            classes = sorted(list(classes_iter), key=lambda c: c.name)
            if len(classes) == 0:
                continue

            module_path = out_file / f"{module_name}.py"
            with module_path.open("w") as w:
                write_imports_to(domain_name, classes, module_name, w)

                for c in classes:
                    if not c.loaded:
                        continue

                    if isinstance(c, ClassInfo) and c.is_primitive:
                        continue

                    if isinstance(c, ClassInfo) and c.raw:
                        continue

                    if c.versioned and any((i for i in classes if func_match_newer(c)(i))):
                        warn(f"Exist newer version '{c}'")
                        continue

                    if isinstance(c, EnumInfo) and c.name in CIRCULAR_REFERENCE_VALUES:
                        values.append(c)
                        continue

                    count += 1
                    print(f"{count}: {c} to {module_path}")

                    w.write("\n")
                    w.write("\n")
                    c.write_to(w)

        if len(values) > 0:
            module_path = out_file / "values.py"
            with module_path.open("w") as w:
                write_imports_to(domain_name, classes, "values", w)

                for v in values:
                    count += 1
                    print(f"{count}: {v} to {module_path}")

                    w.write("\n")
                    w.write("\n")
                    v.write_to(w)


def write_imports_to(
    domaon: str, classall: list[ClassInfo | EnumInfo], module: str, w: Any
) -> None:
    w.write("from __future__ import annotations  # PEP563 Forward References\n")
    w.write("\n")

    w.write("from enum import StrEnum\n")
    w.write("from typing import Any\n")
    w.write("\n")

    w.write("from pydantic import Field\n")
    w.write("\n")

    parent = "."
    if domaon == "swordfish":
        parent = ".."

    w.write(f"from {parent} import RedfishModel\n")

    imports: set[ClassInfo | EnumInfo] = set([])
    for c in classall:
        if isinstance(c, EnumInfo):
            continue

        for p in c.properties:
            if isinstance(p.type, EnumInfo):
                imports.add(p.type)

            if isinstance(p.type, ClassInfo):
                if not p.type.is_primitive and not p.type.raw:
                    imports.add(p.type)

    for i in sorted(imports, key=lambda i: i.module):
        if i.name in CIRCULAR_REFERENCE_VALUES:
            w.write(f"from {parent}values import {i.cls_name}\n")
        elif i.module != module:
            w.write(f"from {parent}{i.module_path} import {i.cls_name}\n")


def write_imports_router_to(
    domaon: str, classall: list[ClassInfo | EnumInfo], module: str, w: Any
) -> None:
    w.write("from typing import Any, cast\n")
    w.write("\n")

    w.write("from fastapi import APIRouter, Request, Response\n")
    w.write("\n")

    parent = ".."
    if domaon == "swordfish":
        parent = "..."

    for c in classall:
        if isinstance(c, ClassInfo) and c.impl_info:
            w.write(
                f"from {parent}model.{c.impl_info.module_path} import {c.impl_info.cls_name}\n"
            )
        else:
            w.write(f"from {parent}model.{c.module_path} import {c.cls_name}\n")

    w.write(f"from {parent}service import Service, find_service\n")
    w.write(f"from {parent}authenticate import authenticate\n")
    w.write("\n")

    w.write("router = APIRouter()\n")


def write_routers(
    out_path: Path, classall: list[ClassInfo | EnumInfo]
) -> list[ClassInfo | EnumInfo]:
    out_path = out_path / "router"

    if not out_path.exists():
        out_path.mkdir()

    urls: list[str] = []
    routing: list[ClassInfo | EnumInfo] = []
    for domain_name, modules_iter in itertools.groupby(classall, lambda c: c.domain):
        out_dir = out_path
        if domain_name == "swordfish":
            out_dir = out_path / "swordfish"

        if not out_dir.exists():
            out_dir.mkdir()

        modules = sorted(list(modules_iter), key=lambda m: m.module)
        for module_name, classes_iter in itertools.groupby(modules, lambda c: c.module):
            if module_name.find(".") > -1:
                continue

            classes = sorted(
                [c for c in classes_iter if "uris" in c.definition], key=lambda c: c.name
            )
            if len(classes) == 0:
                continue

            module_path = out_dir / f"{module_name}.py"
            with module_path.open("w") as w:
                write_imports_router_to(domain_name, classes, module_name, w)

                for c in classes:
                    index = 0
                    for url in c.definition["uris"]:
                        if url == "/redfish/v1":
                            # redirect to /redfish/v1/
                            continue

                        if url in urls:
                            warn(f"{c} {url} is duplicated.")
                            continue

                        params: list[str] = []
                        for p in re.findall(r"{[^}]+}", url):
                            name = get_snake_case(p.strip("{}"))
                            params.append(name)
                            url = url.replace(p, f"{{{name}}}")

                        args_list = [f"{p}: str" for p in params]
                        body_list = [f'"{p}": {p}' for p in params]

                        args = ",".join([*args_list, "request: Request", "response: Response"])
                        body = ",".join([*body_list, '"request": request', '"response": response'])

                        index += 1
                        w.writelines(
                            [
                                "\n",
                                "\n",
                                f'@router.get("{url}", response_model_exclude_none=True)\n',
                                "@authenticate\n",
                                f"async def get{index}({args}) -> {c.cls_name}:\n",
                                f"    s: Service = find_service({c.cls_name})\n",
                                f"    b: dict[str, Any] = {{{body}}}\n",
                                "\n",
                                '    response.headers["OData-Version"] = "4.0"\n',
                                "\n",
                                f"    return cast({c.cls_name}, s.get(**b))\n",
                            ]
                        )

                        urls.append(url)
                        print(f"{len(urls)}: {url} to {module_path}")

                    routing.append(c)

    return routing


def write_routers_init(out_path: Path, classall: list[ClassInfo | EnumInfo]) -> None:
    out_path = out_path / "router"

    redfish_file = out_path / "__init__.py"
    swordfish_file = out_path / "swordfish" / "__init__.py"
    with redfish_file.open("w") as redfish, swordfish_file.open("w") as swordfish:
        redfish.write("from fastapi import FastAPI\n")
        redfish.write("\n")

        swordfish.write("from fastapi import FastAPI\n")
        swordfish.write("\n")

        for c in classall:
            if c.domain == "swordfish":
                swordfish.write(f"from . import {c.module}\n")
            else:
                redfish.write(f"from . import {c.module}\n")

        redfish.write("\n")
        redfish.write("\n")
        redfish.write("def include_router(app: FastAPI) -> None:\n")

        swordfish.write("\n")
        swordfish.write("\n")
        swordfish.write("def include_router(app: FastAPI) -> None:\n")

        for c in classall:
            if c.domain == "swordfish":
                swordfish.write(f"    app.include_router({c.module}.router)\n")
            else:
                redfish.write(f"    app.include_router({c.module}.router)\n")


def main() -> int:
    redfish_path = Path(sys.argv[1])
    if not redfish_path.is_dir():
        raise Exception(f"'{redfish_path}' is not directory.")

    swordfish_path = Path(sys.argv[2])
    if not swordfish_path.is_dir():
        raise Exception(f"'{swordfish_path}' is not directory.")

    out_path = Path(sys.argv[3])
    if out_path.is_file():
        raise Exception(f"'{out_path}' is not directory.")

    classall = load_classes(redfish_path, swordfish_path)

    for c in (c for c in classall if not c.versioned):
        if isinstance(c, ClassInfo):
            c.reachable = True

    for c in (c for c in classall if c.schema_path.name in VERSIONED_ONLY):
        if isinstance(c, ClassInfo):
            c.reachable = True

    old_reachable = 0
    new_reachable = len([c for c in classall if c.reachable])

    while old_reachable != new_reachable:
        print(f"reachable: {new_reachable}")
        old_reachable = new_reachable
        load_properties(classall, classall)
        new_reachable = len([c for c in classall if c.reachable])

    for c in classall:
        if c.loaded and c.versioned:
            c.set_module(c.module.split(".", 1)[0])

    loaded = len([c for c in classall if c.loaded])
    print(f"loaded: {loaded}")

    write_base_classes(out_path)
    write_classes(out_path, classall)

    routing = write_routers(out_path, classall)
    write_routers_init(out_path, routing)

    return 0


if __name__ == "__main__":
    sys.exit(main())
