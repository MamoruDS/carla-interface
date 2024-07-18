from __future__ import annotations
from enum import IntFlag, auto


class GetNamesRules(IntFlag):
    NONE = 0
    ATTRIBUTES = auto()
    CLASSES = auto()
    FUNCTIONS = auto()
    TYPE_VARS = auto()
    RE_EXPORT_ALT_IMPORTS = auto()
    MODULE = auto()
