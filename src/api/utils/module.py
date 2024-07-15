from __future__ import annotations
from dataclasses import dataclass

from pybind11_stubgen.structs import Identifier, Import, QualifiedName
from typing_extensions import Self


class ModulePath(tuple[Identifier, ...]):
    def __str__(self):
        return ".".join(self)

    def __getitem__(self, key) -> Self | Identifier:
        if isinstance(key, slice):
            return self.__new__(self.__class__, tuple(self).__getitem__(key))
        else:
            return tuple(self)[key]

    def imports(self, *, names: list[Identifier] | None = None, all: bool = False):
        if all:
            name = Identifier("*")
        elif names is not None:
            name = Identifier(", ".join(names))
        else:
            raise NotImplementedError()
        return Import(name, QualifiedName([*self, name]))


@dataclass
class ModuleUnreachableException(Exception):
    from_mod: Module
    to: Module


class Module:
    name: Identifier
    parent: Module | None
    children: list[Module]

    def __init__(self, name: Identifier):
        self.name = name
        self.children = []
        self.parent = None

    def append_child(self, child: Module):
        if child.parent:
            child.parent.remove_child(child)
        self.children.append(child)
        child.parent = self

    def remove_child(self, child: Module):
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

    def root(self) -> Module:
        root = self
        while root.parent:
            root = root.parent
        return root

    def relative(self, other: Module) -> ModulePath:
        if self.root() is not other.root():
            raise ModuleUnreachableException(self, other)
        abs_self = self.abs()
        abs_other = other.abs()
        path = ["."]
        for i in range(min(len(abs_self), len(abs_other))):
            if abs_self[i] == abs_other[i]:
                continue
            else:
                path = [""] * (len(abs_self) - i) + list(abs_other[i:])
        return ModulePath([Identifier(p) for p in path])
