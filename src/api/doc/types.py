from serde import serde


@serde
class DocClsInstanceVar:
    var_name: str
    type: str | None = None
    doc: str | None = None


@serde
class DocClsMethodParam:
    param_name: str
    type: str
    doc: str | None = None


@serde
class DocClsMethod:
    def_name: str
    params: list[DocClsMethodParam] | None = None
    doc: str | None = None


@serde
class DocClass:
    class_name: str
    doc: str
    instance_variables: list[DocClsInstanceVar] | None = None
    methods: list[DocClsMethod] | None = None


@serde
class DocModule:
    module_name: str
    classes: list[DocClass]
