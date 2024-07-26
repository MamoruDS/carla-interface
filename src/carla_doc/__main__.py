from pathlib import Path

from pybind11_stubgen.printer import Printer
from typed_cap import Cap

from .cli import Args
from .utils.logging import set_level
from .utils.writer import Writer
from . import parse_carla_doc_to_module, write_module


if __name__ == "__main__":
    cap = Cap(Args)
    _, args = cap.parse().unpack()

    doc_root = Path(args.input_root)
    patches_root = Path(args.patches_root)
    extra_root = Path(args.extra_root)
    output_root = Path(args.output_root)

    set_level(args.level)

    module = parse_carla_doc_to_module(doc_root, patches_root, extra_root)

    printer = Printer(invalid_expr_as_ellipses=True)
    writer = Writer("carla-stubs", printer)
    write_module(module, writer, output_root)
