from .patcher import DocPatch
from . import logging

CARLA_DOC_PATCHER = DocPatch(
    {
        "modules": "module_name",
        "classes": "class_name",
        "instance_variables": "var_name",
        "methods": "def_name",
        "params": "param_name",
    }
)

logging.setup(logging.LogLevel.DEBUG)
