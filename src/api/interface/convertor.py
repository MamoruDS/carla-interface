from __future__ import annotations
from dataclasses import dataclass
import builtins
import importlib
import re

from pybind11_stubgen import structs

from carla_doc.utils.logging import get_logger

log = get_logger("carla_doc")


@dataclass
class TypeInStr:
    name: str
    params: list[TypeInStr] | None = None


class TypeConvertor:
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

    def from_value(self, value: TypeInStr) -> structs.ResolvedType:
        params = []
        for param in value.params or []:
            params.append(self.from_value(param))
        resolved = self.from_str(value.name)
        if len(params):
            resolved.parameters = params
        return resolved


class Convertor:
    def __init__(self): ...

    def arg_self(self) -> structs.Argument:
        return structs.Argument(structs.Identifier("self"))
