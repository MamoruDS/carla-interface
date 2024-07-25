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
    def is_enum(doc_cls: dt.DocClass) -> bool:
        if doc_cls.parent is not None:
            return False
        if doc_cls.methods is not None and len(doc_cls.methods) > 0:
            return False
        if doc_cls.instance_variables is None or len(doc_cls.instance_variables) == 0:
            return False
        else:
            for var in doc_cls.instance_variables:
                if not var.var_name[0].isupper():
                    return False
                if var.type is not None:
                    return False
        return True

    @staticmethod
    def cvt_docstr(doc: str | None) -> structs.Docstring | None:
        if doc is not None:
            return structs.Docstring(doc)
        else:
            return None

    @classmethod
    def cvt_enum(cls, target: dt.DocClass, tc: TypeResolver) -> structs.Class:
        fields: list[structs.Field] = []
        for var in target.instance_variables or []:
            if var.var_name == "None":
                var.var_name = "NONE"
            f = cls.cvt_field(var, tc)
            f.attribute.value = structs.Value("auto()", is_print_safe=True)
            fields.append(f)
        # FIXME:
        tc.cvt_type("enum.IntEnum", tc)
        tc.cvt_type("enum.auto", tc)
        return structs.Class(
            structs.Identifier(target.class_name),
            doc=cls.cvt_docstr(target.doc),
            bases=[structs.QualifiedName.from_str("IntEnum")],
            fields=fields,
        )

    @classmethod
    def cvt_field(cls, target: dt.DocClsInstanceVar, tc: TypeResolver) -> structs.Field:
        f_type = None
        if target.type is not None:
            f_type = tc.cvt_type(target.type, tc)
        # TODO: structs.Field doesn't come with doc
        return structs.Field(
            structs.Attribute(
                structs.Identifier(target.var_name),
                None,
                f_type,
            ),
            None,
        )

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
