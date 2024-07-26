from pathlib import Path

from pybind11_stubgen.printer import Printer

from ..module.types import ModuleWrapper
from ..utils.logging import get_logger

log = get_logger(__name__)


class Writer:
    package_name: str
    _printer: Printer

    def __init__(self, package_name: str, printer: Printer | None = None) -> None:
        self.package_name = package_name
        self._printer = printer or Printer(invalid_expr_as_ellipses=True)

    def write_to_files(self, module: ModuleWrapper, root: Path):
        mod = module.get_print_ready_module()
        name = mod.name if module.tree.root() is not module.tree else self.package_name
        if len(module.tree.children):
            mod_root = root / name
            mod_root.mkdir()
            mod_file = mod_root / "__init__.pyi"
            with mod_file.open("w") as f:
                log.info(f"writing module <{module}> to file {mod_file} ...")
                f.writelines(ln + "\n" for ln in self._printer.print_module(mod))
            for child in module.children:
                # TODO: mod.sub_modules or print-ready?
                self.write_to_files(child, mod_root)

        else:
            mod_file = root / f"{name}.pyi"
            with mod_file.open("w") as f:
                log.info(f"writing module <{module}> to file {mod_file} ...")
                f.writelines(ln + "\n" for ln in self._printer.print_module(mod))
