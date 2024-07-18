from __future__ import annotations
from dataclasses import dataclass
from enum import IntFlag, auto
from typing import Iterable, overload

from pybind11_stubgen.structs import Identifier, Import, QualifiedName
from typing_extensions import Self


class GetNamesRules(IntFlag):
    NONE = 0
    ATTRIBUTES = auto()
    CLASSES = auto()
    FUNCTIONS = auto()
    TYPE_VARS = auto()
    RE_EXPORT_ALT_IMPORTS = auto()
    MODULE = auto()


class ModulePath(tuple[Identifier, ...]):
    _root: bool
    """unset warning; use `hasattr`!"""

    def __str__(self):
        return ".".join(self)

    @overload
    def __getitem__(self, key: slice) -> Self: ...
    @overload
    def __getitem__(self, key: int) -> Identifier: ...
    def __getitem__(self, key) -> Self | Identifier:
        if isinstance(key, slice):
            return self.__new__(self.__class__, tuple(self).__getitem__(key))
        else:
            return tuple(self)[key]

    @classmethod
    def root(cls, iterable: Iterable[Identifier]) -> Self:
        path = cls.__new__(cls, iterable)
        path._root = True
        if path[0] == "" and path._root:
            raise TypeError("relative path is not allowed")
        return path

    def imports(self, *, names: Iterable[Identifier] | None = None, all: bool = False):
        if all:
            name = Identifier("*")
        elif names is not None:
            name = Identifier(",".join(names))
        else:
            raise NotImplementedError()
        if self.is_relative() and self[0] != "":
            self_path = ["", *self]
        else:
            self_path = [*self]
        return Import(name, QualifiedName([*self_path, name]))

    def is_absolute(self) -> bool:
        return hasattr(self, "_root") and self._root

    def is_relative(self) -> bool:
        return not self.is_absolute()


@dataclass
class ModuleUnreachableException(Exception):
    from_mod: ModuleTree
    to: ModuleTree


class ModuleTree:
    name: Identifier
    is_file: bool
    parent: ModuleTree | None
    children: list[ModuleTree]

    def __init__(self, name: Identifier, *, is_file: bool = False):
        self.name = name
        self.is_file = is_file
        self.children = []
        self.parent = None

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "Module <{}>".format(self.abs())

    def append_child(self, child: ModuleTree):
        if child.parent:
            child.parent.remove_child(child)
        self.children.append(child)
        child.parent = self

    def get_child(self, name: Identifier) -> ModuleTree:
        for child in self.children:
            if child.name == name:
                return child
        raise KeyError()

    def remove_child(self, child: ModuleTree):
        assert child.parent is self
        self.children.remove(child)
        child.parent = None

    def abs(self) -> ModulePath:
        path = [self.name]
        mod = self
        while mod.parent:
            mod = mod.parent
            path.insert(0, mod.name)

        return ModulePath(path)

    def root(self) -> ModuleTree:
        root = self
        while root.parent:
            root = root.parent
        return root

    def relative(self, other: ModuleTree) -> ModulePath:
        if self.root() is not other.root():
            raise ModuleUnreachableException(self, other)
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
        return ModulePath([Identifier(p) for p in path])
