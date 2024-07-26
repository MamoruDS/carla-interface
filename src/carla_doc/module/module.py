from __future__ import annotations
from copy import deepcopy
from typing import Iterable, overload

from typing_extensions import Self

from ..utils.logging import get_logger
from .register import DEFAULT_REGISTER
from . import errors as e
from . import types as t

log = get_logger(__name__)


class ModulePath(tuple[t.Identifier, ...], t.ModulePath):
    _root: bool
    """unset warning; use `hasattr`!"""

    def __str__(self):
        return ".".join(self)

    @overload
    def __getitem__(self, key: slice) -> Self: ...
    @overload
    def __getitem__(self, key: int) -> t.Identifier: ...
    def __getitem__(self, key) -> Self | t.Identifier:
        if isinstance(key, slice):
            return self.__new__(self.__class__, tuple(self).__getitem__(key))
        else:
            return tuple(self)[key]

    @classmethod
    def root(cls, iterable: Iterable[t.Identifier]) -> Self:
        path = cls.__new__(cls, iterable)
        path._root = True
        if path[0] == "" and path._root:
            raise TypeError("relative path is not allowed")
        return path

    def imports(
        self, *, names: Iterable[t.Identifier] | None = None, all: bool = False
    ):
        if all:
            name = t.Identifier("*")
        elif names is not None:
            name = t.Identifier(",".join(names))
        else:
            raise NotImplementedError()
        if self.is_relative() and self[0] != "":
            self_path = ["", *self]
        else:
            self_path = [*self]
        return t.Import(name, t.QualifiedName([*self_path, name]))

    def is_absolute(self) -> bool:
        return hasattr(self, "_root") and self._root

    def is_relative(self) -> bool:
        return not self.is_absolute()


class ModuleTree(t.ModuleTree):
    _name: t.Identifier
    _is_file: bool
    _parent: ModuleTree | None
    _children: list[ModuleTree]

    def __init__(self, name: t.Identifier, *, is_file: bool = False):
        self._name = name
        self._is_file = is_file
        self._children = []
        self._parent = None

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "Module <{}>".format(self.abs())

    @property
    def is_file(self):
        return self._is_file

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    def append_child(self, child: ModuleTree):
        if child._parent:
            child._parent.remove_child(child)
        self._children.append(child)
        child._parent = self

    def get_child(self, name: t.Identifier) -> ModuleTree:
        for child in self._children:
            if child._name == name:
                return child
        raise KeyError("child {} not exist in {}".format(name, self.abs()))

    def remove_child(self, child: ModuleTree):
        assert child._parent is self
        self._children.remove(child)
        child._parent = None

    def abs(self) -> ModulePath:
        path = [self._name]
        mod = self
        while mod._parent:
            mod = mod._parent
            path.insert(0, mod._name)
        return ModulePath.root(path)

    def root(self) -> ModuleTree:
        root = self
        while root._parent:
            root = root._parent
        return root

    def relative(self, other: ModuleTree) -> ModulePath:
        if self.root() is not other.root():
            raise e.ModuleUnreachableException(self, other)
        abs_self = self.abs()
        abs_other = other.abs()
        idx = 0
        for i in range(min(len(abs_self), len(abs_other))):
            if abs_self[i] == abs_other[i]:
                idx = i + 1
                continue
            else:
                idx = i
                break
        path = [""] * (len(abs_self) - idx) + list(abs_other[idx:])
        return ModulePath([t.Identifier(p) for p in path])

    def resolve(self, path: ModulePath) -> ModuleTree:
        if path.is_absolute():
            mod = self.root()
            for pi, name in enumerate(path):
                if pi == 0:
                    if mod._name != name:
                        raise ImportError(name=name)
                else:
                    mod = mod.get_child(name)
            return mod
        else:
            if len(path) == 0:
                return self
            else:
                if len(path) > 1 and path[:2] == ("", ""):
                    mod = self._parent
                elif path[0] == "":
                    if self._is_file:
                        mod = self._parent
                    else:
                        mod = self
                else:
                    mod = self.get_child(path[0])
                if mod is None:
                    raise NotImplementedError(
                        "might caused by using the root module for the parent"
                    )
                return mod.resolve(path[1:])


