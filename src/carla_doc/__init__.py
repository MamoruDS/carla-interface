from __future__ import annotations
from pathlib import Path

import yaml
from pybind11_stubgen.printer import Printer
from pybind11_stubgen import structs
from serde import from_dict
from serde.yaml import from_yaml

from .api_doc.types import DocModule
from .api_doc.convert import Convertor
from .helpers import merge_imports
from .module.import_alt import ImportAlt
from .module.module import ModuleWrapper
from .module.type_resolver import TypeResolver
from .module.types import GetNamesRules, MWPrintFlags
from .utils import CARLA_DOC_PATCHER
from .utils.logging import get_logger
from .utils.writer import Writer

log = get_logger(__name__)

DEFAULT_IMPORT_RULES = (
    GetNamesRules.ATTRIBUTES
    | GetNamesRules.CLASSES
    | GetNamesRules.FUNCTIONS
    | GetNamesRules.TYPE_VARS
)


def load_modules_from_doc(
    doc_fp: Path, patch_fp: Path | None = None
) -> list[ModuleWrapper]:
    data: list[DocModule]
    modules: list[ModuleWrapper] = []
    log.info(f"loading modules from {doc_fp}")
    try:
        if patch_fp is not None and patch_fp.exists():
            log.info(f" ! patching modules from {patch_fp}")
            patched = yaml.safe_load(doc_fp.read_text())
            CARLA_DOC_PATCHER.patch_list(
                patched,
                yaml.safe_load(patch_fp.read_text()) or [],
                key_field="module_name",
            )
            data = from_dict(list[DocModule], patched)
        else:
            data = from_yaml(list[DocModule], doc_fp.read_text())
        for module in data:
            resolver = TypeResolver.carla_default()
            modules.append(
                ModuleWrapper(
                    Convertor.cvt_module(
                        module,
                        resolver,
                        name=doc_fp.stem
                        if module.module_name == "carla"
                        else module.module_name,
                    ),
                    resolver,
                )
            )
        return modules
    except Exception as err:
        log.error(
            f"failed to load {doc_fp.name}"
            + (
                f" with patch {patch_fp}"
                if patch_fp is not None and patch_fp.exists()
                else ""
            )
        )
        raise err


def write_module(module: ModuleWrapper, writer: Writer, root: Path):
    writer.write_to_files(module, root)


