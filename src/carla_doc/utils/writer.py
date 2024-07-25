from pathlib import Path

from pybind11_stubgen.printer import Printer

from ..module.types import ModuleWrapper
from ..utils.logging import get_logger

log = get_logger(__name__)


class Writer:
    _printer: Printer

    def __init__(self, printer: Printer | None = None) -> None:
        self._printer = printer or Printer(invalid_expr_as_ellipses=True)

    def write_to_files(self, module: ModuleWrapper, root: Path):
        mod = module.get_print_ready_module()
        if len(module.tree.children):
            mod_root = root / mod.name
            mod_root.mkdir()
            mod_file = mod_root / "__init__.pyi"
            with mod_file.open("w") as f:
                log.info(f"writing module <{module}> to file {mod_file} ...")
                f.writelines(ln + "\n" for ln in self._printer.print_module(mod))
            for child in module.children:
                # TODO: mod.sub_modules or print-ready?
                self.write_to_files(child, mod_root)

        else:
            mod_file = root / f"{mod.name}.pyi"
            with mod_file.open("w") as f:
                log.info(f"writing module <{module}> to file {mod_file} ...")
                f.writelines(ln + "\n" for ln in self._printer.print_module(mod))
