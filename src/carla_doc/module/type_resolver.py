from __future__ import annotations
import builtins
import importlib
import re

from pybind11_stubgen import structs

from ..utils.logging import get_logger
from . import types as t

log = get_logger("carla_doc")


class TypeResolver(t.TypeResolver):
    RE_FIX_BRACKETS_LHS = re.compile(r"[<(]")
    RE_FIX_BRACKETS_RHS = re.compile(r"[>)]")
    RE_TYPEVAR_WITH_PARAMS = re.compile(r"^([\w\.]+)(\[[\s\w,\.\(\)\[\]<>]+\])")
    RE_PARAM_SPLITOR = re.compile(r",\s*(?![^\[]*\])")

    imports: set[structs.Import]
    pending: list[tuple[str, structs.QualifiedName]]
    no_cache: bool
    caches: dict[str, structs.ResolvedType]
    banned_modules: set[structs.Identifier]
    """useful for blocking certain modules, e.g., the parsing one."""
    skipped_modules: set[structs.Identifier]
    """assume modules are importable without checking, useful for external dependencies"""

    def __init__(
        self,
        no_cache: bool = False,
        *,
        banned_modules: set[structs.Identifier] | None = None,
        skipped_modules: set[structs.Identifier] | None = None,
    ) -> None:
        self.imports = set()
        self.pending = []
        self.no_cache = no_cache
        self.caches = {}
        self.banned_modules = banned_modules or set()
        self.skipped_modules = skipped_modules or set()

    @classmethod
    def fix_brackets(cls, text: str) -> str:
        text = cls.RE_FIX_BRACKETS_LHS.sub("[", text)
        text = cls.RE_FIX_BRACKETS_RHS.sub("]", text)
        return text

    @staticmethod
    def fix_bs_types(type_name: str | None) -> str | None:
        if type_name == "array":
            return "list"
        elif type_name == "boolean":
            return "bool"
        elif type_name == "callback":
            return "typing.Callable"
        elif type_name == "function":
            return "typing.Callable"
        elif type_name == "string":
            return "str"
        elif type_name == "vector":
            """
            TODO:
            carla::RssSensor.routing_targets: vector<carla.Transform>
            """
            return "list"
        elif isinstance(type_name, str) and type_name.startswith("uint"):
            return "int"
        else:
            return type_name

    @staticmethod
    def fix_carla_imports(type_name: str | None) -> str | None:
        if type_name == "command.Response":
            return "carla.libcarla.command.Response"
        elif type_name == "TextureFloatColor":
            """carla::World::apply_flaot_color_texture_to_object etc."""
            return "carla.TextureFloatColor"
        elif type_name == "TextureColor":
            """same as above"""
            return "carla.TextureColor"
        # elif type_name == "carla.OSM2ODRSettings":
        #     """fixed by doc patch"""
        #     return "carla.Osm2OdrSettings"
        else:
            return type_name

    @staticmethod
    def fix_type_in_anchor(text: str) -> tuple[str, str | None]:
        """return [fixed, href]"""
        from xml.etree import ElementTree

        if text.startswith("<"):
            try:
                root = ElementTree.fromstring(f"<root>{text}</root>")
                a_tag = root.find(".//a")
                if a_tag is not None and a_tag.text is not None:
                    return a_tag.text, a_tag.attrib.get("href", None)
            except Exception:
                log.warning("skip anchor element convert")
        return text, None

    def is_importable(self, module: structs.Identifier) -> bool:
        if module in self.banned_modules:
            return False
        elif module in self.skipped_modules:
            return True
        try:
            importlib.import_module(module)
            return True
        except ImportError:
            return False

    def fix(self, type_name: str, fixed: structs.QualifiedName):
        self.caches[type_name].name = fixed

    def from_str(self, type_name: str) -> structs.ResolvedType:
        name = structs.QualifiedName.from_str(type_name)
        if type_name in dir(builtins):
            return structs.ResolvedType(name)
        if type_name not in self.caches:
            if len(type_name) > 1 and self.is_importable(name[0]):
                self.imports.add(structs.Import(name[-1], name))
                self.caches[type_name] = structs.ResolvedType(
                    structs.QualifiedName(name[-1:])
                )
            else:
                self.pending.append((type_name, name))
                self.caches[type_name] = structs.ResolvedType(name)
        return self.caches[type_name]  # shallow is okay

    def from_value(self, value: t.TypeInStr) -> structs.ResolvedType:
        params = []
        for param in value.params or []:
            params.append(self.from_value(param))
        resolved = self.from_str(value.name)
        if len(params):
            resolved.parameters = params
        return resolved
