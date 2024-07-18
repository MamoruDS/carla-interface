from dataclasses import dataclass

from . import types as t


@dataclass
class ModuleNotFoundInRegister(Exception):
    module: t.ModulePath | t.ModuleTree
    register: t.ModuleRegister


@dataclass
class ModuleUnreachableException(Exception):
    from_mod: t.ModuleTree
    to: t.ModuleTree