def parse_carla_doc_to_module(doc_root: Path, patches_root: Path, extra_root: Path):
    prt = Printer(invalid_expr_as_ellipses=False)
    loaded: dict[str, ModuleWrapper] = {}
    extra_modules: dict[str, Path] = {
        "traffic_manager": Path("_c/traffic_manager.yml"),
    }

    for fp in doc_root.glob("*.yml"):
        for mod in load_modules_from_doc(fp, patches_root / fp.relative_to(doc_root)):
            # TODO: [0]
            loaded[fp.stem] = mod

    for mod_name, fp_str in extra_modules.items():
        for mod in load_modules_from_doc(extra_root / fp_str):
            # TODO: [0]
            loaded[mod_name] = mod

    # module -> $ROOT/carla._carla._c
    mod__c = ModuleWrapper(
        structs.Module(structs.Identifier("_c")),
        resolver=TypeResolver.carla_default(),
    )
    mod__c.append_child(loaded["traffic_manager"])

    # module -> $ROOT/carla._carla
    mod__carla = ModuleWrapper(
        structs.Module(
            structs.Identifier("_carla"),
        ),
        resolver=TypeResolver.carla_default(),
        imports=[],
    )
    mod__carla.append_child(mod__c)
    mod__carla.append_child(loaded["actor"])
    mod__carla.append_child(loaded["blueprint"])
    mod__carla.append_child(loaded["client"])
    mod__carla.append_child(loaded["commands"])
    mod__carla.append_child(loaded["control"])
    # mod__carla.append_child(mods["exception"]) # TODO:
    mod__carla.append_child(loaded["geom"])
    mod__carla.append_child(loaded["light_manager"])
    mod__carla.append_child(loaded["map"])
    mod__carla.append_child(loaded["osm2odr"])
    mod__carla.append_child(loaded["sensor_data"])
    mod__carla.append_child(loaded["sensor"])
    mod__carla.append_child(loaded["snapshot"])
    mod__carla.append_child(loaded["weather"])
    mod__carla.append_child(loaded["world"])

    # module -> $ROOT/carla.libcarla
    mod_libcarla = ModuleWrapper(
        structs.Module(
            structs.Identifier("libcarla"),
            sub_modules=[],
        ),
        resolver=TypeResolver.carla_default(),
        imports=[
            ImportAlt(loaded["actor"], filter_rules=DEFAULT_IMPORT_RULES),
            ImportAlt(loaded["blueprint"], filter_rules=DEFAULT_IMPORT_RULES),
            ImportAlt(loaded["client"], filter_rules=DEFAULT_IMPORT_RULES),
            ImportAlt(loaded["commands"], import_module=True),
            ImportAlt(loaded["control"], filter_rules=DEFAULT_IMPORT_RULES),
            ImportAlt(loaded["geom"], filter_rules=DEFAULT_IMPORT_RULES),
            ImportAlt(loaded["light_manager"], filter_rules=DEFAULT_IMPORT_RULES),
            ImportAlt(loaded["map"], filter_rules=DEFAULT_IMPORT_RULES),
            ImportAlt(loaded["osm2odr"], filter_rules=DEFAULT_IMPORT_RULES),
            ImportAlt(loaded["sensor_data"], filter_rules=DEFAULT_IMPORT_RULES),
            ImportAlt(loaded["sensor"], filter_rules=DEFAULT_IMPORT_RULES),
            ImportAlt(loaded["snapshot"], filter_rules=DEFAULT_IMPORT_RULES),
            ImportAlt(loaded["weather"], filter_rules=DEFAULT_IMPORT_RULES),
            ImportAlt(loaded["world"], filter_rules=DEFAULT_IMPORT_RULES),
        ],
        print_flags=MWPrintFlags.INCLUDE_ADD,
    )

    # module -> $ROOT/carla
    mod_carla = ModuleWrapper(
        structs.Module(
            structs.Identifier("carla"),
            sub_modules=[],
        ),
        resolver=TypeResolver.carla_default(),
        imports=[ImportAlt(mod_libcarla, import_all=True)],
    )
    mod_carla.append_child(mod_libcarla)
    mod_carla.append_child(mod__carla)

    # TODO: add `annotations` import

    for mi, (mod_name, mod) in enumerate(loaded.items()):
        log.info(
            "[{}/{}] ".format(str(mi + 1).rjust(len(str(len(loaded)))), len(loaded))
            + f"fixing & resovling types for module {mod_name} - {mod}",
        )
        while len(mod.resolver.pending):
            cache_name, pending = mod.resolver.pending.pop()
            try:
                import_, name = mod.fix_unresolved(pending)  # type: ignore
                if import_ is None:
                    # skipping local
                    log.debug(f'-> skipped type "{pending}"')
                    mod.resolver.fix(cache_name, structs.QualifiedName([name]))
                else:
                    log.debug(
                        '-> fixed type from "{}" to "{}"'.format(
                            pending, prt.print_import(import_)[0]
                        )
                    )
                    # mod.imports.append(ImportAlt(mods["world"], names=[name])) # FIXME:
                    # FIXME: carla.sequence[int] -> ?, what about params handle?
                    # params also need to be shallow copied
                    mod.resolver.fix(cache_name, structs.QualifiedName([name]))
                    # TODO: check
                    mod.module.imports.add(import_)
            except Exception as err:
                log.error(err)
                raise err

        for import_ in mod.resolver.imports:
            mod.module.imports.add(import_)

        mod.module.imports = merge_imports(mod.module.imports)

    return mod_carla
