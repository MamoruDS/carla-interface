from typing import Iterable

from pybind11_stubgen.structs import Identifier, Import, QualifiedName


# def sort_imports(imports: Iterable[Import]): ...


def merge_imports(imports: Iterable[Import]) -> set[Import]:
    origin: dict[QualifiedName, set[Identifier]] = {}

    for import_ in imports:
        # FIXME: alias
        names_origin = import_.origin[-1]
        assert names_origin == import_.name

        # FIXME:
        assert import_.name is not None

        for name in import_.name.split(","):
            origin.setdefault(QualifiedName(import_.origin[:-1]), set()).add(
                Identifier(name.strip())
            )

    merged: set[Import] = set()
    for org, names in origin.items():
        name = Identifier(",".join(list(names)))
        merged.add(Import(name=name, origin=QualifiedName([*org, name])))
    return merged
