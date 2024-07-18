from . import errors as e
from . import types as t


class Register(t.ModuleRegister):
    _modules: set[t.ModuleWrapper]
    _name: str

    def __init__(self, name: str) -> None:
        self._modules = set()
        self._name = name

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "ModuleRegister[{}]".format(self._name)

    def add(self, module: t.ModuleWrapper) -> t.ModuleWrapper:
        self._modules.add(module)
        return module

    def append_child(self, parent: t.ModuleWrapper, child: t.ModuleWrapper):
        assert parent in self._modules
        assert child in self._modules
        parent.tree.append_child(child.tree)

    def get_by_abs(self, abs: t.ModulePath) -> t.ModuleWrapper:
        if not abs.is_absolute():
            raise TypeError("param `abs: ModulePath` is not absolute")
        abs_str = str(abs)
        for mod in self._modules:
            if str(mod.tree.abs()) == abs_str:
                return mod
        raise e.ModuleNotFoundInRegister(abs, self)

    def get_by_tree(self, tree: t.ModuleTree) -> t.ModuleWrapper:
        for mod in self._modules:
            if mod.tree is tree:
                return mod
        raise e.ModuleNotFoundInRegister(tree, self)

    def get_children(self, parent: t.ModuleWrapper) -> set[t.ModuleWrapper]:
        assert parent in self._modules
        children = set()
        for child in parent.tree.children:
            # alt: use `self.get_by_abs`
            children.add(self.get_by_tree(child))
        return children


DEFAULT_REGISTER = Register(name="default")
