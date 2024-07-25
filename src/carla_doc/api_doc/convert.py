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
    def fix_special_method_params(fn: dt.DocClsMethod):
        params_map: dict[str, list[tuple[str, str | None]]] = {
            "__bool__": [],
            "__eq__": [("other", "typing_extensions.Self")],
            "__float__": [],
            # "__getitem__":
            "__int__": [],
            # "__init__":
            "__len__": [],
            "__ne__": [("other", "typing_extensions.Self")],
            # "__non_zero__":
            # "__setitem__":
            "__str__": [],
        }
        params = params_map.get(fn.def_name, None)
        if params is not None:
            fn.params = []
            for pn, pt in params:
                fn.params.append(
                    dt.DocClsMethodParam(
                        param_name=pn,
                        units=None,
                        type=pt,
                    )
                )

    @staticmethod
    def fix_special_method_return(fn: dt.DocClsMethod):
        return_map = {
            "__bool__": "bool",
            "__eq__": "bool",
            "__float__": "float",
            # "__getitem__":
            "__int__": "int",
            "__init__": None,
            "__len__": "int",
            "__ne__": "bool",
            # "__non_zero__":
            # "__setitem__":
            "__str__": "str",
        }
        if fn.def_name in return_map:
            fn.return_type = return_map[fn.def_name]

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

    @classmethod
    def cvt_class(cls, target: dt.DocClass, tc: TypeResolver) -> structs.Class:
        if cls.is_enum(target):
            return cls.cvt_enum(target, tc)
        props: list[structs.Property] = []
        methods: list[structs.Method] = []
        for var in target.instance_variables or []:
            props.append(cls.cvt_property(var, tc))
        for method in target.methods or []:
            cls.fix_special_method_params(method)
            cls.fix_special_method_return(method)
            methods.append(cls.cvt_method(method, tc))
        return structs.Class(
            structs.Identifier(target.class_name),
            doc=cls.cvt_docstr(target.doc),
            methods=methods,
            properties=props,
        )

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
    def cvt_method(cls, target: dt.DocClsMethod, tc: TypeResolver) -> structs.Method:
        return_type, modifier = None, None
        if target.return_type is not None:
            return_type = tc.cvt_type(target.return_type, tc)
        if target.static:
            modifier = "static"
        args: list[structs.Argument] = []
        if modifier is None:
            args.append(cls.arg_self())
        for arg in target.params or []:
            arg_type = None
            if arg.type is not None:
                arg_type = tc.cvt_type(arg.type, tc)
            args.append(
                structs.Argument(
                    structs.Identifier(arg.param_name),
                    annotation=arg_type,
                )
            )
        return structs.Method(
            structs.Function(
                structs.Identifier(target.def_name),
                args=args,
                returns=return_type,
                doc=cls.cvt_docstr(target.doc),
            ),
            modifier,
        )

    @classmethod
    def cvt_module(
        cls, target: dt.DocModule, tc: TypeResolver, name: str | None = None
    ) -> structs.Module:
        classes: list[structs.Class] = []
        for class_ in target.classes:
            classes.append(cls.cvt_class(class_, tc))
        return structs.Module(
            structs.Identifier(name or target.module_name),
            doc=cls.cvt_docstr(target.doc),
            classes=classes,
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
