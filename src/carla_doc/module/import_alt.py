from dataclasses import dataclass

from . import types as t


@dataclass
class ImportAlt(t.ImportAlt):
    module: t.ModuleWrapper
    filter_rules: t.GetNamesRules | None = None
    filter_names: list[t.Identifier] | None = None
    import_all: bool = False
    import_module: bool = False

    def get_imported_namespace(self) -> t.NamespaceItems:
        namespace: t.NamespaceItems = {}
        exports = self.module.exports()
        if self.import_all:
            if self.filter_names is not None or self.filter_rules is not None:
                # TODO: log warn skip
                ...
            namespace.update(exports)
        elif self.import_module:
            if self.filter_names is not None or self.filter_rules is not None:
                # TODO: log warn skip
                ...
            namespace.update(
                {self.module.module.name: (self.module, t.GetNamesRules.MODULE)}
            )
        else:
            if self.filter_rules is not None:
                exports = {
                    n: (m, r) for n, (m, r) in exports.items() if r & self.filter_rules
                }
            if self.filter_names is not None:
                exports = {n: e for n, e in exports.items() if n in self.filter_names}
            namespace.update(exports)
        return namespace

    def to_pybind11_import(self, import_from: t.ModuleWrapper) -> t.Import:
        mp = import_from.tree.relative(self.module.tree)
        if self.import_all:
            return mp.imports(all=True)
        elif self.import_module:
            return mp.imports(names=[self.module.module.name])
        else:
            return mp.imports(names=self.get_imported_namespace().keys())