class ModuleWrapper(t.ModuleWrapper):
    DEFAULT_EXPORTS_RULES = (
        t.GetNamesRules.ATTRIBUTES
        | t.GetNamesRules.CLASSES
        | t.GetNamesRules.FUNCTIONS
        | t.GetNamesRules.TYPE_VARS
        | t.GetNamesRules.RE_EXPORT_ALT_IMPORTS
    )
    _module: t.Module
    _resolver: t.TypeResolver
    _imports: list[t.ImportAlt]
    _exports_rules: t.GetNamesRules
    _printable_flags: t.MWPrintFlags
    _tree: t.ModuleTree
    _register: t.ModuleRegister

    def __init__(
        self,
        module: t.Module,
        resolver: t.TypeResolver,
        register: t.ModuleRegister = DEFAULT_REGISTER,
        imports: list[t.ImportAlt] | None = None,
        exports_rules_negative: t.GetNamesRules = t.GetNamesRules.NONE,
        print_flags: t.MWPrintFlags = t.MWPrintFlags.NONE,
    ) -> None:
        self._module = module
        self._resolver = resolver
        self._register = register
        self._imports = imports or []
        self._exports_rules = self.DEFAULT_EXPORTS_RULES ^ exports_rules_negative
        self._printable_flags = print_flags
        self._tree = ModuleTree(module.name)
        self._register.add(self)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "ModuleWrapper <{}>".format(self._tree.abs())

    @property
    def module(self):
        return self._module

    @property
    def resolver(self):
        return self._resolver

    @property
    def tree(self):
        return self._tree

    @property
    def children(self):
        return self._register.get_children(self)

    def append_child(self, child: ModuleWrapper):
        return self._register.append_child(self, child)

    def exports(
        self, rules_overwrite: t.GetNamesRules | None = None
    ) -> t.NamespaceItems:
        rules = rules_overwrite or self._exports_rules
        items: t.NamespaceItems = {}
        if t.GetNamesRules.ATTRIBUTES & rules:
            for attr in self._module.attributes:
                items[attr.name] = (self, t.GetNamesRules.ATTRIBUTES)
        if t.GetNamesRules.CLASSES & rules:
            for cl in self._module.classes:
                items[cl.name] = (self, t.GetNamesRules.CLASSES)
        if t.GetNamesRules.FUNCTIONS & rules:
            for fn in self._module.functions:
                items[fn.name] = (self, t.GetNamesRules.FUNCTIONS)
        if t.GetNamesRules.TYPE_VARS & rules:
            for tvar in self._module.type_vars:
                items[tvar.name] = (self, t.GetNamesRules.TYPE_VARS)
        if t.GetNamesRules.RE_EXPORT_ALT_IMPORTS & rules:
            for imports in self._imports:
                items.update(imports.get_imported_namespace())
        if t.GetNamesRules.MODULE & rules:
            for imports in self._imports:
                items[imports.module.module.name] = (
                    imports.module,
                    t.GetNamesRules.MODULE,
                )

        return items

    def fix_unresolved(
        self, name: t.QualifiedName
    ) -> tuple[t.Import | None, t.Identifier] | None:
        if len(name) < 2:
            if len(name) == 1:
                # TODO: search from local exports
                # world.TextureFloatColor
                ...
            log.error(
                f"fix_unresolved failed in module <{self.module.name}>\n"
                + f" > reason: input name with invalid length <{len(name)}> (required >= 2)\n"
                + f' > name: "{name}"\n'
                + "   aborting..."
            )
            exit(1)

        path = ModulePath.root(name[:-1])
        target = name[-1]

        mod: t.ModuleWrapper | None = None

        # plan.a path is valid and following tree
        try:
            mod = self._register.get_by_tree(self._tree.resolve(path))
            """
            FIXME: buggy for re-export
            e.g., carla.command.Foo (origin: carla.libcarla.command.Foo)
            need Rules.MODULE be enabled
            """
        except Exception as err:
            log.warning(
                f"fix_unresolved failed in module <{self.module.name}>:\n"
                + f" > err: {type(err)} - {err}\n"
                + " > import\n"
                + f"\t{target}\n"
                + " > from\n"
                + f"\t{path}\n"
                + f'   with origin name: "{name}", trying plan-b'
            )

        # plan.b path is valid but need discover from exports
        if mod is None:
            # FIXME: length
            target_mod = path[-1]
            parent = self._register.get_by_tree(
                self._tree.resolve(ModulePath.root(path[:-1]))
            )
            ep = parent.exports(
                t.GetNamesRules.RE_EXPORT_ALT_IMPORTS | t.GetNamesRules.MODULE
            ).get(target_mod)
            if ep is not None:
                mod, ep_type = ep
                assert ep_type is t.GetNamesRules.MODULE

        if mod is None:
            raise KeyError("")

        # FIXME: try resolve import

        origin, _ = mod.exports().get(target, (None, None))
        if origin is None:
            raise NotImplementedError(
                "type <{}> cannot be found in {}".format(target, mod)
            )
        elif origin is self:
            return None, target
        else:
            try:
                import_ = self._tree.relative(origin.tree).imports(names=[target])
            except IndexError as err:
                log.error(
                    "fix_unresolved failed on import with relative\n"
                    + f" > imports: {target}\n"
                    + f" >    from: {origin}\n"
                    + f" >      to: {self}"
                )
                raise err
            return import_, target

    def get_print_ready_module(self) -> t.Module:
        # TODO: sub_module
        mod = deepcopy(self._module)  # FIXME: not necessary
        for import_ in self._imports:
            mod.imports.add(import_.to_pybind11_import(self))
        if self._printable_flags & t.MWPrintFlags.INCLUDE_ADD:
            mod.attributes.append(
                t.Attribute(
                    t.Identifier("__all__"),
                    t.Value(
                        "[{}]".format(",".join([f'"{i}"' for i in self.exports()])),
                        is_print_safe=True,
                    ),
                )
            )
        return mod
