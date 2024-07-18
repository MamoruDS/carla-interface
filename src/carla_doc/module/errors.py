from dataclasses import dataclass

from . import types as t


@dataclass
class ModuleUnreachableException(Exception):
    from_mod: t.ModuleTree
    to: t.ModuleTree
