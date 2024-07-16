from pybind11_stubgen import structs


class TypeConvertor:
    imports: set[structs.Import]
    pending: list[structs.QualifiedName]
    no_cache: bool
    caches: dict[str, structs.ResolvedType]
    banned_modules: list[structs.Identifier] | None
    """useful for blocking certain modules, e.g., the parsing one."""

    def __init__(
        self,
        no_cache: bool = False,
        *,
        banned_modules: list[structs.Identifier] | None = None,
    ) -> None:
        self.imports = set()
        self.pending = []
        self.no_cache = no_cache
        self.caches = {}
        self.banned_modules = banned_modules

    def is_importable(self, module: structs.Identifier) -> bool:
        if module in (self.banned_modules or []):
            return False
        try:
            importlib.import_module(module)
            return True
        except ImportError:
            return False

    def from_str(self, type_name: str) -> structs.ResolvedType:
        name = structs.QualifiedName.from_str(type_name)
        if type_name in dir(builtins):
            return structs.ResolvedType(name)
        if type_name not in self.caches:
            if self.is_importable(type_name):
                self.imports.add(structs.Import(name[-1], name))
                self.caches[type_name] = structs.ResolvedType(
                    structs.QualifiedName(name[-1:])
                )
            else:
                self.pending.append(name)
                self.caches[type_name] = structs.ResolvedType(name)
        return self.caches[type_name]  # shallow is okay


class Convertor:
    def __init__(self): ...

    def arg_self(self) -> structs.Argument:
        return structs.Argument(structs.Identifier("self"))
