from typing import Any

from serde import serde, field


@serde
class DocClsInstanceVar:
    var_name: str
    units: str | None = field(alias=["param_units", "var_units"])
    type: str | None = None
    doc: str | None = None


@serde
class DocClsMethodParam:
    param_name: str
    units: str | None = field(alias=["param_units", "var_units"])
    type: str | None = None
    default: Any | None = None  # TODO:
    doc: str | None = None


@serde
class DocClsMethod:
    def_name: str
    return_type: str | None = field(alias=["return", "Return"])
    static: bool | None = None
    params: list[DocClsMethodParam] | None = None
    return_units: str | None = None
    raises: str | None = None
    doc: str | None = None
    note: str | None = None
    warning: str | None = None


@serde
class DocClass:
    class_name: str
    doc: str
    parent: str | None = None
    instance_variables: list[DocClsInstanceVar] | None = None
    methods: list[DocClsMethod] | None = None


@serde
class DocModule:
    module_name: str
    classes: list[DocClass]
    doc: str | None = field(skip=True)
