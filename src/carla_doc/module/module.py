from __future__ import annotations
from typing import Iterable, overload

from typing_extensions import Self

from . import errors as e
from . import types as t


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
