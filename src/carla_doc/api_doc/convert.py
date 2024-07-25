from enum import IntFlag, auto

from pybind11_stubgen import structs

from ..module.type_resolver import TypeResolver
from . import types as dt


class PropertyFns(IntFlag):
    NONE = 0
    FDEL = auto()
    FGET = auto()
    FSET = auto()


class Convertor:
    def __init__(self): ...

    @staticmethod
    def arg_self() -> structs.Argument:
        return structs.Argument(structs.Identifier("self"))

    @staticmethod
    def cvt_docstr(doc: str | None) -> structs.Docstring | None:
        if doc is not None:
            return structs.Docstring(doc)
        else:
            return None

    @classmethod
    def cvt_property(
        cls,
        target: dt.DocClsInstanceVar,
        tc: TypeResolver,
        *,
        flag: PropertyFns = PropertyFns.FGET,
    ) -> structs.Property:
        prop_type, getter, setter = None, None, None
        doc = cls.cvt_docstr(target.doc)
        if target.type is not None:
            prop_type = tc.cvt_type(target.type, tc)
        # TODO:
        # if PropertyFns.FDEL & flag:
        if PropertyFns.FGET & flag:
            getter = structs.Function(
                structs.Identifier(target.var_name),
                args=[cls.arg_self()],
                returns=prop_type,
                doc=doc,
            )
        if PropertyFns.FSET & flag:
            setter = structs.Function(
                structs.Identifier(target.var_name),
                args=[
                    cls.arg_self(),
                    structs.Argument(
                        structs.Identifier("val"),
                        annotation=prop_type,
                    ),
                ],
                returns=None,
                doc=doc,
            )
        return structs.Property(
            structs.Identifier(target.var_name),
            modifier=None,
            doc=doc,
            getter=getter,
            setter=setter,
        )
